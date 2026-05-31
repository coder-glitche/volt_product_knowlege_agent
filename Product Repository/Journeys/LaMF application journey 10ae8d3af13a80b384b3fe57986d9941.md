# LaMF application journey

[APIs](LaMF%20application%20journey/APIs%2010ae8d3af13a80ca9cb6eb9f1a098ddf.md)

[API grouping ](LaMF%20application%20journey/API%20grouping%2010ae8d3af13a8076bcdce2f44a6ea73f.md)

[flows api ](LaMF%20application%20journey/flows%20api%2010de8d3af13a80b8ad4dce117eda38b2.md)

[Pledge Error PRD](LaMF%20application%20journey/Pledge%20Error%20PRD%2010de8d3af13a8002a237cae253c5b23e.md)

The journey to create a loan against mf is as follows 

- login
    - user logs in using mobile number and otp validation
- PAN verification
    - user enter DOB and PAN to validate pan , API - decentro
- Fetch folio
    - we ping Cams/KFin to get the folio for the user
    - We ping them manually
    - we have option of gettign both from MF central
- One the folio is fetched we run BRE to calcualte eligible LImits as per lender prescribed calculation and appored lists
    - Folio have ISIN , NAV etc details
- We assign the customer basis BRE to either Bajaj ot TATA capital
- KYC of the customer aadhar - API is diifetent for tata and bajaj
- Bank account verification
- Mandate setting
- Logement
- KFS and docuemnttation

Support 

I have created and displayed the table documenting the journey steps, partners, and API names in Google Sheets format. Let me know if you'd like to modify or download the table.

[Journey_Steps_with_Partner_and_API_Info.csv](LaMF%20application%20journey/Journey_Steps_with_Partner_and_API_Info.csv)

| Step | improvements | Description | Partner/Service | API Name |  |
| --- | --- | --- | --- | --- | --- |
| Login |  | User logs in using mobile number and OTP validation |  | [https://api.staging.voltmoney.in/api/client/auth/requestOtp/v2/+919892732644?enableWhatsapp=true](https://api.staging.voltmoney.in/api/client/auth/requestOtp/v2/+919892732644?enableWhatsapp=true) |  |
| Verify OTP |  |  |  | https://api.staging.voltmoney.in/api/client/auth/verifyOtp/
 |  |
| user details  |  |  |  | https://api.staging.voltmoney.in/app/borrower/user
 |  |
| Email verification  |  |  | Google sso | 
https://accounts.google.com/o/oauth2/iframerpc?action=checkOrigin&origin=https%3A%2F%2Ftest.staging.voltmoney.in&client_id=62646021413-queb1g13go0snvnotl0ee06t68jcgb98.apps.googleusercontent.com |  |
|  |  |  | Email / manual |  |  |
|  |  |  |  | [https://api.staging.voltmoney.in/app/borrower/accountAttributes/3a11389a-c67f-4e79-b4ab-fce1d385e913](https://api.staging.voltmoney.in/app/borrower/accountAttributes/3a11389a-c67f-4e79-b4ab-fce1d385e913) |  |
|  |  |  |  |  |  |
| PAN Verification |  | User enters DOB and PAN to validate PAN | Decentro | Decentro PAN API |  |
| Fetch Folio |  | Ping CAMS/KFin to get the folio for the user | CAMS/KFin, MF Central (optionally) | CAMS/KFin API, MF Central API |  |
| Run BRE and Calculate Eligible Limits |  | Run BRE to calculate eligible limits as per lender prescribed calculations | Internal BRE system |  |  |
| Assign Lender |  | Assign customer to either Bajaj or TATA Capital based on BRE | Internal BRE system |  |  |
| KYC Verification |  | KYC of the customer with different APIs for Bajaj and TATA Capital | Bajaj/TATA Capital KYC APIs | Bajaj KYC API, TATA Capital KYC API |  |
| Bank Account Verification |  | Verify the user's bank account |  |  |  |
| Mandate Setting |  | Set up the mandate for auto-debit |  |  |  |
| Lodgement |  | Process loan lodgment |  |  |  |
| KFS and Documentation |  | Complete KFS (Key Fact Statement) and documentation process |  |  |  |