# MFD client management

: Naman Agarwal
Created time: April 10, 2025 4:32 PM
Status: In progress
Last edited: April 30, 2025 10:50 AM

# **What problem are we solving?**

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

### **MFD Actions/Features Page for Client Management:**

**I. Application Status & Initiation:**

1. **Check Application Status:** View the current stage and any blockers for a specific client's application 
2. **Resend Application Link/Invite:** If the client hasn't started or lost the link.
    1. Send SMS to user, Send via WA, E-mail
3. **Check Eligibility:** Initiate or re-check the loan eligibility limit for a client 

**II. KYC & Verification Assistance:**

**III. Portfolio, Pledge & Limit Management:**

1. **View Client Portfolio:** See the fetched mutual fund holdings in excel and PDF .
    1. **View Eligible/Ineligible Funds** 
    2. Download as a PDF 
2. Check pledged funds , Holding statement 
3. Pledge more 
4. **Initiate Unpledge Request** *(Requires Client OTP/Action & Zero/Sufficient Balance):* For releasing funds after repayment/closure.
5. **Check Lien Status:** Confirm if the lien is active or has been removed post-closure/unpledging.
6. **Check Eligibility for Limit Enhancement:** Based on current portfolio value/additional funds.
7. **Initiate Limit Enhancement Request** *(Requires Client OTP/Action):* Start the process to increase the loan limit by pledging more funds.
8. **View Current Sanctioned Limit & Available Limit.**

**IV. Mandate Management:**

1. **Check Mandate Status:** View if the mandate is Pending, Active, Rejected, or requires Physical process.
2. **Trigger Resend Mandate Link/OTP:** If the client missed the initial trigger for digital mandate.
3. **Enable Physical Mandate Option:** If digital mandate fails repeatedly or isn't possible for the client's bank.
4. **Download Physical Mandate Form:** Provide the form for the client to print and sign.
5. **Upload Signed Physical Mandate Form:** Allow MFD to upload the scanned copy signed by the client.
6. **View Mandate Rejection Reason:** See why a digital or physical mandate failed.

**V. Loan Servicing (Withdrawal & Repayment):**

1. **View Available Withdrawal Amount:** Check the real-time cash available for the client.
2. **Check Withdrawal Request Status:** See if a client's withdrawal is Pending, Processed, Credited, Failed/Rejected.
3. **View Withdrawal History/Statement Snippet.**
4. **View Outstanding Loan Balance.**
5. **View Repayment History/Statement Snippet.**
6. **Generate Statement of Account (SOA):** Download or email the detailed statement to the client/MFD.
7. **View Repayment Schedule/Interest Due Date.**
8. **Flag Repayment Reflection Issue:** Allow MFD to report if a client's payment hasn't reflected after the standard TAT.
9. **View Penalty Charges Applied:** See details of any penalties levied on the account.

**VI. Account Closure & Documents:**

1. **Check Foreclosure Status:** View the status of an initiated foreclosure request.
2. **View Foreclosure Statement/Amount Due.**
3. **Initiate Foreclosure Request** *(Likely requires significant client validation/OTP):* Start the loan closure process.
4. **Download/Request NOC (Post-Closure).**
5. **Download/Request Interest Certificate.**
6. **Download/Request KFS/Agreement Copy:** Access copies of key loan documents for the client.

**VII. Profile Updates (Initiation for Client Action):**

1. **Initiate Mobile Number Change Request** *(Requires Client OTP/Verification):* Start the process for the client to update their number.
2. **Initiate Email ID Change Request** *(Requires Client Verification):* Start the process for the client to update their email.
3. **Initiate Bank Account Change Request (Payout)** *(Requires Client Verification & Document Upload):* Start the process to change the designated payout account.

**VIII. Support & Communication:**

1. **Raise Support Ticket on Behalf of Client:** Log an issue directly linked to the client's account.
2. **View Client-Specific Ticket Status.**

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