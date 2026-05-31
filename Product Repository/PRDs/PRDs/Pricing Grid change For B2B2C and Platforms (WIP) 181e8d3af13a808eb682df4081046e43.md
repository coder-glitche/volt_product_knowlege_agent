# Pricing Grid change For B2B2C and Platforms (WIP)

: Naman Agarwal
Created time: January 20, 2025 2:36 PM
Status: In progress
Last edited: February 21, 2025 6:02 PM

Implementation Details:

Eligibility: Feature flag-enabled for selected platforms
Eligible Platforms: RedVision, Investwell, Prudent, Assetplus, Zfunds, FundsIndia, Advisorkhoj, Compound Express, MFD Direct(B2B2C) partners with Partner ID
Not Eligible: Affiliate partners
Rates based on Pledged Portfolio amount at Final Agreement stage:

< ₹50L: 10.49%
=₹50L - <1Cr: 10.35%
≥ ₹1Cr: 10.25%
PF : 999
Enhancement : 499
Next Steps:

Resolve mandate step issue
Complete QA testing
Get approvals from Business team
Deploy to production

**Rates excluding Gst**

| **SL Grid** | **ROI** | **PF(Rs.)** | **Enhancement fee(Rs.)** | **AMC(Rs.)** |
| --- | --- | --- | --- | --- |
| Upto 50L | 10.49% | 999 | 499 | 499 |
| 50L-1Cr | 10.35% | 999 | 499 | 499 |
| >1cr | 10.25% | 999 | 499 | 499 |
|  |  |  |  |  |

what the SL is the Limit Pledged by the customer ?

What happens incase of Enhancement or lien removal ?

Intrest calculator changes ?

AMC? - FAQ How will we collect ?

When will we post the AMC charges ?

How can we vaive AMC charges ?

how can we modify PF and enhancements?

Is AMC charges are taken by LSP or DSP?

Is AMC is part of SOA?

is AMC scheduled in the 2nd year ?

Identify the Design screens 

Identify the messaging sms, Website, WA, email 

KFS and agreement changes 

Questions ?

When are AMC charges posted 

- Along with PF ( ~2000 PF)
- 1 year after 1 PF * 3
- 1y after PF *2 for a 3 y loan

Date of posting?

ROI changes based on slabs

- Identify the DP range
- above the range  rate change

user registed and take a fetch 

they select the Funds and select a limit 

Next screen they see a offer

offer contains 

- PF 999
- AMC 499
- Interest rate 10.49— %

Refundablity of AMC if <7 days to foreclose?

Annual Maintaince charges

AMC Definition

- Annual maintenance fee for servicing the loan account
- Charged on loan anniversary date
- Non-refundable after first 3 days of charging

Closure Rules

- No pro-rata refund on early closure
- Full AMC charged even if closed within year
- Next AMC cycle starts from Loan Anniversary date
- AMC not applicable if loan is closed or Suspended

# 

## Billing Cycle Examples

| Sanction Date | PF + AMC Added to Bill | First Billing Date | Due Date | Example |
| --- | --- | --- | --- | --- |
| Jan 1-20 | February Bill | Feb 1 | Feb 7 | Sanctioned Jan 15 → Feb Bill |
| Jan 21-31 | March Bill | Mar 1 | Mar 7 | Sanctioned Jan 25 → Mar Bill |

## Fee Components

| Fee Type | Amount | Collection Timing | Failures Handling |
| --- | --- | --- | --- |
| PF | ₹999 | Next/Next-to-Next Bill | Added to subsequent bill + interest |
| AMC | ₹499 | Next/Next-to-Next Bill | Added to subsequent bill + interest |
| GST | 18% | Charged with PF & AMC | Follows principal amount |

## System Rules

1. Cut-off Date: 20th of each month
2. Bill Generation: 1st of month
3. Due Date: 5th of month
4. Auto Debit Date: 7th of month
5. Failure Handling: Roll to next cycle with interest

SLAB based ROI

SL definition 

- The Pledged Limit Fetched by the Lender will be considered for the slab
- The Pledged limit will be User selected Limit form the initial fetch amount

ROI to the user 

- the User will first see the ROI in the

AMC charges 

- waive off for a high utilisation rate
-