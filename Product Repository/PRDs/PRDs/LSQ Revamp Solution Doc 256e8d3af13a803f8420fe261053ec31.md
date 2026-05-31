# LSQ Revamp Solution Doc

: Vijay Kumar S
Created time: August 21, 2025 11:15 AM
Status: Not started
Last edited: October 6, 2025 12:50 PM

# **What problem are we solving?**

Currently, both the **MFD activation journey** and the **customer LAMF journey** run through a **single combined flow**, which is leading to multiple challenges:

- Difficult to manage MFDs handling multiple applications/customers
- Limited ability to manage multiple products at the customer level
- Workflow and opportunity overlaps and causing confusion
- Lack of clarity on which opportunity belongs to which journey
- Inadequate visibility into MFD vs. customer progress tracking
- **Phone number as the primary identifier creates a constraint** — if an MFD and a customer share the same number, separate applications cannot be created
- Automation triggers are overlapping, creating conflicts

To address these issues, we need to **structurally separate the MFD and customer journeys (or opportunities)**, ensuring clearer ownership, better tracking, and improved scalability

---

# **What is the solution?**

## We will proceed with using Leads and Opportunities, rather than shifting to the Lead and Account view.

**Scope of the Revamp of LSQ:**

- **Separation of Journeys**
    - Customer journey and MFD (partner) journey handled separately to avoid conflicts.
    - No account-level structure; instead, using **Leads + Opportunities** to manage flows.
- **Opportunities Design**
    - Different opportunity types: **LAMF, LAS, Term Loan, Renewal, Foreclosure, Enhancement, MFD Activation**.
    - Each opportunity type has its own schema and activities, avoiding overlap.
    - Lead fields are being migrated to opportunity fields for better tracking.
- **Activity Handling**
    - All activities bifurcated and linked directly to their respective opportunity (instead of being dumped under the lead).
    - Example: customer loan activities → loan opportunity, MFD onboarding activities → MFD activation opportunity.
- **Multiple Journeys**
    - A person can act as both **Customer and MFD**.
    - Two opportunities:
        - **MFD Activation Opportunity** → once won, MFD is considered active.
        - **Customer Loan Opportunity** → runs in parallel for their own borrowing journey.
- **Phased Execution**
    - **Phase 1:** LAMF opportunity clean-up (removing extra activities like MFD, enhancement, foreclosure, renewal).
    - **Phase 2:** Structuring other opportunities (Enhancement, Renewal, Foreclosure, MFD Activation).
    - **Phase 3:** Migration of automation + reporting on opportunities.

We will be proceeding with the LSQ clean-up initiative (‘Swachh Abhiyan’) to streamline the architecture and ensure that multiple opportunities can be handled in parallel without conflicts.”

Currently we will be having multiple opportunities:

1. LAMF - Loan against mutual Funds
2. LEAMF - Loan enhancement against mutual funds - 
    1. Use cases:
        1. Enhancement of the limit
        2. Margin Pledge
3. MFD to be Activated
4. Renewal
5. Foreclosure
6. LAS - Loan against stocks

**NOTE:** In the revamped architecture, the **MFD Activation Journey will be managed as an Opportunity**. Once the MFD is successfully activated, all subsequent journeys or repeat interactions with the MFD will be handled at the **lead level**, instead of creating new opportunities.

The complete journey and the activity will be passed to the opportunity,

example - lead activity , executive action, sales touch, last activity dates and each action done by the customer will be reflected in the 

the activites are mapped with respect to each opportunity in the file attached : 

The **entire journey and all related activities** will be captured within the **opportunity**.

For example:

- Lead activities
- Executive actions
- Sales touches
- Last activity dates
- Customer actions and responses

Each of these activities will be mapped and reflected against the respective opportunity.
A detailed mapping of activities to opportunities is provided in the attached file: [LSQ Doc for Revamp](https://docs.google.com/spreadsheets/d/1m4hAhJbcqBxqqmNn9YgfwfpIZBZmTo8UM8wP9JMBIXc/edit?usp=sharing)

### Opportunity Journeys – Start & End Points

1. **LAMF Opportunity**
    - **Start (Open):** Customer fetch
    - **End (Closed):** Loan created
2. **MFD Activation Opportunity**
    - **Start (Open):** Unregistered
    - **End (Closed):** Activated
3. **LEAMF Opportunity** *(Prerequisite: LAMF opportunity must be WON)*
    - **Start (Open):** Customer fetch
    - **End (Closed):** Loan enhancement
4. **Renewal Opportunity** *(Prerequisite: Tenure of at least one LAMF opportunity must be completed)*
    - **Start (Open):** Renewal initiated
    - **End (Closed):** Renewal completed
5. **Foreclosure Opportunity** *(Prerequisite: At least one LAMF must be open)*
    - **Start (Open):** Foreclosure initiated
    - **End (Closed):** Foreclosure completed

## Opportunity Journeys

### 1. **LAMF Opportunity**

- **Open:** Portfolio fetch Started
- **In Progress (Customer Activities):**
    - MF Fetched using MFC
    - Offer page
    - KYC verification started
    - Photo verification started
    - Link bank account started
    - Set up Mandate started
    - Portfolio pledge started
    - MF pledged using CAMS
    - MF Pledged using KFIN
    - Sign Agreement Started
    - Credit Approval
- **Closed (Won):** Loan created
- **Closed (Lost):** Offer Page < 10k Closed lost

### 2. **MFD Activation Opportunity**

- **Open:** Unregistered MFD created
- **In Progress:**
    - Registration initiated
    - Empanelled
    - Partially Activated
- **Closed (Won):** MFD Activated
- **Closed (Lost):** MFD is Customer → Move the lead to B2C team if the limit is above 25000

### 3. **LEAMF Opportunity** *(Prerequisite: LAMF opportunity = Won)*

- **Open:** Customer fetch
- **In Progress:**
    - Eligibility check
    - Loan application submitted
    - Verification & approval
- **Closed (Won):** Loan created
- **Closed (Lost):** Loan not sanctioned / dropped

### 4. **Renewal Opportunity** *(Prerequisite: LAMF tenure completed)*

- **Open:** Renewal initiated
- **In Progress:**
    - Initiate
    - Renewal documents submitted
    - Verification & approval
- **Closed (Won):** Renewal completed
- **Closed (Lost):** Renewal not completed / dropped

### 5. **Foreclosure Opportunity** *(Prerequisite: At least one LAMF open)*

- **Open:** Foreclosure initiated
- **In Progress:**
    - Request validated
    - Payment settlement process
    - Closure documentation
- **Closed (Won):** Foreclosure completed
- **Closed (Lost):** Foreclosure request withdrawn

👉 This way, each opportunity has:

- **Start point (Open)**
- **Journey stages (In Progress milestones)**
- **End point (Closed – Won/Lost)**

## **Solutions for Opportunity-Based Revamp**

### 1. Lead & Identity Management

- Lead will only act as the **master identity record** (Phone Number, Role flags: Customer/MFD).
- No journey-related clutter will remain at the Lead level.

### 2. Independent Opportunities

- Each business flow (LAMF, MFD Activation, Renewal, Enhancement, Foreclosure, Term Loan, LAS, etc.) will exist as a **separate opportunity**.
- Opportunities will be **self-contained** and will not depend on or interact with each other.
- Each opportunity will have its own stages, activities, and reporting.

### 3. Activity Routing

- Activities will be filtered and routed **only to the relevant opportunity**.
- This ensures no spillover or confusion across journeys.

### 4. Customer–MFD Opportunity Handling

- **LAMF** and **MFD Activation** are two completely separate opportunities under the same Lead.
- Once the **MFD Activation opportunity** is marked as *Won*, the person is considered an **Activated MFD**.

### Use Cases:

1. **Self Line**
    - The individual takes a loan as a customer (LAMF opportunity) **and** completes the MFD onboarding (MFD Activation opportunity).
    - In this case, **both opportunities are Won**.
2. **Client Referrals**
    - The individual refers external customers.
    - Only the **MFD Activation opportunity** is marked as Won when referral-led journeys are completed.

### Reporting Requirement

- A report is being built in the **Lead tab** (requirement shared with LSQ by Tushar and Vijay).
- This report will display all **referred leads** for each MFD using the fields *Referred By* and *Referred Phone Number*.
- The report will show:
    - How many leads each MFD has referred.
    - The current status of each referred lead.
- As the report contains **hyperlinks**, users can click through to view the respective lead records directly.

### 5. Referral Flow

- MFDs can refer multiple customers.
- Referrals will be maintained at the **Lead-to-Lead level** via a referral table.
- Customer journeys (opportunities) will progress independently of MFD journeys.

### 6. Scalability

- New products or flows (e.g., Term Loan, Loan Against Stocks) can be added as new opportunities without disturbing existing ones.
- The design is modular and extensible.

### 7. Reporting

- **Per Opportunity:** Clean visibility into stages, conversion rates, and TAT.
- **At Lead Level:** A consolidated view of all opportunities linked to the same Lead.
- **MFD Performance:** Referrals, conversions, loan disbursed, activation status.
- **Customer Portfolio:** Multiple loans and products linked independently.

The respective revamp all the below use cases are covered:

1. **The admin action** : which will be used to change the mobile number/ email / partner name / partner platform / platform 
2. The error activity must be shared to the LSQ as this will help the executive to communicate with the customer more effectively
3. MFD activation can be tracked separately 

The Revamp tasks and field and schema and everything will be tracked in this master sheet:
[https://docs.google.com/spreadsheets/d/1JhLRaGeTshJML1TuXzrPYZAUNuVVIVuHeMSn7KYpTEI/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1JhLRaGeTshJML1TuXzrPYZAUNuVVIVuHeMSn7KYpTEI/edit?usp=sharing)

[LAMF Opportunity](LSQ%20Revamp%20Solution%20Doc/LAMF%20Opportunity%20276e8d3af13a807caee0c1044363e09f.md)

[LAMF Enhancement](LSQ%20Revamp%20Solution%20Doc/LAMF%20Enhancement%20276e8d3af13a80ab945cd027758b5bc2.md)

[MFD Activation Journey](LSQ%20Revamp%20Solution%20Doc/MFD%20Activation%20Journey%20276e8d3af13a80e1ac1ec0d488c6a3b8.md)

[Repeat B2B2C](LSQ%20Revamp%20Solution%20Doc/Repeat%20B2B2C%20281e8d3af13a801a999ecb6fb813d725.md)

[Elevate Cases in LSQ- LAMF:](LSQ%20Revamp%20Solution%20Doc/Elevate%20Cases%20in%20LSQ-%20LAMF%20284e8d3af13a806492ffd29d43740556.md)