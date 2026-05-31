# [Volt LSP] Pre fill bank account number from MFC data

: Saksham Srivastava
Created time: December 26, 2024 2:23 PM
Status: In progress
Last edited: December 27, 2024 10:40 AM

# **What problem are we solving?**

Customers on the bank verification step are currently required to enter their complete Bank account number and IFSC code to verify their bank account this is a pain for customers. 

[https://app.amplitude.com/analytics/volt-hq/chart/vnjl9new/edit/5ajc3t99](https://app.amplitude.com/analytics/volt-hq/chart/vnjl9new/edit/5ajc3t99)

---

# **How do we measure success?**

- Bank verification conversion should improve
- TAT between customer initiating and completing should be reduced Bank account verification

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

- For customers fetching from MFCentral (currently from partners such as PhonePe, Jupiter or direct B2C from check eligibility page; This will be extended to in-app MFC fetch as well), pre-fill Bank account details for the customer as they come to the Bank verification step.
- MFC shares bank details of the customer used to make investment in each folio.

[MFC Fetch](%5BVolt%20LSP%5D%20Pre%20fill%20bank%20account%20number%20from%20MFC%20d/8768d87e-4895-4b2c-8c06-1e55c48611cf_1735201563630.json)

![Screenshot 2024-12-27 at 9.36.11 AM.png](%5BVolt%20LSP%5D%20Pre%20fill%20bank%20account%20number%20from%20MFC%20d/Screenshot_2024-12-27_at_9.36.11_AM.png)

- Fetch account number and IFSC of the banks linked to customer folios
- Post the bank verification start page, customer should land on the below screen to select one of the bank accounts fetched from MFC
    
    ![Screenshot 2024-12-26 at 6.06.04 PM.png](%5BVolt%20LSP%5D%20Pre%20fill%20bank%20account%20number%20from%20MFC%20d/Screenshot_2024-12-26_at_6.06.04_PM.png)
    
- **Validations** -
    - Check if the bank IFSC is in the IFSC whitelist, if not, don’t show the particular bank account.
    - Check bank IFSC with the lender approved list, if not, don’t show the particular bank account.
    - If there are two entries of bank account with same bank acc number and different IFSC codes. Discard both and don’t show these in the UI.
- Monitoring requirement - Post release of this feature monitor bank verification errors to make sure this feature doesn’t result in increased errors on this errors.
- In case, MFC is not able to provide bank data or data is rejected because of validations on our end customer should directly move to the add bank account flow (Same as current flow).

FE requirement

- Customers might be surprised on how did we get their bank account details without them entering this information, they should be educated on where did we get the Bank verification data from. Include the top callout shown in the design below. [Figma.](https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=1548-48120&t=PmqQ7rXopNdWKkbR-0)
    
    ![image.png](%5BVolt%20LSP%5D%20Pre%20fill%20bank%20account%20number%20from%20MFC%20d/image.png)
    
- This callout should only be shown to the customers on this page when they have not added an additional bank account yet. If customer add an additional bank account the callout should not be shown.

## User stories / User flow

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