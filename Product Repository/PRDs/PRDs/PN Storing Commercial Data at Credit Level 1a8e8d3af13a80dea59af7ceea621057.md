# PN: Storing Commercial Data at Credit Level

: Naman Agarwal
Created time: February 28, 2025 3:29 PM
Status: Pending Review
Last edited: March 3, 2025 12:37 PM

## Problem Statement

Currently, we do not store Platform-level commercial data directly at the Credit level. Instead, this data is maintained in external Excel sheets, which creates inefficiencies in the payout calculation process. The data team must manually add these commercial details when creating payout files, resulting in:

- Increased processing time
- Higher risk of manual errors
- Difficulty in data reconciliation
- Lack of data integrity between systems

## Proposed Solution

Implement a dedicated commercial data object at the Credit application level that will store all relevant commercial parameters at the time of application processing.

## Key Data Points to Store

The Credit level commercial data object should include:

- **Lender**: The financial institution providing the loan
- **Base ROI**: Original interest rate from lender pricing grid
- **Base PF**: Original processing fee from lender pricing grid
- **PF Split**: Processing fee revenue distribution between platform and partners
- **ROI Split**: Interest revenue distribution between platform and partners
- **Payout Amount PF**: Calculated processing fee payout amount
- **Payout ROI**: Calculated interest-based payout amount

## Implementation Benefits

1. **Data Integrity**: Single source of truth for commercial terms at the application level
2. **Audit Trail**: Historical record of commercial terms applied to each application
3. **Streamlined Reporting**: Direct data access for reporting without manual intervention
4. **Efficient Payout Processing**: Automated payout file generation based on stored values
5. **Reduced Manual Effort**: Elimination of manual data enrichment processes

## Considerations

- Create a new data structure to store commercial data as part of the credit application object
- Implement data validation to ensure complete commercial information
- Add timestamp and user attribution for commercial data changes

## Example data table

| **S_No** | **Platform** | **Type** | **Tata Interest base rate** | **Bajaj Interest base rate** | **DSP Interest base rate** | **Tata PF base rate** | **Bajaj PF base rate** | **DSP PF base rate** | **PF Sharing** | **Trail Sharing** | **PF Sharing %** | **Trail Sharing %** | **Comments** | Signoff | Actionable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Advisorkhoj | Partner |  |  |  |  |  |  |  | 0.5 |  |  |  |  |  |
| 2 | Advisorkhoj | Platform |  |  |  |  |  |  |  | 0.1 |  |  |  |  |  |
| 3 | AssetPlus | Borrower |  |  |  |  |  |  |  | 0.5, 0 |  |  | Line created, Enhanced (Agreement, Margin), Renewal after 1st May 2024, sharing is 0 else 0.5 |  |  |
| 4 | AssetPlus | Platform |  |  |  |  |  |  |  | 0.55 |  |  |  |  |  |
| 5 | Beyond Irr | Platform |  |  |  |  |  |  | 200 | 0.5 |  |  |  |  |  |
| 6 | BharatNXT | Platform | 9.5 | 9.5 | 9.5 |  |  |  |  |  | 50% | 50% | 1. PF: 50% of PF charged above base rate2. Trail: 50% sharing above the base rate (interest rate) |  |  |
| 7 | BharatPe | Platform |  |  |  |  |  |  |  |  |  |  | Slab based sharing Disbursal amount in a calendar month by Referrer customers ->Less than Rs.1croreRs.Icrore Rs.and above but lessthanRs.ScroreScroreand above but lessthanRs. 10croreRs.10crore and aboveWhere sanctioned limit isFees payable per customer basis the sanction limit per calendar monthLess than Rs. 2 Lakh1,8001,8751,9502,025Rs. 2 Lakh and above but less thanRs. 5 Lakh1,9502,0252,1002,175Rs. 5 Lakh and above but less thanRs. 10 Lakh2,2002,2752,3502,425Rs.10 Lakh and above3,0003,0753,1503,225 |  |  |
| 8 | Credit Mantri | Platform | 10 | 10 | 10 | 999 | 999 | 999 |  |  | 50% |  | 1. PF: 50% of PF charged above base rate2. Tral: if agreement_roi > 10.75, then 70% above base rate else 100% above base rate |  |  |
| 9 | FundsIndia | Platform |  |  |  |  |  |  | 200 | 0.6 |  |  |  | Keyur |  |
| 10 | IndiaLends | Platform | 9.95 | 9.95 | 9.95 | 999 | 999 | 999 |  |  | 70% |  | 1. PF: 70% of PF charged above base rate2. Tral: if agreement_roi > 10.75, then 70% above base rate else 100% above base rate | Keyur |  |
| 11 | Investwell | Borrower |  |  |  |  |  |  |  | 0.5, 0 |  |  | Line created, Enhanced (Agreement, Margin), Renewal after 1st May 2024, sharing is 0 else 0.5 |  |  |
| 12 | Investwell | Platform |  |  |  |  |  |  | 200 | 0.6 |  |  |  |  |  |
| 13 | Jupiter | Platform | 9.5 | 9.5 | 9.5 | 350 | 500 | 350 |  |  | Tata: 60%Bajaj: 50%DSP: 60% | Tata: 80%Bajaj: 50%DSP: 80% | Sharing above base rateTata rate to be confirmed as per agreement -pending on [Nitesh kumar](mailto:nitesh.kumar@voltmoney.in) [Kapil Nagal](mailto:kapil.nagal@voltmoney.in) |  |  |
| 14 | Lark | Platform |  |  |  | 999 | 999 | 999 |  |  |  |  | PF: 100% above base rate till 4999abvoe 4999 50%Trail: 100% revenue sharing to lark till 11% abvoe 11% 70% revenue sharing BaseRate:1. Monthly avg. AUM < 100Cr - 9.9%2. 100Cr <Monthly avg. AUM < 250 Cr - 9.85%3. Monthly avg. AUM > 250Cr - 9.8% |  |  |
| 15 | MyFi | Platform | 9.99 | 9.99 | 9.99 | 999 | 999 | 999 |  |  | 70% |  | 1. PF: Sharing above base rate2. Tral: if agreement_roi > 10.75, then 70% above base rate else 100% above base rate |  |  |
| 16 | ParkPlus | Platform | 9.75 | 9.75 | 9.75 | 999 | 999 | 999 |  |  | 50% | 50% | Sharing above base rateIf monthly average POS > 50Cr then revenue sharing = 70% | Keyur |  |
| 17 | PhonePe | Platform |  |  |  |  |  |  |  |  |  |  | Sanction Limit        Payout per application10,000- 25,000.        50025,000 - 1,00,000        ₹7501,00,000- 5,00,000      ₹1,000> 5,00,000                   ₹1,250 | Keyur |  |
| 18 | Niyo | Platform | 9.5 | 9.5 | 9.5 | 500 | 500 | 500 |  |  | 60% | 65% | Sharing above base rate |  |  |
| 19 | Prudent | Platform |  |  |  | 750 | 750 | 750 |  |  |  |  | As discussed, PFA new commercials:Base Processing fees (remains same)Base PF is equal to Rs 750/-70% of PF income above Rs 750/- belongs to Prudent. Trail incomeif end customer interest rate <=10.50% p.a.:100% belongs to Prudent from a base rate of 9.85% to 10.50%.if end customer interest rate >10.50% p.a.:80% belongs to Prudent above base rate of 9.75%Example:If end customer interest rate is 10.50%, 65bps trail income goes to PrudentIf end customer interest rate is 10.75%, 80bps trail income goes to Prudent | Keyur | Puneet |
| 20 | PostPe | Platform |  |  |  |  |  |  |  |  |  |  | Slab based sharing Disbursal amount in a calendar month by Referrer customers ->Less than Rs.1croreRs.Icrore Rs.and above but lessthanRs.ScroreScroreand above but lessthanRs. 10croreRs.10crore and aboveWhere sanctioned limit isFees payable per customer basis the sanction limit per calendar monthLess than Rs. 2 Lakh1,8001,8751,9502,025Rs. 2 Lakh and above but less thanRs. 5 Lakh1,9502,0252,1002,175Rs. 5 Lakh and above but less thanRs. 10 Lakh2,2002,2752,3502,425Rs.10 Lakh and above3,0003,0753,1503,225 |  |  |
| 21 | Redvision | Borrower |  |  |  |  |  |  |  | 0.5, 0 |  |  | Line created, Enhanced (Agreement, Margin), Renewal after 1st May 2024, sharing is 0 else 0.5 |  |  |
| 22 | Redvision | Partner |  |  |  |  |  |  | 200 | 0.5 |  |  |  |  |  |
| 23 | Redvision | Platform |  |  |  |  |  |  |  | 0.1 |  |  |  |  |  |
| 24 | Tata digital | Platform | 9.85 | 9.85 | 9.85 | 999 | 999 | 999 |  |  | 50% | 100% | Sharing above base rate | Keyur |  |
| 25 | Sankash | Platform | 9.5 | 9.5 | 9.5 |  |  |  |  |  |  | 60% | Sharing above base rate |  |  |
| 26 | ZFunds | Borrower |  |  |  |  |  |  |  | 0.5, 0 |  |  | Line created, Enhanced (Agreement, Margin), Renewal after 1st May 2024, sharing is 0 else 0.5 |  |  |
| 27 | ZFunds | Platform |  |  |  |  |  |  | 200 | 0.5 |  |  |  |  |  |
| 28 | Choice | Platform | 9.99 | 9.99 | 9.99 | 999 | 999 | 999 |  |  | 70% |  | Sharing above base rate100% trail income above base rate till 10.5%Above 10.5%, 70% trail income belongs to Choice | Keyur | Puneet |
| 29 | Zype | Platform | 9.9 | 9.9 | 9.9 | 750 | 750 | 750 |  |  | 100% | 100% | Sharing above base rate |  |  |
| 30 | Compound Express | Platform |  |  |  |  |  |  |  |  |  |  |  |  |  |