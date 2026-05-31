# TATA KFS and Agreement Phase 2

: Gautam Mahesh
Created time: September 27, 2024 5:19 PM
Status: In progress
Last edited: October 24, 2024 10:46 AM
Owner: Ayush Kumar

# **What problem are we solving?**

RBI guidelines requires that lenders and LSP showcase the KFS format as specified. While the KFS is designed keeping borrower protection in mind, handling it in a elegant way without compromising on the experience is a challenge.

---

# **How do we measure success?**

We intend to measure the success rate using the below metrics.

- Acceptance rate of atleast 95%
- Generating TAT of <5s
- Acceptance TAT from rendering of <30s
- Number of tickets related to KFS to be <5% of the KFS step applications

---

# **How are others solving this problem?**

Most lenders are solving the KFS in one of the below approaches.

- **Approach 1**: In this approach, the customer is displayed an offer page with a link to the KFS PDF itself. This PDF can be viewed and downloaded but is optional. The customer signs the agreement separately in the end. This is the approach taken by Piramal.
- **Approach 2**: In this approach, the customer is displayed an offer page with a link to the KFS PDF itself. This PDF needs to be consented by the customer as a mandatory step. The customer signs the agreement only in the end. This is the approach taken by InCred and suggested by Tata.
- **Approach 3**: In this approach, the customer is displayed with a link to the KFS PDF itself. This PDF can be viewed and downloaded but is optional. This is displayed on the Agreement page. The customer needs to sign the KFS with the agreement in the end. This is the approach taken by Cashe and Bajaj.

Below is a comparison of the approaches and their impact on customer experience.

| Aspect | Approach 1 | Approach 2 | Approach 3 |
| --- | --- | --- | --- |
| Placement of KFS | Offer | Offer | Agreement |
| Ease of understanding | High | High | High |
| Drop-offs | Low | Medium | Low |
| Effort on customer | Low | Medium | Medium |
| KFS - Agreement consistency | Medium | Medium | High |
| Customer viewing of KFS | Optional | Mandatory | Mandatory |
| Impact on Sanctions | Medium | High | Low |

There are some considerations for KFS that lenders have kept in mind.

- Customer needs to consent the KFS but not necessarily view the KFS
- RBI’s objective here is that the customer knows the charges they will be levied

After considering the subjective and objective elements, Approach 3 seems to the most experience friendly since it optimizes for most of the metrics.

Most lenders are solving the challenge of rendering KFS itself in 1 of the ways.

- Render as a full PDF or document object
- Render as a elegant UI like we have done for DSP
- Render the key items on UI elegantly with a detailed document

---

# **What is the solution?**

## Requirements overview (optional)

We are breaking down the requirement from TATA into 2 phase.

- Phase 1: In this phase, we will only modify the Agreement since TATA is good with this. This is live.
- Phase 2: As soon as Phase 1 is deployed to UAT, we will modify the KFS in one of the ways depending on the effort and faster go-live.
    - Replicate the DSP UI OR
    - Pass the HTML/PDF from BE

For now, we are going ahead with the approach of rendering the HTML/PDF from backend.

## User Flow Approaches

Broadly, there are 2 approaches that

## User stories / User flow

- **Current User Flow:**
    
    Below is the current Customer journey after the pledge step:
    
    **Step 1: Customer lands on the current page after completing the pledge step**
    
    ![Screenshot 2024-10-03 at 11.07.53 AM.png](TATA%20KFS%20and%20Agreement%20Phase%202/Screenshot_2024-10-03_at_11.07.53_AM.png)
    
    **Step 2: Customer sees the loader as mentioned below which redirects the customer to the agreement landing page. At this stage, we hit the SignDesk API with the updated agreement template**
    
    ![Screenshot 2024-10-03 at 11.08.19 AM.png](TATA%20KFS%20and%20Agreement%20Phase%202/Screenshot_2024-10-03_at_11.08.19_AM.png)
    
    **Step 3: Customer is redirected to the Agreement page generated in the new Agreement template designed by Volt through SignDesk as below.**
    
    ![Screenshot 2024-10-03 at 11.08.36 AM.png](TATA%20KFS%20and%20Agreement%20Phase%202/Screenshot_2024-10-03_at_11.08.36_AM.png)
    
    ![Screenshot 2024-10-03 at 11.08.53 AM.png](TATA%20KFS%20and%20Agreement%20Phase%202/Screenshot_2024-10-03_at_11.08.53_AM.png)
    
    **Step 4: Customer is redirected back to the page in case of app or closes the window and sees the page below after we receive a callback from TATA.**
    
    ![Screenshot 2024-10-03 at 11.09.06 AM.png](TATA%20KFS%20and%20Agreement%20Phase%202/Screenshot_2024-10-03_at_11.09.06_AM.png)
    
    **Step 5: The uploadDocument API is called to upload all documents to the webtop and the customer completes the loan application journey after the above step.**
    

 

- **Proposed User Flow (Approach 1)**
    
    Below is the modified Customer journey after the pledge step:
    
    **Step 1:** Customer lands on the below page after completing the pledge step. Here, we are adding the Key Fact Statement along with Agreement.
    
    ![Screenshot 2024-09-27 at 12.30.23 AM.png](TATA%20KFS%20and%20Agreement%20Phase%202/Screenshot_2024-09-27_at_12.30.23_AM.png)
    
    **Step 2:** Customer views the KFS as it is currently and consents. This will be changed in phase 2. In parallel, we hit TATA’s APIs and the customer is redirected to the next page
    
    ![Screenshot 2024-09-27 at 12.32.04 AM.png](TATA%20KFS%20and%20Agreement%20Phase%202/Screenshot_2024-09-27_at_12.32.04_AM.png)
    
    **Step 3:** Customer can see the agreement landing page where they click on the button. At this stage, we hit the SignDesk API with the updated agreement template
    
    ![Screenshot 2024-09-27 at 12.32.17 AM.png](TATA%20KFS%20and%20Agreement%20Phase%202/Screenshot_2024-09-27_at_12.32.17_AM.png)
    
    **Step 4:** Customer sees the loader as mentioned below which redirects the customer to the agreement landing page. At this stage, we hit the Signdesk API with the updated agreement template.
    
    ![Screenshot 2024-10-03 at 11.08.19 AM.png](TATA%20KFS%20and%20Agreement%20Phase%202/Screenshot_2024-10-03_at_11.08.19_AM%201.png)
    
    **Step 5:** Customer is redirected to the Agreement page generated in the new Agreement template designed by Volt through SignDesk as below.
    
    ![Screenshot 2024-10-03 at 11.08.36 AM.png](TATA%20KFS%20and%20Agreement%20Phase%202/Screenshot_2024-10-03_at_11.08.36_AM%201.png)
    
    ![Screenshot 2024-10-03 at 11.08.53 AM.png](TATA%20KFS%20and%20Agreement%20Phase%202/Screenshot_2024-10-03_at_11.08.53_AM%201.png)
    
    **Step 6:** customer is redirected back to the page in case of app or closes the window and sees the page below after we receive a callback from TATA.
    
    ![Screenshot 2024-10-03 at 11.09.06 AM.png](TATA%20KFS%20and%20Agreement%20Phase%202/Screenshot_2024-10-03_at_11.09.06_AM%201.png)
    
    **Step 7:** The uploadDocument API is called to upload all documents to the webtop and the customer completes the loan application journey after the above step.
    

**Below is the modified Customer journey which is to be implemented: (Both for fresh and enhancement)**

**KFS template is same across Fresh and Enhancement Loan Application flow**

**—> Step 1**: Customer sees the Pledge page which allows him to pledge the funds after confirming the OTP. Customer has already chosen the funds to be pledged and receives the offer accordingly.

![image.png](TATA%20KFS%20and%20Agreement%20Phase%202/image.png)

**—> Step 2**: Customer sees the Pledging confirmation page which redirects him to the Agreement page

![image.png](TATA%20KFS%20and%20Agreement%20Phase%202/image%201.png)

**—> Step 3:** The customer is at the Agreement step. At this stage the customer sees the link to the KFS hyperlinked in the consent checkbox. Viewing KFS is optional before providing the consent by the user.

- Note: **At this step, the CURRENT_STEP_ID is AGREEMENT_SIGN, frontend should trigger an API to render the KFS in the backend**
- **The validity of KFS should be 5 days from the day of generation. The KFS should not be regenerated if the customer refreshes or comes back to the Agreement step within 5 days. (This might change in the future)**
- **If any variable in the KFS is altered, then a new KFS should be generated.**
- **All details related to KFS should be logged.**

![image.png](TATA%20KFS%20and%20Agreement%20Phase%202/image%202.png)

- Note**: Timestamp and KFS acceptance needs to be stored and logged.**

The CTA should be **Proceed to sign agreement.** 

- **Changes**—> The icon in the CTA next to the text “**Proceed to sign agreement**” should be removed.(for app only not for web app)
- For Web app: See on the screen below

![image.png](TATA%20KFS%20and%20Agreement%20Phase%202/image%203.png)

—> The Customer can click on the Key fact statement hyperlink to view the KFS.

![image.png](TATA%20KFS%20and%20Agreement%20Phase%202/image%204.png)

![image.png](TATA%20KFS%20and%20Agreement%20Phase%202/image%205.png)

If any error occurs while loading the KFS, we will display the page:

On clicking on "**Reload**”, **frontend should again trigger an API to render the KFS in the backend**

![image.png](TATA%20KFS%20and%20Agreement%20Phase%202/image%206.png)

**—> Step 4: Customer now sees the complete KFS and provides a consent to it.**

**—> Step 5: Once the customer completes the KFS acceptance, the customer is directed to the agreement page as below.**

- Note: **The** **logs and timestamp to be stored.**

![image.png](TATA%20KFS%20and%20Agreement%20Phase%202/image%207.png)

After the customer clicks on the ‘Proceed’ button, the customer is directed to the SignDesk page of TATA where the customer completes the signing flow.

- Note: The KFS should be uploaded to webtop along with the Agreement.
- Name of the KFS document uploaded to webtop: **borrower_account_id-KEY_FACT_STATEMENT.pdf**

- **Loan Offer page changes:**
    
    KFS should be removed from this page
    
    ![image.png](TATA%20KFS%20and%20Agreement%20Phase%202/image%208.png)
    

- **UI Changes:**
    
    ![image.png](TATA%20KFS%20and%20Agreement%20Phase%202/image%209.png)
    

## Additional Requirements

1. **Fields required at the KYC Verification—> Additional Information Screen**

Figma design link: [https://www.figma.com/design/OknsxSuPc6UK9TIjuzpCsW/Untitled?node-id=0-1&node-type=canvas&t=c20Ckq9TEWIPzQls-0](https://www.figma.com/design/u5fpymb6jC6ubzT9YUXFgb/Loan-application-flow?node-id=10772-113376&node-type=section&t=X61F0GT3iB7VqX9Y-11)

- Qualification
    - Upto 12
    - Diploma
    - Graduate
    - Post Graduate
- Purpose of loan
    
    The Purpose of loan is currently called End use of loan. We can can rename it for better communication to the users and the dropdown values are listed below:
    
    | **Personal** |  |
    | --- | --- |
    | Wedding |  |
    | Home Renovation/Décor |  |
    | Medical or Hospitalisation expenses |  |
    | Education |  |
    | Holiday/Vacation |  |
- Occupation
    - Student
    - Salaried
    - Self Employed
    - Retired
- Source of income
    
    **New addition**
    
    - Employment
    - Self-Employment
    - Investment
    - Rental
    - Retirement
    - Other (e.g., gifts, inheritances, royalties)
- Income range
    - 3 - 10 lacs
    - 10 - 25 lacs
    - More than 25 lacs

**Note: We are removing the input fields for the Mother’s Name from the UI**

- UI Changes for above:
    
    ![image.png](TATA%20KFS%20and%20Agreement%20Phase%202/image%2010.png)
    

1. KFS Changes:

—> We will scrap the details of KFS which is displayed on the Confirm Pledge Screen before the KFS.

![image.png](TATA%20KFS%20and%20Agreement%20Phase%202/image%2011.png)

---

# **Design**

---

No design changes is required in phase 1. In the subsequent phase, we will modify the KFS UI.

[https://www.figma.com/design/u5fpymb6jC6ubzT9YUXFgb/Loan-application-flow?node-id=10772-113376&node-type=section&t=X61F0GT3iB7VqX9Y-11](https://www.figma.com/design/u5fpymb6jC6ubzT9YUXFgb/Loan-application-flow?node-id=10772-113376&node-type=section&t=X61F0GT3iB7VqX9Y-11)

# **Analytics**

---

Below are the metrics we will review.

- TAT for loading the Agreement
- TAT for generating the Agreement
- Agreement generation success %age
- Agreement acceptance %age
- KFS acceptance %age
- KFS acceptance TAT

# **Timeline/Release Planning**

---

# **Go to market**

## Partner

- [ ]  Get sign-off on the document by TATA

## Ops & Sales training

- [ ]  Inform Sales/MFD/Ops team about the new flow
- [ ]  Inform Sales/MFD/Ops team about the new KFS

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [x]  Get XHMTL designed from Labdhi  - ETA: 30th Sep’ 24.
    - [x]  Get sign-off from TCL - ETA: 30th Sep’ 24.
- [x]  Business
    - [ ]  -
- [x]  Design
    - [ ]  N

---

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

# **Feedback**

---

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes