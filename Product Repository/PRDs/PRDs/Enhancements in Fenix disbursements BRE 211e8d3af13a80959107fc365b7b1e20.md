# Enhancements in Fenix disbursements BRE

: Ameya Aglawe
Created time: June 13, 2025 12:57 PM
Status: Pending Review
Last edited: April 7, 2026 11:50 AM

# **What problem are we solving?**

---

- The overall SR for payouts is 99.2% and payment method wise the SR is the
    - IMPS : 99.59%
    - NEFT : 83.81 % (lower SR because these are retry attempts after IMPS failures - usually an issue at bene bank)
    - RTGS : 97. 66%
- As confirmed with Cashfree and YES Bank the SR of disbursements through NEFT is significantly higher than IMPS (Cashfree to share exact data points for this).
- Bifurcation of 0.8% disbursement failures in Apr-May
    
    
    | Reason | Count | Percentage |
    | --- | --- | --- |
    | Beneficiary bank side decline | 138 | 46.78% |
    | Beneficiary bank side decline | 12 | 4.07% |
    | Return from beneficiary | 14 | 4.75% |
    | Return from beneficiary | 35 | 11.86% |
    | Bene_Bank_Declided | 25 | 11.8% |
    | Returned_from_Beneficiary | 1 | 0.3% |
    | Account_Blocked | 18 | 6.1% |
    | Intermittent YB decline | 2 | 0.68% |
    | Bank_Gateway_Error (YB error) | 35 | 8.8% |
    | **Invalid_Account_Failed** | **11** | **3.7%** |
    | Payout_Internal_Error | 1 | 0.3% |
    |  | 295 | 100% |

### **Key Insights from the Analysis**

1. **Root Cause of Failures:**
    
    Approximately **76% of payout failures are attributable to issues at the beneficiary bank's end**, indicating that the elevated failure rate for NEFT may not reflect a flaw in the NEFT system itself but rather operational issues on the receiving bank's side.
    
2. **Invalid Account** 
    
    The occurrence of **“Invalid account” errors requires deeper investigation**, as such errors are unexpected given that a penny drop validation is already conducted during the application journey.
    
3. **NEFT Success Potential:**
    
    Additionally, the success rate of NEFT is around 83%, even when it's only used as a fallback payout method. The hypothesis is that if the initial disbursement had been attempted directly via NEFT, it might have succeeded on the first try itself.
    

# **How do we measure success?**

---

- Improving first attempt disbursement success rate
- Improving disbursement settlement TAT
- Reduction in T90 TAT for status confirmation from 3.5 days to 30 mins in cases of failures

# **How are others solving this problem?**

---

- WIP

# **What is the solution?**

**Experiment 1 - Pilot NEFT as a primary payout method** 

- Objective -
    - Understand if Success Rate (SR) will increase by using NEFT
    - Settlement Time (TAT) of NEFT across business hour and non business hours
- Introduce NEFT as an alternate disbursement method to improve success rates as NEFT has a higher success rate than IMPS (as confirmed with Cashfree)
- 1st disbursement will continue to be IMPS upto 5L and RTGS >5L
- Logic for subsequent disbursements.
    - Every disbursement less the amount of ₹5 lakhs (except the first disbursement) will be routed via NEFT, since amounts above ₹5 lakhs are already handled through RTGS
- Implement a configurable flag to enable or disable NEFT routing instantly in case of any issues during the pilot.

**Results of experiment 1 -** 

- During this 10 day experiment -
    - There were 2 outages at YBL & Cashfree end due to which this experiment had to be rolled back (as Cashfree had not handled a specific error code for NEFT failures)
    - The disbursements flowed through all the 3 payout methods during the 10 day time frame and following is the SR & TAT analysis (negating the disbursements which failed during the outage)
        
        ![image.png](Enhancements%20in%20Fenix%20disbursements%20BRE/image.png)
        
    - Insights -
        - Success Rate Analysis: NEFT achieved the highest success rate (99.61%), followed by IMPS (99.42%) and RTGS (99.12%). However, NEFT exhibited significantly higher settlement times, making RTGS more favourable when balancing success rate against turnaround time.
        - RTGS Failure Analysis: Among 342 RTGS transactions, only 3 failures occurred, with the primary failure mode being invalid IFSC codes. This stems from the application journey using IMPS for penny drops, which validates account numbers but not IFSC codes, while NEFT and RTGS perform IFSC validation during transaction processing.
        - Root Cause & Solution: Historical RTGS failures were attributed to either YBL-to-YBL transfer issues (now resolved) or invalid IFSC codes. The latter can be mitigated through an IMPS retry mechanism, as IMPS bypasses IFSC validation entirely.
        - Optimal Method Selection: Considering the TAT versus success rate trade-off, RTGS emerges as the superior payout method compared to NEFT, offering faster settlement with minimal failure risk that can be further reduced through intelligent retry logic.
    
    **Updated disbursement BRE**
    
    - Following is the BRE based on the insights from the pilot
        
        
        | Nth disbursement/Amount | < 2 lacs | 2 lacs < X < 5 lacs | > 5 lacs |
        | --- | --- | --- | --- |
        | 1st  | IMPS | IMPS | RTGS |
        | Subsequent  | NEFT  | RTGS | RTGS |
    - There will be a retry with IMPS payout method on NEFT and RTGS failures in case we get the incorrect IFSC code error message from Cashfree
        - Response
            
            ```jsx
            {
                "payoutRequestId": "8a813eb9979cf5ec0197c49b7350213b",
                "providerTransactionId": "2055246478",
                "fenixTransactionId": "DRID975858384197",
                "chosenProvider": "CASHFREE",
                "usedTransferMode": "NEFT",
                "utrNumber": null,
                "payoutStatus": "FAILED",
                "payoutSubStatus": null,
                "beneficiaryDetails": {
                    "beneficiaryName": "SACHIN GANPAT GHORPADE",
                    "beneficiaryAccountNumber": "520101043283892",
                    "beneficiaryIFSC": "UBIN0914029",
                    "beneficiaryMobileNumber": null,
                    "beneficiaryEmail": null,
                    "vpaForUpiPayment": null
                },
                "remarks": "Payment transfer for disbursement request",
                "payoutStatusDescription": "The transfer has failed because the IFSC is invalid. After correcting the IFSC,  You can reinitiate the transfer via Cashfree so that the transfer can be reattempted again by Cashfree with the partner bank(s).",
                "payoutAmount": 50000,
                "requestedOn": 1751350211408,
                "settlementDate": null,
                "expectedTransferBy": null,
                "isFirstTransaction": false
            }
            ```
            
        - We won’t be able to retry transaction with invalid IFSC code with amount > 5 lacs because IMPS has a upper limit of 5 lacs.
        - Such cases will have to be handled operationally on a case to case basis where DSP Ops team will have to get customer’s correct IFSC updated in Fenix.
            - DSP Operations team will be given an access to a QuickSight dashboard which will list all the details of the payouts with failed due to an IFSC invalid error and have amount > 5 lacs
    - Volt side changes
        - ETA tracking
            - While storing ETA for disbursement would now be based on payment method and the same should reflect in Volt app.
                - IMPS - 5 mins
                - NEFT - 140 mins
                - RTGS - 50 mins

## Requirements

---

# **Design**

---

# **Analytics**

---

- SR and TAT (mean, P50, P90, P99) for success/failures for working/non-working hours and payment mode wise bi-furcation (IMPS, NEFT, RTGS)
- Create a dashboard in Quick sight which will maintain the list of all invalid IFSC code errors with the relevant details (payouts table)

# **Timeline/Release Planning**

---

# **Go to market**

- Going to make this change across all LSPs

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

- Below is the analysis of distribution of number of disbursements and total disbursement amount of disbursements against the different ranges of disbursements amounts

![Screenshot 2025-06-16 at 5.32.20 PM.png](Enhancements%20in%20Fenix%20disbursements%20BRE/Screenshot_2025-06-16_at_5.32.20_PM.png)