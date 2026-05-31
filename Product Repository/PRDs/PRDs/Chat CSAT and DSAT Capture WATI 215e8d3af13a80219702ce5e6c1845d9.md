# Chat CSAT and DSAT Capture <> WATI

: Vijay Kumar S
Created time: June 17, 2025 10:09 AM
Status: Not started
Last edited: June 24, 2025 5:00 PM

## 🧩 **Objective**

To capture structured customer satisfaction (CSAT) and dissatisfaction (DSAT) data via a chatbot workflow that can be automatically stored, tagged, and actioned via escalation or closure, based on customer responses.

---

## 📌 **Platform**

**Tool Used:** **WATI**

WATI is used to automate and manage the chatbot-based feedback collection journey on WhatsApp.

---

## 🧭 **User Journey Overview**

1. Agents initiates feedback collection chatbot after service interaction.
2. Customer gives a feedback rating (1 to 3 scale).
3. Depending on the rating:
    - DSAT (Not Satisfied1 or 2): Capture reason and offer callback.
    - CSAT (Satisfied)3): Thank the customer and end.
4. Store all responses in a Google Sheet and update chat status.

---

## 🤖 ⏳Wati CSAT Automation **Flow :**

---

![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image.png)

Updated Flow:

![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%201.png)

Old Flow:

## Customer experience in the CSAT Automation flow:

![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%202.png)

![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%203.png)

**Bot Auto closing the chat and ending the chatbot flow once the chatbot flow is completed by customer:**

![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%204.png)

Updated Journey:

![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%205.png)

![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%206.png)

## 🔧 **Flow Components**

### 1. **Initiation**

- **Step:** Send Message
- **Message:**
Hi {{name}},
Can you please share with us your valuable feedback?

Instead, it should be this

*Hey!, How was your experience with us today?*

*A) Satisfied*

*B) It was okay/Average*

*C) Not Satisfied*

---

### 2. **Tagging & Storage**

- **Set Tags:** Mark feedback process started (e.g., `feedback_triggered`)
- **Google Spreadsheet:** Record initial engagement
    - This tag is used to record the agent bot initiation time and also this can be used as the tat for resolving the ticket even if the customer do not fill the feedback options

---

### 3. **Feedback Rating**

- **Step:** Button Input
- **Message:**
Please rate us from 1 to 3
    - 1 (Not Satisfied)
    - 2 (Satisfied)
    - 3 (Very Satisfied)

---

### 4. **DSAT Handling (Rating 1 or 2)**

- **Step:** Button Input
- **Message:**
We are sorry your experience wasn't great.
Could you help us improve by sharing what went wrong?
    - Yes, Please Call Me
    - Just Share Feedback
- **Step:** Button Input (Detailed Issue)
Can you help us understand what went wrong?
    - Delay in Service
    - Poor Support
    - App/Portal Issues
- **Storage:** Log issue category and callback preference to Google Sheet
- **Tagging:** e.g., `CSAT`, `Feedback`, or `issue_logged`

---

### 5. **CSAT Handling (Rating 3)**

- **Step:** Direct conditional path
- **Message:
@Name,** Thank you for your valuable feedback. Your feedback helps us to improve our services further.
- **Action:** Store response + close the loop

---

### 6. **Finalization**

- **Google Spreadsheet:** Capture all final values:
    - Customer Name
    - Rating
    - Callback Preference (if any)
    - Specific Issue (if any)
    - Time of CSAT score
- **Update Chat Status:** Set as “Solved”

---

### 7. Feedback Loop

1. **Callback Protocol for DSAT Feedback:**
    1. For every DSAT (Dissatisfied) feedback, a callback must be scheduled within **1 hour** to understand the root cause of the issue.
2. **Issue Handling Based on Callback Outcome:**
    - **If the issue is still unresolved**, an agent must be assigned to work on it. The loop will only be considered closed when the customer **reinitiates the conversation** and provides **positive feedback**.
    - **If the issue is due to a system error**, the details must be shared with the **tech team**. Once resolved, the **updated status** must be communicated to the customer.
3. **Disposition Tracking for Each Chat:**
    - Every chat must be tagged with structured dispositions:
        - **Level 1**: Pre-loan / Post-loan
        - **Level 2**: Type of issue
        - **Level 3**: Issue status – *Issue Raised* / *Issue Resolved*

---

## ✅ **Success Metrics**

- % Fill Rate
- % of DSAT escalated with callback requested
- % DSAT/CSAT ratio over time
- Average rating per agent
- Monthly feedback volume logged
- Issue x DSAT

---

## 🧠 **Future Enhancements**

- Add Net Promoter Score (NPS) follow-up.
- Include multilingual support.
- Can we add the tags of agents and flow the tags in the chatbot flow to capture in the google sheets?
-