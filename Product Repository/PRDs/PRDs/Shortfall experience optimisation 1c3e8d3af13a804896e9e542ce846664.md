# Shortfall experience optimisation

: Ranjan kumar Singh
Created time: March 27, 2025 10:54 AM
Status: Not started
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

- Scoping rough
    
    BAJAJ:
    Web: We open the URL in the same tab replacing Volt's URL.
    Android/iOS: We navigate to another screen which is a webview and open the url in the WebView.
    TATA:
    Web: We open the URL in the same tab replacing Volt's URL.
    Android/iOS: We open in inApp browser.
    

# **What problem are we solving?**

- When users experience a shortfall and fail to meet it on time, lenders sell the funds on the 7th day by 12 PM. However, our app UI and communications indicate that users have 7 days to meet the shortfall.

---

# **How do we measure success?**

- Tickets and escalation should reduce related for shortfall sell-off

---

# **How are others solving this problem?**

---

# **What is the solution?**

- We need to ask user to meet short-fall within 6 days instead of 7 days
- Portfolio will be sold-off on 7th day
- Repayment of shortfall has to be done on or before 6th days before 6 PM

## Requirements overview (optional)

**Change on UI:**

- Notification card:
    - Show “Meet shortfall within 6 days instead of 7 days”
    - On 6th day, we need to say “Last reminder: Meet shortfall before 6 PM”
        - This message will be visibile to customer on 6th day from 12:00 AM to 5:59 PM
        - Once 6 PM is passed: We need to inform user that “Shortfall deadline has expired!”
- Shortfall landing page: Please refer design for the changes
- Learn more page:
    - Change: instead of saying meet shortfall within 7 days, We need to say meet shortfall within 6 days [This content is powered by Firebase]
- FAQ [Under “What happens if I fail to meet the shortfall?”]: https://docs.google.com/spreadsheets/d/1aXJxo-F6ru5BDGp-rI2vqaJc2ko0roNDLkMA_9LeVpI/edit?usp=sharing

**Change in communication:** 

[https://docs.google.com/document/d/1rgHi2F9fY4fDY2HgRAeAMNzydLYQuy45ihXk2YfhR-8/edit?usp=sharing](https://docs.google.com/document/d/1rgHi2F9fY4fDY2HgRAeAMNzydLYQuy45ihXk2YfhR-8/edit?usp=sharing)

Logic to calculate “Last date to meet shortfall”

- Last date to meet shortfall has to calculated based on the aging and the current date when Shortfall status is DUE
- Example:
    - If shortfall generated on 20 Mar 25, aging is 1 and status is DUE then last day to meet shortfall date will be: 25th Mar 25
- Fix Shortfall Amount formatting in comms
- When aging is 1, than in the communication we need to send “Today before 5 PM” instead of sending aging as 1
- When aging is 1, than we need to show “Today before 5 PM” Under Meet shortfall within column in shortfall tables.

## User stories / User flow

## Requirements

---

# **Design**

Updated design link: [https://www.figma.com/design/UgxBSWFtQ0uuPULMHy2eWY/Shortfall?node-id=2131-2015&t=S8yuv2tHg8oJ1PoX-4](https://www.figma.com/design/UgxBSWFtQ0uuPULMHy2eWY/Shortfall?node-id=2131-2015&t=S8yuv2tHg8oJ1PoX-4)

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