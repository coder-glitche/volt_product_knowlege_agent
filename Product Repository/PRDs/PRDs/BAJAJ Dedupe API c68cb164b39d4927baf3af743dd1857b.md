# BAJAJ Dedupe API

: Ameya Aglawe
Created time: July 29, 2024 11:49 AM
Status: Done
Last edited: September 12, 2024 5:02 PM

# **What problem are we solving?**

Users who have their lender assigned as BAJAJ (either through BRE or Hardcode) when have an already existing loan account with BAJAJ then we come to know about this only after the user has completed the application process. 

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

We will hit the BAJAJ dedupe APIs -  

1. At the step of lender assigning through BRE 
2. Whenever there is a lender change from TATA to BAJAJ through admin panel  

 Following are cases which we will consider - 

1. When the user comes to the “SET LIMIT PAGE” & “USER CONFIRMED THE LIMIT”, lender is assigned to the application either through BRE or it is hardcoded for various MFDs. 
    1. **In case of MFDs : (sending comms is de-prioritised as confirmed with Ranjan/Nishant, kindly ignore)**
        1. if BAJAJ is hardcoded, and there is a dedupe, then we’ll change the lender to TATA, while also sending the comms to the MFD. 
        2. The comms to the MFD will be, when we send the comms for application completed, we can also show : 
        ***”The lender for this user has been changed from BAJAJ to TATA because user’s loan account already exists with BAJAJ”***
    2. **In case of lender assigning through BRE :** 
        1. BAJAJ assigned as lender - 
            1. There will be a dedupe check 
            2. If there is a dedupe, backend will change the lender to TATA and the user will continue the application with lender as TATA
            3. Lender changed to TATA
                1. User completes the application with No-blocker
                2. User application gets rejected at credit referral → Ops will inform the customer that loan account cannot be created
        2. TATA assigned as lender - 
            1. If there is any issue while the user is going through the application (like updateLead, createLead API failed, CIBIL etc)
                1. Then the Ops team tries to change the lender to BAJAJ through admin action 
                2. Once the Ops person taps on the CTA to change lender 
                3. Then we will again hit the dedupe API 
                    1. If there is a dedupe with BAJAJ, then : 
                        1. We show error in the admin panel that “Dedupe - Loan account already with BAJAJ exists. Cannot change the lender to BAJAJ” 
                        2. And not change the lender to BAJAJ. 
                    2. If there is no dedupe then we change the lender to BAJAJ  

**Flow diagram :** https://whimsical.com/dedupe-api-GMGphqmhqDj6bxyJRm1KhB

## Requirements overview (optional)

1. *Sending the comms to the MFD* 
    1. The comms will tell the MFD that for the particular user the lender has been changed from BAJAJ to TATA. 
2. Need to show error message in admin panel in case Ops team changes lender from TATA to BAJAJ and there is a dedupe in BAJAJ that “Dedupe - Loan account already with BAJAJ exists. Cannot change the lender to BAJAJ” 
3. Dedupe API documentation 

[LASMiles_API.pdf](BAJAJ%20Dedupe%20API/LASMiles_API.pdf)

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

## Meeting notes

Information dump

**Taking context on process**

- First time lender assign then we will put that in BRE, if BAJAJ assigned then there will be a Dedupe check, in case there is a duplicate then will shift the lender to TATA
    - If according to BRE there is a lender assigning to BAJAJ, and there is a dedupe then what to do in this case? Then we can start a new user application with lender as TATA
    - Reasons why lender is cahnged from TATA → BAJAJ
        - Tenure : BAJAJ is 3 years
        - MFD is specific
        - Unapproved funds in TATA but approved in BAJAJ
        - User stuck at check customer eligibility (updatelead, create lead API)
        - If CBILL < 650 : (CBILL check happens after KYC step) → Credit referral → Ops checks the case
            - Passes to the lender
            - Changes the lender through admin action
    - BAJAJ → TATA
        - Reasons
        - What does Ops do?
            - Ask customer if they are comfortable to move with a different lender - TATA (Rs 400 payment required)
            - If the customer is not comfortable, we raise this application to BAJAJ to lodge the newly pledged funds to existing loan account of the customer.
- In case of manual override/ change, from TATA to BAJAJ, there’s a Dedupe in BAJAJ, then what would we do?
- If BAJAJ is hardcoded in BRE and Dedupe with BAJAJ happens then what will we do? (happens in case of partners which have preference to BAJAJ as a lender)
    - Ask MFD
        - Un-pledge ⇒ Move to TATA
        - Lodge it with existing loan account

Credit referral 

- Name mistmatch (PAN-aadhar, Bank-PAN)
- CIBIL < 650

**What happens right now?**

- First time lender assigned, then we will put that in BRE, if BAJAJ assigned then there will be a Dedupe check, in case there is a duplicate then will shift the lender to TATA
- In case of manual override/ lender change, from TATA to BAJAJ, there’s a Dedupe in BAJAJ, then what would we do?
    - We ask customer -
        - They want to lodge the funds with the existing loan account?
            - [interest rate of new agreement will be applied]
        - Do they want to un-pledge the funds.
- If BAJAJ is hardcoded in BRE and Dedupe with BAJAJ happens then what will we do? (happens in case of partners which have preference to BAJAJ as a lender)
    - Ask MFD
        - Un-pledge and move to TATA
        - Lodge it with existing loan account **(how is interest rate difference handled in this case?)**

- What response/request will we get from BAJAJ?

**Steps -** 

- KYC Verification step
- Fetch step
- Verify interest & charges
- KYC documents

- **What are different types of application in which Ops receives**
    - CIBIL < 650 ,
    - Poxidex check failure : Bad history
    - PAN-aadhar mismatch
    - Bank-aadhar name mistmatch
    - Bank current account
- **In what cases Ops approves & in what cases Ops rejects the application**
    - Approve
        - CIBIL > 650
        - PAN-aadhar name mismatch
            - Ask customer to add supporting document
    - Reject
        - Reject the current account
- **In what cases TATA rejects & in what cases TATA approves the application**
    - Approve
        - In most of the cases aadhar name mismatch
    - Reject
        - Posidex, ask SOA of the user
- **How will the Ops team know the reason for lender change?**
- **What does the user see when a application is in credit referral?**

**Cases**

1. If BAJAJ is assigned the first time then there will be a Dedupe check, in case the loan account with BAJAJ already exists for the user then will shift the lender to TATA
2. If through BRE, TATA was assigned and Ops changed the lender from TATA to BAJAJ, and user’s loan account already exists with BAJAJ then 
3. If BAJAJ is hardcoded in BRE (happens in case of MFD lender’s preferences) and then user’s loan account already exists with BAJAJ happens then
4. TATA’s Update lead API is down on a particular day and we shift the traffic to BAJAJ, & then there’s a dedupe in case of BAJAJ, what will we do then?
    1. **Doubt?**

**Doubt :** 

1. How will the Ops team determine if in a particular the lender was assigned for the first time, or if the lender has already been changed through admin actions?
2. What are the parameters which are checked in the BRE while assigning the lender? 
3. **In case of MFD should we directly change the lender in the back-end or do we need to handle this case operationally?**
4. In case of of lender change from TATA to BAJAJ, and then there’s a dedupe in BAJAJ, then what should be first priority?
    1. Asking the customer if they wanna lodge their funds to BAJAJ?
    2. Or should we again change the lender back to TATA
    

**How handling happen at Ops level for cases 2&3 right now?**

- Case 2 : In this case Ops asks the user if they want to
    - Un-pledge their funds
    - Lodge it with existing loan account
- Case 3 : Our Ops asks MFD/user if they want to
    - Un-pledge and move to TATA
    - Lodge it with existing loan account **(interest rate of the new agreement is considered)**

1. ***[De-prioritized]*** Also we need to add a tracker in the admin action which will show the history of lender changes made, with the reason & timestamp. 
    1. Whenever there is a dedupe & the lender is changed from BAJAJ to TATA, it should show up in this tracker, with the reason “Dedupe - Loan account already with BAJAJ exists”