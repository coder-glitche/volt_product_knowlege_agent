# 📄 Loan Offer Funnel Optimisation Document

## **Problem Statement**

Users are dropping off heavily between **Eligibility → Credit Limit setup**, with first-time success at ~36% (vs ~50% overall conversion). Trust, comprehension, and late surfacing of loan details are the biggest blockers.

## **Problem Breakdown (L1 → L2 → L3)**

### **L1 Problem 1: Early Drop-Off at Credit Limit Setup**

- **L2.1:** Incomplete visibility of portfolio value.
    - **L3:** Users don’t understand why “eligible limit” < “portfolio amount” (45% LTV logic hidden).
- **L2.2:** Fetched MF page creates doubt.
    - **L3:** Users who click here convert 50% less. Refresh/back CTA adds friction.

### **L1 Problem 2: Lack of Clarity on Loan Structure**

- **L2.1:** Flexi-repay not understood.
    - **L3:** Most users think in EMI terms; confusion elongates decision cycle.
- **L2.2:** EMI/Charges/Rate appear late.
    - **L3:** Users rely on WATI/FAQs to understand basics → long-tail conversions (p75–p90 = hours).

### **L1 Problem 3: Low Trust & Confidence**

- **L2.1:** Mutual fund safety doubts.
    - **L3:** “Will my MF be locked?”, “Will it stop growing?”
- **L2.2:** Competitive comparison behaviour.
    - **L3:** Users revisit multiple times to benchmark vs other lenders.

---

## **Current Journey**

1. **Eligibility Check** → Shows eligible limit only.
2. **Anchor Page (Fetched MFs optional)** → Users click “Fetched Mutual Funds” or Refresh → major drop-offs.
3. **Set Credit Limit Page** → Users reduce eligible limit 75% of the time.
4. **Loan Offer Page** → EMI, fees, rate only revealed here.
5. **KYC** → Initiation post-offer.

---

## **Proposed Journey**

1. **Eligibility Check (improved)** → Show eligible limit + simple breakdown of how it’s calculated (45% LTV).
    1. **Portfolio Transparency (optional disclosure)** → Clear net eligible vs non-eligible MFs with logos.
    2. **Set Credit Limit Page** → Inline EMI calculator (slider updates EMI/fees instantly).
2. **Review details** → Focus on trust badges (RBI registered lender, secure pledge), repayment clarity, upfront EMI vs Flexi toggle.
3. **KYC** → Smooth handoff.