# [IronGrid] Email trigger for ops in case of disbursal rejection due to bank account mistmatch

: Ameya Aglawe
Created time: October 24, 2024 3:21 PM
Status: Not started
Last edited: March 31, 2026 8:24 AM

## What is the problem?

- After the application is complete, if a user requests Ops team for a bank account change then our operation team updates the bank account in our system through admin action, and asks lender operations team to update the bank account is their system.
- In a few cases where the bank account is not updated on the lender’s end, and user withdrawal requests gets rejected because the lender disbursement (save disbursement API) throws an error -

```jsx
("Bank account details for creditId: " +
        credit.getCreditId() + " does not match with the bank account details from " +
        "lender. Lender details " + Serializer.toJsonString(disbursementInfo.getBankAccountDetails())
        + ", Our details " + applicationBankAccount, VoltErrorCode.MAPPED_BANK_MISMATCH);
```

- This error reflects the bank mismatch at our & lender’s end. In such cases the Ops comes to know about this issue at the end of day report, and there is no trigger system to quickly unblock the user

## What is the solution?

- We raise a send grid email to the ops team as soon as a disbursal is rejected due bank mis-mismatch, so that Ops is notified and they can quickly un-block the customer by contacting lender’s operation team and getting bank account updated at their end.

## Requirements

### Phase 1 - Send email to our Ops

- Email sender & receiver
    - from : [no-reply@voltmoney.in](mailto:support.internal@voltmoney.in)
    - to : [tata.operations@voltmoney.in](mailto:tata.operations@voltmoney.in) (If lender of the application is TATA)
    - to : [operations@voltmoney.in](mailto:operations@voltmoney.in) (If lender of the credit application is BAJAJ)
- Email subject : Disbursal on hold - /disbursal_id/
- Email template :
    
    <aside>
    💡
    
    # Disbursal on hold - bank account mismatch
    
    Hi team, 
    
    Please find the details for the disbursal on hold due to customer bank account not found in lender system
    
    - Customer’s name :  {full_name}
    - Customer’s PAN : {account_holderpan}
    - Disbursal request : {Amount} at
    - Bank account details in our system : 232801527196 - ICIC0002328 [Bank account number - IFSC number]
    - Lender loan account number : /filler/
    - Lender credit ID : /filler/
    
    Please map the correct bank account of the customer to unblock the disbursal.
    
    ---
    
    </aside>
    

- Send Grid : https://docs.google.com/document/d/1kDuuuykxsS3LuQzVdgejHuQxWry87v1EPOVp6JxiPSg/edit?usp=sharing

### Phase 2 - Send email to lender operations team directly with our Ops in cc.