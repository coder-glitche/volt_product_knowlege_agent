# MFC Summary API integration

: Saksham Srivastava
Created time: May 6, 2024 7:48 AM
Status: In progress
Last edited: May 23, 2024 4:59 PM
Owner: Saksham Srivastava

# **What problem are we solving?**

Currently for the Check eligibility in 15s landing page we use the MFC CAS detailed API, this has the following problems:

1. Detailed API takes longer to give CAS response.
2. Detailed API in alot of cases gives locked units as available units.

Shifting to CAS summary API will solve both of these problems. 

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

## Requirements

BE:

1. For totalFundsSummary: Add all **data.schemes[].currentMktValue**. Keep these segregated basis their **data.schemes[].rtaName**
2. For nonEligibleFundsSummary: 
    1. DEMAT: For all **data.schemes[].isDemat: Y** ,add **data.schemes[].currentMktValue.** Keep these segregated basis their **data.schemes[].rtaName**
    2. UNAPPROVED: For the remaining schemes, check if **data.schemes[].isin** is in the approved list of primary lender. If not add the **data.schemes[].currentMktValue** for such schemes**.** Keep these segregated basis their **data.schemes[].rtaName**
    3. LOCKED(New): For the remaining schemes, check for the difference between **data.schemes[].availableUnits** and **data.schemes[].lienEligibleUnits.** If the difference is non zero, (**data.schemes[].availableUnits - data.schemes[].lienEligibleUnits**)***data.schemes[].nav** is the locked value. Keep these segregated basis their **data.schemes[].rtaName**
3. For eligibleFundsSummary: For all schemes adding **data.schemes[].lienEligibleUnits*****data.schemes[].nav** will give eligibleFundsSummary. Schemes that are non Demat and approved should be considered. 
4. For eligibleCreditLimit: Use **data.schemes[].lienEligibleUnits*data.schemes[].nav*LTV** data from approved list of schemes. 
5. portfolio_asset_data mapping:
    1. free_units column to have lienEligibleUnits data

[d53ea7d3-6f36-4da2-88fa-7c8da88d4a39.csv](MFC%20Summary%20API%20integration/d53ea7d3-6f36-4da2-88fa-7c8da88d4a39.csv)

1. leads_portfolio_data mapping: 

[13479c0e-cf62-4364-bb6c-07d725f5047a.csv](MFC%20Summary%20API%20integration/13479c0e-cf62-4364-bb6c-07d725f5047a.csv)

Mapping analysis: https://docs.google.com/spreadsheets/d/1Ch_g0KMPVwWRh8iNgTEsFLxGOht6ZYizhoG2gE3NEOo/edit?usp=sharing

FE: 

1. Add a new child element in Non eligible Portfolio section called “Locked”. 
2. Add a new info icon in front of “Locked”.
3. Clicking on info icon should open pop up with text:
**Non eligibility reason**
Mutual funds such as locked ELSS funds, retirement funds, children funds and funds that are already lien marked are not eligible for Volt money credit line. 

Update (16th May): Where-ever  we are using **data.schemes[].availableUnits** use **data.schemes[].closingBalance @Parvesh Garg** 

Update (23rd May): Use **data.schemes[].availableUnits is place of data.schemes[].lienEligibleUnits @Parvesh Garg** 

---

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