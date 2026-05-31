# Credit line Journey Metrics

We have an opportunity for us to improve how we manage and access our API data. Right now, we don’t have formal documentation for the APIs or tables capturing the data logs, which could make it difficult for us to track user behavior effectively or run data-driven experiments.

**Here’s what I think we could achieve with a stronger data process:**

1.	**Empowering Better Decision-Making:**

•	One of the first things I’ve noticed is that our ability to make timely, data-driven decisions is limited by how we handle our data. By formalizing the documentation of our APIs and creating a system of structured tables, we’ll be in a position to quickly identify user patterns, track conversion rates, and pinpoint where users drop off in the flow.

•	I believe this will help us move from reacting to issues to proactively improving the user experience based on solid data.

2.	**Establishing a Data Lake for Efficient Access:**

•	By creating tables from our API logs and building a **data lake**, we can make our data more accessible across teams. This would make it easier to query information, run analysis, and track critical metrics like user progression through the funnel or the success rates of various stages (e.g., KYC, bank verification).

•	I think this would enable faster, more accurate insights and help us optimize the product iteratively, without relying on manual log pulls or guesswork.

3.	**Laying the Foundation for Scalability:**

•	Right now, the absence of formal documentation and structured data is adding some inefficiency to how we operate. By documenting our APIs and creating these data structures, we’ll not only address immediate challenges but also lay a foundation that can scale with us as we grow.

•	This could also prevent future issues where manual data collection slows down our response times or limits our ability to act quickly on insights.

4.	**Creating Transparency Across Teams:**

•	A clear, organized data process would give everyone—product, engineering, and other teams—better visibility into how our product is performing. With standardized documentation and data tables, we can create a culture where data is accessible, and decisions are made with transparency and accountability.

**Suggestions for Next Steps:**

•	We could start by identifying key API logs that need to be structured into tables and documented. This would give us a good foundation for creating a **data lake** that we can all query when needed.

•	I’d be happy to work closely with the engineering team to ensure we’re capturing the right data points, especially those that impact user journeys, conversion rates, and drop-offs.

---

| **Stage** | **Metric** | **Definition of "Number of"** | **Source API** | **Probability Calculation** |
| --- | --- | --- | --- | --- |
| **Login** | Successful logins | Number of users who successfully log in during the day | `/api/client/auth/login` | (Successful Logins / Total Logins) |
|  | Failed logins | Number of users who attempted but failed to log in | `/api/client/auth/login` | N/A |
|  | Conversion to PAN verification | Number of users who move from login to PAN verification stage | Calculated internally | (Users who begin PAN Verification / Successful Logins) |
| **PAN Verification** | PAN submissions | Number of users who submit PAN for verification on that day | `/app/analytics/application` | N/A |
|  | Successful PAN verifications | Number of PAN verifications completed successfully | `/app/analytics/application` | (Successful PAN Verifications / PAN Submissions) |
|  | Failed PAN verifications | Number of users whose PAN verification failed | `/app/analytics/application` | N/A |
| **Fetch Folio** | Folio fetch requests | Number of requests made to fetch mutual fund folios | `/app/borrower/application/asset/fetch/credentials` | N/A |
|  | Successful folio fetches | Number of mutual fund folio details successfully retrieved | `/app/borrower/application/asset/fetch/credentials` | (Successful Folio Fetches / Folio Fetch Requests) |
|  | Failed folio fetches | Number of failed attempts to fetch folio details | `/app/borrower/application/asset/fetch/credentials` | N/A |
| **Eligibility Assessment & Lender Assignment** | Eligibility checks performed | Number of times eligibility is checked for a user | `/app/borrower/application/approval/check/{applicationId}` | N/A |
|  | Successful lender assignments | Number of users successfully assigned a lender | `/app/borrower/application/approval/check/{applicationId}` | (Successful Lender Assignments / Eligibility Checks Performed) |
|  | Failed lender assignments | Number of failed lender assignments | `/app/borrower/application/approval/check/{applicationId}` | N/A |
| **KYC Verification** | KYC checks initiated | Number of KYC verifications initiated | `/app/borrower/application/additionalDetails/{applicationId}` | N/A |
|  | Successful KYC verifications | Number of users who successfully complete KYC |  | (Successful KYC Verifications / KYC Checks Initiated) |
|  | Failed KYC verifications | Number of users who fail KYC verification |  | N/A |
| **Bank Account Verification** | Bank account verification requests | Number of requests made to verify a bank account | `/utils/bank/verification` | N/A |
|  | Successful bank account verifications | Number of successful bank account verifications | `/utils/bank/verification` | (Successful Bank Verifications / Bank Verification Requests) |
|  | Failed bank account verifications | Number of failed bank account verifications | `/utils/bank/verification` | N/A |
| **Mandate Setting** | Mandate requests | Number of requests made to set up a mandate | `/app/borrower/application/mandate/setup` | N/A |
|  | Successful mandate setups | Number of mandates successfully set up | `/app/borrower/application/mandate/setup` | (Successful Mandate Setups / Mandate Requests) |
|  | Failed mandate setups | Number of failed mandate setups | `/app/borrower/application/mandate/setup` | N/A |
| **Asset Pledge** | Pledge requests | Number of requests made to pledge an asset | `/app/borrower/application/asset/pledge/init/otp` | N/A |
|  | Successful pledges | Number of successfully pledged assets | `/app/borrower/application/asset/pledge/init/otp` | (Successful Pledges / Pledge Requests) |
|  | Failed pledges | Number of failed attempts to pledge assets | `/app/borrower/application/asset/pledge/init/otp` | N/A |
| **KFS and Documentation** | KFS document generations | Number of KFS (Key Fact Sheet) documents generated | `/app/borrower/application/agreement/link/{applicationId}` | N/A |
|  | Successful KFS signatures | Number of KFS documents successfully signed by users | `/app/borrower/application/agreement/link/{applicationId}` | (Successful KFS Signatures / KFS Document Generations) |
|  | Failed KFS signatures | Number of failed attempts to sign KFS documents | `/app/borrower/application/agreement/link/{applicationId}` | N/A |
| **Loan Agreement Execution** | Loan agreement generations | Number of loan agreements generated | `/app/borrower/application/agreement/status/{applicationId}` | N/A |
|  | Successful loan agreement signatures | Number of loan agreements successfully signed | `/app/borrower/application/agreement/status/{applicationId}` | (Successful Loan Agreement Signatures / Loan Agreement Generations) |
|  | Failed loan agreement signatures | Number of failed attempts to sign loan agreements | `/app/borrower/application/agreement/status/{applicationId}` | N/A |

---

### **Explanation:**

- The "Number of" in each metric refers to a daily count of occurrences (e.g., successful logins in a day).
- The **Probability** column captures the likelihood that a user moves from one stage to the next by dividing the number of successful completions at a stage by the number of users entering that stage.