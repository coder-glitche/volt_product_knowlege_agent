# Redemption vs. LAMF Calculator & Comparison Tool

: Naman Agarwal
Created time: May 20, 2025 3:19 PM
Status: In progress
Last edited: May 20, 2025 3:46 PM

## Problem We’re Solving

- Our TG sell their assets to meet short-term cash needs, unaware that they can leverage their assets to achieve their short-term goals more effectively.
- Others explore alternatives to meet short-term need such as personal loans or business loans, but often encounter challenges such as high interest rates & other charges, cumbersome application processes, closure of loan.
- Some are hesitant to take loans due to a lack of understanding between good loans and bad loans and end up selling assets to meet goal.
- Currently,  MFDs rely on pen and paper to explain to their clients the benefits of LAMF and the potential losses associated with selling mutual funds.
- Through RRC, we aim to address the following objectives:
    - Education and awareness about LAMF to out TG
    - Branding through marketing and organic sharing

## Objectives

- Educate and raise awareness around LAMF.
- Help clients make **informed financial decisions**.
- Arm MFDs with a professional, branded, easy-to-use digital tool.
- Drive brand trust through co-branded PDF reports and shareable content.

## User Stories (MFD-Focused)

1. **Fetch & Consent**
    - *As an MFD, I want to enter a client’s phone and PAN, trigger OTP-based consent, and fetch LAMF eligibility in real time.*
2. **Custom Amount & Instant Comparison**
    - *Once I have the LAMF limit, I want to enter any amount (up to the limit) and instantly show a side-by-side comparison of “Redeeming” vs. “Taking LAMF.”*
3. **Crystal-Clear Visuals**
    - *I want to show tax impact, exit load, interest costs, and future value—so my client easily sees the pros and cons.*
4. **Branded Takeaway**
    - *I want to download a co-branded PDF with this comparison to give my client a clear, professional summary.*

## 🛠️ Tool Overview & Flow

### 1. **Customer Consent & Details (Screen 1)**

- Inputs: Client Mobile Number, Client PAN
- Button: “Enter OTP”

### 2. **OTP & Eligibility Fetch (Screen 2)**

- Input: OTP
- Fetch: MF holdings + Max LAMF limit
- Errors:-
    - Combination is not registered on the MF central
    - No funds
    - Available limit is insufficient.

### 3. **Input Desired Amount (Screen 3)**

- Display: Max eligible amount (e.g., ₹5,00,000)
- Input: Desired amount (editable)
- Button: “Compare Redemption vs. LAMF”

### 4. **Comparison View (Screen 4)**

Two-column layout:

| Parameter | Redeeming MFs | Loan Against MFs |
| --- | --- | --- |
| Action | Taken redemtion | Opened Credit line with VOLT |
| Ownership | Sold | Lien Hold |
| Investment Growth | Stops | Continues |
| Funds Received | ₹X - exit load | ₹X - PF |
| Exit Load | ₹Y (if any) | ₹0 |
| Capital Gains Tax | ₹Z LTCG, STCG | ₹0 |
| Net Cash | ₹X - Y - Z | ₹X |
| Interest Cost | -  ROI of the MFs | 10.49% |
| Repayment | None | Required |
| Future Value Impact | Lost | Retained & growing |
| Financial Goals | May suffer | Preserved |
| Time to Receive | T+2 days | 15 mins |
| Credit Score | No impact | No Impact — Have to check |
| Flexibility | One-time | Interest only repayment, credit line take money out as needed |

- Buttons: “Download PDF”, “Start New Comparison”

### 5. **Downloadable PDF**

- Branded with Volt  + MFD
    - Non Branded with volt -  Just MFD name
- Includes:
    - Date, customer name (optional), entered amount
    - Comparison table
    - Disclaimers + contact info
- Design: A4 printable, shareable

---

### 📊 Data Requirements

- **Fetched via API**:
    - MFC Summary and Detailed API,
    - MFC CGS for past redemptions
- **Input by MFD**:
    - Phone, PAN, OTP
    - Desired loan amount(default)
- **Calculated**:
    - Exit Load
    - Capital Gains Tax
    - Past Redemptions
    - Interest cost
    - Opportunity cost / future value

---

### 🧑‍🎨 UX & Design Priorities

- Mobile responsive
- Trust signals
- Clear language + visual hierarchy
- Professionally designed PDF output

---

### Additional Touchpoints (Marketing)

- Add to check eligibility page , MFD dashboard
- Multi-lingual, Hindi, English, Telgu, Gujarati
- Shareable on WhatsApp/social

---

### Success Metrics

- % of MFDs using tool weekly
    - of PDF downloads
    - of LAMF applications initiated post-comparison
- Registration to Offer selection rate

## References

- Regret calculator reference:
    
    [https://finezzy.com/loan-against-mutual-funds/](https://finezzy.com/loan-against-mutual-funds/)
    
- Calculator design reference:
    
    [https://www.etmoney.com/tools-and-calculators/mutual-fund-calculator](https://www.etmoney.com/tools-and-calculators/mutual-fund-calculator)
    
    [https://www.5paisa.com/calculators/mutual-fund-calculator](https://www.5paisa.com/calculators/mutual-fund-calculator)
    

- Understand taxation:
    
    [https://www.etmoney.com/learn/mutual-funds/how-to-avoid-capital-gains-tax-in-mutual-funds/](https://www.etmoney.com/learn/mutual-funds/how-to-avoid-capital-gains-tax-in-mutual-funds/)
    

- User query: [Plan to answer all such query on internet after launch]
    
    [https://www.quora.com/How-do-I-calculate-profit-for-tax-calculation-when-mutual-fund-partial-withdrawal-redemption-is-done](https://www.quora.com/How-do-I-calculate-profit-for-tax-calculation-when-mutual-fund-partial-withdrawal-redemption-is-done)