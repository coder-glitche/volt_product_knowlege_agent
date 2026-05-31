# Application form, T&C and Agreement updation

: Ayush Kumar
Created time: November 18, 2024 11:39 AM
Status: Not started
Last edited: April 4, 2025 1:49 PM

# **What problem are we solving?**

RBI guidelines requires that lenders and LSP showcase the Agreement, Application form and T&C clearly as per the specified format. Meeting the compliance and clearly stating the terms to user in a elegant way is a challenge.

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## Requirements:

1. **I have attached the TATA specific and enhancement Agreement with the changes highlighted in the document attached below:**
- LAS_Specific_Agreement:

[https://docs.google.com/document/d/1EGdJXuOz8M70BooRDQUBsWPRmliBhDQJnaGSjXsoLak/edit](https://docs.google.com/document/d/1EGdJXuOz8M70BooRDQUBsWPRmliBhDQJnaGSjXsoLak/edit)

- LAS_Enhancement_Agreement:

[https://docs.google.com/document/d/18xR7TfjSOmWpNM_VfRKBxiHQjglABd_dWa8cX5ZWVcA/edit](https://docs.google.com/document/d/18xR7TfjSOmWpNM_VfRKBxiHQjglABd_dWa8cX5ZWVcA/edit)

1. **Attaching below the updated application form with the mapped variables.**

[https://docs.google.com/document/d/1j2pmg2iPvu23ZKeABu3VS8C7DwIjEOxqyozbYORB3qU/edit](https://docs.google.com/document/d/1j2pmg2iPvu23ZKeABu3VS8C7DwIjEOxqyozbYORB3qU/edit)

- This doc has to be converted to pdf format and uploaded to webtop after the Agreement step.
- **Open points:** I have not mapped BE variables for the fields **Title, Aadhaar (last 4 digits)** in the application form. I have randomly assigned a value against that.

1. **TATA T&C also has to be updated and I have created a JIRA story for the same. Please find the link below:**

The TATA Capital limited (TCL) T&C needs to be changed.

Attaching the updated T&C of TATA: [LAS-Digital- T&C Sep2024_template (2)](https://docs.google.com/document/d/1vtc7euKFPOWNCXv_wVKmepJjgXAqvFzLSQjhzamqeos/edit)

![](https://developers.google.com/drive/images/drive_icon.png)

The T&C displayed at: [Volt Money | Learn about our privacy policy and data protection policy](https://voltmoney.in/terms-tata-capital-las) has to be updated with [LAS-Digital- T&C Sep2024_template (2)](https://docs.google.com/document/d/1vtc7euKFPOWNCXv_wVKmepJjgXAqvFzLSQjhzamqeos/edit)

![](https://voltmoney.in/favicon.svg)

![](https://developers.google.com/drive/images/drive_icon.png)

**JIRA story for reference:**

[https://voltmoney.atlassian.net/jira/software/projects/PSB/list?direction=ASC&filter=assignee%20%3D%20%22712020%3A8e4c7965-dee3-480e-b4c1-d7b3d1a3d9e6%22&selectedIssue=PSB-290&sortBy=assignee&text=tata](https://voltmoney.atlassian.net/jira/software/projects/PSB/list?direction=ASC&filter=assignee%20%3D%20%22712020%3A8e4c7965-dee3-480e-b4c1-d7b3d1a3d9e6%22&selectedIssue=PSB-290&sortBy=assignee&text=tata)

---

# **Design**

1. **Fields required at the KYC Verification—> Additional Information Screen**

Figma design link: [https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/[New]-Loan-application-journey?node-id=28-20617&node-type=section&t=FRk4X7nmIzDXa51Q-0](https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=28-20617&node-type=section&t=FRk4X7nmIzDXa51Q-0)

- Qualification
    - Upto 12
    - Diploma
    - Graduate
    - Post Graduate
- Purpose of loan
    
    The Purpose of loan is currently called End use of loan. We can can rename it for better communication to the users and the dropdown values are listed below:
    
    | Wedding |  |
    | --- | --- |
    | Personal |  |
    | Emergency |  |
    | Education |  |
    | Holiday/Vacation |  |
    | Others |  |
    | Business |  |
    | Investments |  |
- **Occupation**
    
    New addition
    
    - Student
    - Salaried
    - Self Employed
    - Retired
- **Source of income**
    
    New addition
    
    - Employment
    - Self-Employment
    - Investment
    - Rental
    - Retirement
    - Other (e.g. gifts, inheritances, royalties)
- Income range
    - 3 - 10 lacs
    - 10 - 25 lacs
    - More than 25 lacs

**Note: We are removing the input fields for the Mother’s Name from the UI**

- UI Changes for above:
    
    ![image.png](Application%20form,%20T&C%20and%20Agreement%20updation/image.png)
    

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

9:41

9:41

9:41

9:41

KYC Verification

Share

KYC Verification

Share

KYC Verification

Share

KYC Verification

Share

KYC

Bank account

AutoPay

Agreement

KYC

Bank account

AutoPay

Agreement

KYC

Bank account

AutoPay

Agreement

KYC

Bank account

AutoPay

Agreement

Additional information

Additional information

Additional information

Additional information

Marital status

Marital status

Marital status

Marital status

Single

Married

Single

Married

Single

Married

Single

Married

Qualification

Qualification

Qualification

Qualification

Select qualification

Select qualification

Select qualification

Select qualification

Father’s name

Father’s name

Father’s name

Father’s name

First name

Last name

First name

Last name

First name

Last name

First name

Last name

Purpose of loan

Purpose of loan

Purpose of loan

Purpose of loan

Select purpose

Select purpose

Select purpose

Select purpose

Occupation

Occupation

Wedding

Occupation

Occupation

Select occupation

Education

Select occupation

Select occupation

Select occupation

Source of income

Source of income

Travel

Source of income

Student

Source of income

Medical expenses

Salaried

Select source of income

Select source of income

Select source of income

Select source of income

Home Renovation/Decor

Self employed

Income range

Income range

Other purpose

Income range

Income range

Employment

Retired

Self employment

Select income

Select income

Select income

Select income

Investment

Your data is secure with us

Rental

Continue

Your data is secure with us

Your data is secure with us

Retirement

Continue

Continue

Other (e.g., gifts, inheritances, royalties)

Additional information

Marital status

Single

Married

Qualification

Your data is secure with us

Graduate

Continue

Father’s name

9:41

9:41

Father’s first name

Father’s last name

KYC Verification

Ayush

KYC Verification

Kumar

Share

Share

KYC

Bank account

AutoPay

Agreement

KYC

Purpose of loan

Bank account

AutoPay

Agreement

9:41

Additional information

Travel

KYC Verification

Share

Marital status

Occupation

KYC

Bank account

AutoPay

Agreement

Single

Married

Salaried

Additional information

Qualification

Marital status

Select qualification

Source of income

Single

Married

Employment

Qualification

Father’s name

First name

Last name

Income range

Graduate

Please enter father’s name as per PAN

Error handling in red

Select income

Father’s name

Description

Current functionality: Auto scroll to the field below when last field in the viewport is clicked

Father’s first name

Father’s last name

Purpose of loan

Description

Ayush

Kumar

Select purpose

Your data is secure with us

Purpose of loan

Occupation

Continue

Wedding

Select occupation

Occupation

Source of income

Salaried

Select source of income

Source of income

Income range

Employment

Select income

Income range

10 - 25 lakhs

Your data is secure with us

Continue

Your data is secure with us

Continue