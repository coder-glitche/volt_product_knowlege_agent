# [IronGrid] Un-lien related issues

: Ameya Aglawe
Created time: October 24, 2024 4:51 PM
Status: Not started
Last edited: November 5, 2024 12:48 PM

## Fund level status of un-pledge request

**Phase 1** 

- Terminal statuses of funds’ un-pledge request are SUCCESS, FAILED.
- We will keep polling the status of all the funds until we get the terminal statuses of each of the funds
- We keep polling the API for 4 days every hour until we get the status of all the fund
- Un-pledge request level terminal status (will be updated once terminal state of all the funds is reached)
    - If all the funds’ status is SUCCESS, we mark the status of un-pledge as SUCCESS → In FE we will show Success as the status of unpledge request
    - If any of one the funds’ status is SUCCESS, we mark the status of un-pledge as PARTIAL_SUCCESS → In FE we will show Success as the status of unpledge request
    - If status of all the funds are rejected/failed then we store status as FAILED → In FE we will show Failed as the status of unpledge request
- We will store the individual status of all the funds under the un-pledge request
- API Documentation :

[Release Status 1 (1).docx](%5BIronGrid%5D%20Un-lien%20related%20issues/Release_Status_1_(1).docx)

**Phase 2** 

- We will monitor the partial success un-pledge request occurrence, and accordingly chart out a UI handling, where we can show and convey partial un-pledge success to the user.

## Excess margin handling in un-pledge request

**For BFL (only need to make this change for BAJAJ)** 

- While a user is requesting, we get the net payable from the ForeClosure details API for using it in our buffer calculation to calculate the number of units the user can raise for un-pledge.
- 3 fields which are present in Foreclosure details API :
    - net payable = Total due - Excess Margin
    - Total Due
    - Excess Margin
- For BAJAJ, we will use totalDue field in place of net payable field for calculating total outstanding.

### **User not able to request un-lien request if stocks present in their holding**

- **Issue**
    - When a user has stock in their account, and when they tap on view details, they we get a null pointer error. This is because we hit asset_meta_data table for showing fund details in the manage limit screen, but this table just contains data for MFs and not stocks, hence gives a null pointer error
- **Solution**
    - We will only show the ISINs present in the asset_meta_data table & won’t store ISINs which are not in asset_meta_data table in the credit_asset_mapping data
    - PAN : AERPL7873B (Bharat’s account)
        - Holding statement
            
            ![Screenshot 2024-10-29 at 6.33.34 PM.png](%5BIronGrid%5D%20Un-lien%20related%20issues/Screenshot_2024-10-29_at_6.33.34_PM.png)
            
        - Credit_asset_mapping_main table (audit)
            
            *Stock not present in the credit_asset mapping table* 
            
            Credit_asset_mapping_id :  8a80100486a7d11b0186badc4419004c	
            amfi_code : 119016	
            asset_repository: CAMS	
            asset_type : **MUTUAL_FUND**	
            created on : 2023-03-07 06:57:22.969	
            credit_id : 8a80100486a7d11b0186badc43f6004b	
            dp_of_security: 51338.42	
            folio no: 15254301	
            isin code : **INF179K01YM7**		
            last_updated_on : 2024-03-04 19:54:34.214	
            ltv : 0.80		
            pledged_units : 2174.2880		
            audit_sequence_number : 9321491602152		
            updated_date_time : 2024-03-04 20:05:25.564	
            
        - Credit_asset_mapping_main query result against the credit_id
            
            ![image.png](%5BIronGrid%5D%20Un-lien%20related%20issues/image.png)
            

### Adding un-pledge related validation in BE

**Checks to be added** 

- Jay to share the tech solutioning doc of the customer
- Folio level checks need to be added
- Need to create validation in init API using this API :

app/borrower/lms/credit/lender/manageLimitConfig

- BAJAJ Issue highlight
- BAJAJ Ops → KYC Documents
- POD transaction ID
- Anirudh, Pratik, Sagar everyone is travelling
- Analytics CRON job
- Wanted to keep you in loop as TAT might be impacted