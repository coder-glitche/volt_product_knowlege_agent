# BRE Proposal for cases above 1 Cr

: Ameya Aglawe
Created time: September 2, 2024 12:34 PM
Status: Done
Last edited: September 12, 2024 4:44 PM
Owner: Ameya Aglawe

# **What problem are we solving?**

For the users with eligible limit > 1 Cr when they complete the application with BAJAJ as lender then - 
a. SPDC (BAJAJ's Form need to be filled & signed)
b. Cancel cheque (Signed blank cheque)
c. These 2 documents need to be done by user & couriered to BAJAJ office by the user [Very high effort]
d. It takes about 3-4 days for the lodgement to be done by after the user has couriered the documents

---

# **How do we measure success?**

- TAT for account creation for BAJAJ in cases of eligible limit > 1 Cr
- Reduction in man-hours spent on application creation per user (for BAJAJ in cases of eligible limit > 1 Cr)

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

## Requirements

- **For new application**
    - **BRE (Business Rules Engine) Execution During Credit Limit Setup:**
        - When the user fetches their portfolio and proceeds to set their credit limit, the BRE will run upon the user tapping "Set Credit Limit" at unlock credit limit page
        - An additional rule will be implemented in the BRE:
            - If the fetched eligible limit ≥ 1Cr, the lender will automatically be assigned as TATA.
    - **Edge Cases:**
        - Scenario:
            - During the initial portfolio fetch, if the eligible limit is below ₹1 crore, the BRE will run and assigns BAJAJ as the lender.
            - The user proceeds in the flow but later edits their credit limit and fetches additional portfolio information, pushing the eligible limit above ₹1 crore.
        - Current System Limitation:
            - Our system currently executes the BRE only once, during the initial fetch. As a result, even if the eligible limit exceeds ₹1 crore after a subsequent portfolio fetch, the lender remains BAJAJ.
        - Temporary Solution:
            - For the current version, the BRE will continue to run only once during the initial portfolio fetch.
            - We'll monitor the impact of this approach and consider implementing functionality to re-run the BRE if the user fetches the portfolio again in future updates.
- **For enhancement & renewals (De-prioritized : Will be taken in v2)**
    - For cases where first eligible limit ≤ 1 Cr
        - **1st approach**
            - While enhancing, if user’s total eligible limit (limit of original application + limit of enhancement) crosses 1 Cr then we can show a call out at the “SET CREDIT LIMIT” page -
                - You’ll have to provide an SPDC form & a cancel cheque if you select credit limit more than Rs XXXXXX.
                - This amount (Rs XXXXXX) will be calculated by -
                    - Let current/updated value of already pledged funds = Rs X **(check if we can get this data at this step of application)**
                    - Let value of newly fetch funds = Rs Y
                    - Then Limit till which SPDC & cancel cheque is not required = 1 Cr - (X)
        - **2nd approach**
            - If the customer is a BAJAJ customer and goes for enhancement, and then we can give a call out to the user “You will have to fill a SPDC form & cancel cheque for eligible limit ≥ 1 Cr”
    - For cases where first eligible limit ≥ 1 Cr
        - You’ll have to provide an SPDC form & a cancel cheque if you select credit limit more than Rs XXXXXX.
        - This amount (Rs XXXXXX) will be calculated by -
            - Let current/updated value of already pledged funds = Rs X **(check if we can get this data at this step of application)**
            - Then Limit till which SPDC & cancel cheque is not required = Sanction limit - (X)
    - For the current version, the BRE will continue to run only once during the initial portfolio fetch when new application is being created. We won’t run the BRE agin at the time of enhancement & renewal since there are only 22 application which have who have undergone enhancement with eligible limit > 1 Cr.
    - We'll monitor the impact of the current approach (just run BRE during application creation) and consider implementing functionality to re-run the BRE if the user fetches the portfolio again at the time of enhancement/renewal in the future.

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