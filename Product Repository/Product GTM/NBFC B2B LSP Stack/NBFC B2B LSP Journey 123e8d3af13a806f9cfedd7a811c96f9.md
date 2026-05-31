# NBFC B2B LSP : Journey

# Journey Overview

Below is the envisaged customer journey as part of the B2B stack.

- **Mobile verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP based) in an API to DSP.
- **Email verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP/SSO based) in an API to DSP.
- **Fetch**: this step requires explicit consent through OTP from the customer using MFC or CAMS/KFin. This can be done through one of the methods mentioned in [Fetch step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a802a83dac810aab506a5).
- **Offer acceptance**: this step requires the customer to confirm the offer on the partner’s UI and the partner intimates DSP as mentioned in [Offer Acceptance step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a8056b782ece5c9307d35).
- **KYC verification**:
- **Bank account validation**:
- **Mandate registration**:
- **Pledge**:
- **KFS**:
- **Agreement**:
- Loan creation:
- **Withdrawal**:
- 

# Journey Points

## Approach Overview

Below are the key interactions/ touchpoints in the journey and the preferred and fallback approach for each step.

| Step | Preferred Approach | Secondary Approach |
| --- | --- | --- |
| Mobile verification | Approach 2: LSP passes the mobile verification log to DSP |  |
| Email verification | Approach 2: LSP passes the email verification log to DSP |  |
| Funds fetch | Approach 2: LSP fetches the funds from MFC through DSP APIs |  |
| NAV and LTVs | DSP to maintain the NAV and LTVs of each fund at its end. LSP can use that or can use their list as long as the values are aligned to our policy |  |
| Offer acceptance | Approach 2: LSP fetches the offer from DSP passes the offer acceptance details to DSP |  |
| KYC verification | Approach 2: LSP verifies the KYC through DSP’s APIs directly |  |
| Bank account validation | Approach 2: LSP passes the bank account to be added which will be validated async |  |
| Mandate registration | Approach 2: LSP integrates with DSP’s APIs and handles redirection to NPCI, etc |  |
| Pledge | Approach 2: LSP pledges the funds from MFC through DSP APIs |  |
| KFS | Approach 2: LSP integrates with DSP’s APIs and renders the KFS on their UI |  |
| Agreement | Approach 1: LSP integrates with DSP’s APIs and customer accepts on DSP’s URL |  |
| Account Creation | LSP integrates with DSP’s APIs and passes all the fields to confirm account creation  |  |
| Withdrawal | Approach 1: Integrate with DSP’s APIs directly. Payout method and logic decided by DSP | Approach 2: Integrate with DSP’s  APIs directly. Payout method and logic decided by LSP |
| Adhoc Repayments | Approach 1: Integrate with DSP’s  APIs directly. Payment method and logic decided by DSP | Approach 3: Use DSP’s sub-MID on a PG like Razorpay/ Cashfree/ PayU |
| Interest Repayments (Mandate presentation) | DSP presents the mandate from its end and intimates the LSP of the presentation status |  |
| Unpledge | Approach 2: LSP pledges the funds from MFC through DSP APIs |  |
| Closure/Foreclosure | LSP places a request for closure and DSP validates and confirm |  |
| Enhancements | LSP integrates with DSP’s APIs to enhance limits by pledging additional funds |  |
|  |  |  |

Open points/ Next steps.

- MFC integration across fetch, pledge and unpledge
- Setup effort → Mandate
- Account creation
- Communications
- Compliance

## Communication Overview

| Template | Event | Frequency | Sender |
| --- | --- | --- | --- |
| Welcome mail | Account opening | Once | DSP |
| Collateral valuation & statement of account | Monthly statements | 1st of every month at 6PM | DSP |
| Margin call/ Shortfall | On short-fall | Everyday post 10AM cron job | DSP |
| Collateral release confirmation | On event | On event | DSP |
| No due certificate | Loan closure | Once | DSP |
| Additional Pledge | On event | On event | DSP |
| Collateral valuation | On demand | On demand | DSP/ LSP |
| Loan disbursement confirmation | On event | On event | DSP/ LSP |
| Account Statement | On demand | On demand | DSP/ LSP |
| Deviations + Credit referral communication | - | - | LSP |
| Loan Approval | On event | On event | LSP |
| Payment reminders(Mandate/ outstanding dues) | On event | 48hrs before presentation | LSP |
| Repayment confirmations  | On event | On event | LSP |
| Loan Closure Initiation | On event | On event | LSP |
| Bounce notification | On event | On event | LSp |

## Lead Creation

|  |  |
| --- | --- |
|  |  |
|  |  |

## Funds Fetch

There are 2 options to handle fetching of funds.

- MFC
- CAMS & KFin

MFC is the most seamless way of fetching funds from a DSP as well as a partner perspective.

- There are 3 ways to bring the fetched funds into our system with MFC fetch as the preferred approach. Below are the scores against each approach.
    
    
    | Aspect | Approach 1 | Approach 2 | Approach 3 |
    | --- | --- | --- | --- |
    | **Overview** | Integrate with MFC with DSP’s credentials and push the data to DSP | Integrate with DSP’s MFC fetch APIs directly | Integrate with MFC with partner’s credentials and push the data to DSP |
    | **Customer Experience** | High (3) | High (3) | High (3) |
    | **Partner dev. effort** | Medium (2) | Medium (2) | Medium (2) |
    | Accuracy of data | Medium (2) | High (3) | Medium (2) |
    | Success rate (fetch) | High (3) | High (3) | Medium (2) |
    | Effort to consume (DSP) | Low (1) | High (3) | High (3) |
    | Compliance adherence | High (3) | High (3) | Medium (2) |
    | Security concerns | High (3) | High (3) | Low (1) |
    | Beta go-live effort | High (3) | High (3) | High (3) |
    | Overall | 20 | 22 | 18 |

Basis the above considerations, approach 2 is the most recommended flow.

## Offer Acceptance

The offer acceptance allows the customer sets the credit limit basis the funds fetched. This will be an iterative flow where the LSP can share the updated list of funds to fetch the updated offer amount.

The LSP can also inform DSP on the limit the customer wants basis their preference which will be validated before the same is confirmed to the LSP. In addition, the LSP informs DSP of the commercials for the customer within the agreed limits.

- There are 2 approaches to building this capability for LSPs. Below are the scores against each approach. Below are the scores against each approach.
    
    
    | Aspect | Approach 1 | Approach 2 |
    | --- | --- | --- |
    | **Overview** | Integrate with DSP’s credentials for offer generation & acceptance | Integrate with DSP’s credentials for acceptance. LSP renders the offer on their end |
    | **Customer Experience** | High (3) | High (3) |
    | **Partner dev. effort** | High (3) | Medium (2) |
    | **Partner UI experience** | Medium (2) | High (3) |
    | **Accuracy of data** | High (3) | Medium (2) |
    | **Effort to consume (DSP)** | Medium (2) | High (3) |
    | **Compliance adherence** | High (3) | High (3) |
    | **Security concerns** | High (3) | High (3) |
    | **Beta go-live effort** | High (3) | High (3) |
    | **Overall** | 19 | 22 |

Basis the above considerations, approach 2 is the most recommended flow as it provides the partner complete control as well as a native experience.

## KYC

The KYC setup is the step where the customer confirms their KYC. This will be initiating the Digilocker flow for now, which will be eventually augmented with CKYC and Aadhaar XML flow as additional capabilities. 

In this flow, the LSP hits DSP’s APIs to initiate each step and at the end of the session, DSP confirms if the KYC is as per DSP’s compliance requirements after backend validations on Fenix’s end.

- There are 3 approaches to this step. Below are the scores against each approach.
    
    
    | Aspect | Approach 1 | Approach 2 | Approach 3 |
    | --- | --- | --- | --- |
    | **Overview** | Integrate with Digilocker with DSP’s code and push the data to DSP | Integrate with DSP’s KYC APIs directly | Integrate with Digilocker with partner’s credentials and push the data to DSP |
    | **Customer Experience** | High (3) | High (3) | High (3) |
    | **Partner dev. effort** | High (3) | Medium (2) | High (3) |
    | **Accuracy of data** | Medium (2) | High (3) | Medium (2) |
    | **Success rate (fetch)** | High (3) | High (3) | High (3) |
    | **Effort to consume (DSP)** | Medium (2) | High (3) | High (3) |
    | **Compliance adherence** | High (3) | High (3) | Medium (2) |
    | **Security concerns** | Medium (2) | High (3) | Low (1) |
    | **Beta go-live effort** | High (3) | High (3) | High (3) |
    | **Overall** | 21 | 23 | 20 |

Basis the above considerations, approach 2 is the most recommended flow as it provides the partner complete control as well as a native experience without compromising on security.

## Bank Account Verification

This step requires the LSP to pass the bank account to be mapped at DSP’s end. DSP validates the bank account at its end irrespective of where the LSP validates or not.

DSP confirms if the added bank account meets the criteria as per our backend checks like name match, type of account, etc.

- There are 3 approaches to this step. Below are the scores against each approach.
    
    
    | **Aspect** | **Approach 1** | **Approach 2** | **Approach 3** |
    | --- | --- | --- | --- |
    | **Overview** | Integrate with DSP’s  APIs directly (validation immediately) | Integrate with DSP’s  APIs directly (validation later) | Validate bank account at LSP’s end and push the data (DSP validates it separately) |
    | **Customer Experience** | Medium (2) | High (3) | High (3) |
    | **Partner dev. effort** | Medium (2) | Medium (2) | High (3) |
    | **Accuracy of data** | Medium (2) | High (3) | Medium (2) |
    | **Success rate (validation)** | High (3) | High (3) | High (3) |
    | **Effort to consume (DSP)** | Medium (2) | High (3) | High (3) |
    | **Compliance adherence** | High (3) | High (3) | Medium (2) |
    | **Security concerns** | High (3) | High (3) | Medium (2) |
    | **Beta go-live effort** | High (3) | High (3) | Medium (2) |
    | **Overall** | 20 | 23 | 20 |

Basis the above considerations, approach 2 is the most recommended flow as it provides the partner complete control as well as a native experience without compromising on security and at the same time, ensures the customer isn’t blocked in terms of flow.

## Pledge

This step requires the LSP to confirm from the customer which all funds they want to pledge. The LSP can choose to build the UI of their choice. DSP, from its end, shares the entire list of funds fetched from MFC in this API for the customer to pledge.

- There are 3 ways to bring the pledged funds into our system with MFC pledge as the preferred approach. Below are the scores against each approach.
    
    
    | **Aspect** | **Approach 1** | **Approach 2** |
    | --- | --- | --- |
    | **Overview** | Integrate with MFC with DSP’s credentials and push the data to DSP | Integrate with DSP’s MFC fetch APIs directly |
    | Integration with | MFC | DSP |
    | Credentials | DSP | DSP |
    | **Customer Experience** | High (3) | High (3) |
    | **Partner dev. effort** | Medium (2) | Medium (2) |
    | **Accuracy of data** | Medium (2) | High (3) |
    | **Success rate (fetch)** | High (3) | High (3) |
    | **Effort to consume (DSP)** | Low (1) | High (3) |
    | **Compliance adherence** | High (3) | High (3) |
    | **Security concerns** | High (3) | High (3) |
    | **Beta go-live effort** | High (3) | High (3) |
    | **Overall** | 20 | 22 |

Basis the above considerations, approach 2 is the most recommended flow as it provides the partner complete control as well as a native experience without compromising on security and at the same time, ensures the customer isn’t blocked in terms of flow.

## Mandate Registration

This step requires the LSP to register a NACH based mandate through one of the supported modes (Debit card, Netbanking, Aadhaar) using DSP’s utility code.

DSP informs the LSP if the mandate registered is accepted after backend validations like name match, UMRN validations, etc.

- There are 2 approaches to this step. Below are the scores against each approach.
    
    
    | Aspect | Approach 1 | Approach 2 |
    | --- | --- | --- |
    | **Overview** | Integrate with DSP’s credentials for mandate generation | Integrate with DSP’s credentials for mandate generation |
    | **Customer Experience** | High (3) | High (3) |
    | **Partner dev. effort** | High (3) | Medium (2) |
    | **Partner UI experience** | High (3) | High (3) |
    | **Accuracy of data** | Medium (2) | High (3) |
    | **Effort to consume (DSP)** | Medium (2) | High (3) |
    | **Compliance adherence** | Medium (2) | High (3) |
    | **Security concerns** | Medium (2) | High (3) |
    | **Beta go-live effort** | Medium (2) | High (3) |
    | **Overall** | 19 | 23 |

Basis the above considerations, approach 2 is the most recommended flow as it provides the partner complete control as well as a native experience though it does require additional effort

## KFS

This step requires the LSP to asks the customer to accept the KFS by hitting DSP’s APIs. The LSP can choose to build the UI of their choice. DSP, from its end, shares the entire KFS details as well as a PDF with DSP letterhead for the customer to view as required.

- There are 2 approaches to this step. Below are the scores against each approach.
    
    
    | Aspect | Approach 1 | Approach 2 |
    | --- | --- | --- |
    | **Overview** | DSP generates the KFS URL and PDF which the customer can accept on the DSP URL and DSP redirects the customer to the LSP’s URL | DSP generates the KFS parameters and PDF which the customer can accept on the LSP URL and the consent timestamp is passed to DSP |
    | Host URL | DSP | LSP |
    | **Customer Experience** | Medium (2) | High (3) |
    | **Partner dev. effort** | High (3) | Medium (2) |
    | **Partner UI experience** | Medium (2) | High (3) |
    | **Accuracy of data** | High (3) | Medium (2) |
    | **Effort to consume (DSP)** | High (3) | High (3) |
    | **Compliance adherence** | High (3) | Medium (2) |
    | **Security concerns** | High (3) | Medium (2) |
    | **Beta go-live effort** | High (3) | Medium (2) |
    | **Overall** | 23 | 19 |

<aside>
💡

Are we OK with the partner not showing the KFS PDF on UI? 

</aside>

Basis the above considerations, approach 2 is the most recommended flow as it provides the partner complete control as well as a native experience though it does require additional effort.

## Agreement

This step requires the LSP to asks the customer to accept the agreement and loan kit by hitting DSP’s APIs. Agreement, being a legal document needs to be handled with care.

- There are 2 approaches to this step. Below are the scores against each approach.
    
    
    | Aspect | Approach 1 | Approach 2 |
    | --- | --- | --- |
    | Host URL | DSP | LSP |
    | Type of sign | Explicit consent | Mobile/Aadhaar OTP |
    | **Overview** | Integrate with DSP’s APIs for agreement generation. Agreement is rendered on DSP’s URL | Integrate with DSP’s APIs for agreement initiation. Agreement is rendered on LSP’s URL but consented using OTP |
    | **Customer Experience** | Medium (2) | High (3) |
    | **Partner dev. effort** | High (3) | Medium (2) |
    | **Partner UI experience** | Medium (2) | High (3) |
    | **Accuracy of data** | High (3) | High (3) |
    | **Effort to consume (DSP)** | High (3) | High (3) |
    | **Compliance adherence** | High (3) | High (3) |
    | **Security concerns** | High (3) | Medium (2) |
    | **Beta go-live effort** | High (3) | Medium (2) |
    | **Overall** | 22 | 21 |

Basis the above considerations, approach 1 is the most recommended flow as it is highly compliant. At the same time, we will need to factor in approach 2 as this is expected to be of high interest among partners.

## Account Opening

This step requires the LSP to confirm if the customer is ready to take the facility from DSP as well as pass all the various details to DSP. This step will also involve lodgment of funds as well as opening a loan on Finflux’s end and confirming the Loan opening to the partner including LAN generation.

This step will vary depending on the flow that the LSP has incorporated at their end. DSP, from its end will validate the entire application flow at its end before creating the loan at its end. 

- Below are the validations that will be built at our end before the account is opened.
    
    
    | Aspect | Details | Comments |
    | --- | --- | --- |
    | Host URL | DSP |  |
    | Type of sign | Explicit consent |  |
    | PAN validation | PAN is valid and matches the application |  |
    | KYC validation | Digilocker is fetched for the application |  |
    | Credit Limit | Within the limits set by the  |  |
    | **Partner UI experience** | Medium (2) |  |
    | **Accuracy of data** | High (3) |  |
    | **Effort to consume (DSP)** | High (3) |  |
    | **Compliance adherence** | High (3) |  |
    | **Security concerns** | High (3) |  |
    | **Beta go-live effort** | High (3) |  |
    | **Overall** | 22 |  |

## Withdrawal

This step involves the LSP requesting DSP for withdrawal of funds. This will either be a sync or async capability depending on the type of transfer. The LSP is intimated of the status of the withdrawal in the response itself. The status of the response can be Success, Failure or Pending for IMPS and Failure or Pending for RTGS.

- There are 3 approaches to this step. Below are the scores against each approach.
    
    
    | **Aspect** | **Approach 1** | **Approach 2** | **Approach 3** |
    | --- | --- | --- | --- |
    | **Overview** | Integrate with DSP’s  APIs directly. Payout method and logic decided by DSP | Integrate with DSP’s  APIs directly. Payout method and logic decided by LSP | Disburse to borrowers from a dedicated account. Payout method and logic decided by LSP |
    | **Payout Method Control** | DSP | LSP | LSP |
    | **Payout Type Control (Net/Gross)** | DSP | LSP | LSP |
    | **Confirmation** | Sync/ Async | Sync/ Async | Sync/ Async |
    | **Customer Experience** | High (3) | High (3) | High (3) |
    | **Partner dev. effort** | Medium (2) | Medium (2) | High (3) |
    | **Accuracy of data** | High (3) | Medium (2) | Medium (2) |
    | **Success rate (validation)** | High (3) | High (3) | High (3) |
    | **Effort to consume (DSP)** | Medium (2) | High (3) | High (3) |
    | **Compliance adherence** | High (3) | Medium (2) | Medium (2) |
    | **Security concerns** | High (3) | High (3) | Low (1) |
    | **Beta go-live effort** | High (3) | Low (1) | NA |
    | **Overall** | 20 | 23 | 20 |

The LSP can subscribe to DSP’s withdrawal transaction callback where DSP will post the status of the withdrawal if subscribed. Alternatively, the LSP can poll the status of a withdrawal after a specific timeframe.

- 30 minutes for RTGS
- 10 seconds for IMPS
- Below are the elements of the withdrawal step.
    
    
    | Aspect | Details | Comments |
    | --- | --- | --- |
    | Host URL | DSP |  |
    | Payout BRE | Hosted by DSP |  |
    | Payout method | Defined by BRE |  |
    | Bank account | Needs to be valid |  |
    | Payout logic | Net disbursement | This can be gross going forward |
    |  |  |  |
    |  |  |  |
    |  |  |  |
    |  |  |  |
    |  |  |  |
    |  |  |  |
    |  |  |  |
    

## Adhoc Repayments

This step involves the borrower repaying DSP through a payment gateway flow on the LSP’s app or UI.

- There are 3 approaches to this step. Below are the scores against each approach.
    
    
    | **Aspect** | **Approach 1** | **Approach 2** | **Approach 3** |
    | --- | --- | --- | --- |
    | **Overview** | Integrate with DSP’s  APIs directly. Payment method and logic decided by DSP | Integrate with DSP’s  APIs directly. Payment method and logic decided by LSP | Use DSP’s sub-MID on a PG like Razorpay/ Cashfree/ PayU |
    | **Payment Method Control** | DSP | LSP | LSP |
    | **Commercial impact** | DSP | LSP? | LSP? |
    | **Payment Confirmation** | Sync | Sync | Sync |
    | **Customer Experience** | High (3) | High (3) | High (3) |
    | **Partner dev. effort** | Medium (2) | Medium (2) | High (3) |
    | **Accuracy of data** | High (3) | Medium (2) | Medium (2) |
    | **Success rate (payment)** | Medium (2) | Medium (2) | High (3) |
    | **Effort to consume (DSP)** | High (3) | High (3) | Medium (3) |
    | **Compliance adherence** | High (3) | Medium (2) | Medium (2) |
    | **Security concerns** | High (3) | High (3) | Low (1) |
    | **Beta go-live effort** | High (3) | Low (1) | Low (1) |
    | **Operational effort** | High (3) | Medium (2) | Medium (2) |
    | **Overall** | 25 | 20 | 21 |

## Interest Repayments

This step involves the borrower’s account being debited from the mandate being setup as per the registration step.

Interest repayment through NACH presentation will purely be managed by DSP.

- DSP intimates the LSP of the status of the mandate through webhook
- DSP intimates the LSP in case of bounce and representation

An alternative approach can be where the LSP hits the presentation APIs of DSP to present the mandate as well as fetch the status.