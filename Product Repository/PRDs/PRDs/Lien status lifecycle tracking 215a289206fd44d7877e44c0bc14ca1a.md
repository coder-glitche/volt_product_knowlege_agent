# Lien status lifecycle tracking

: Vaibhav Arora
Created time: March 5, 2024 3:18 PM
Status: In progress
Last edited: March 23, 2025 9:16 PM

# **What problem are we solving?**

- Users keep seeing the notification on dashboard till it is not removed via admin action.
    - Once a request was raised manually to the lenders, and the selected folio is unlodged from the account, there is little to no visibility to volt on the status of unpledging.
    - Since this is shown to the user when they login, it creates an urgency in the user’s mind regarding their pending request.
- Users are not communicated the steps and the involved stakeholders to complete their unpledge request.
    - This makes the user think that Volt is responsible for the end to end process and the delay is being caused by Volt.
    - Users do not see progress/movement in their request and feel blindsided for their requests.

Context: Users after raising an unpledge request are shown a notification on their dashboard describing their request to be in process and it would take 3-4 days to complete

![Untitled](Lien%20status%20lifecycle%20tracking/Untitled.png)

![Untitled](Lien%20status%20lifecycle%20tracking/Untitled%201.png)

---

# **How do we measure success?**

Number of requests raised for updates on unlien request/total unlien request raised by the customers

- Sources:
    - Wati
    - Zendesk

---

# **How are others solving this problem?**

Communicating external dependencies via UI:

![Untitled](Lien%20status%20lifecycle%20tracking/Untitled%202.png)

![Untitled](Lien%20status%20lifecycle%20tracking/Untitled%203.png)

![Untitled](Lien%20status%20lifecycle%20tracking/Untitled%204.png)

![Untitled](Lien%20status%20lifecycle%20tracking/Untitled%205.png)

---

![Untitled](Lien%20status%20lifecycle%20tracking/Untitled%206.png)

![Untitled](Lien%20status%20lifecycle%20tracking/Untitled%207.png)

Other players communicating external dependencies via UI to communicate the steps involved to the customer and handle queries via product

# **What is the solution?**

<aside>
⚠️ Users keep seeing the notification on dashboard till it is not removed via admin action.

</aside>

We will change the discovery of pending unpledge request from dashboard to pledged portfolio discussion to make it less apparent and more contextual for the user.

- Only users who want to track their pledged portfolio would discover the notification and can act on it accordingly.
- User will be able to close their unpledge request once all necessary steps are made and communicated to the user.

<aside>
⚠️ Users are not communicated the steps and the involved stakeholders to complete their unpledge request.

</aside>

We will communicate the involved steps and stakeholders in the unpledge journey and show active states of the user’s request in the track pledge request screen to handle user queries UI and effectively communicate ETAs.

- User will receive communication on the successful unlodgement and notification to RTAs on the unpledging of their respective portfolio

## Requirements overview (optional)

States shown to the user:

- Request raised - initial state
- Request approved - Unlodgement (Poll holding statement)
- RTAs notified to remove pledge - Automatically when unlodgement is done.

## User stories / User flow

![Screenshot 2024-03-08 at 3.54.43 PM.png](Lien%20status%20lifecycle%20tracking/Screenshot_2024-03-08_at_3.54.43_PM.png)

## Requirements

### Request status handling

Request Status:

User should be able to track all requests via the request tracking screen → Unpledge request notification

- Request submitted (Initial default state)
- Request approved (Credit limit reduced/Unlodgement done - Holding Statement updated)
- Notification sent to RTAs

### UI and cases that need to be handled

- New screen addition describing steps of unpledging before user selects portfolio
- Movement of notification from top of dashboard to manage limit under pledged portfolio section
- Track status request (interface for users to track all existing and completed request) - BE change required
- Design change on track unpledge request screen
    - Addition of steppers (backend linked - status handling from backend)
    - Directly send user to the status screen showing portfolios requested to be unpledged.

### Backend status handling

- Once a request for unpledge is raised poll account holding statement to identify when designated portfolios are removed (polling every hour)
- Update status of request when credit limit changes - Poll sanctioned limit (Frontend will show status accordingly).

### Reporting and analytics

- Admin action to close unpledge request (change on UI) manually coordinated with Volt and lender (BFL and Tata)
- Recording of following values to enable data tracking and impact measurement:
    - Unpledge request raised at (timestamp)
    - Holding statement validated at (When holding statement is updated as per the requested unpledge of the user) - Polled daily at EOD
        - Identification via number of units, and ISIN of the respective folio

### User comms

---

# **Design**

[https://www.figma.com/design/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?node-id=7968-107763&t=77QQVIv6Zpn6YG0P-4](https://www.figma.com/design/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?node-id=7968-107763&t=77QQVIv6Zpn6YG0P-4)

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