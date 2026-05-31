# Dynamic Contact Us / WhatsApp Configuration for Support Numbers across various touchpoints

: Mohit Pareek
Created time: March 20, 2026 5:13 PM
Status: Not started
Last edited: April 21, 2026 5:20 PM

# **What problem are we solving?**

---

Support contact details (WhatsApp and calling numbers) are currently hardcoded across multiple touchpoints (Website, App, Partner Dashboard, and templates).

- This results in high operational effort, as any change requires updates across multiple systems.
- There is a need to centralize these details into a dynamic configuration, enabling updates from a single place for current and future use.

# **Why Now ?**

---

- We are migrating the customer support WhatsApp number from **X to Y**, which currently requires manual updates across multiple touchpoints
- This exposes the inefficiency of the existing hardcoded setup

This migration serves as a trigger to implement a centralised, dynamic system, enabling seamless updates for future changes.

- Number to be change from : **919611749097** to **918105574747**

# **How do we measure success?**

---

- 100% replacement of hardcoded numbers
- Contact update TAT: **hours/days → < 1 hour**
- Zero inconsistencies across platforms post-update

# **How are others solving this problem?**

---

# **What is the solution?**

---

- Introduce a centralized dynamic configuration for Contact Us / WhatsApp details
- Replace all hardcoded instances with config-driven variables
- Ensure all platforms (Partner’s Dashboard, Customer Website and App) fetch this value dynamically
- Create separate variables for different support numbers, as currently multiple numbers are in use :
    - Volt Customer Support WhatsApp Number [ 919611749097 ]
    - Volt Customer Support Calling Number [ 08071174410 ]
    - Partner’s Support Number WhatsApp Number [ 9611749295 ]
    - Partner’s Support Number Calling Number [ 9611749295 ]

**Note** : 

- Update the Volt Customer Support number from existing WhatsApp Number to New WhatsApp Number
    - Existing WhatsApp Number : 919611749097
    - New / Updated Number : 918105574747
- No changes required for Partner Support number

## Touchpoint Coverage

- All touchpoints have been identified and documented across platforms, including:
    - Partner Dashboard
    - Customer Website
    - Mobile App

### Refer for Touchpoints

## 1. Partner’s Dashboard

1. Contact Us Floating Button in Footer of Partner’s Dashboard [ [Refer Screenshot](https://docs.google.com/document/d/1g0jg62ls2C2xGLeTdcO0dA7eTn82Sm53C4HIqkJqhV8/edit?usp=sharing) ] 
2. On the Top Bar on the Partner’s Dashboard [ [Refer Screenshot](https://docs.google.com/document/d/1g0jg62ls2C2xGLeTdcO0dA7eTn82Sm53C4HIqkJqhV8/edit?tab=t.ev3u4l73l9za) ]

## 2. Customer Website

1. **Benefits Page :**
    1. Chat with us CTA [ [Refer SS](https://docs.google.com/document/d/1g0jg62ls2C2xGLeTdcO0dA7eTn82Sm53C4HIqkJqhV8/edit?tab=t.o5m61hn7qx90) ]
    2. Contact us at the end of Page 
    3. Floating WhatsApp Icon on the Right Side 
2. **FAQ Page :**
    1. Chat with us CTA [ [Refer SS](https://docs.google.com/document/d/1g0jg62ls2C2xGLeTdcO0dA7eTn82Sm53C4HIqkJqhV8/edit?tab=t.o5m61hn7qx90) ]
    2. Contact us at the end of Page 
    3. Floating WhatsApp Icon on the Right Side 
3. **Resource Page** :
    1. Contact us at the end of Page 
    2. Floating WhatsApp Icon on the Right Side 
4. **Partner with us :**
    1. Chat with us CTA [ [Refer SS](https://docs.google.com/document/d/1g0jg62ls2C2xGLeTdcO0dA7eTn82Sm53C4HIqkJqhV8/edit?tab=t.2dx56qexgwzp) ]
    2. Contact Us at the end of the page
    3. Contact Us on Header
    4. Each Header level CTA and Contact us at the end of the page
    5. Floating WhatsApp Icon on the Right Side 
5. **Contact Us Page :** 
    1. WhatsApp Number in UI and when clicked on let’s talk button [ [Refer SS](https://docs.google.com/document/d/1g0jg62ls2C2xGLeTdcO0dA7eTn82Sm53C4HIqkJqhV8/edit?tab=t.q54y6v6u4opt) ]
    2. Call us displayed on UI - 08071174410  [ [Refer SS](https://docs.google.com/document/d/1g0jg62ls2C2xGLeTdcO0dA7eTn82Sm53C4HIqkJqhV8/edit?tab=t.q54y6v6u4opt) ]
6. **About Us :**
    1. Contact us in header
    2. Contact section at the end of the page 

## 3. App

1. Chat with us beside Need help CTA in Header [ in WebApp - [Refer SS](https://docs.google.com/document/d/1g0jg62ls2C2xGLeTdcO0dA7eTn82Sm53C4HIqkJqhV8/edit?tab=t.tsjz9r9rnjoi) ]
2. Need Help ? CTA in app 
3. Under User Profile - Contact Us [ [Refer SS](https://docs.google.com/document/d/1g0jg62ls2C2xGLeTdcO0dA7eTn82Sm53C4HIqkJqhV8/edit?tab=t.cfldo26395c4) ]
4. Contact Us Button - When wrong PAN entered a Popup opens showing PAN entered is not Valid [ [Refer SS](https://docs.google.com/document/d/1g0jg62ls2C2xGLeTdcO0dA7eTn82Sm53C4HIqkJqhV8/edit?tab=t.7h3h945xwg4a) ]
5. Check when Contact Us is triggered - During any failure etc

# **Design**

---

- Not required

# **Analytics**

---

# **Timeline/Release Planning**

**NOTE** : 

1. Ensure development and UAT readiness are completed from all touchpoints
2. Do not make this LIVE yet - Go-live date will be communicated

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