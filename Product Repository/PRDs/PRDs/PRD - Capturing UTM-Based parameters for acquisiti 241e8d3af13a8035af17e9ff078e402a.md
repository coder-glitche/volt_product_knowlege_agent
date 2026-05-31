# PRD - Capturing UTM-Based  parameters for acquisition & activation attribution and tracking for MFDs

: Devansh Kar
Created time: July 31, 2025 6:58 AM
Status: Not started
Last edited: August 29, 2025 4:46 PM

Volt Money onboards **Mutual Fund Distributors (MFDs)** through multiple channels:

- **Organic** — direct visits, SEO traffic
- **Events** — physical/virtual events with pre-registered attendees
- **Marketing Campaigns** — Google, Facebook, email campaigns
- **Webinars** — promotional landing pages with UTMs (to confirm)
- **Referrals** — MFD-shared referral links with embedded UTMs

UTM parameters (`utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`) are often present on the **first visit** but get lost during the onboarding journey and are not persisted.

Currently:

- Marketing Campaign-driven signups are often **misclassified as “Organic”** as UTM parameters get lost.
- LSQ (LeadSquared) does not store original campaign UTMs.
- We have no visibility into **which channels produce active, revenue-generating MFDs** (activation attribution) ([i.e. No linkage between acquisition source and activation milestones.]

This limits our ability to:

- Measure marketing ROI and CAC
- Optimize GTM spend
- Identify high-converting channels

---

# **What problem are we solving?**

We need a **robust end-to-end attribution system** that:

1. **Capture & persist** both first-touch and last-touch UTMs from initial visit to post-registration lifecycle across sessions/ devices for every MFD
2. Stores them in the **MFD master record (MFD table)** for permanent reference.
3. ~~Sends UTM data to LSQ during lead creation.~~
4. Retains them for use in **activation attribution** (linking post-onboarding milestones/ activation events back to acquisition source for full funnel attribution).

---

# **How do we measure success?**

- MFDs with accurate onboarding attribution (# of mfds clicked on a utm campaign, # of mfds registered through link etc)
- MFDs with activation attribution (# of mfds activated)
- Reduction in misclassified organic signup
- Funnel visibility: Visit → Registration → Activation
- Campaign ROI reporting accuracy

---

# **How are others solving this problem?**

---

# Scope

**In Scope:**

- UTM capture on web and mobile
- Storage in cookies, localStorage, and backend DB
- DB schema changes for UTM fields
- ~~LSQ integration for UTM data~~
- Signup and Activation attribution mapping
- Fallback attribution logic when UTMs are missing

**Out of Scope:**

- Historical data backfill
- Non-UTM attribution methods (pure referral codes are handled separately)

---

# Goals/ Objectives

**Primary Goals**

- **Onboarding Attribution** — Accurately capture and store first-touch & last-touch UTMs for every registering MFD.
- **Activation Attribution** — Link activation events back to original acquisition source.
- **Reporting Enablement** — Make attribution data available for dashboards, and BI tools.

**Secondary Goals**

- Support **cross-session and cross-device** attribution.
- Handle **mobile deep-link onboarding**.
- Enable both **first-touch** and **last-touch** analysis for channel performance.

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

## Requirements

1. **Functional Requirements:**
    1. **UTM Capture Logic**
        1. Detect UTM parameters from any page where an MFD first lands (whether web URL or mobile deep link).
        2. Recognized Parameters:
            - campaign_id
            - `utm_id`
            - `utm_source` (e.g. google, facebook, referral_code_123)
            - `utm_medium` (e.g. social, email, referral)
            - `utm_campaign` (e.g., july_ads, august_webinar)
            - `utm_term` (paid search keyword)
            - `utm_content` (creative version)
        3. Store **first-touch UTMs** on first visit and MFD registration(never overwritten).
        4. Store middle touch points of UTMs
        5. Store **last-touch UTMs** on most recent campaign/referral visit before registration via mobile number.
        - Retain UTMs in:
            - LocalStorage (30-day expiry)
            - Cookie (`volt_first_touch`, `volt_last_touch`)
            - Server-side session storage (linked to temporary visitor ID).
        
        v. **Cross-Session & Cross-Device**
        
        - If MFD returns after days/weeks, keep UTMs linked.
        - If MFD starts on desktop but finishes on mobile (or vice versa) and uses the same phone/email, merge attribution data.
        - Map final platform attribution through which registration is done (Android app, web, etc.).
        
        vi. **Activation Attribution**
        
        - Store UTMs  at an activity level for each MFD.
        - Mapping MFD_ID to utm clicked
        - When activation milestone achieved (e.g., first borrower onboarded, first loan disbursed, first referral success):
            - Retrieve and log UTMs alongside activation event.
        - Enable reporting:
            - Activation rate per acquisition channel
            - CAC vs LTV per channel
            - Track through marketing campaign, webinar links, etc.
2. **Data Requirements**

| Field Name | Type |
| --- | --- |
| campaign_id | varchar(100) |
| utm_id | varchar(100) |
| first_utm_source | varchar(100) |
| first_utm_medium | varchar(100) |
| first_utm_campaign | varchar(100) |
| first_utm_term | varchar(255) |
| first_utm_content | varchar(255) |
| first_touch_date | datetime |
| last_utm_source | varchar(100) |
| last_utm_medium | varchar(100) |
| last_utm_campaign | varchar(100) |
| last_utm_term | varchar(255) |
| last_utm_content | varchar(255) |
| last_touch_date | datetime |

**Activation event logging**

When an activation event occurs:

- Log: `mfd_id`, current_stage (registered, empanelled), `activation_date`, **first-touch UTMs**, **last-touch UTMs**.
- This will allow funnel reporting like:
    
    **Visit → Registration → Activation → Revenue by Channel**
    
1. **~~LSQ requirements~~**

**~~Custom Fields in LSQ~~**

- `~~first_utm_source`, `first_utm_medium`, `first_utm_campaign`, `first_utm_term`, `first_utm_content`~~
- `~~last_utm_source`, `last_utm_medium`, `last_utm_campaign`, `last_utm_term`, `last_utm_content`~~

**~~Lead Creation Process~~**

- ~~On registration, send UTMs as part of LSQ lead creation API payload.~~

**~~Update Rules~~**

- ~~Confirm with Vijay~~

**~~Reporting in LSQ~~**

- ~~Allow filtering leads by first-touch/last-touch.~~
- ~~Enable export for BI analysis.~~

---

# Edge Cases

- Multiple campaign clicks before signup → first-touch fixed, last-touch updated.
- Referral after campaign visit → referral attribution overrides UTMs.
- No UTMs present → fallback to referrer or direct.
- Cookie expiry before signup → first-touch unknown, last-touch updated if available.
- Cross-device without identifier → attribution lost.
- UTM tampering → validate against known campaign whitelist.

---

# **Design**

---

# **Analytics**

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Ops & Sales training

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