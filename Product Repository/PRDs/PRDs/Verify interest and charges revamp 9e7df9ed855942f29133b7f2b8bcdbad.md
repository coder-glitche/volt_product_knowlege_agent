# Verify interest and charges revamp

: Saksham Srivastava
Created time: June 3, 2024 11:11 AM
Status: Not started
Last edited: February 21, 2025 12:28 PM

# **What problem are we solving?**

1. One day conversion rate of Verify interest and charges page is ~46%
2. Most users are dropping off this screen because of the following problems:
    1. Users think that this is the last page of the application.
        1. “Mutual fund lock ho jayega”
        2. “Loan ho jayega agar aagay jayegay”
    2. Benefits are not properly communicated. key benefits such as
        1. One time processing fee
        2. OD
        3. Interest only EMI
        4. Unlimited withdrawals and repayments are not shown to the user
    3. User thinks that the “Pledge Funds” value is too high.

---

# **How do we measure success?**

Current 1d conversion rate of the verify interest and charges page: 

[https://app.amplitude.com/analytics/volt-hq/chart/new/r1zby656](https://app.amplitude.com/analytics/volt-hq/chart/new/r1zby656)

We will directly track the conversion rate of the following page and measure impact. 

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

1. User should be able to see the updated design to show benefits as well on the verify interest and charges page.
2. User will see two tool tips, which will educate users about interest charged and loan tenure. 
3. Based on the interest rate of the user, user should see how much avg interest will user pay monthly on a withdrawal of ₹10,000. Formula will be: (ROI%/365)*30*10000.
4. For each charge user will be have a dropdown to expand and get more information on the particular charge. The copies here are unchanged for now. 
5. User will only be shown charges shown in the updated design. 
6. User will be allowed to change the registered state, basis which the stamp duty will increase. 

## Requirements

1. Change the page title to “Loan offer”.
2. Change the CTA to “Get more details”

---

# **Design**

Final design: [https://www.figma.com/design/DvtYv9CUzQjyTqhfupbljC/Dashboard?node-id=626-50885&t=bYaviAQ3yNGvZZGM-11](https://www.figma.com/design/DvtYv9CUzQjyTqhfupbljC/Dashboard?node-id=626-50885&t=bYaviAQ3yNGvZZGM-11)

[Design requirements](Verify%20interest%20and%20charges%20revamp/Design%20requirements%20b06802343faf49a49415406805edc2f1.md)

---

# **Analytics**

Amplitude analytics to be setup: [https://docs.google.com/spreadsheets/d/1mx2ktWwy3UkUFRtG7mVPxx9v4yN6beo5mbrM2E9ht28/edit?gid=1183851218#gid=1183851218&range=A1](https://docs.google.com/spreadsheets/d/1mx2ktWwy3UkUFRtG7mVPxx9v4yN6beo5mbrM2E9ht28/edit?gid=1183851218#gid=1183851218&range=A1)

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