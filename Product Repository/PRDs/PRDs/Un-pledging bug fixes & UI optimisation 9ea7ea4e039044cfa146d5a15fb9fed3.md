# Un-pledging bug fixes & UI optimisation

: Ameya Aglawe
Created time: August 7, 2024 2:46 PM
Status: In progress
Last edited: December 11, 2024 6:31 PM

# **What problem are we solving?**

1. For the users who are making an un-pledging request in our app, when there is auto-adjust of limit according to credit allowance, 
    - Then users are just shown the limit of the fund un-pledged, because of which it is not clear to the user that only partial funds are selected for un-pledging
    - The message “We have accommodated the last fund as per credit allowance” which we show in this case might not be very clear for the user who is un-pledging funds for the first time. They may have questions like -
        - What does credit allowance exactly mean?
        - How does this accommodation work?
    - Post this accommodation, when user looks at the the list of funds, they can’t differentiate the fund for which accommodation is done from all the other funds.
2. Fixing of few bugs 
    1. Front-end 
        1. NaN value visible in fund value 
        2. Fund value showing up to be 0
        3. All units being taken up when just partial fund units are selected for un-pledging **(Backend+Frontend)**
    2. Back-end 
        1. Wrong un-pledging request being passed from our side
        2. All units being taken up when just partial fund units are selected for un-pledging **(Backend+Frontend)**

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

1. Currently we show the user the total limit of funds requested for un-pledging
2. We will show the user total units for un-pledging vs the total limit of funds, so that they get a clear idea of accommodation has been done for which fund. 

## Requirements

1. **For un-clear messaging of un-pledged funds** 
    1. Refer design file 
2. **Front end bug fixes** 
    1. NaN
    
    ![image.png](Un-pledging%20bug%20fixes%20&%20UI%20optimisation/image.png)
    
    b. Limit showing up to be zero 
    
    [VID-20240807-WA0001.mp4](Un-pledging%20bug%20fixes%20&%20UI%20optimisation/VID-20240807-WA0001.mp4)
    
    c. All units being taken up when just partial fund units are selected for un-pledging **(Backend+Frontend) :** More context in Backend bug point (b)
    
    ****
    
3. **Other bug** 
    1.  Un-pledging limit request is more than allowable un-pledging request still the un-pledging request is being passed to the lender from our end. 
        
        ![Screenshot 2024-08-14 at 1.18.58 AM.png](Un-pledging%20bug%20fixes%20&%20UI%20optimisation/Screenshot_2024-08-14_at_1.18.58_AM.png)
        
    2. All funds taken up for un-pledging when only partial funds are being selected by the user for un-pledging. 

![image.png](Un-pledging%20bug%20fixes%20&%20UI%20optimisation/image%201.png)

- Un-pledging of partial unit of funds was raised by the user. But un-pledging request of all of units of this fund (worth Rs 9.22L) was sent from our side to the lender as confirmed with BAJAJ (for more context refer : VTS-5452).
- Arpit had fixed worked on this bug when it was raised, but this requires a more deeper dive for RCA & complete resolution
- Debudding required
    - If user edits the selected fund value, then we don’t allow the user to select any value which is greater than the value selected by user

c. De-bugging needs to be required on why cases with buffer less than 1.05 are being passed from our side? 

**Sheet :** [https://docs.google.com/spreadsheets/d/1hSQYow8x6RA9Q5WQxudIuUnUBgAyrvhR/edit?usp=sharing&ouid=113204369488543186528&rtpof=true&sd=true](https://docs.google.com/spreadsheets/d/1hSQYow8x6RA9Q5WQxudIuUnUBgAyrvhR/edit?usp=sharing&ouid=113204369488543186528&rtpof=true&sd=true)

d. When user selects a fund value of Rs 1, then Limit selected shows up to be 0 (should be 0.5 but it rounds down to 0) & such un-pledge request can be raised from our app as of now. The minimum noted LTV is 30%, thus we minimum fund value the user should be allowed to un-pledge should be Rs 4, so that limit does not round down to 0. 

---

# **Design**

---

1. Please refer to the designs here : https://www.figma.com/design/jYRvz34fgH47FywaqCrm25/Un-pledge-(Vinit)?node-id=33-865&t=7jqUorFO6f4Zc8Xo-1
2. We will show the un-pledging limit as we show now, we’ll just add total limit, in both Limit & Funds Value like ⇒ un-pledge limit (of total fund limit) 
3. Add a small dashboard which shows the user how much limit they can un-pledge 
    1. Should the dashboard update based as and when user selects the funds?
        1. This will be dev demanding 
    2. The dashboard should show the limit for un-pledging or the fund value that can be un-pledged? 
        1. Need to check how do we check in our system? - Based on Limit 
        2. User will want to see based on fund value 
    3. Need to add an “i button” in the dashboard with the copy, here are the variation  :
        1. "The allowable un-pledging limit is calculated by considering a safety buffer above your outstanding dues (including interest and charges) against your credit limit"
            1. Mentioning buffer in copy might raise questions in users’ minds
        2. "The allowable un-pledging limit is calculated by considering your outstanding dues (including interest and charges) against your credit limit”
        3. **"The allowable un-pledging limit is calculated taking into account your credit limit and outstanding dues (including interest and charges)”** 
        4. "The allowable un-pledging limit is calculated based on your credit limit while taking into account your outstanding dues (including interest and charges)” 
        5. Copy for OTP limit : 
            1. OTP Attempts Exceeded

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

1. Logic & calucaltion 
    1. TATA
    2. BAJAJ (5% buffer) 
        1. If outstanding already greater than the buffer than we show the warning to the user 
2. Handling for edge 
3. Is it working fine? Any issue with it? Discuss with Nishant 
4. The 2 bugs 
5. Is flooring necessary?
6. Note : Issue with updation of credit asset mapping table. 
7. Next step : 
    1. Kick off for bug fixes 
    2. UI part is pending and get the designs ready by sharing the problem statement with designer. 

**Un-pledging reasons :** 

1. Complete un-pledging 
    1. Urgency for more funds : There requirement of complete funds (we just give the loan of 45% value of pledged funds) 
        1. Holdings : 10L 
            1. Equity : 45%
            2. Debt : Upto 90% (we can nudge) 
    2. In cases where there is delay in disbursals (due to technical issues at lender or our end) customer un-pledges due to bad experience 
        1. Call 
2. Partial un-pledging : 
    1. MFD : Switch to different fund, change in fund plan
    2. B2C channel : 
        1. Partial un-pledging : Customer un-pledges partially as & when they are clearing the outstanding 
            1. In these cases customers urgent requirement of funds have been fulfilled, and they don’t have any further requirement of loan thus they keep un-pledging funds as and when they are clearing POS. 

- Copy variations
    - Max un-pledgeable fund value reached. Fund value adjusted based on available limit and dues.
    - Max un-pledgeable fund value reached. Fund value adjusted based on available credit limit
    - Max un-pledgeable fund value reached. Fund value adjusted based on available credit limit and dues
    - Max un-pledgeable fund value reached. The fund value adjusted based on available credit limit and dues

- Open points
    - Fund value : Green → Black
    - Might be a technical challenge of showing the box in the each fund container