# PhonePe Landing page requirement - 15th April

: Saksham Srivastava
Created time: April 15, 2024 5:31 PM
Status: Not started
Last edited: September 17, 2024 12:13 PM
Owner: Saksham Srivastava

# **What problem are we solving?**

1. **What is LAMF?** - Not a personal loan
2. Filter junk leads
3. Education about LAMF
4. **Product features- ROI, No FC, 3 hour disbursement**
5. **Use cases of this loan**
6. **Trust- TATA & Bajaj as lending partners**
7. **Steps to take loan**
8. Testimonials

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

1. PhonePe users should see the landing page when they click on “Mutual Funds loan” entry point on PhonePe.
2. Users should be able to do MFC fetch from the landing page.
3. Post successful MFC fetch user can click to go in the app jouney.
4. When user clicks on Check eligibility CTA any where on the page it should scroll user to the form.
5. User should not:
    1. See the download app pill in header
    2. See hamburger menu in header
    3. be able to click links such as CAMS, KFin, Volt logo (header) etc
    4. See landing page footer. 
6. When user clicks on T&C and Privacy Policy
    1. User should view the pages in webview
    2. They should be able to comeback to the main landing page. (Design to be given)
    3. User should still be attributed to PhonePe through out. UTM and platform should be present in these links as well. 
    4. The handling should be similar to current handling on Mobile input form for PhonePe. 
7. Users are currently shown USP carousel, that should not be shown post implementing the landing page. 

## Other Requirements

- The padding between FAQ and Volt in press section is off fix that for current MFC landing page and PhonePe requirement.
- Support contact handling should be taken care of.
- When user drops off from app.voltmoney, user should come back to that step of the journey
- Make the page Non-SEO indexable.

## Links to create and get whitelisted from PhonePe:

1. Static link: This link we will configure to control redirection of user when user clicks on “Mutual fund loan” entry point on PhonePe.
    1. Current redirection: [https://app.voltmoney.in/partnerPlatform?platform=PHONEPE&utm_source=Phonepe](https://app.voltmoney.in/partnerPlatform?platform=PHONEPE&utm_source=Phonepe)
    2. Post landing page development:
2. Landing page: 
    
    [https://voltmoney.in/check-loan-eligibility-against-mutual-funds-partner/Platform?platform=PHONEPE&utm_source=Phonepe](https://voltmoney.in/check-loan-eligibility-against-mutual-funds-partner/Platform?platform=PHONEPE&utm_source=Phonepe)
    

1. Static link:

[https://voltmoney.in/partner-redirect?platform=PHONEPE&utm_source=Phonepe](https://voltmoney.in/partner-redirect?platform=PHONEPE&utm_source=Phonepe)

[https://staging.voltmoney.in/partner-redirect?platform=PHONEPE&utm_source=Phonepe](https://voltmoney.in/partner-redirect?platform=PHONEPE&utm_source=Phonepe)

---

# **Design**

[https://www.figma.com/file/4Jw8te9DVzKQbb6GovyCK2/Wireframes?type=design&node-id=102-299&mode=design&t=cR174i17UsWSQLtW-11](https://www.figma.com/file/4Jw8te9DVzKQbb6GovyCK2/Wireframes?type=design&node-id=102-299&mode=design&t=cR174i17UsWSQLtW-11)

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

Questions

- Trust building- Can we add Tata & Bajaj to the landing page?

## Meeting notes

**What is Loan against Mutual Funds?**

![Untitled](PhonePe%20Landing%20page%20requirement%20-%2015th%20April/Untitled.png)

**What is LAMF? (Copy)**
It's a type of loan where you pledge your mutual funds as a collateral to get cash quickly & conveniently, often at lower interest rates compared to traditional loans.

**How it Works?** 

![WhatsApp Image 2024-04-16 at 11.03.39.jpeg](PhonePe%20Landing%20page%20requirement%20-%2015th%20April/WhatsApp_Image_2024-04-16_at_11.03.39.jpeg)

**COPY**

**VOLT BENEFITS**

![WhatsApp Image 2024-04-16 at 11.08.59.jpeg](PhonePe%20Landing%20page%20requirement%20-%2015th%20April/WhatsApp_Image_2024-04-16_at_11.08.59.jpeg)

**Benefits section copy**

- **Very low interest rate of just 10.49% (reducing)**
*(Same sub-header)*
- **Zero pre-payment fees**
Option - 1- Become debt free early at your own terms
Option- 2 - Pay Off Your Loan Whenever You Want
- **Withdraw flexibly**
(Same content as existing)
- **100% Digital process**
Receive cash directly into your account from the comfort of your home, no branch visit required.
- Kickoff call 17th April 2024
    - Non SEO indexable, title and everything
    - lead_token validity
    - Current step context, when user comes back.
    - Design for T&C and Privacy policy changes.