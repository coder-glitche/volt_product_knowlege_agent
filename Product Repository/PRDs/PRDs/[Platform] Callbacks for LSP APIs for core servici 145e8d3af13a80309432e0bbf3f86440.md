# [Platform] Callbacks for LSP APIs for core servicing flows

: Vaibhav Arora
Created time: November 21, 2024 9:23 AM
Status: In progress
Last edited: May 29, 2026 6:19 PM

# **What problem are we solving?**

There are core transaction and request lifecycles that need to be managed by the LSP. 

Volt as an LSP has built a lot of pollers and CRON jobs at specific days over existing lender APIs to solve for this. However this approach has a lot of challenges.

- Introduces a lot of computational load both at the LSP as well as the lender
- Not very accurate, as logic is based on top of hitting jobs on specific dates and times
- Requires a lot of maintenance at an engineering level across systems

Most of these APIs get data from core systems like the CTMS or the LMS, and this often brings slowness to the system hence impacting the core internal flows for the NBFC like EOD jobs, reconciliation activities etc

To solve for this, callbacks can be built at lender’s end to improve integration experience and ensuring accurate data is shared with the LSP and the corresponding customer 

---

# **How do we measure success?**

- Improved LSP integrations (reduction in development TAT)
- Lower load on core APIs like loan details and loan summary
- Lower customer support tickets (due to wrong data/information)

---

# **How are others solving this problem?**

Most legacy lenders do not have callbacks for such core systems (Given from our experience in working with BFL and TCL and LSPs often solve for this by building CRON jobs and pollers on top of APIs which are not designed for such a load

---

# **What is the solution?**

Building callbacks for core servicing flows:

- Due collection (lifecycle)
    - When interest becomes due
    - When mandate is presented
    - When mandate collection is successful
    - When mandate collection fails
    - When interest is settled
- Repayment
    - When a repayment is posted into the user’s loan account
- Shortfall
    - When shortfall is identified (daily job) in a user’s loan account
    - When shortfall updates for a loan account (change in amount/ageing)
    - When shortfall is settled for a user’s loan account
    - When shortfall crosses grace period (due date) and sell-off is initiated for the user
    - When sell off is completed
- Foreclosure
    - When a foreclosure request is approved for the user

## Requirements

Due collection:

 

![image.png](%5BPlatform%5D%20Callbacks%20for%20LSP%20APIs%20for%20core%20servici/image.png)

Due generation callback

```json
interface DueCallback {
    loanId: string;
    dueDate: Date;
    amount: number;
    duePeriod: {
        from: Date;
        to: Date;
    };
}
```

Mandate presentation callback:

```json
Interface MandatePresentedCallback {
    loanId: string;
    umrn: string;
    amount: number;
    presentationDate: Date;
    expectedCollectionDate: Date; (can keep for future scope: Collection BRE)
    bankAccount: {
        accountNumber: string;
        bankName: string;
    };
}
```

Mandate collection success callback

```json
interface MandateCollectionSuccessCallback {
    loanId: string;
    umrn: string;
    amount: number;
    collectionDate: Date;
    transactionRequestId: string;
    settlementStatus: 'PENDING' | 'COMPLETED'; (as per business hour logic)
}
```

Mandate collection failure callback:

```json
interface MandateCollectionFailureCallback {
    loanId: string;
    umrn: string;
    amount: number;
    failureDate: Date;
    failureReason: string;
    retryEligible: boolean; (can keep for future)
    nextRetryDate?: Date; (can keep for future)
}
```

Interest settlement callback:

```json
interface InterestSettlementCallback {
    loanId: string;
    amount: number;
    settlementDate: Date;
    settlementMode: 'MANDATE';
    transactionReference: string;
    transactionRequestId: string;
    interestPeriod: {
        from: Date;
        to: Date;
    };
}
```

Repayment:

![image.png](%5BPlatform%5D%20Callbacks%20for%20LSP%20APIs%20for%20core%20servici/image%201.png)

Repayment settlement callback:

```json
interface RepaymentPostedCallback {
    loanId: string;
    amount: number;
    paymentDate: Date;
    paymentMode: 'UPI' | 'NEFT' | 'RTGS' | 'IMPS';
    transactionReference: string
    };
}
```

Sell off callbacks:

![Screenshot 2024-11-21 at 10.24.33 AM.png](%5BPlatform%5D%20Callbacks%20for%20LSP%20APIs%20for%20core%20servici/Screenshot_2024-11-21_at_10.24.33_AM.png)

Shortfall identified / update callback

```json
{
    loanId: string;
    shortfallId: string;
    shortfallAmount: number;
    identificationDate: Date;
    shortfallDueDate: Date;
}
```

Shortfall covered callback

```json
interface ShortfallSettlementCallback {
    loanId: string;
    shortfallId: string;
    shortfallAmount: 0
   
}
```

Sell off initiated callback:

```json
interface SellOffInitiatedCallback {
    loanId: string;
    shortfallAmount: number;
    gracePeriodEndDate: Date;
    sellOffDate: Date;
    shortfallAgeing: number; // in days
    collateralDetails: {[
        portfolioValue: number;
        collateralId: string;
        isin: string;
        units: number]
    };
}
```

Foreclosure:

![Screenshot 2024-11-21 at 10.28.54 AM.png](%5BPlatform%5D%20Callbacks%20for%20LSP%20APIs%20for%20core%20servici/Screenshot_2024-11-21_at_10.28.54_AM.png)

Foreclosure completed callback

```json
interface LoanClosureCallback {
    loanId: string;
    closureDate: Date;
    finalSettlementAmount: number;
    settlementBreakup: {
        principal: number;
        interest: number;
        charges: number;
        preclosurePenalty: number;
    };
    transactionReference: string
}
```

Foreclosure rejected callback;

```json
interface ForeclosureRejectedCallback {
    loanId: string;
    rejectionDate: Date;
    rejectionRemarks: string;
}
```

---

# **Design**

NA

---

# **Analytics
Logging of all callbacks**

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