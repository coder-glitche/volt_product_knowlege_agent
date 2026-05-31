# In app user review [Play store]

: Ranjan kumar Singh
Created time: August 5, 2024 3:49 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

We currently do not collect user experience feedback directly at key moments in the app journey, which has led to the following challenges. 

- **Missed Pain Points:** Without timely feedback, we risk missing critical pain points during specific stages of the app journey, such as loan applications, payments, or withdrawals. These missed insights can result in unresolved issues, leading to decreased user satisfaction.
- **Lost Improvement Opportunities:** Journey-based feedback offers real-time insights into what’s working and what needs improvement. Without this feedback, we may miss opportunities to innovate and optimize features, slowing down our product’s evolution.
- **Delayed Problem Detection:** Not collecting feedback "in the moment" means we only discover issues after they’ve affected a large number of users, leading to increased churn rates and reduced retention.
- **Poor Prioritization of Development:** Lacking direct user feedback makes it challenging to effectively prioritize feature enhancements or bug fixes, possibly leading to the wrong areas being addressed.
- **Negative Impact on User Satisfaction:** Unaddressed user frustrations due to the absence of timely feedback can result in negative reviews, poor word-of-mouth, and overall dissatisfaction with the app, which could impact long-term user loyalty.

To address these, we are planning to implement journey-based user experience feedback collection.

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview

We are planning to implement a real-time, journey-based user feedback feature on our Volt apps to capture insights at key moments of the user experience.

- Implementing journey-based feedback pop-ups.
- We will add “Share feedback” CTA on success/failure page of each request
    - Redirect user to dedicated feedback page when user click on share feedback CTA.
- User can provide product/service related feedback anytime from the dedicated feedback collection page.
    - User profile page > Share feedback > Open feedback form
- Nudging satisfied user to rate us on Play store/App store

## User stories / User flow

User flow: https://www.figma.com/board/iKWb40YwUDawQg3p5J85yf/User-feedback?node-id=52-156&t=0WSVaL4NCjtrdLgO-1

## Requirements

1. Config to enable feedback collection feature: we should be able to enable feature based on below parameters; Ex: If feature is enable for “VOLT_MOBILE_APP” && Channel = B2C then feedback feature should be only enabled for platform volt money app and for B2C channel
    - Platform [VOLT_MOBILE_APP,PHONEPE]
    - Channel [B2C]
    - Lender [TATA, BAJAJ, DSP]
    - xPlatform [Web, Android, iOS]
2. Config to trigger feedback pop-up based on user journey.
    1. Collect feedback about the loan application experience
        1. Trigger condition: 
            1. New loan application
            2. Loan account opened successfully 
            3. Lodgement is complete
            4. New loan application feedback status = Pending
    2. Collect feedback about the withdrawal experience
        1. Trigger condition:
            1. Second withdrawal
            2. Second withdrawal status is settled
            3. Withdrawal feedback status = Pending
    3. Collect feedback about the repayment experience
        1. Trigger condition:
            1. Second repayment
            2. Second repayment status is settled
            3. Repayment feedback status = Pending
    4. Collect feedback about the lien removal experience [P1]
    5. Collect feedback about the foreclosure experience [P1]
3. Manage feedback form content
    1. Event based feedback modal
        1. When user select the rating [Very bad - Excellent], based on the selection we need to ask the follow up question from the user.
            1. Follow up question mapped with scale should come from the backend
            2. For each trigger type follow up question will vary.
                1. Example: 
                
                {
                "feedback": {
                "repayment": {
                "scale_1_3": {
                "options": ["A", "B", "C"]
                },
                "scale_4": {
                "options": ["1", "2", "3"]
                }
                },
                "withdrawal": {
                "scale_1_3_4": {
                "options": ["A", "B", "C"]
                },
                "scale_4": {
                "options": ["1", "2", "3"]
                }
                }
                }
                }
                

1. Logic to manage the feedback status

| Journey | Scenario | Feedback status |
| --- | --- | --- |
| Loan application | User completed the loan application | loan application feedback = Pending |
| Loan application | User closed the loan application feedback form | loan application feedback = Closed |
| Loan application | User submitted the loan application feedback form | loan application feedback = Completed |
| Loan application | If submitted feedback form from the profile section after selecting loan application | loan application feedback = Completed |
| Withdrawal | By default | Withdrawal feedback = Pending |
| Withdrawal | User closed the withdrawal feedback form | Withdrawal feedback = Closed |
| Withdrawal | User completed the withdrawal feedback form | Withdrawal feedback = Completed |
| Withdrawal | If submitted feedback form from the profile section after selecting withdrawal | Withdrawal feedback = Completed |
| Repayment | By default  | Repayment feedback = Pending |
| Repayment | User closed the repayment feedback form | Repayment feedback = Closed |
| Repayment | User completed the Repayment feedback form | Repayment feedback = Completed |
| Repayment | If submitted feedback form from the profile section after selecting repayment | Repayment feedback = Completed |

---

# **Design**

[https://www.figma.com/design/ns4QtJTdQItBNHHDLs7YcK/User-feedback?node-id=8-1998&t=iqSp0fu7FRgWn75R-0](https://www.figma.com/design/ns4QtJTdQItBNHHDLs7YcK/User-feedback?node-id=8-1998&t=iqSp0fu7FRgWn75R-0)

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

- Without direct feedback from users, making informed decisions about improving  products and services is challenging.
- Feedback pop-ups based on journey can help us collect feedback directly from your users and gain valuable insights into their needs and wants.
- User feedback can be great for getting an overview of your products from a fresh perspective to uncover problem areas and get new ideas
- collecting in-app feedback directly from the customers will help you dig deeper into the specific customer pain points and offer a better customer experience.
- almost [**87%**](https://www.pointillist.com/blog/cx-survey-2021-journey-management-cx-measurement/) of companies consider customer experience to be the driving force behind customer loyalty and retention
- gathering in-moment feedback from the customers about the elements of the application that they don’t like or have a hard time understanding

Nudge User on Volt Money App to Rate us on Play Store. we can achieve this by three approaches:

### Approach 1: Ask User to Rate Us Based on Events

1. **Criteria for Prompting:**
    - Users who have been using the app for at least 1 month.
    - The user's last withdrawal status is settled.
2. **Process:**
    - Ask the user to share their experience when user lands on app:
        - If the shared experience is positive, then prompt the user to rate the app on the Play Store.
        - If the shared experience is negative, capture the feedback and make it visible to the OPS/Sales and Product teams. This allows sales or product teams to call and understand the issue with the customer.
    - Do not ask the user to rate if they have already provided feedback through the feedback prompt modal.

### Approach 2: Create a “Rate Us” Section in User Profile Page

1. **User-Initiated Rating:**
    - Add a “Rate Us” section in the user profile page.
2. **Process:**
    - On user CTA click, take the user to the Play Store for rating.
    - Create a deep link and send it to satisfied users to rate the app on the Play Store.

### Approach 3: Combination of Approach 1 and Approach 2

1. **Integrated Strategy:**
    - Implement both approaches on the app.
2. **Process:**
    - Use event-based prompts to ask users to rate the app, following the criteria and process outlined in Approach 1.
    - If the user skips the rating based on event triggers, they should still have the option to rate the app by navigating to the “Rate Us” section in the user profile page.

### Pro and Cons

|  | Pro | Cons |
| --- | --- | --- |
| Approach 1 | 1. Users who have been with the app for at least a month and have successfully completed transactions are more likely to provide meaningful feedback.

2. Users are only prompted to rate the app when they are likely to be satisfied, potentially increasing positive ratings on the Play Store.

3. Negative feedback is captured and directed to the appropriate teams (OPS/Sales and Product), allowing for timely intervention and improvement.

4. Asking users to share their experience can make them feel valued and heard, improving overall user engagement and satisfaction.
 | Play store guideline says: 

”Your app should not ask the user any questions before or while presenting the rating button or card, including questions about their opinion (such as “Do you like the app?”) or predictive questions (such as “Would you rate this app 5 stars”).”

**To avoid this: Instead of opening rating modal on app, we can show thank you message to user and on same modal we can show ”Rate us on play store/app store” CTA** |
| Approach 2 | 1. The option to rate the app is always visible and accessible, which can capture ratings from users who are particularly motivated to provide feedback.

2. Users can choose when to rate the app, reducing the feeling of being pressured or interrupted by prompts.

3. Easier to implement  | 1. Users may ignore the “Rate Us” section, leading to fewer ratings and potentially missing out on capturing feedback from satisfied users.

2. Chances to get low rating from the user |

Play store in app rating API doc and guideline: [https://developer.android.com/guide/playcore/in-app-review](https://developer.android.com/guide/playcore/in-app-review)