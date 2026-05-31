# Term Loan: Customer Statements

# **What problem are we solving?**

Customers availing term loans against mutual funds will want to have a clear visibility of their **collateral, loan obligations, tranche-level details, and closure status**. These statements will help in solving the below:

- Customer confusion on pledged securities and their valuation.
- Lack of transparency around principal outstanding, EMI dues, and charges at the loan and tranche level.
- Difficulty in obtaining official proof of loan closure (No Dues Certificates).
- Increased customer support queries and operational overhead for servicing teams.

We need a standardized set of customer-facing statements that provide clarity, compliance, and ease of use across the lifecycle of a loan.

---

# **How do we measure success?**

- Reduction in customer queries related to outstanding dues / pledged holdings / loan closure.
- Higher adoption of digital self-service (customers accessing statements via app rather than calling RM/ops).
- Compliance with RBI Fair Practices Code (statement of account requirement) and SEBI depository guidelines (pledge/holding disclosure).
- Improved customer experience with transparent, timely, and easy-to-understand statements.

---

# **How are others solving this problem?**

- **Banks (HDFC, ICICI, Axis)** → Provide separate loan account statements and pledge confirmation slips via net banking/email.
- **NBFCs (Bajaj Finance, Aditya Birla Finance, DSP Finance)** → Issue periodic statements of accounts and No Dues Certificates (NDC) on closure.
- **Broker-led LAS journeys (Zerodha, Upstox, Kotak Sec)** → Offer holding/pledge details through the demat CAS (Consolidated Account Statement), but loan dues are shown separately by the NBFC partner.
- Most players do not provide consolidated tranche-level views, requiring manual reconciliation by customers.

---

# **What is the solution?**

We will design and deliver **five standard customer statements** for the Term Loan Against Mutual Funds product in V0:

1. **Holding Statement**
    - We will be providing this to the customer so that they are informed about their Holdings with us.
2. **Statement of Accounts (Loan and Tranche)**
    - These documents will help the customer with an understanding about their Dues and transactions.
3. **Loan and Tranche No Dues Certificates (NOC) - Loan and Tranche**
    - When a Loan or a Tranche is closed/foreclosed we will be providing these statements.

---

Documents which CRED shares with their customers in their current product:

At loan level:

- sanction letter
- ⁠holding document

At each Tranche level:

- Loan agreement
- ⁠ key fact statement

If Tranche is closed

- NOC document

## **Requirements**

The Holding Statement, Loan SOA and Tranche SOA needs to be sent out in an email on the 1st of every month which is triggered to the customer’s email id. The email will have the following template:

Email Subject: **Statements for loan against mutual funds as on *{DD-MM-YYYY date}***

Dear *{Customer Name}*,

Thank you for your trust in DSP Finance. Please find attached your account statement and holding statement as on {DD-MM-YYYY date} for your loan against mutual funds with DSP Finance Pvt. Ltd.

Please follow the following steps given below for opening the attachment:

1. Click on the attachment provided with this email.

2. You will be prompted for your password.

3. The password is: The first four letters of your name in caps followed by year of birth (YYYY).

- In case your first name is less than 4 letters, use your complete first name in caps followed by year of birth (YYYY).

Please note: This statement may not include recent updates from collateral transactions(additions or removals), withdrawals, or repayments that are still being processed.

For any queries or feedback, please write to us at support@dspfin.com

Phone

022-414-84529

Email

support@dspfin.com

Registered Address: Mafatlal Centre, 11th Floor, Nariman Point, Mumbai - 400 021

This is an auto generated email. The details mentioned in this email are for sole use by the recipient and not for circulation.

www.dspfin.com

Policies and disclosures | Terms and conditions | Grievance redressal

Below is the exact template for the email which needs to be sent to the customer:

![Screenshot 2025-09-29 at 3.02.43 PM.png](Term%20Loan%20Customer%20Statements/Screenshot_2025-09-29_at_3.02.43_PM.png)

![Screenshot 2025-09-29 at 3.04.03 PM.png](Term%20Loan%20Customer%20Statements/Screenshot_2025-09-29_at_3.04.03_PM.png)

### Functional Requirements

Figma templates for the statements:

[Statements](https://docs.google.com/spreadsheets/d/1ZLBWSwd0E5Nnjh9VqbVSFzL9aO1UVUrE716XdjjkCkI/edit?usp=sharing): https://www.figma.com/design/CZ9HkE9u7JRE0UqcpAHclY/Statements--invoices--lending-stack?node-id=560-1179

### **Holding Statement:**

This statement will contain the details of the customer’s holdings. Below are the section required in the statement along with the parameters in each section:

**Header**: Same as OD

**Account Details**: 

- Name
- Client code
- Email id
- Mobile number
- Loan Status
- Address
- Account type
- Primary bank
- Loan account no.
- Account opened on
- Loan Expiry Date

All the parameters are same as OD except **Renewal Date and ROI**, which should not be present in Term Loan Holding statement. Loan Expiry Date is a new parameter which we need to add in the Holding Statement. We will be able to get the Account details information from the Client & Loan Details API provided by Finflux.

**Balance Summary:** Same as OD

- Drawing Power
- Outstanding Principal
- Excess Amount
- Available Cash

We will be able to get the Balance Summary information from the Balance Summary API provided by Finflux.

**Interest and Charges: This section will not be present in Term Loan Holding Statement to be removed for both products**

**MF Holding:** Same as OD

- No.
- Scrip name
- Units
- Market Value
- LTV% (Cred’s LTV)
- Eligible Limit

We will be able to get the MF Holding information from the Get Holding Details API provided by Finflux.

**Grievance Redressal Mechanism**: Same as OD

**Footer:** Same as OD

Holding statement can be triggered in the following two ways:

- LSP(Cred) will trigger based on the customer’s need. We need to provide the LSP with an API for the same. The API will be similar to the OD API: [https://api.staging.dspfin.com/lms/api/loan/account/holdings/report/v1/FXLAN65378191](https://api.staging.dspfin.com/lms/api/loan/account/holdings/report/v1/FXLAN65378191)
- DSP will trigger this statement on the 1st of every month same as OD.

### **Statement of Accounts (Loan)**

This statement will contain the details of the customer’s Dues and Transactions at the Loan level. Below are the section required in the statement along with the parameters in each section:

**Header**: Loan Account Statement

**Account Details**: 

- Name
- Client code
- Email id
- Mobile number
- Loan Status
- Address
- Account type
- Primary bank
- Loan account no.
- Account opened on
- Loan Expiry Date
- EMI Due Date

All the parameters are same as OD except **Renewal Date and ROI**, which should not be present in Term Loan Holding statement. **Loan Expiry Date** and **EMI** **Due Date** are the new parameters which needs to be added to the Loan SOA. We will be able to get the Account details information from the Client & Loan Details API provided by Finflux.

**Balance Summary:** Same as OD

- Drawing Power
- Outstanding Principal
- Excess Amount
- Available Cash

The Excess amount field will include the entire excess i.e. both Loan Level excess and Tranche tagged Loan Level excess. We will be able to get the Balance Summary information from the Balance Summary API provided by Finflux.

**EMI & Charges Due:** Similar to Interest and Charges section in OD 
****

This section will contain the Total Due components of Principal, Interest and Charges on the Loan level:

a. Principal Due
b. Interest Due
c. Charges

We will be able to get the Loan Dues information from the Loan Details API provided by Finflux. Please refer to the below sheet for the Remarks logic: [https://docs.google.com/spreadsheets/d/1lcD9lj6reh4Z4yO6xnGPqxN_mARPHGihBNmjpAMnxAs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1lcD9lj6reh4Z4yO6xnGPqxN_mARPHGihBNmjpAMnxAs/edit?usp=sharing)

Below is an example of the following to be shown in the Loan SOA:

**EMI & Charges Due**

| Type | Remarks | Amount |
| --- | --- | --- |
| a. Principal Dues |  | Rs 900 |
| b. Interest Dues |  | Rs 100 |
| c. Charges |  | Rs 0 |
| Total(a+b+c) |  | Rs 1000 |

**Upcoming EMI:** This will include the consolidated Upcoming EMI for the loan: 

It will have the below structure and fields:

| Due On  | EMI Components  | Amount |
| --- | --- | --- |
| 5 Nov 2025 | a. Principal  | Rs 950 |
| 5 Nov 2025 | b. Interest | Rs 50 |
| Total(a+b) |  | Rs 1000 |

**Transactions(Loan start to SOA generation date):**(Same as OD)

- Date
- Type of Transaction
- Description: It will include Tranche level transactions
- Debit
- Credit
- Balance
- Dr/Cr

We will be able to get the Transactions information from the Get All Transactions(Line) API provided by Finflux. Please refer to the attached sheet for the transaction details/narrations: [https://docs.google.com/spreadsheets/d/1lcD9lj6reh4Z4yO6xnGPqxN_mARPHGihBNmjpAMnxAs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1lcD9lj6reh4Z4yO6xnGPqxN_mARPHGihBNmjpAMnxAs/edit?usp=sharing)

**Grievance Redressal Mechanism**: Same as OD

**Footer:** Same as OD

Loan SOA can be triggered in the following two ways:

- LSP(Cred) will trigger based on the customer’s need. We need to provide the LSP with an API for the same. The API will be similar to the OD API: [https://api.staging.dspfin.com/lms/api/loan/account/soa/report/v1/FXLAN65378191](https://api.staging.dspfin.com/lms/api/loan/account/soa/report/v1/FXLAN65378191)
- DSP will trigger this statement on the 1st of every month same as OD.

### **Statement of Accounts (Tranche)**

This statement will contain the details of the customer’s Dues and Transactions at the Tranche level. Below are the sections required in the statement along with the parameters in each section:

**Header**: Tranche Account Statement

**Account Details**: 

- Name
- Client code
- Email id
- Mobile number
- Loan Status
- Tranche Status
- Address
- Account type
- Primary bank
- Loan account no.
- Tranche account no.
- Tranche disbursed on
- Tranche ending on
- Tranche ROI
- Next Due Date

All the parameter marked in RED color above are to be added extra in the Tranche SOA wrt to the parameters present in the Loan SOA. We will be able to get the Account details information from the Client & Loan Details API provided by Finflux.

**Outstanding Principal:** This section will provide information about the outstanding principal of the Tranche to the customer. The calculation displayed in the Tranche SOA will be as below:

**Disbursed Amount - Principal Repaid = Outstanding Principal**

**EMI & Charges Due:** Similar to Interest and Charges section in OD 
****

This section will contain the Total Due components of Principal, Interest, Charges and Excess on the Tranche level: 

a. Principal Due
b. Interest Due
c. Charges
d. Excess(pre-paid amount)

We will be able to get the Tranche Dues information from the Tranche Details API provided by Finflux. Please refer to the below sheet for the Remarks logic: [https://docs.google.com/spreadsheets/d/1lcD9lj6reh4Z4yO6xnGPqxN_mARPHGihBNmjpAMnxAs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1lcD9lj6reh4Z4yO6xnGPqxN_mARPHGihBNmjpAMnxAs/edit?usp=sharing)

Below is an example of the following to be shown in the Tranche SOA:

**EMI & Charges Due**

| Type |  | Amount |
| --- | --- | --- |
| a. Principal Dues |  | Rs 900 |
| b. Interest Dues |  | Rs 100 |
| c. Charges |  | Rs 0 |
| d. Excess(pre-paid amount) |  | Rs 200 |
| Total(a+b+c-d) |  | Rs 800 |

**Upcoming EMI:** This section will include the Upcoming EMI for the Tranche along with the Due date and the amount for each EMI component. It won’t deduct the excess from the EMI. 

It will have the below structure and fields:

| Due On  | EMI Components  | Amount |
| --- | --- | --- |
| 5 Nov 2025 | a. Principal  | Rs 950 |
| 5 Nov 2025 | b. Interest | Rs 50 |
| Total(a+b) |  | Rs 1000 |

**Transactions(Tranche start to SOA generation date):**

- Date
- Type of Transaction
- Description:
- Debit
- Credit
- Balance
- Dr/Cr

We will be able to get the Transactions information from the Get All Transactions(Loan) API provided by Finflux. Please refer to the below sheet for the transaction details/narrations: [https://docs.google.com/spreadsheets/d/1lcD9lj6reh4Z4yO6xnGPqxN_mARPHGihBNmjpAMnxAs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1lcD9lj6reh4Z4yO6xnGPqxN_mARPHGihBNmjpAMnxAs/edit?usp=sharing)

**Grievance Redressal Mechanism**: Same as Loan SOA in OD

**Footer:** Same as Loan SOA in OD

Tranche SOA can be triggered in the following two ways:

- LSP(Cred) will trigger based on the customer’s need. We need to provide the LSP with an API for the same. Tranche SOA API: We will have to build this API similar to Loan SOA API in order to provide to LSP
- DSP will trigger this statement on the 1st of every month same as Loan SOA in OD.

### **Loan and Tranche NOC**

These will be automatically triggered when a Loan/Tranche gets closed or foreclosed.

**Loan NOC:** This will be same as OD.

![Screenshot 2025-09-26 at 1.52.03 PM.png](Term%20Loan%20Customer%20Statements/Screenshot_2025-09-26_at_1.52.03_PM.png)

We will be able to get the details from the Client and Loan Details API of Finflux. 

**Footer:** Same as OD

@Parikshit Kumar Provide Email Template ID with the List of the Parameters.

**Tranche NOC:** This will be similar to Loan NOC in OD but it needs to be triggered when Tranche gets closed. Below is a text template for the same:

**Header:** Same as Loan SOA in OD

TRANCHE NO DUES CERTIFICATE

LOAN ACCOUNT NUMBER: [Insert Loan Account No.]

TRANCHE ACCOUNT NUMBER: [Insert Tranche ID / Number]

CUSTOMER NAME: [Insert Borrower Name]

This is to certify that [Lender Name] has received complete payment (including all applicable charges) towards [Loan Against Securities – Tranche Number] [Tranche Number] availed by you under the Loan Account Number [Insert Loan Account No.] on [Tranche Disbursement Date].

No further amount is payable by you under the afore-mentioned Tranche.

Please note, this certificate pertains specifically to the above tranche. Other tranches, if any, under the Loan Account may continue to remain active and obligations (if applicable) under those tranches shall remain payable.

[Lender Name]

This is a system-generated communication and does not require any signature.

**Footer:** Same as Loan NOC in OD

---

# Open Pointers

1. Description of Tranche level txns in Loan SOA examples? 
2. Which is the API which will give Tranche level transactions details for Loan SOA and Tranche SOA? Get All Transactions API(Line and Loan)
3. How will we bifurcate between Tranche and Loan level transactions?
4. Mail template of sending the docs to customers? Discussed in Communication prd
5. Examples pe example? For the time being we will go ahead with Term Loan against Securities
6. Remarks

Remarks logic:

1. If principal outstanding is 0, no text
2. If interest outstanding is 0, no text

If principal or interest outstanding is not zero

1. Principal due from  {Statement generation month -1 in MMM format} to {last day of generation month -1 can be 28th/30th/31st} {Statement generation month -1 in MMM format}
a. Principal due from 5th Sept(Due Date) to 30th Sept
b. Principal due from 5th Sept(Due Date) to 5th Oct(On Demand)
2. Interest due from 1st {Statement generation month -1 in MMM format} to {last day of generation month -1 can be 28th/30th/31st} {Statement generation month -1 in MMM format}

Charges: Charges applied due to non repayment of dues from {Statement generation month -1 in MMM format}

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