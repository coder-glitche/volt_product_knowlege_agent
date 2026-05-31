# PRD – Volt MFD Payouts Process

: Naman Agarwal
Created time: March 7, 2025 1:31 PM
Status: In progress
Last edited: May 27, 2025 2:52 PM

# **PRD – Volt MFD Payouts Process**

## **1. What Problem Are We Solving?**

### **Key Issues Identified**

1. Business continuity risk as we are too dependent on one analyst for the calculations 
2. **~~GST Invoice Issues:** No GST invoices sent to MFDs, leading to ad-hoc payments, accounting issues, incorrect payouts, and complaints.~~
3. **Payout Report Clarity:** Reports are difficult to read, leading to customer support queries.
4. **Partner Accounts Payable Tracking:** Currently tracked monthly, leading to missed payouts for MFDs without added bank accounts.
5. **Payout Processing Issues:** Manually triggered payments through HSBC takes 3-4 days to get the Payment status and to retry payment if failed.
6. **Accounting Errors (~2% of partners):** Issues only discovered during tax filings (26AS).
7. **Support Visibility:** No centralized tracking for payout-related support issues.
8. **Reconciliation Issues:** Discrepancies due to outdated commercial excel files.
9. **Tracking Ad-hoc Payouts:** Older ad-hoc payouts are scattered across multiple files and emails.
10. **GSTN Verification:** No automated verification of correct GST numbers.

---

## **2. Changes needed for Payout automation (Current vs. Proposed)**

| Database  | Current | Proposed |
| --- | --- | --- |
| Application Data | DB | No change |
| Transaction Data | DB | No change |
| Principle Outstanding | Google Sheets | DB |
| Partner Commercials | Google Sheets | DB |
| Payout Ledger Table | Google Sheets | DB |
| Account Payable (AP) | Not tracked | DB |
| Base Payout Calculations | Google Sheets | DB |
| GST & TDS Calculations | Google Sheets | DB |
| Payout & GST Invoice | Google Sheets | DB |
| GST Tax & TDS Filing | Google Sheets | DB |
| Bank Account Data | Manual Check | DB |
| Payout File to Bank | Excel | API |
| Payout Payment Status | Statement | API |
| Reconciliation & UTR Backfill | Google Sheets | DB |

---

## **3. User Needs**

### **MFD / Partner**

- Expect accurate, on-time payments.
- Need clear payout breakdowns, including GST invoices.
- Require an easy way to highlight and resolve discrepancies.
- Want Volt to handle tax filings accurately.
- Prefer a payout experience similar to top AMCs.

### **Business Team**

- Aims to improve MFD service by resolving payout issues efficiently.
- Requires accurate invoices and payout reports.
- Needs to automate TDS/GST calculations and reconciliation.

### **Accounting Team**

- Needs a consistent and accurate ledger with invoices for every transaction.
- Requires clear tracking of payment reasons and partner accounts payable.

### **Payment Ops**

- Needs verified bank accounts before processing payouts.
- No issues with sending files to HSBC.

### **Analytics Team**

- Requires accurate source data tables for reconciliation.
- Needs clear tracking of offline payouts against partners.

### **Support Team (RMs)**

- Prefer to assist new customers rather than handle payout issues.
- Need better tools to track and resolve GST-related concerns.

---

## **4. How Do We Measure Success?**

1. **Reduction in support queries** related to payout issues.
2. **Increased MFD satisfaction** with clear invoices and statements.
3. **Accurate and automated reconciliation** of payouts and tax filings.
4. **Faster resolution of discrepancies** through better tracking.
5. **Seamless processing of GST and TDS** without manual intervention.

---

## **5. Industry Best Practices (How Others Solve This Problem)**

- Store all MFD-lender commercials in the system.
- Provide real-time earnings visibility via a dashboard.
- Automate payout calculations and invoice generation.
- Set clear payout timelines:
    - Invoice generation by 5th.
    - Payout processing by 10th.
    - Discrepancy resolution by 15th.
- Automate TDS deductions and GST invoicing.
- Ensure clear communication on earnings and tax calculations.

---

## **6. Proposed Solution & Phases**

### **Phase 1: Reduce Support Issues & Improve Visibility**

- ~~Implement **GST & payout invoice creation** with MFD approval.~~
- Build a **dashboard for payout tracking** and issue resolution.
- Enable **ledger-based tracking** of partner balances.
- **Automate ad-hoc payout tracking for better reconciliation.**

### **Phase 2: Automate Reconciliation & Payouts**

- Reduce internal reconciliation efforts.
- Enhance **payout accuracy and partner satisfaction**.

### **Phase 3: Best-in-Class MFD Experience**

- Create a seamless **payout and tax filing experience**.
- Reduce MFD acquisition costs through a strong reputation.

---

## **7. Implementation Timeline**

### **Phase 1**

- ~~Automate GST invoice creation and approval.~~
- Implement an MFD-facing payout dashboard.
- Improve tracking of ad-hoc payouts.

### **Phase 2**

- Automate reconciliation processes.
- Enhance ledger visibility for payouts.

### **Phase 3**

- Finalize the best-in-class payout experience.
- Ensure MFDs can track and manage their earnings seamlessly.

---

## **8. Action Items & Checklist**

- **Product Team**
    - Define invoice formats.
    - Implement partner ledger tracking.
- **Business Team**
    - Identify key MFD concerns.
    - Establish a clear dispute resolution process.
- **Operations Team**
    - Automate ad-hoc payout tracking.
    - Improve bank account verification.
- **Analytics Team**
    - Develop accurate source data tables.
    - Improve reconciliation processes.

---

## **9. Go-To-Market Plan**

- **Marketing:** Educate MFDs on new payout processes.
- **Ops & Sales Training:** Ensure teams can address MFD concerns.
- **FAQs:** Create a repository for common payout questions.

---

## **10. Learnings & Next Steps**

- **Track MFD feedback** and iterate on the payout process.
- **Analyze support trends** to identify ongoing issues.
- **Optimize reconciliation and tax filing processes** for future automation.

---

## **11. Appendix & Resources**

- [Volt MFD Payouts Process](https://www.notion.so/Volt-MFD-Payouts-Process-129e8d3af13a80f0a322dd388f71d70c?pvs=21)
- [Payout Working File](https://www.notion.so/Payout-Working-File-129e8d3af13a80c8ba52c870cda414ea?pvs=21)
- [GST Invoice & Payout Statement PRD](https://www.notion.so/PRD-GST-Invoice-and-Payout-statement-creation-and-approval-12ee8d3af13a80189662fc13cfe7d2a1?pvs=21)
- [Process Note: Payouts](https://www.notion.so/Process-note-Payouts-13be8d3af13a80d58fbaf763902d7ca0?pvs=21)
- [Payouts Phase 2](https://www.notion.so/Payouts-Phase-2-149e8d3af13a80bdb2f2cf6c1b703c32?pvs=21)
- [Bulk Email Sender Setup Guide](https://www.notion.so/Bulk-Email-Sender-Setup-Guide-14ae8d3af13a8091889eccaec480fbee?pvs=21)
- 

[MFD payouts payment reconciliation ](PRD%20%E2%80%93%20Volt%20MFD%20Payouts%20Process/MFD%20payouts%20payment%20reconciliation%201afe8d3af13a80f2804fde8b113b03b5.md)

---

[**MFD Payout Calculation Automation**](PRD%20%E2%80%93%20Volt%20MFD%20Payouts%20Process/MFD%20Payout%20Calculation%20Automation%201bae8d3af13a808d88eaf700a360398b.md)