# Loan Offer Optimisation experiment for CheQ

: Devansh Kar
Created time: September 1, 2025 10:49 AM
Status: In progress
Last edited: September 2, 2025 5:55 AM

# **What problem are we solving?**

Currently we are observing low conversion rate at loan offer page selection for CheQ compared to other B2B partners for (June and Aug month) ~ 7pp lower.

**For ≥10K eligible limit (CheQ):**

| **Step** | **Aug** | **Jul** | **Jun** |
| --- | --- | --- | --- |
| **Loan Offer selection %** | 19% | 29% | 18% |

**For ≥10K eligible limit (Other B2B partners ex CheQ and PP)**

| **Step** | **Aug** | **Jul** | **Jun** |
| --- | --- | --- | --- |
| **Loan Offer selection %** | 25% | 30% | 31% |

For **July** month overview of drop-offs at each stage in the funnel from eligible credit limit page to loan offer selection:

![image.png](Loan%20Offer%20Optimisation%20experiment%20for%20CheQ/image.png)

For **Aug** month overview of drops at each stage in the funnel from eligible credit limit page to loan offer selection:

![image.png](Loan%20Offer%20Optimisation%20experiment%20for%20CheQ/image%201.png)

As we can see from the above stepwise funnel data:
  1. There is  ~75% drop happening from MFC Fetch eligible limit page to Set credit limit page.

1. Another 7% drop happening from Set Credit limit page to Loan offer page.

On calling CheQ users dropping off at this stage we found that:

![image.png](Loan%20Offer%20Optimisation%20experiment%20for%20CheQ/image%202.png)

Currently, 2 screens precede loan offer details page:

- Eligible limit screen (post-portfolio fetch).
- Credit limit slider screen.
- Loan offer details page.

This fragmented flow creates cognitive load and drop-offs before users even see the actual loan offer.

---

# **How do we measure success?**

~ 5-10% improvement in loan offer selection conversion percentage

---

# **How are others solving this problem?**

---

# Scope

- **In Scope:**
    - Redesign of eligible limit + credit limit slider + loan offer screens into a **single optimised offer page**.
    - Inclusion of contextual information: eligible funds, PF/IRPA breakdown, EMI calculator, FAQs.
    - Experimentation with visual hierarchy & CTAs (A/B testing).
- **Out of Scope:**
    - Changes to backend eligibility/credit engine.
    - Changes to pricing/charges (PF, IRPA).
    - Partner-specific branding (focus on Cheq for this pilot).

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

### **Current:**

1. Eligible limit shown along with fetched mutual funds.
2. User sets credit limit via slider.
3. Loan offer displayed (details + CTA).

### **Proposed (Optimised):**

**Single Loan Offer Page combining Steps 1–3**

**Sections of Redesigned Loan Offer Page:**

1. **Header:** “Your Eligible Loan Limit” (e.g., ₹2,00,000) [How is it calculated?].
2. **Offer Summary Card:**
    - Loan Amount (with edit option to navigate to adjusted via slider).
    - ROI (per annum), PF, tenure, EMI (schedule - example).
    - Eligible Funds .
3. **Credit Limit Slider (inline):** Pre-set to recommended limit; on clicking on edit button.
4. **Key Context & Benefits (Expandable):**
    - “No impact on ownership of MF units.”
    - “Instant liquidity against idle investments.”
    - “Flexible repayment.”
5. **FAQs / Terms (Accordion style).**
6. **Primary CTA:** “Proceed”.

## Requirements

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