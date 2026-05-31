# V-KYC Integration with Bajaj

We are asked by Bajaj to include V-kyc to do full KYC  according to compliance 

Scope 

| [S.No](http://s.no/) | Feature | Description | Why | Approach 1 / Tradeoff | Approach 2 | Approach 3 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Add Agent Call | Full KYC (DIGI+VCIP) | RBI compliance and Bajaj requirement | Integrate Bajaj V-KYC – may lower conversion rates | Do not integrate V-KYC and send to Tata – lower flexibility | Get Bajaj to waive V-KYC for existing customers |
| 2 | Digilocker KYC | Existing KYC | Required for KYC | Start V-KYC with Digilocker; if not completed, run it in parallel | Start V-KYC after Digilocker; user must complete V-KYC before Bank Account Verification (BAV) | Continue current funnel and start V-KYC at the end |
| 3 | In-app Link | URL callback with KYC URL | For an in-app experience | Use current setup for in-app view – requires testing | Send SMS from Bajaj with URL, schedule, and notification |  |
| 4 | Present Address Check | Bajaj will disable this from the frontend | To verify registered and present addresses | Bypass and mark address as the same, as the check is within India | Ask user to select Yes/No; if No, ask for proof of present address |  |
| 5 | URL Timeout | 1 hour from API call | N/A | Have a screen where the user triggers the API just before starting the call |  |  |
| 6 | Update Transaction ID | Required once V-KYC is complete | Needed in the agreement | Send the Transaction ID via the new API developed by the SFDC team |  |  |
| 7 | Existing Customer Handling | N/A | Existing customers do not require V-KYC | No V-KYC needed; we will get an "existing customer" flag in the response |  |  |
| 8 | Where to Add Agent Call | N/A | Integrate agent call into the flow | - Provide an option in the KYC step to continue with V-KYC.
 - If the user chooses "Do V-KYC later" or skips, start at the end. 
- Pros: Lets users know V-KYC is required early and keeps flexibility. - Cons: May increase drop-off and require more development time. | - Keep the existing flow until the Mandate and Agreement steps.
- Trigger V-KYC after the Agreement as a new step. 
- Add V-KYC to the stepper. 
- Pros: Easier to develop. 
- Cons: Frustration after agreement and document steps; stepper may look complicated.  |  |
| 9 | B2B2C, For MFD to get V-KYC of Users |  |  | MFD can send link to the users to get the V-KYC from customer |  |  |
|  | B2B |  |  | In case we have do not permissions in the Partner journey then we need to send comms to user to get V-KYC, Our SDK permissions - getting from saagar |  |  |
|  | UAT TESTING  |  | V-KYC till agent call is working. As no agents are provided in UAT we are unable to have a end to end test  |  |  |  |

V-kyc test video after Digilocker

[Screen_Recording_20241014_183426_Samsung Internet_2.mp4](V-KYC%20Integration%20with%20Bajaj/Screen_Recording_20241014_183426_Samsung_Internet_2.mp4)

![Screenshot 2024-10-14 at 12.10.26 PM.png](V-KYC%20Integration%20with%20Bajaj/Screenshot_2024-10-14_at_12.10.26_PM.png)

Alternate 

- Provide option in the KYC step to continue with V_KYC
- will selfie be required?
- if user “Do V_KYC later” or skips then the start at the end
- This has the benefit of letting user know that V-KYC  is required and does not surprise them in the end. Make the stepper less intimidating.
- it keeps the flexibility with the user. user can complete the V-KYC is any other step is taking time
- It Might lead to increased drop-off, and will require more dev time to enable parallel V-kyc task

B2B2c

End customer has to do the KYC  flow. 

- MFD can send user link to the app. Challenge - APP download will create significant friction
- MFD can send a link to the V-KYC to be open in browser - simpler

points 

Talk to RM, 

B2b 

SDK 

Comms 

B2c APp 

funnel 

Vinit 

Partners -  Partner dashboard 

- IOS
- android
- PhonePe - web journey
- SDK
- permissions in partner app
-