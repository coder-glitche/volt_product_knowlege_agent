# MFD Channel

: Naman Agarwal
Created time: October 28, 2024 8:05 AM
Status: Not started
Last edited: November 4, 2024 1:23 PM

Volt provides LAMF 

MFD are important

MFD 

- Onboarding
- Activation
- Servicing

Capabilities 

- To Disburse loans
    - In 30mins
    - without documents

# MFD Channel PRD

## Executive Summary

- Product Overview
    - Volt provides loan against mutual fund.
    - 

- Business Objectives
- Stakeholders
    - MFDs
        - 
        
        ### MFD User Persona for Volt Money
        
        At Volt Money, Mutual Fund Distributors (MFDs) play a vital role in connecting clients to our Loan Against Mutual Funds (LAMF) product. These professionals manage their clients' investments and are constantly on the lookout for opportunities to increase their revenue streams, primarily relying on trail commissions from their AUM (Assets Under Management). LAMF allows MFDs to provide liquidity to their clients without the need to redeem their mutual fund units, offering a seamless option to access funds while keeping investments intact. This approach also benefits MFDs by earning them commissions in the process, making it a win-win situation.
        
        ### Why MFDs Choose Volt Money
        
        The reasons MFDs opt for Volt Money go beyond just financial incentives. Sure, we offer competitive interest rates on LAMF products, generally ranging between 10.4% and 10.69%, which attracts both MFDs and their clients. We also give MFDs ₹200 for every account opened, along with an annual 0.5% commission on trades. However, the service we offer makes a big difference too. Each MFD is assigned a dedicated Relationship Manager (RM) to ensure smooth operations and personalized support, something many competitors don’t provide.
        
        ### The MFD Journey at Volt Money
        
        The MFD journey starts with client sign-ups, which we’ve designed to be as frictionless as possible. Clients go through OTP verification followed by PAN validation through Decentro’s API, which doesn’t require a date of birth, making the process smoother for clients. The next step is fetching collateral data, a critical process for securing loans. We retrieve this data from major RTAs like CAMS and KFintech, using the ISIN number to identify available and locked mutual fund units. For added security and ease, we also integrate MF Central to obtain transaction data.
        
        Once collateral is secured, the client is assigned a lender. We work with multiple lenders, such as Tata, which requires a minimum CIBIL score of 650. Our business rule engine ensures that the client is matched with the right lender, though we have had occasional fallback mode issues that we’re actively addressing.
        
        ### Verification and Disbursement Process
        
        The KYC process follows lender assignment, supported by our partnership with Digilocker for fast, secure verification. Depending on the lender, the KYC experience might vary slightly, but our aim is to keep it seamless for both clients and MFDs. Once KYC is completed, the client’s bank account is verified using Digio, after which they can register their mandate. For example, Tata uses Digio, while Bajaj relies on its own system for mandates.
        
        A critical step is lien marking, where the mutual fund units are pledged against the loan. This is managed through the RTAs and verified with the loan ID. Once this is done, we finalize the process with a Key Facts Statement (KFS) and agreements, where Tata prefers Aadhar eSign and Bajaj uses mobile OTP.
        
        ### Challenges MFDs Face
        
        While we strive for a smooth process, there are some hurdles. One major issue MFDs face is errors in fetching collateral from CAMS and KFintech, which affect about 30-40% of clients. This can cause delays and frustration. Similarly, the lien marking process can take longer than expected, sometimes up to three days, and mismatches between PAN and Aadhaar can further slow down the process. We’re continually improving these areas to enhance the overall experience.
        
        ### Supporting the MFDs
        
        We provide dedicated RMs to help MFDs with client onboarding and troubleshooting. Our CRM, LSQ, is used to keep track of everything, although there have been issues with missed calls not being rerouted efficiently when RMs are busy. We’re also improving integrations between our communication systems like Presiscope and Exotel to better manage client interest through calls and WhatsApp.
        
        ### Payouts and Trust Building
        
        Payouts are crucial for MFDs, and while they currently earn ₹200 per account opened and 0.5% on trades, there have been occasional delays related to GST and payout timing. We’re addressing these issues to ensure smoother payouts in the future. Moving forward, our goal is to build trust and improve the MFD experience by making the platform more efficient and responsive.
        
        At Volt Money, our relationship with MFDs is built on shared success—helping their clients access liquidity while preserving their investments. We aim to provide the best tools, services, and support, ensuring a seamless experience for both MFDs and their clients.
        

## Current State Analysis

- System Overview
- Key Metrics
- Existing Workflows
- Pain Points

## Product Requirements
A. Partner Lifecycle Management

- Onboarding
- Engagement
- Performance Tracking
- Support

B. Operations Management

- Loan Processing
- Documentation
- Communication
- Issue Resolution

C. Business Management

- Revenue Tracking
- Payments
- Reporting
- Analytics

## Technical Requirements

- System Architecture
- Integrations
- Security
- Performance

## User Requirements

- MFD Partners
- MFD Saas partners
- Relationship Managers
- Support Team
- Business Team

## Success Metrics

- Business KPIs
- Operational KPIs
- Technical KPIs

## Implementation Plan

- Phase 1: Core Features
- Phase 2: Enhancements
- Phase 3: Advanced Features

## Risk Assessment

- Technical Risks
- Operational Risks
- Business Risks

## Future Roadmap

- Planned Features
- Potential Enhancements
- Market Evolution

## Appendix

- Glossary
- Technical Specs
- Process Flows
- User Stories

MFD 

- Volt direct
- MFD Saas

Sales 

- issues in Product journey

Support 

- list of support issues

Servicing 

- Inbound
- Outbound

Product 

Sales 

What are typical sales issues ?

What are typical Support issues ?

Product issues?

Partner issues ?