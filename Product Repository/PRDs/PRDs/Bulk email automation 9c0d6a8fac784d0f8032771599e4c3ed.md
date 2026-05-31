# Bulk email automation

: Ayush Kumar
Created time: September 11, 2024 4:19 PM
Status: Not started
Last edited: October 14, 2024 2:40 PM
Owner: Ayush Kumar

# **What problem are we solving?**

- All emails that are directed to [operations@voltmoney.in](mailto:operations@voltmoney.in) trigger automatic ticket creation and assignment without distinction, leading to delays in addressing urgent queries. Lender query emails sent to [operations@voltmoney.in](mailto:operations@voltmoney.in) are not prioritized due to this.
- Individual lien removal emails are sent manually to BAJAJ along with bulk emails comprising of individual lien removal request, resulting in duplicate data being sent for the same case twice in a day.
- Improving the communication after Pledging and Agreement as in case of Line Enhancement, the customer’s securities which are pledged gets lodged against the LAN irrespective of the fact the the Agreement was signed by the customer. We are sending communications regarding Lodgement in both the mails.

---

# **How do we measure success?**

- Number of tickets being created at ZenDesk should reduce.
- Operational efficiency in tracking cases regarding the lien removal, foreclosure, account opening and lodgement, margin pledge and line enhancement should increase.

---

# **How are others solving this problem?**

---

# **What is the solution?**

—> Lien Removal and Foreclosure emails should **not be sent** individually to lender(BAJAJ). For sending communications regarding Lien Removal and Foreclosure, we will send bulk reports as follows:

1. Update recipient and CC fields for individual Lien Removal and Foreclosure emails send to Volt:
- Change the recipient from [operations@voltmoney.in](mailto:operations@voltmoney.in) to [support.internal@voltmoney.in](mailto:support.internal@voltmoney.in)
    
    This ensures that tickets are not created for each Lien Removal and Foreclosure request
    

- Remove all other recipients and CCs, keeping [support.internal@voltmoney.in](mailto:support.internal@voltmoney.in) as the sole recipient
    
    This includes removing [las.crm@bajajfinserv.in](mailto:las.crm@bajajfinserv.in) and [las.collateral@bajajfinserv.in](mailto:las.collateral@bajajfinserv.in) in particular from individual emails
    
    Earlier the Email was sent to:
    
    ![image.png](Bulk%20email%20automation/image.png)
    
    Now, the email will sent:
    
    Email sent from: [no-reply@voltmoney.in](mailto:support.internal@voltmoney.in)
    
    Email sent to: [support.internal@voltmoney.in](mailto:support.internal@voltmoney.in)
    
    **Unpledging:**
    
    ![image.png](Bulk%20email%20automation/image%201.png)
    
    **Foreclosure:**
    
    ![image.png](Bulk%20email%20automation/image%202.png)
    
1. Implement a automatic daily bulk reporting process for Lien Removal and Foreclosure requests to BFL:

**Lien Removal:**

**CURRENT:**

- The sheet containing the individual Revocation requests raised each day is sent to [operations@voltmoney.in](mailto:operations@voltmoney.in) from [no-reply@voltmoney.in](mailto:support.internal@voltmoney.in). (The email template is attached below)
- The sheet is then send as a bulk email to BFL by the ops team, with the following recipients:

—> [las.crm@bajajfinserv.in
—>](mailto:las.crm@bajajfinserv.in) [las.collateral@bajajfinserv.in
—>](mailto:las.collateral@bajajfinserv.in) [satirtha.joshi@bajajfinserv.in](mailto:satirtha.joshi@bajajfinserv.in)

- The bulk email is sent from [operations@voltmoney.in](mailto:operations@voltmoney.in)

**CHANGES:**

- The sheet containing the individual Revocation requests raised each day should be sent to

—> [operations@voltmoney.in](mailto:operations@voltmoney.in) 

—> [las.crm@bajajfinserv.in
—>](mailto:las.crm@bajajfinserv.in) [las.collateral@bajajfinserv.in
—>](mailto:las.collateral@bajajfinserv.in) [satirtha.joshi@bajajfinserv.in](mailto:satirtha.joshi@bajajfinserv.in)

        from [no-reply@voltmoney.in](mailto:support.internal@voltmoney.in).

**Foreclosure:**

- This is the sheet we have to prepare containing the individual Foreclosure requests raised each day which is sent to [operations@voltmoney.in](mailto:operations@voltmoney.in) from [no-reply@voltmoney.in](mailto:support.internal@voltmoney.in). (The email template is attached below)

**Note: Lender Loan account number should not be blank in the foreclosure sheet (validation)**

         **: FORECLOSURE STATUS as FAILED should not be considered.**

- The sheet is then send as a bulk email to BFL by the ops team, with the following recipients:

—> [las.crm@bajajfinserv.in
—>](mailto:las.crm@bajajfinserv.in) [las.collateral@bajajfinserv.in
—>](mailto:las.collateral@bajajfinserv.in) [satirtha.joshi@bajajfinserv.in](mailto:satirtha.joshi@bajajfinserv.in)

- The bulk email is sent from [operations@voltmoney.in](mailto:operations@voltmoney.in) by the ops team
- Ops team will require foreclosure bulk emails to be sent automatically to

—> [las.crm@bajajfinserv.in
—>](mailto:las.crm@bajajfinserv.in) [las.collateral@bajajfinserv.in
—>](mailto:las.collateral@bajajfinserv.in) [satirtha.joshi@bajajfinserv.in](mailto:satirtha.joshi@bajajfinserv.in)

after testing for 10 days similar to lien removal emails.

Field mapping to DB tables:

| **Credit ID** | **Lender partner ID** | **Loan Account Number** | **Loan Contract Number** | **Customer Name** | **VOLT Request ID** | **Request created On** | **Customer PAN** | **Net Payable** | **Collection ID** | **Amount Collected** | **Time of collection** | **Transaction ID** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| credits | credits | credits | credits | borrower_accounts | foreclosure_request | foreclosure_request | borrower_accounts | credits | collections | collections | collections | tranctions |

[foreclosure_data.py](Bulk%20email%20automation/foreclosure_data.py)

[foreclosure_email_account.py](Bulk%20email%20automation/foreclosure_email_account.py)

1. Email format for the automated mail which will be sent to BAJAJ containing individual foreclosure requests raised in a day as a bulk along with the attached sheet(**Volt - BFL Foreclosure request report**). (Same template as below for lien removal)

<aside>
💡

# Volt - BFL Foreclosure request report

Dear Team,

Please find the attached reports for DD-MM-YYYY

Please note :

- Revocation requests in the report are for  to
    
    6 PM, DD-MM-YYYY
    
    6 PM, DD-MM-YYYY
    

Please review the attached files for more detailed information.

---

</aside>

Template ID: d-2a9e6e4dde394c579eec4211290b3aed   (For Foreclosure MIS)

1. This has been implemented for the individual Lien Removal requests sent as a bulk to BAJAJ. The sheet is sent manually to BAJAJ by the ops team as of now. We have to automate the process and implement it for foreclosure.
- The Email format for the automated mail which will be sent to BAJAJ containing individual lien removal requests raised in a day as a bulk along with the attached sheet.

<aside>
💡

![image.png](Bulk%20email%20automation/image%203.png)

</aside>

Template ID: d-e81d65b641f94be3b2d0917fb1257503     (For Revocation MIS)

## Requirements overview (optional)

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