# [Fenix] Lodgement maker bulk approval

: Vaibhav Arora
Created time: February 18, 2025 6:57 AM
Status: Done
Last edited: January 16, 2026 7:47 PM

# **What problem are we solving?**

We operate with two RTAs, CAMS and KFIN, while CAMS currently offers synchronous lien marking of funds (will soon move to asynchronous pledging), KFIN’s lien marking process is asynchronous.

That is upon submitting a lien marking request, we get a request successfully accepted status, post which we poll for a confirmation of lien marking with KFIN using lien status API to get a confirmation. 

Following requirements and discussions will be specific (as per current implementation) to KFIN pledging but would be designed in a way to support both CAMS and KFIN asynchronous pledging so that it is easier for us to extend the same implementation to CAMS when they move to async pledging.

There are 4 possible statuses of a lien marking request by KFIN:

1. LM success (Terminal)
2. LM failed (Terminal)
3. LM on hold (Non terminal that is can move to LM success or failed)
4. LM pending (Non terminal that is can move to LM success or failed)

In the current implementation, once a lien marking request is submitted to KFIN, and if get a non terminal status (LM pending) when validating the lien transaction (using lien status API) we poll it for 30 minutes in the workflow. If the same request is not processed within 30 minutes the non terminal transactions are rejected in the workflow and the request is processed for lodgement.

The lodgement request then passes through our BRE logic to decide if it will go under a straight through processing or manual approval via the operations team.

Due to this handling, few non terminal pledge requests have moved to LM success and are pending for lodgement as we prioritise this feature (200+ transactions).

<aside>
⚠️

**Note**: This is transaction verification and not unit verification which happens as a subsequent step using the RTA portfolio APIs

</aside>

Following are problems that arise due to this problem statement:

- Lack of visibility to LSP and end customer (Customers expect a certain DP post their application is submitted by the LSP)
- DSP operations team are not able to process such requests at the moment and resort to reaching the tech ops team for manually pledging these securities into the loan account
- Since these transactions are processed manually and pass through multiple stakeholders across teams, a lot of risk for double lodgement/incorrect lodgement are introduced which can have direct financial implication for the NBFC

---

# **How do we measure success?**

- Number of securities pledged against the NBFC but not lodged against a credit line
- TAT of lodgement securities (pledging to lodgement)
- Ticket resolution TAT for pending lodgements (TAT from raising the ticket to ticket resolution)

---

# **How are others solving this problem?**

- Volt supports pending lodgements with LSP (Raises to lenders which then post confirmation (manual verification via BFL/TCL) are lodged into the loan account of the user

---

# **What is the solution?**

We will be building a bulk lodgement maker which will enable DSP operations team to manually lodge securities into a loan account of users which were previously rejected / or were failed to be raised for lodgement by the NBFC.

(Customers can directly reach DSP Finance support team for lodgements if their requests are not supported by the LSP)

While we give this functionality to the operations team, it is of utmost important to build validations both via operations (maker/checker) and system (validations) to ensure there are no invalid lodgements into the loan account of the user.

If a lodgement is incorrectly lodged into the loan account of the user, it will expose the NBFC to open financial risk, where the user can withdraw more than they could have causing LTV breaches and even scenarios where even after invocation of the actually pledged securities, the NBFC is not able to recover the complete outstanding amount

## Requirements overview (optional)

- Bulk (file based) maker task for the operations team to raise lodgement requests for multiple loan accounts at a time
- Bulk (file based) checker task for validation of the bulk lodgement file by the operations team (Manual verification of the initially lodged file)
- Handling of bulk file as independent lodgement requests at a loan account level (For launch all bulk file based lodgement requests will be non STP that is independent checker tasks at a loan account level will be created for the operations team to verify individual lodgements from the bulk file)
- Referencing and analytics of bulk files uploaded by the operations team (Will be visible to the checker agent while approving independent loan account level lodgements
- Validations (Regex based) in the maker and checker bulk based file task)
- Independent request level checks (use existing workflow validations) for each request
    - Dedupe check
    - Portfolio validation
    - Lien status validation
    - Sanity checks (Loan account is active / valid / not frozen / ISIN is in approved list)

## User stories / User flow

## Requirements

Bulk file based maker:

- Operations agent will be able to upload a bulk lodgement file on the command centre in the NBFC operations section (NBFC operations section will be renamed to ops and mandate presentation section will be moved to an independent section in the side navigation panel) - @Karuna Sankolli
- File will have the following parameters (Each row will describe one ISIN + Folio + Lien ref combination:
    - FXLAN: Loan account in which the security has to be lodged (mapped)
    - PAN: PAN number of the user whose securities are being lodged into the loan account
    - ISIN: Unique security identification number of the mutual fund that has to be lodged
    - Folio Number: Unique Folio of the user whose mutual fund has to be lodged into the loan account
    - Lien reference number (CAMS) / KFIN reference number (KFIN): Unique transaction reference ID (Available with LSP when a lien marking transaction is initiated for the user)
    - Units: Number of units that were pledged in the name of the NBFC and now have to be lodged against the loan account
- The file will then go through basic sanity checks:
    - Regex check on FXLAN
    - Regex check on PAN
    - Regex check on ISIN
- Post sanity checks a response file will be created where the operations agent will be able to check valid requests raised by them in the file (to begin with we will limit the bulk operation to 100 items)
- Response file can then be validated and verified by the ops agent and the maker request can be submitted for checker approval
- Corresponding checker approval task will be created in the operations section (Maker who created the task will not be able to approve the corresponding checker, only a different checker can approve the file)
- Checker will be able to see the post regex validated file (rows accepted for processing) and will be able to approve or reject the file, checker will see the following parameters in the request details section
    - Request created on
    - Number of securities for lodgement
    - Request created by (Maker)
    - (Attached file - post regex processing)
- Once approved, the file will then be processed into individual lodgement requests, the requests may fail initial validations and not reach the following checker approval of a lodgement request workflow (BE will batch lodgement requests at a loan level)
- Reference of the file name and the task ID (of the maker of bulk file processing) should be stored against each lodgement request so that the analytics team can build the corresponding analytics on top of it
- Checker task for the lodgement requests will be modified (additional parameters will be added) so that the operations team can get why the individual lodgement went into the approval flow and the file was uploaded by whom
    
    

---

# **Design**

[https://www.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS%3A-Command-center?node-id=576-6955&t=GdEt4WEnlYxPwmFn-4](https://www.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS%3A-Command-center?node-id=576-6955&t=GdEt4WEnlYxPwmFn-4)

---

# **Analytics**

- File based analytics (Each lodgement request will have a reference to the task) Operations team should be able to track the following file based metrics:
    - Number of lodgement requests in file
    - Status level distribution (lodgement) for each task/file uploaded
        - Number of lodgements accepted
        - Number of lodgements rejected
        - Number of lodgements failed (before checker creation)
        - Number of lodgements successfully lodged
- Number of files processed
- TAT to process a file (maker submitted to checker approved)
- TAT for individual lodgements (Started on and completed on)

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