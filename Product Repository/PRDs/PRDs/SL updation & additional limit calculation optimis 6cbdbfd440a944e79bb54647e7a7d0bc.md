# SL updation & additional limit calculation optimisation  for renewal, enhancement and margin pledge

: Ameya Aglawe
Created time: July 26, 2024 6:45 PM
Status: On Hold
Last edited: August 27, 2024 5:20 PM

# **What problem are we solving?**

For users who are undergoing line enhancement and loan renewal flow, when we are calculating the additional limit, then we are not considering the increased value of the already pledged portfolio in calculation of SL in front-end

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

## Requirements

We need to add update handling in our front-end for additional limit for including change in the value of already pledged portfolio. 

### Value of already pledged portfolio increased

- While user is going for enhancement, we will also consider the increase in portfolio value of the already pledged portfolio.
- **Current handling (Front-end)**
    - Additional credit limit is calculated based on the new funds which the user has fetched for enhancement
    - When user is checking the increased limit, and gets additional credit limit, then we only allow user to proceed for enhancement only if additional credit limit ≥ 25k
- **Optimised handling (for front-end)**
    - When user is checking the increased limit, we should consider the following in the additional credit limit
        - Additional credit limit due to new funds which the user has fetched for enhancement ***(handled)***
        - Increased DP due to increase in portolio value of the already pledged funds ***(New)***
- **Explanation with example**
    - User does the pledging in the first application on 1-1-2024
        - Portfolio value : Rs 50,000
        - Drawing power Rs 25,000
        - Existing Sanction limit : Rs 22,500
    - The value of pledged funds increased as on 1-6-2024
        - Updated portfolio value : Rs 80,000
        - Updated drawing power : Rs 40,000
        - Sanction limit : Rs 22,500
    - User goes for enhancement on 1-6-2024
        - New funds pledged : Rs 20,000
        - New DP pledged : Rs 10,000
    - Current handling :
        - We won’t allow the pledging of funds with DP worth Rs 10,000 since we don’t allow the user enhancement if additional credit limit less than Rs 25000.
    - Optimised handling :
        - We will check the delta(DP) due to increase in portfolio, which in this case is Rs 40,000 - Rs 25,000 = Rs 15,000
        - Then we will add this with New DP pledged 
        ⇒ Effective DP = Rs 15,000 (delta DP) + Rs 10,000 (new DP pledged) = Rs 25,000
        - Since this effective satisfies the condition (≥25k), the enhancement will be allowed for this application according to optimised handling.
        - New sanction limit should be set as ⇒ 0.45 x (Total portfolio value) = 0.45 x (80,000+20,000) = Rs 45,000

### Essential check for the above cases : Sanction limit is already set higher

- **PV does not change**
    - User does the pledging in the first application on 1-1-2024
        - Portfolio value : Rs 40,000
        - Drawing power : Rs 20,000
        - Existing sanction limit : Rs 50,000 ***(already set higher)***
    - User does enhancement on 1-6-2024
        - Portfolio value : Rs 60,000
        - Drawing power : Rs 30,000
    - Sanction limit = 0.45 x Total portfolio value = 0.45 x 1,00,000 = Rs 45,000
    - Since the new sanction limit is less than existing sanction limit, we should not change the value of sanction limit while doing the enhancement.
- **PV changes**
    - User does the pledging in the first application on 1-1-2024
        - Portfolio value : Rs 40,000
        - Drawing power : Rs 20,000
        - Existing sanction limit : Rs 50,000
    - The value of pledged funds increased as on 1-6-2024
        - Portfolio value : Rs 50,000
        - Drawing power : Rs 25,000
        - Existing sanction limit : Rs 50,000
    - User does enhancement on 1-6-2024
        - Portfolio value : Rs 60,000
        - Drawing power : Rs 30,000
    - Sanction limit = 0.45 x Total portfolio value = 0.45 x 1,10,000 = Rs 49,500
    - Since the new sanction limit is less than existing sanction limit, we should not change the value of sanction limit while doing the enhancement.

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

### When user un-pledges all of their funds

- **Explanation with example**
    - User does the pledging in the first application on 1-1-2024
        - Portfolio value : Rs 50,000
        - Drawing power Rs 25,000
        - Existing Sanction limit : Rs 22,500
    - User un-pledged all their funds on 1-6-2024
        - Portfolio value : Rs 0
        - Drawing power : Rs 0
        - Existing Sanction limit : Rs 22,500
    - User does enhancement
        - Portfolio value : Rs 60,000
        - Drawing power : Rs 30,000
    - Current handling
        - We don’t update the sanction limit if there is enhancement after un-pledging of all funds.
    - Optimised handling
        - Total PV = Rs 60,000 + 0 = Rs 60,000
        - So the sanction limit should be set to = 0.45 x 60,000 = Rs 27000
        - Thus the sanction limit should be updated to Rs 27,000 from Rs 22,500.

### Value of already pledged portfolio decreased

- Like the above case ,while user going for enhancement, there will be case of decrease in portfolio value leading which is not considered in current handling.
- **Explanation with example**
    - User does the pledging in the first application on 1-1-2024
        - Portfolio value : Rs 50,000
        - Drawing power Rs 25,000
        - Sanction limit : Rs 22,500
    - The value of pledged funds decreased as on 1-6-2024
        - Updated portfolio value : Rs 30,000
        - Updated drawing power : Rs 15,000
        - Sanction limit : Rs 22,500
    - User goes for enhancement on 1-6-2024
        - New funds pledged : Rs 60,000
        - New DP pledged : Rs 30,000
    - Current handling
        - Since additional credit limit = Rs 30,000 which is greater than ≥ Rs 25000, so the enhancement will be allowed.
    - Optimised handling
        - We will check the delta(DP) due to increase in portfolio, which in this case is - 10,000
        - Then we will add this with New DP pledged 
        ⇒ Effective DP =-10,000 (delta DP) + 30,000 = Rs 20,000
        - Since the effective DP < Rs 25,000 , the enhancement should not be allowed according to the optimised handling.
        - New sanction limit should be set as ⇒ 0.45 x (total portfolio value) = 0.45 x

Though this case is not handled, but still we should not stop the user to make enhancements just because their already pledged portfolio value decreased such that net additional credit limit get < 25k, because this will necessarily impact a lot of users who want to make enhancement 

**Additional cases for which solution is required :** 

### User’s sanction limit was already set higher

- Portfolio value : Rs 40,000
- Drawing power : Rs 20,000
- Existing sanction limit : Rs 30,000
- In this case the customer should be able to make an enhancement of Rs 10,000, but our front-end does not allow the user to do so.

### Margin shortfall

- User’s shortfall : Rs 5000
- User won’t be able to pledge more funds to cover their shortfall if there’s a margin shortfall less than Rs 25,000