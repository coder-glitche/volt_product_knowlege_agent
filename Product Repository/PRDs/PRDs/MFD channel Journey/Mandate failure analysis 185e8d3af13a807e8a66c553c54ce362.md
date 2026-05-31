# Mandate failure analysis

Top 5 banks with highest failure rates (minimum 20 transactions):

1. State Bank of India has the highest number of failures (429) with failure rate of 33.36%
2. Airtel Payments Bank: 64.71% (22/34)
3. Fino Payments Bank: 52.00% (13/25)
4. UCO Bank: 46.15% (18/39)
5. AU Small Finance Bank & Dhanlaxmi Bank: 45.00% (9/20)
6. IDBI: 40.28% (29/72)

Customer-Related (738 cases):

- No response received from customer while performing: 415 @Vinit Pramod Sarode @Nihal Simha M S can you call these customers ? /
- Transaction rejected/cancelled by Customer: 122
- Browser closed by customer in mid transaction: 96
- User rejected transaction on pre-Login page: 23
- Previous Request in Progress: 21
- Maximum tries exceeded for OTP: 5
- Time expired for OTP: 1

Authentication/Validation Issues (217 cases):

- Aadhaar Number not linked with Debtor AccNo: 77
- Debit card validation failed - Invalid PIN: 25
- Authentication Failed: 9
- Debit card not activated: 11
- Invalid User Credentials: 5
- Invalid OTP value: 2
- Invalid Aadhaar Number/Virtual ID: 2
- Debit card Blocked: 5
- Invalid bank OTP: 1
- OTP invalid: 1
- Debit card validation failed - Invalid card: 1
- Debit card validation failed - Invalid CVV: 1

Technical Issues (168 cases):

- UNNKNOWN_ERROR: 79
- Technical errors/connectivity at bank: 75
- Error in Processing Mandate: 3
- Error in decrypting: 3
- Error in Posting Details: 2
- INVALID BANK RESPONSE: 1
- Error processing Aadhaar OTP: 1

Account-Related Issues (127 cases):

- Mandate Not Registered (insufficient balance): 47
- Account not in regular Status: 13
- No such account: 7
- Account Number not registered with Net-banking: 7
- Account Number registered for view-only: 8
- Account inactive: 3
- Account Inoperative: 1
- Account type mismatch with CBS: 1

Limit/Restriction Issues (32 cases):

- Bank Restricts Duplicate request/Amount Exceeds Limit: 21
- Amount Exceeds E-mandate Limit: 11

Other Issues (49 cases):

- Merchant MsgId duplicate: 11
- Mandate registration not allowed for Joint account: 8
- Bank RjctRsn ReasonCode empty/incorrect: 5
- AUA license expired: 2
- Aadhaar number does not have mobile number: 8