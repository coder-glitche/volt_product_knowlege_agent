# Dishonour charge enhancement

Last Edited: July 4, 2025 2:02 PM
PRD ETA: June 16, 2025
PRD Owner: Vaibhav Arora
Status: Completed

# **What problem are we solving?**

Dishonour charges are applied to user loan accounts when monthly dues are not paid before the 7th of the month. However, the current application is tied to the outcome of mandate presentation, which results in inconsistent charge application across accounts.

**Problems Identified**

1. **Missed Charges Due to No Mandate:**
    
    Dishonour charges are **not applied** to users who do not have an active mandate (e.g., revoked mandates), even if they miss their due date.
    
2. **Incorrect Charges Despite Repayment:**
    
    Users who have already paid their dues manually (e.g., via UPI or netbanking) are **still charged** dishonour fees if the mandate fails later due to reasons like insufficient balance or a frozen account.
    

---

# **How do we measure success?**

- Accuracy of application of charges: # number of waiver requests for dishonour charges
    - Tickets raised for waiver of dishonour charges
    - Amount of dishonour charges that are waived every month
    - Number of customers who made the payment on the 7th (due date) but dishonour fees is applied (invalid application of charges)
    - Number of customers where dishonour should have been applied but were not applied due to mandate presentation failure.

---

# **How are others solving this problem?**

- NA (Internal to DSP)

---

# **What is the solution?**

To make the application of dishonour charges **independent of the mandate presentation process** by introducing a post-due date review mechanism that ensures charges are applied fairly and consistently based on actual repayment behaviour.d

<aside>
⚠️

In case mandate is revoked or does not exist, if the collection amount is less than 10 Rs, it should be waived

</aside>

### Revised Workflow

**1. Collection Request Creation**

- A collection request is created for every user with an outstanding **interest due** amount, post validation and approval from the **Risk Operations team**.

**2. Scheduled Review on 8th of Each Month**

- A review task will be triggered **on the 8th of every month** to check the status of repayments.
- This review will be scheduled **post business hours**, to accommodate and account for **delayed payments made after 6 PM on the 7th**.

### Review Logic (Review task will only be created for users who were eligible for collection: Even if presentation fails, review task should be created for the user).

For each user with an active collection request:

- Check if the **interest due amount** was **cleared by end-of-day on the 7th**.
- If the user **has not paid the interest due**, a **dishonour charge** should be applied.
- If the user **has cleared the interest due**, even if **some charges are still unpaid**, **no dishonour charge** should be applied.

| Condition | Behaviour |
| --- | --- |
| Interest due is unpaid

(Interest due is >1 Rs) | Apply Dishonour fees |
| Interest due is paid, charges due is not paid | Do not apply Dishonour fees |
| Payment made after 6 PM on 7th	 | Considered in review (no charge if interest is paid) |
| No mandate registered or mandate revoked	 | Reviewed like all others |

## User stories / User flow

### Scenario 1

- Due collection request is created for the user for Rs 100 interest and Rs 100 charges (Total 200 Rs)
- Mandate presentation request is created (collection)
- Mandate presentation for the user fails due to insufficient balance on 7th.
- User makes a repayment of 100 Rs which is apportioned towards interest due as per apportionment logic on the 7th
- On 8th at 2 AM, collection is reviewed, user had an interest due of Rs 0, dishonour charges will not be applied.

### Scenario 2

- Due collection request is created for the user for Rs 100 interest and Rs 100 charges (Total 200 Rs)
- Mandate presentation request is created (collection)
- Mandate presentation for the user fails due to insufficient balance on 7th.
- User makes a repayment of 95 Rs which is apportioned towards interest due as per apportionment logic on the 7th
- On 8th at 2 AM, collection is reviewed, user had an interest due of Rs 5, dishonour charges will be applied.

### Scenario 3

- Due collection request is created for the user for Rs 0 interest and Rs 100 charges (Total 100 Rs)
- Mandate presentation request is created (collection)
- Mandate presentation for the user fails due to insufficient balance on 7th.
- On 8th at 2 AM, collection is reviewed, user had an interest due of Rs 0, dishonour charges will not be applied.

### Scenario 4

- Due collection request is created for the user for Rs 100 interest and Rs 100 charges (Total 200 Rs)
- Mandate presentation request is created (collection)
- Mandate presentation for the user fails due to insufficient balance on 7th.
- User makes a repayment of 99.8 Rs which is apportioned towards interest due as per apportionment logic on the 7th
- On 8th at 2 AM, collection is reviewed, user had an interest due of Rs 0.2, dishonour charges will not be applied.

### Scenario 5

- Due collection request is created for the user for Rs 100 interest and Rs 100 charges (Total 200 Rs)
- Mandate presentation request fails for the user as the mandate status was revoked
- On 8th at 2 AM, collection is reviewed, user had an interest due of Rs 100, dishonour charges will be applied.

### Scenario 6

- Due collection request is created for the user for Rs 5 interest and Rs 4 charges (Total 9 Rs)
- Mandate presentation request fails for the user as the mandate status was revoked
- As total due amount is less than 10 Rs, interest due and charges due will be waived for the user
- No review task will be created for the user

# **Design**

![image.png](Dishonour%20charge%20enhancement/image.png)

---

# **Analytics**

NA

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

## **Release Notes**