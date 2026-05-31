# Enhancement to MFD partner Signup page

: Naman Agarwal
Created time: May 8, 2025 4:03 PM
Status: Pending Review
Last edited: May 8, 2025 4:19 PM

**Product Updates** 

## **1. Enhanced Partner Login Experience:**

- **Feature:** Mobile Number Pre-fill & Browser Autofill Support.
- **Problem:** Returning partners re-enter mobile numbers, causing friction.
- **Goal:** Faster, more convenient login.
- **Solution:**
    - **Custom Pre-fill:** Store last successfully used/OTP-requested mobile number in browser local storage for automatic pre-population. (Editable by partner).
    - **Browser Autofill Hint:** Add autocomplete="tel" to the mobile number field to allow browsers (like Chrome) to suggest saved phone numbers.
- **Benefit:** Quicker login, reduced errors, improved partner experience.

## **2. Improved Partner Empanelment Form:**

- **Feature:** Browser Autofill for Empanelment Details.
- **Problem:** Manual entry of common details (name, email, city, company) is time-consuming.
- **Goal:** Faster and more accurate empanelment.
- **Solution:** Implement standard HTML autocomplete attributes (e.g., name, email, address-level2, organization) on relevant input fields.
- **Benefit:** Quicker form completion, fewer typing errors, smoother empanelment.

## **3. Branding & Content Updates:**

- **Logo Update:** Replaced Bajaj Finserv logo with DSP logo in "Our trusted partners" section.
- **Partner Count Update:** Updated "2000+ Partners have joined Volt Money" to "3000+ Partners have joined Volt Money".
- **Benefit:** Reflects current partnerships and growth accurately.