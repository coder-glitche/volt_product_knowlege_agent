# [B2B2C] Fixed deposits via partner dashboard

: Ameya Aglawe
Created time: December 23, 2025 12:38 PM
Status: Pending Review
Last edited: January 8, 2026 4:23 PM

# **What problem are we solving?**

---

- Volt is looking to improve partner engagement by helping partners monetise their existing clients better and sell multiple financial products through one platform. Adding Fixed Deposits (FDs) as a product offering allows partners to offer a popular, high-value product along with loans.
- The objective of this initiative is to integrate FD booking and servicing into the existing Volt Partner Dashboard, leveraging Fixxera for the booking journey while providing partners with a unified interface to initiate, track, and manage FD applications.

# **How do we measure success?**

---

- # of partner of landing on the FD landing page weekly
- # of partner initiating FD booking for their clients
- # of partners completing FD booking for their clients
- Average number of FD bookings per partner
- 0 touch application FD application completion rate

# **How are others solving this problem?**

---

To understand how fixed deposit (FD) journeys are being handled in the market, we evaluated both **MFD-facing platforms** and **B2C consumer platforms**.

### **MFD Software Platforms**

- These platforms focus on enabling advisors to manage FD discovery, booking, and servicing for their customers, following are the takeaways -
    - These platforms have a dedicated page for FD discovery and offers, while the placing of the FD module and the offer presentation varies from platform from platform
    - Platforms like AssetPlus have a direct API integration with the FD issuers while Redvision, Prudent have done API integration with Fixxera

![Prudent](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/Screenshot_2025-12-25_at_1.26.35_PM.png)

Prudent

![Prudent](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/Screenshot_2025-12-25_at_1.27.23_PM.png)

Prudent

![Redvision](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/Screenshot_2025-12-25_at_1.28.01_PM.png)

Redvision

![Redvision](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/Screenshot_2025-12-25_at_1.29.02_PM.png)

Redvision

![AssetPlus](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/Screenshot_2025-12-25_at_1.32.38_PM.png)

AssetPlus

![AssetPlus](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/Screenshot_2025-12-25_at_1.33.45_PM.png)

AssetPlus

![AssetPlus](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/Screenshot_2025-12-25_at_1.34.13_PM.png)

AssetPlus

### **B2C Platforms**

These platforms offer a direct-to-consumer FD booking experience with simplified flows and minimal advisor involvement 

- **Stable Money**

![FD landing with sections](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0345.png)

FD landing with sections

![Interest & Tenure](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0348.png)

Interest & Tenure

![FD offers](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0346.png)

FD offers

![Issuers list](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0351.png)

Issuers list

![Issuer FD page](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0347.png)

Issuer FD page

![IMG_0349.png](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0349.png)

![IMG_0353.png](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0353.png)

![All offers](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0354.png)

All offers

![IMG_0352.png](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0352.png)

![FAQs](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0355.png)

FAQs

- **Moneyview**

![Landing page](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0358.png)

Landing page

![FAQ](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0361.png)

FAQ

![FD offers](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0359.png)

FD offers

![Issuer](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0362.png)

Issuer

![Moneyview value prop](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0360.png)

Moneyview value prop

![FD growth](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0363.png)

FD growth

![Issuer FD prop ](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0364.png)

Issuer FD prop 

![FAQ ](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0365.png)

FAQ 

![FAQ](%5BB2B2C%5D%20Fixed%20deposits%20via%20partner%20dashboard/IMG_0366.png)

FAQ

# **What is the solution?**

## Requirements overview

**1. Partner–Customer–Product Dedupe Logic**

- A single customer can avail multiple financial products from the same or different partners at any point in time.
- For Fixed Deposits specifically, a customer can book multiple FDs with the same partner or across multiple partners, requiring product-level (FD-level) deduplication instead of partner-level dedupe.

**2. FD Discovery within Partner Dashboard**

- A dedicated FD landing page within the Volt Partner Dashboard enables clear discovery of FD offers.
- This separates FD discovery from other product journeys and avoids confusion with existing loan or investment flows.

**3. Structured Entry Points for Actions**

- Clear and distinct entry points are defined for:
    - FD booking
    - FD servicing actions (e.g., status checks, withdrawals, updates)
- This ensures partners can quickly navigate to the relevant stage of the FD lifecycle.

**4. Status Tracking & Updates**

- FD application and lifecycle status is tracked via Fixxera webhooks.
- Webhook-based updates ensure near real-time visibility of FD states within the partner dashboard.

**5. Communications**

- System-driven communications are triggered at key milestones in the FD lifecycle.
- Communications are aligned with booking, confirmation, and servicing events to ensure clarity for both partners and customers.

## User stories / User flow

- **FD discovery & booking**
    - Partner logged in the partner dashboard
    - Partner tap on the FD module
    - Partner explore FD different offers
    - Partner taps on book FD
    - Partner selects FD
    - Partner select/registers customers
    - Partner initiates the FD booking & receives journey link (which is shareable with the customer)
    - Partner completes the FD booking
- **FD bookings tracking & servicing**
    - Partner logged in the partner dashboard
    - Partner tap on the FD module
    - Taps on pending booking tab
        - List of pending FD bookings
            - Details in the section
                - Customer name
                - Customer phone
                - Status
                - Investment amount
                - ROI
                - Tenure
                - Actions - Complete application
    - Taps on Booked FD sections
        - List of pending FD bookings
            - Details in the section
                - Customer name
                - Customer phone
                - Status
                - Investment amount
                - ROI
                - Tenure
                - Actions
                    - View/update details(Attempts the servicing actions)

## Requirements

---

## FD Journey Overview

### 1. User Experience

### a. FD Discovery

- **Promotional Banners**
    - Why FD with Volt
    - Multiple partner issuers
    - Best available ROI highlights
    - 5 easy steps
- **FD Schemes**
    - Schemes are organised into intuitive sections for easier discovery:
        - Tax Saver FDs
        - High ROI FDs
        - Tenure-based FDs
        - Minimum investment-based FDs
- **Explore FDs**
    - Consolidated list of available FD schemes
    - Each scheme leads to a dedicated **FD Details Page** with key attributes and benefits
- **FAQs**
    - Common questions around FD booking, eligibility, payouts, and servicing

### b. FD Booking States

- **Pending FD Bookings**
    - Displays FDs where the booking journey is in progress
    - Allows users to resume from the last completed step
- **Completed FD Bookings**
    - Displays successfully booked FDs
    - Acts as the entry point for post-booking servicing and tracking

---

### 2. Backend Capabilities

### a. FD Booking Entity

Each FD booking is tracked at an individual FD level with the following attributes:

- **Identifiers**
    - FD Booking ID
    - Agent Code
- **Customer Details**
    - Customer Name
    - Customer Phone Number
- **FD details**
    - Issuer
    - ROI
    - Tenure
    - Investment Amount
    - Payout Type
    - Renewal Status
- **FD Type**
    - Women FD (true / false)
    - Senior Citizen FD (true / false)
    - Tax Saver FD (true / false)
- **Journey Tracking**
    - Current Step ID
        - FD Details
        - PAN Verification
        - Email & Personal Details
        - Aadhaar Verification
        - Review & Pay
        - Video KYC
    - Journey Link (deep link to resume booking)
- **Post-Booking Status**
    - Holding status
    - Transaction ID

---

### b. FD Servicing Entity

For completed bookings, the system maintains servicing-related data:

- Holding Status
- Transaction ID
- Portfolio Link (for viewing FD details and servicing actions)

---

### 3. Integrations & Webhooks (Fixxera)

- Volt will consume **Fixxera webhooks** to:
    - Track the current step of the FD booking journey
    - Identify completion or failure of the FD booking flow
- Webhook payloads will be used as the source of truth for:
    - Step progression updates
    - Booking completion status
    - Transition from booking to servicing state
- The webhook structure and fields will align with the [**Fixxera API documentation**](https://fixed-api-integration.readme.io/reference/get_login) for FD journey [events](https://fixerra-my.sharepoint.com/:x:/g/personal/archita_fixerra_in/IQD_f-4RDYOASIjKBf2jzDJiAfeovBDSh4qpFxtGxO1l75I?rtime=KoxUf9FD3kg).

---

### 4. Communications

- Trigger points
    - FD booking initiation (after customer registration/selection)
    - FD booking VKYC step
    - FD booking review & pay step
    - FD booked successfully
    - FD matured/renewed

# **Design**

---

# **Analytics**

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  -
- [ ]  Business
    - [ ]  -
- [ ]  Design
    - [ ]  -

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