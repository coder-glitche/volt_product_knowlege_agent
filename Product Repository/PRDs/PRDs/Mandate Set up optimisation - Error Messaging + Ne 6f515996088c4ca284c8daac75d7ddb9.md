# Mandate Set up optimisation - Error Messaging + New Flow + Tracking improvements

: Vaibhav Arora
Created time: February 22, 2024 9:36 AM
Status: Ready for Tech
Last edited: November 8, 2024 12:55 PM
Owner: Vaibhav Arora
Tasks: Mandate issues (https://app.notion.com/p/Mandate-issues-b2d58f93a1ce4632baf35b013a1b046d?pvs=21)
Due Date: 22/02/2024

# **What problem are we solving?**

Setting a mandate is an important step in our loan application process. However only 30-40% of our users are able to set up a mandate successfully in their first attempt.

Other users end up either dropping or relying on our RMs to assist them with the journeys. RMs do not have clarity on the kind of errors the users are facing and what is the optimal way to help the user in completing the process.

We currently use Digio for setting up e-mandates for the loan application journey of BFL and Tata’s own e-mandate flow for Tata’s application journey.

Currently we solve this problem by the following measures:

- Switching lenders (Tata → Bajaj) to be able to set up physical mandates
- Asking users to change bank accounts

https://docs.google.com/spreadsheets/d/1KN3VFNOq2g3P6u4kC8RsrjCZ0PX5ulh4n2pK1EEMmQU/edit?usp=sharing

https://docs.google.com/spreadsheets/d/1duBekviW-pSHlWOep-TVnDFcJPA-y3B8moudMckdvok/edit?usp=sharing

https://docs.google.com/spreadsheets/d/16vRADy-je6wcJL4yWnV7gYmKc1X7yOAa67ZkxFQdjRE/edit#gid=0

Primary Problems:

- User
    - General messaging to the user “Something went wrong” in case of all errors that does not mention the exact error and actionable steps to resolve
    - Incorrect information regarding mandate amount is being passed on to the customer which leads to confusion and dissonance
- Ops
    - Ops team rely on engineering team on identifying issues ( and pin point if it is an internal error, bank level error and user side error) which increases our resolution TAT and loan application time
    - Lack of clarity and tools with Ops to identify, understand, and solve mandate errors
- Tracking and Data
    - Lack of tracking and measurement of errors and their respective resolution to build product/process based solutions

---

# **How do we measure success?**

- Number of attempts it takes (on average) a user to complete a mandate set up request
- Mandate failure rate (most common errors on a unique application level)
- Bank level analysis of mandate failure rates (if some issues are specific to some banks)
- Self served error handling on user level, where user retried basis the error presented to them and was successfully able to set up the mandate without ops help

---

# **How are others solving this problem?**

Competitor Study:

- Cred, Smallcase, 50fin, and other primary LAS and PL service providers have not handled specific errors to assist users in the process.
- 50fin and Dhanlap have built strong operational follow up flows where they identify journey drop offs and close pending requests

---

# **What is the solution?**

We intend to solve this issue with a three pronged approach:

- Communicating and enabling users to identify and solve issues by themselves by providing contextual messaging and CTAs
- Sharing exact issues on Retool against mandate set up step for ops team to assist the user better and not rely on tech team for RCA

## Requirements overview (optional)

## User stories / User flow

https://drive.google.com/file/d/1R0KaqYA16QAcyFy4gwRA6kY_cmvvH3Dg/view?usp=sharing

User Flow Diagram

## Requirements

- Handle error codes from Digio and Tata and show respective designs (Headings + Copy as per design below) error messages compiled in:
    - https://docs.google.com/spreadsheets/d/1KN3VFNOq2g3P6u4kC8RsrjCZ0PX5ulh4n2pK1EEMmQU/edit?usp=sharing
- New UI Screen with bank account error directing user to add another bank account to set up mandate
- Copy change on mandate creation screen to explain mandate amount to the user
- Amplitude event creation: Need help on Mandate error bottom sheet with event name “MANDATE_ERROR_HELP_BUTTON_CLICKED” and log error message as event property in the event for user journey level tracking in event field “error_message”
- Populate error message on retool as remarks (create new parameter) in search customer tab in “details of application by pan number” against mandate set up stage
    - Remarks would be a general field which can be utilised to show current errors for the respective steps in the user journey in user look up which can assist support team to identify issues and handle escalations as per support SOP.

---

# **Design**

[https://www.figma.com/file/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?type=design&node-id=6867-31798&mode=design&t=kvshiqPir530gTsR-0](https://www.figma.com/file/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?type=design&node-id=6867-31798&mode=design&t=kvshiqPir530gTsR-0)

---

# **Analytics**

---

# **Timeline/Release Planning**

---

# **Go to market**

NA

## Marketing

NA

## Ops & Sales training

Customer Support Manual Addendum (Check Support Manual)

https://docs.google.com/spreadsheets/d/1KN3VFNOq2g3P6u4kC8RsrjCZ0PX5ulh4n2pK1EEMmQU/edit#gid=501172732

## Frequently asked questions (FAQs)

- Why is my mandate amount higher than my loan amount? (user)
- My mandate request failed, what do I do next? (user)
- X user’s mandate is failing, how do we solve it? (Ops)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - Prepare queries to measure impact
    - Check self served journey (dependency: [Measuring Customer Support Events and 5XX errors](Measuring%20Customer%20Support%20Events%20and%205XX%20errors%20a1fc72e84d234f74b38715c8a1afdcfd.md))
    - Ops workflow training and customer support manual
- [ ]  Business
    - [ ]  -
- [ ]  Design
    - Design Review: https://www.figma.com/file/u5fpymb6jC6ubzT9YUXFgb/Loan-application-flow?type=design&node-id=12-1280&mode=design&t=IW8SSMKuE3OVsKYp-0

![Untitled](Mandate%20Set%20up%20optimisation%20-%20Error%20Messaging%20+%20Ne/Untitled.png)

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

[Analytics Requirement: Mandate issues](Mandate%20Set%20up%20optimisation%20-%20Error%20Messaging%20+%20Ne/Analytics%20Requirement%20Mandate%20issues%20b4f283980ab44ecf802498987cc95ada.md)

[Analytics Requirement: Name verification (TCL)](Mandate%20Set%20up%20optimisation%20-%20Error%20Messaging%20+%20Ne/Analytics%20Requirement%20Name%20verification%20(TCL)%20d2758e3664374b399ecbeb25cf2f1d0b.md)

## Meeting notes

[Digio <> Volt: Exploring mandate authorisation flows](Mandate%20Set%20up%20optimisation%20-%20Error%20Messaging%20+%20Ne/Digio%20Volt%20Exploring%20mandate%20authorisation%20flows%20100466f1c1df45ddabecda2324fa605e.md)

# Action Items:

- Understand how many physical and manual mandate switches we do from Digio to Bajaj