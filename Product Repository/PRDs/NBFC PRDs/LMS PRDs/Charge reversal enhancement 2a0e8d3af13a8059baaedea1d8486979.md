# Charge reversal enhancement

Last Edited: November 18, 2025 5:25 PM
PRD ETA: July 22, 2025
PRD Owner: Vaibhav Arora
Status: Completed

# **What problem are we solving?**

Today, waiving or refunding charges for a user is manual, operationally intensive, and people-dependent process. Not only does this make it error prone, it introduces friction across internal teams and impacts customer experience. The key issues we’re addressing include:

---

### **Why Do We Waive or Refund Charges?**

- **Operational Errors:** Invalid or incorrect charges (e.g., dishonour fees, penal charge) are erroneously applied.
- **User Retention or Exceptions:** Charges are waived on humanitarian grounds or as goodwill gestures to retain customers.

---

### **Current Pain Points**

- **Manual Intervention:** All waivers and refunds are routed via the product or engineering team using APIs or backend tools (e.g., Finflux).
- **Process Overhead:** Every waiver/refund request requires Jira ticketing, creating unnecessary delays for the user (experience) and consumes bandwidth of product and engineering teams
- **Billing Constraints:**
    - **Waiver Limitation:** Charges can only be waived if they are still outstanding.
    - **No Refund Mechanism:** Once charges are paid or the billing cycle is closed, there is no way to reverse them — the concept of a "charge refund" transaction doesn't exist.
- **Customer Experience:** Resolution time increases, causing friction in high-sensitivity scenarios (e.g., incorrect penal charge).

---

# **How do we measure success?**

- **Metric: R**eduction in Jira tickets raised for charge waivers/refunds
    
    **Goal:** >90% reduction within the first month post rollout
    
- **Metric:** Average time to process a waiver/refund
    
    **Goal:** Currently it takes 2-3 days to waive charges for the user, the same should be handled within one working day.
    

---

# **How are others solving this problem?**

- TCL and BFL have credit notes that can be given to the users for the following use cases:
    - Invalid charge collected from the user
    - Incorrect interest calculation for the user
    - Backdated repayments or forward dated disbursements for the user (to give benefit on the difference in the interest)

---

# **What is the solution?**

We will be creating a charge waiver task for command centre which will behave in the following manner:

- If a charge is completely outstanding, that is the amount that was applied has not been collected from the user, will be waived.
- If a charge is completely paid/collected from the user, we will be passing a credit note to the user’s loan account

<aside>
🚨

If a charge is partially paid/collected, we will not allow it to be waived or refunded - (Validation error). - We will now be passing a credit note for this as well

</aside>

- If a charge is partially paid/collected, we will not allow it to be waived or refunded - (Validation error).

We will be creating a new payment type called “CREDIT_NOTE” this repayment will not have a corresponding money transaction associated with it. Operations team will use the payment type to identify the transactions and accordingly handle in reconciliation.

The first use case that we will be covering will be the refunds of adhoc charges placed by the NBFC:

- Processing fees
- Margin pledge charges
- Dishonour fees

### Accounting:

A normal payin has the following apportionment:

- Debit: Fund source (Total amount) - (Fund source is equivalent to the bank account and signifies the total cash balance of the NBFC)
- Credit: (Split as per apportionment between)
    - Loan portfolio (POS)
    - Interest receivable (Interest due)
    - Fees receivable (Fees due)
    - Penalties receivable (Penalty due)
    - Excess (Excess across loan accounts - liability for the organisation)

For credit note we will be creating a new proxy liability account called: Credit note balance

### Why?

You're simulating a *reduction in income* or a *credit back to the user* without actual cash movement. 

### 1. **Nature of Credit Note**:

- You're refunding amounts like **processing fees**, **margin pledge charges**, and **dishonour fees** that were earlier recognized as income (i.e., credited to a fees receivable or income account).
- Now you need to reverse them.

### 2. **What actually happens**:

- Instead of debiting **fund source (asset)** (which would reflect money going out), you're creating a **non-cash transaction**.
- So you need a *book entry placeholder* that can absorb the debit.

### 3. **Proxy account purpose**:

This account will hold the debit side temporarily and then flow into:

Post processing of the refund, manual JVs will be placed that will have the following entries:

Credit: Credit note balance

Debit: Income from fees (Refund of income from fees)

Debit: GST/CGST/SGST/IGST/UTGST payables (Refunded payables)

### New accounts:

| Account Name | Entry Type | Account Type |
| --- | --- | --- |
| Expense from waivers | Credit | Liability |
| Income from Fees (reversal) | Debit | Income (negative) |
| GST/CGST/SGST/etc. Payable refund | Debit | Liability |
| GST Payable Expense | Debit | Expense (Post September 30th) |

### Charge details:

For every charge that has to be refunded, operations team will be passing the Fenix charge request ID on the interface. This charge request ID will be used to get the corresponding charge details.

Example: CRID658315q639114

### Validations:

- Already waived charges cannot be refunded
- Already refunded charges cannot be refunded again
- Already collected charges cannot be waived but only be refunded
- Outstanding charges cannot be refunded
- Charges with an existing waiver request cannot be refunded

For every charge refund request we will be performing the following steps:

- Get charge details: (Stretchy report to be built via Finflux: Completed)
    - Amount
    - Tax component (CGST / UTGST / IGST / SGST)
    - Loan account (validation)
    - Status (Active / Refunded)

```json
Request CURL:

curl --location 'https://uat-voltmoney.finfluxtrial.io/fineract-provider/api/v2/runreports/charge_detail/flatdata?R_chargeIdentifier=CRID325313647556' \
--header 'accept: application/json, text/plain, */*' \
--header 'accept-language: en-US,en;q=0.9' \
--header 'authorization: Bearer 3DQz77JKHQAoqFXhUQqxAgre9DU' \
--header 'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "Windows"' \
--header 'sec-fetch-dest: empty' \
--header 'sec-fetch-mode: cors' \
--header 'sec-fetch-site: same-origin' \
--header 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
```

```json
Sample response:
[
    {
        "account_number": "000008048", //Finflux loan account number
        "external_identifier": "CRID325313647556", //Charge request ID passed by Fenix
        "charge_due_on": "1753697507199", //Charge due date/application date
        "charge_type": "Processing Fee", //Charge type / Short name
        "total_charge_amount": "1180.000000", // Total charge amount applied inclusive of GST
        "charge_amount_excluding_tax": "1000.000000", //Total charge amount applied exclusive of GST
        "charge_outstanding_amount": "0.000000", //Present outstanding amount for charge
        "tax_name": "IGST", //Which GST was applied (in case it was applied for the respective charge)
        "tax_amount": "180.000000"
    }
]

```

- Validate loan account for which the refund is being processed
- Validate if the charge is paid or outstanding
- Already refunded charges cannot be refunded again (Fenix to build validation here)
- Validate charge application date and populate the refund type:
    - For charges applied from April 1st 2024 to March 31st 2025, and reversal date (current date) is < September 30th 2025 (Refund type will be “Reversal”)
    - For charges applied from April 1st 2024 to March 31st 2025, and reversal date (current date) is ≥ September 30th 2025 (Refund type will be “Expense”)

### Why?

To ensure correct GST treatment and input tax credit (ITC) adjustments, the type of refund (Reversal vs Expense) depends on the **timing** of the refund in relation to the **financial year and GST return filing deadlines**.

- **Applicable when:**
    
    Charge was applied between April 1, 2024, and March 31, 2025, **and** refund (reversal) is initiated **before September 30, 2025**.
    
- **GST Reasoning:**
    
    As per **Section 16(4) of the CGST Act**, input tax credit (ITC) can be **reversed or adjusted** for a transaction **until the earlier of**:
    
    - Filing of the annual return for the financial year, or
    - **September 30 of the following financial year** (or extended date).
    
    Therefore, if the charge is being refunded before the September 30 deadline, it can be classified as a **reversal** of the original charge. In this case:
    
    - GST originally charged can be **adjusted or reversed** in the books.
    - This prevents dual impact on income and ensures GST compliance.

### Interface:

We will be building a charge refund maker which will have the following components

Maker task

![image.png](Charge%20reversal%20enhancement/image.png)

Checker task:

Approve charge refund

![image.png](Charge%20reversal%20enhancement/image%201.png)

---

# **Design**

[https://miro.com/app/board/uXjVKvYl1nc=/](https://miro.com/app/board/uXjVKvYl1nc=/)

---

# **Analytics**

Volume metrics

| Metric Name | Description | Frequency |
| --- | --- | --- |
| `total_refund_requests` | Total number of refund requests initiated | Daily, Weekly |
| `total_refunds_processed` | Number of successfully processed refunds | Daily, Weekly |
| `refund_approval_rate` | `(total_refunds_approved / total_refund_requests)` | Daily, Weekly |
| `average_processing_time` | Avg. time from refund initiation to approval  | Weekly |
| `refunds_by_charge_type` | Refund counts split by Processing fee, Margin pledge, Dishonour | Weekly |

Impact metrics

| Metric Name | Description | Frequency |
| --- | --- | --- |
| `total_refunded_amount` | Aggregate value of all processed refunds | Weekly, Monthly |
| `gst_adjusted_refund_amount` | Refunds eligible for GST reversal (`Reversal` type only) | Monthly |
| `gst_expensed_amount` | Refunds not eligible for GST reversal (`Expense` type) | Monthly |

---

# **Timeline/Release Planning**

---

# **Go to market**

### **Phase 0: Go Live – 28th July**

- Only **ADHOC charges** will be eligible for refunds through the maker.
- **Manual JV entries** will be processed in a **monthly batch** by the finance team.
- **Data layer and validations** will be powered by **Fenix** (single source of truth for charge metadata).

---

### **Phase 1: Go Live – TBD**

- **Penalty charges** will transition from **Finflux-applied (batch-based)** to **Fenix-applied (real-time)**.
- Refund maker functionality will be **extended to support penalty refunds** using the same credit note and JV reversal framework.

---

### **Phase 2: Go Live – TBD**

- Manual JVs will be **automated at the refund level**, removing dependency on month-end batching.
- **Interest waivers** will be supported through **credit note issuance**, completing the full refund lifecycle across all charge types.

---

## Marketing

NA

## Ops & Sales training

To be picked

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  -
- [ ]  Business
    - [ ]  -
- [ ]  Design
    - [ ]  -

---

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

# **Feedback**

---

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes

![image.png](Charge%20reversal%20enhancement/image%202.png)