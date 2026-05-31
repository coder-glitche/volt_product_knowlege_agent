# [IronGrid] Adding un-pledge validations in BE

: Ameya Aglawe
Created time: October 25, 2024 1:04 PM
Status: Not started
Last edited: October 25, 2024 1:20 PM

### Validations present in FE

**FE Checks** 

- Manage limit
    - Remove pledge
    - Pledge more
    - Pledge history
- At this page we have a starting check of buffer
- User taps on Remove pledge and lands on the screen with list of funds
    - Buffer check applied again to calculate the number of units which can be selected by the user for un-pledging

**Checks to be added** 

- Jay to share the tech solutioning doc of the customer
- Folio level checks need to be added
- Need to create validation in init API using this API :

app/borrower/lms/credit/lender/manageLimitConfig