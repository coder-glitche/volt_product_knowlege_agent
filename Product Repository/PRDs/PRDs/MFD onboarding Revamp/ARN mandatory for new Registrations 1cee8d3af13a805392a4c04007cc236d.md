# ARN mandatory for new Registrations

### **Problem Statement:**

- Currently, the partner registration flow allows users to sign up with or without providing an ARN. This has led to a high volume of registrations from individuals who are not certified Mutual Fund Distributors (MFDs).
- Approximately 70% of current partner registrations fall into this category. This influx of non-MFD sign-ups places a significant strain on the onboarding team, requiring manual filtering and follow-up, reducing overall efficiency.

### **Proposed Solution:**

Modify the partner registration process to require a valid AMFI Registration Number (ARN) for successful sign-up. This will ensure that only verified MFDs can register as partners on the platform.

### **Implementation Requirements:**

- **Target Page:** https://staging.voltmoney.in/partner/signup/ (and subsequently production)
- Only applicable on New registrations , not existing MFDs
- **UI Changes:**
    - Remove the option/checkbox/link currently allowing users to proceed without an ARN (e.g., "I don't have an ARN number").
    - Modify the ARN input field to be mandatory.
- **Field Validation:**
    - The ARN field must not be empty upon form submission.
    - ~~The entered ARN must consist of exactly **6 digits**.~~
    - *(Note: For this initial implementation phase, no external validation against the AMFI database is required.)*
- **Error Handling:**
    - If the user attempts to submit the form without entering an ARN, display a clear inline error message (e.g., "ARN is required.").
    - ~~If the user enters an ARN that is not exactly 6 digits, display a clear inline error message (e.g., "ARN must be exactly 6 digits.").~~
- **Informational Text:**
    - Add clear text near the ARN field to inform users about the requirement and guide non-MFDs. Use the following text:
        
        > Enter your AMFI Registration Number (ARN)*
        > 
        > 
        > *Only registered Mutual Fund Distributors (MFDs) can sign up as partners. If you are an investor looking to use Volt Money, please go to our [**Customer registration**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fapp.voltmoney.in%2F%3Fstartnew%3Dtrue).*
        > 

**Expected Outcomes & Benefits:**

- **Reduced Non-MFD Registrations:** Significantly decrease (estimated 70% reduction) the number of sign-ups from users without a valid ARN.
- **Improved Onboarding Efficiency:** Allow the onboarding team to focus solely on qualified MFD partners, streamlining the verification and activation process.
- The Existing MFD has no impact / change

**Potential Risks & Considerations:**

- **Lower Overall Registration Volume:** Expect an initial decrease in the *total* number of registration submissions. However, the number of *qualified* registrations should remain stable or increase relative to effort.
- **User Experience for Non-MFDs:** Clear messaging is crucial to redirect non-MFD visitors appropriately and avoid user frustration. The provided text aims to address this.
- **ARN Validity (Future Scope):** While not in scope for this phase, future enhancements could include API-based validation to confirm the entered ARN is active and legitimate in the AMFI database.

**Next Steps:**

1. **Development:** Implement the UI, validation, and messaging changes as specified above.
2. **Deployment:** Deploy the changes to the staging environment (https://staging.voltmoney.in/partner/signup/) for testing.
3. **Testing:** Verify the changes function correctly (mandatory field, 6-digit validation, error messages, informational text, removal of non-ARN option).
4. **Monitoring:** After deployment to production, closely monitor:
    - Partner registration conversion rates.
    - Volume of successful registrations.
    - Feedback from the onboarding team regarding workload and lead quality.
    - Any user feedback related to the change.