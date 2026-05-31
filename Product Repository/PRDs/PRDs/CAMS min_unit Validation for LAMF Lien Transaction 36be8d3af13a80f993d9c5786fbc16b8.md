# CAMS min_unit Validation for LAMF Lien Transactions

: Yogesh D
Created time: May 25, 2026 7:15 PM
Status: Not started
Last edited: May 26, 2026 5:40 PM

# What problem are we solving?

- CAMS RTA is introducing a mandatory scheme-level `min_unit` validation across all lien transaction APIs for LAMF. This is applicable to **CAMS RTA only** — KFintech RTA, CAMS MFC, and KFin MFC are not affected.
- Prior to this change, a lender could mark a lien of any unit quantity, and invoke or revoke any partial amount regardless of what remained. CAMS will now enforce a floor: any transaction that leaves `remaining_units < min_unit` for a scheme will be rejected at the API level.
- This impacts all three lien transaction types differently:
    - **Pledging (lien marking)** — a new lien mark with `lien_unit < min_unit` is now rejected upfront at the `validatecasdata` step.
    - **Invoke** — a partial invoke that leaves `residual < min_unit` is rejected. If existing `remaining_units` are already below `min_unit` (legacy lien), only full invoke is allowed.
    - **Revoke** — same logic as invoke. A partial revoke that leaves `residual < min_unit` is rejected. If existing `remaining_units` are already below `min_unit`, only full revoke is allowed.
- Currently none of our systems — the E2E sell-off job, the Volt revocation UI, or 3rd party LSP interfaces — are aware of `min_unit`. Without changes, all three will start producing CAMS API failures after this enforcement goes live.
- `min_unit` is sourced dynamically from CAMS API responses (returned as `"minunits"` in `lienmarkbycas` and `consolidatelienstatus` responses). No static master changes are required.

# How do we measure success?

- **Zero CAMS min_unit API rejections** — 0 invoke/revoke/lien-mark requests rejected by CAMS due to min_unit violations after go-live.
- **Zero missed recovery** — all CAMS folios that would have previously failed are handled via adjusted or full-sell logic with no gap in recovery.
- **Legacy lien coverage** — 100% of active CAMS liens where `remaining_units < min_unit` identified before go-live and handled correctly on next transaction.
- **Revocation UI accuracy** — 0 partial revoke submissions reaching CAMS with an invalid residual unit count.
- **Pledging UI accuracy** — 0 lien mark submissions reaching CAMS with `lien_unit < min_unit`.

# Solution

## Overview

- Update the lien transactions and existing process to handle the min_units based validations based on the plege source RTA and repository type CAMS.

### **Transaction 1: Pledging (Lien Marking)**

#### What is changing

CAMS now validates `lien_unit >= min_unit` at the `validatecasdata` step — which is the first step in the lien marking flow, before OTP confirmation. Previously any positive unit count was accepted.

#### **API affected**

 `/lamfapi/trxn/v1/lienmarkbycas`**Step affected:** `validatecasdata` (and downstream `lienmarkcasdata`, `submitlienmarkcasdata`, `validatecasotp`)

**New `minunits` field in response:** `validatecasdata` response now includes `"minunits"` per scheme inside `schemedetails`. This is available even on successful validation — it tells the lender the floor for this scheme.

#### Error introduced

**Scenario:** Lien mark attempted with `lien_unit < min_unit`

Request: `lienunit: "1"`, scheme `minunits: "2"`

Response:

json

```jsx
{
  "validatecasdata": {
    "schemedetails": [
      {
        "lienunit": "1",
        "minunits": "2",
        "remarks": "Pass lien unit greater than min lien eligible unit"
      }
    ]
  },
  "status": "FAILURE",
  "message": "FAILURE"
}
```

#### What needs to change in our system

**Pledging flow (Volt LSP and 3rd party LSPs)**

The pledging UI today allows a user to pledge any unit count for lien marking. After this change, we must:

1. **Show `min_unit` on the pledging screen** — `minunits` is returned in the `validatecasdata` response (which is the first API call in the lien mark flow). Once the response comes back, display the scheme's minimum unit requirement on the screen.
2. **Validate before submission** — if the user enters `lien_unit < min_unit`, show an inline error before the user can proceed to confirmation. Error text: *"Minimum lien units for this scheme is {min_unit}. Please enter {min_unit} or more units."*

**Surface**

- Volt LSP pledging screen
- 3rd party LSP pledging interface (implementation path to be confirmed with tech — frontend SDK change vs API-layer validation)

### Transaction 2: Invoke

#### What is changing

The CAMS invoke API (`/lamfapi/trxn/v1/invoc`) now enforces two new constraints on the `invocationunit` field

#### **API affected**

`/lamfapi/trxn/v1/invoc`

**Field affected:**

"invocationunit" per scheme in schemedetails.

#### **Error 1: Partial invoke leaving residual below min_unit**

**Scenario:** `remaining_units = 2.5`, `min_unit = 2`, `invocation_unit = 1` → residual = 1.5 < 2

Request: `invocationunit: "1"`, `lienunit: "2.5"`

Response:

```jsx
{
  "invocvalidate": {
    "schemedetails": [
      {
        "lienunit": "2.5",
        "invocationunit": "1",
        "lienmarkno": "222220",
        "remarks": "Partial invoke not allowed: remaining lien units would be below the scheme's minimum invoke limit. Please adjust the requested units."
      }
    ],
    "message": "FAILURE"
  }
}
```

#### Error 2: Existing lien already below min_unit (legacy lien)

**Scenario:** `remaining_units = 40` but `remaining_units < min_unit` (lien is in sub-minimum state), partial invoke of 21 attempted

Response:

```jsx
{
  "invocvalidate": {
    "schemedetails": [
      {
        "lienunit": "40",
        "invocationunit": "21",
        "remarks": "Only complete invoke allowed: current lien units are below the scheme's minimum limit"
      }
    ],
    "message": "FAILURE"
  }
}
```

#### What needs to change in our system

#### **E2E fund selection algorithm (backend)**

#### STP-NSTP sell-off approval

#### OPS invocation process

Ops team will now do a validation to ensure full invocation for lagacy lein status.

### Transaction 3: Revoke

#### What is changing

Revoke is user-triggered — initiated by ops users or LSP users (Volt and 3rd party) when releasing a customer's pledged collateral partially or fully, typically on repayment. The CAMS revoke API (`/lamfapi/trxn/v1/revoc`) now enforces the same two constraints as invoke.

#### API affected

`/lamfapi/trxn/v1/revoc`

**Field affected:**

`"revocationunit"` per scheme in schemedetails.

#### **Error 1: Partial revoke leaving residual below min_unit**

**Scenario:** `remaining_units = 2.5`, `min_unit = 2`, `revocation_unit = 1` → residual = 1.5 < 2

Request: `revocationunit: "1"`, `lienrefno: "68572"`

Response:

```jsx
{
  "revocvalidate": {
    "schemedetails": [
      {
        "revocationunit": "1",
        "lienmarkno": "222592",
        "remarks": "Partial revoke not allowed: remaining lien units would be below the scheme's minimum revoke limit. Please adjust the requested units."
      }
    ],
    "message": "FAILURE"
  }
}
```

#### **Error 2: Existing lien already below min_unit (legacy lien)**

**Scenario:** `remaining_units < min_unit`, partial revoke of 21 units attempted

Response:

```jsx
{
  "revocvalidate": {
    "schemedetails": [
      {
        "revocationunit": 21,
        "lienmarkno": "207550",
        "remarks": "Only complete revoke allowed: current lien units are below the scheme's minimum limit"
      }
    ],
    "message": "FAILURE"
  }
}
```

> Note: The existing error for over-revoke ("Units requested for lien revocation is more than lien marked units in the scheme.") is unchanged — this is a pre-existing validation.
> 

#### **What needs to change in our system**

#### **Backend pre-submission validation**

Before calling the CAMS revoke API, the system must check the same pre-flight logic as invoke (using `remaining_units` and `min_unit` from `consolidatelienstatus`):

- If `remaining_units < min_unit` → only full revoke is allowed; send `revocation_unit = remaining_units`
- If `residual < min_unit` (and residual > 0) → reject the request before it reaches CAMS; surface error to the frontend with the adjusted valid range

#### **Revocation UI — Volt LSP**

The revocation screen must surface min_unit constraints to the user before submission. `remaining_units` and `minunits` are available from the `consolidatelienstatus` call that already populates the screen.

**Case 1: Legacy lien (`remaining_units < min_unit`)**

- Unit input field is **disabled** and pre-filled with `remaining_units`
- Banner message: *"This folio's lien units are below the scheme minimum. Only full revoke is allowed."*
- User can only confirm (full revoke) or cancel

**Case 2: Residual breach on partial entry**

- Inline error shown on unit input change before submission
- Error text: *"Remaining units after revoke would be {residual} — below the scheme minimum of {min_unit}. Enter at most {remaining_units − min_unit} units, or revoke all {remaining_units} units."*
- Submit button disabled until input is valid
- Two helper CTAs shown: **"Set to max partial ({remaining_units − min_unit} units)"** and **"Set to full revoke ({remaining_units} units)"**

#### **Revocation UI — 3rd party LSPs**

Same validation logic and error messaging applies. Implementation path (frontend SDK change vs API-layer validation before the call reaches CAMS) to be confirmed with tech based on how 3rd party LSP revocation UIs are served.

## In Scope

- E2E fund selection algorithm — min_unit pre-flight for CAMS folios before invoke
- `min_unit_adjusted_flag` column in `fenix_sell_off_collaterals_request`
- Pledging UI validation (Volt LSP and 3rd party LSPs) — block mark if `lien_unit < min_unit`
- Revocation UI validation (Volt LSP) — inline error and helper CTAs for residual breach and legacy lien
- Revocation UI validation (3rd party LSPs) — same logic, implementation path TBD with tech

## Out of Scope

- KFintech RTA, CAMS MFC, KFin MFC — not affected by this change
- STP/NSTP routing logic changes — min_unit adjustment happens inside fund selection before STP evaluation; no new reason codes needed

# Happy Path

**Pledging:**

1. User enters lien units on pledging screen.
2. `validatecasdata` API called → response includes `minunits`.
3. If `lien_unit >= min_unit` → proceed to OTP confirmation as today.
4. If `lien_unit < min_unit` → inline error shown, confirmation blocked.

**Invoke (sell-off job):**

1. E2E job computes `sell_units_i` for a CAMS folio.
2. Pre-flight fetches `remaining_units` and `min_unit` from `consolidatelienstatus`.
3. If `remaining_units < min_unit` → `sell_units_i` forced to `remaining_units` (full invoke).
4. If residual would breach `min_unit` → `sell_units_i` adjusted to Option A or Option B.
5. Invoke API called with valid units — CAMS accepts.

**Revoke:**

1. User opens revocation screen — `remaining_units` and `min_unit` loaded from `consolidatelienstatus`.
2. User enters `revocation_unit`.
3. If legacy lien → input disabled, full revoke only.
4. If residual breach → inline error, submit blocked until corrected.
5. Revoke API called with valid units — CAMS accepts.

# Edge Cases

| Case | Handling |
| --- | --- |
| `remaining_units < min_unit` (legacy lien) — invoke | Force full invoke in fund selection; `min_unit_adjusted_flag = True` |
| `remaining_units < min_unit` (legacy lien) — revoke | UI disables partial input; pre-submission backend also validates |
| Adjusted partial (Option A) still leaves R > 0 after all CAMS funds exhausted | Existing partial recovery flow — RiskOPS email with residual gap |
| `minunits` field absent in CAMS response (schema fallback) | Treat as `min_unit = 0`; no adjustment applied; proceed as-is |
| Full invoke / full revoke (`requested == remaining`) | Always valid; no min_unit check needed |
| 3rd party LSP revocation UI not served via Volt frontend | Tech to confirm; validation logic identical regardless of implementation path |

# Open Items / Checklist

- [ ]  Tech — confirm `minunits` is consistently present in `consolidatelienstatus` for all active CAMS folios (not just newly marked liens)
- [ ]  Tech — query active CAMS liens where `remaining_units < min_unit` (legacy lien count) before go-live
- [ ]  Tech — confirm implementation path for 3rd party LSP revocation and pledging UI (Volt frontend SDK vs API-layer pre-validation)
- [x]  UAT — validate all 5 error scenarios across the 3 transaction types in CAMS UAT using existing test PANs
- [x]  Tech — `min_unit_adjusted_flag` column migration on `fenix_sell_off_collaterals_request`
- [x]  Go-live gated on CAMS UAT sign-off per CAMS communication