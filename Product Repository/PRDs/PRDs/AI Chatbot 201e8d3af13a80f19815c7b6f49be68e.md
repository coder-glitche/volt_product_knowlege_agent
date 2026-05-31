# AI Chatbot

: Vijay Kumar S
Created time: May 28, 2025 11:52 AM
Status: Not started
Last edited: September 1, 2025 10:48 AM

# **What problem are we solving?**

Currently the FRT for the response is higher (9+ minutes)
Average resolution time of the chat is 60+ minutes)
No 24 hour service limited hour servicing

---

# **How do we measure success?**

Phase 1 : AI Bot Accuracy across different models and different versions

---

# **What is the solution?**

The **AI Chatbot Proof of Concept (POC)**, this document outlines the **Phase 1 scope**, focused on backend integration, benchmarking, and foundational design to prepare for future customer-facing deployment via **WATI**.

### 🔹 Phase 1 Scope

### 1. **Customer Interaction Capture via WATI Webhook**

Leverage the **WATI webhook** to capture real-time customer interactions. This will act as the entry point for routing messages to the LLM (Large Language Model), allowing us to simulate and analyze bot responses based on actual customer queries.

### 2. **LLM Integration for Automated Responses**

Captured interactions will be passed to various LLMs for generating responses. The LLMs will operate **strictly using internal data sources** and will **not access or search the web**.

The two primary sources of information for the LLMs will be:

- **Internal APIs** (e.g., **Samadhan**) for transactional or context-specific data
- The **Internal Knowledge Base** for domain and support-related content

### 3. **Model Benchmarking Across LLMs and Versions**

To determine the most effective AI engine for our use case, we will benchmark responses across:

- Multiple LLMs (e.g., **ChatGPT**, **Gemini**, **Claude**)
- Different **versions** of these LLMs (e.g., GPT-4 vs GPT-4-turbo, Claude 3 variants, etc.)

Each will be evaluated for:

- Accuracy
- Relevance
- Consistency
- Latency (response time)
- Fallback Mechanism

### 4. **Backend-Only Execution**

All development and testing will be conducted **entirely in the backend** during Phase 1. There will be **no customer-facing deployment** until the analysis is complete and the chatbot meets defined performance standards.

### 5. **Design of Fallback & Handover Mechanisms**

As part of building a robust solution, we will evaluate:

- **Fallback strategies** when the bot is unsure or unable to respond
- **Agent handover mechanisms** to ensure smooth transitions to human support
- **Guardrails** to prevent hallucinations, off-topic responses, or policy violations by the bot

These controls are critical for maintaining quality and reliability before any live rollout.

### 6. **Customer Journey Design (Parallel Workstream)**

In parallel, we will map out the **end-to-end customer journey**, ensuring the AI experience is intuitive and aligned with customer experience. This journey design will guide the frontend experience when the bot is later integrated with WATI.

### 7. **Post-Analysis Decision for Production Rollout**

After analysing the data from this phase, we will:

- Select the most effective LLM model and configuration
- Finalize fallback and escalation logic
- Decide on **proceeding with WATI integration** for real-time customer interactions

This phased approach ensures that we rigorously test the AI chatbot in a controlled backend environment before any live deployment. It also gives us the flexibility to fine-tune performance, design a customer-friendly experience, and build the necessary governance into the system.

### 🔹 Out of Scope (for Phase 1)

- Direct customer-facing bot deployment
- Web search or external knowledge integration

## **Functional Requirement**

1. **Webhook Listener**
    1. Capture messages via WATI webhook
    2. Store and route to backend pipeline
2. **LLM Response Handler**
    1. Interface with selected LLMs
    2. Return structured bot responses
3. **Knowledge/Data Integration**
    1. Internal knowledge base lookup
    2. Samadhan API integration for dynamic queries
4. **Response Logging**
    1. Log user queries, bot responses, timestamps, model versions
5. **Fallback and Escalation**
    1. Define when bot triggers fallback
    2. Trigger human handover via predefined condition.

## **Non-Functional Requirements**

- **Latency target**: < seconds for LLM response (TBD)
- **Accuracy threshold**: ≥ X% response match with defined standards (TBD)
- **Security**: Ensure secure handling of sensitive user input
- **Reliability**: > X% uptime of backend services during testing (TBD)

# **Success Criteria / KPIs**

- Benchmark accuracy scores across LLMs (top 3 models)
- 90%+ response success rate with no hallucinations
- Fallback triggers correctly in ≥ 95% failure cases
- Handoff to agent tested and working
- Data storage mechanism.

# Knowledge Base:

1. Initial Knowledge Bases: 
    1. Docs: 
        1. [https://docs.google.com/document/d/1HK_L0fLRlIW2ECdvKxwh-_DrETTtRL-eRlo8TbJRmPI/edit?tab=t.ri9b4eqxl35l](https://docs.google.com/document/d/1HK_L0fLRlIW2ECdvKxwh-_DrETTtRL-eRlo8TbJRmPI/edit?tab=t.ri9b4eqxl35l)
        2. [https://docs.google.com/document/d/1-GdZnTxORaR0Mj8cgMoJjI8OzAvOgChqYCbviKDnoNg/edit?tab=t.0#heading=h.ps3z8clrpwna](https://docs.google.com/document/d/1-GdZnTxORaR0Mj8cgMoJjI8OzAvOgChqYCbviKDnoNg/edit?tab=t.0#heading=h.ps3z8clrpwna)

# **Probing Chatbot Integration**

In **Version 1**, the probing functionality was managed using the **native WATI chatbot**.

As part of the updated implementation, this has been **replaced by Volt’s backend probing chatbot**, which is triggered programmatically from the **Volt backend**. This approach eliminates the need for WATI-native automation, resulting in a **reduction in chatbot automation costs**.

**Workflow:**

1. **Probing Initiation:**
    
    The probing chatbot is triggered directly from the Volt backend upon receiving a new customer message.
    
2. **Chat Filtering:**
    
    The backend chatbot handles initial customer interactions and performs the necessary filtering or categorization.
    
3. **Agent Assignment:**
    
    Once probing is complete, the Volt system triggers WATI’s **allocation mechanism** to assign the chat to an appropriate agent.
    

This new setup ensures tighter backend control, improved flexibility, and cost optimization by limiting reliance on WATI’s chatbot automations.

**I have added below the probing chatbot workflow journey :**

![image.png](AI%20Chatbot/image.png)

**Probing Chatbot  Post Implementation –**

**Overview:**

As part of our phased rollout, the probing chatbot has been deployed to interact with customers and help filter chats before routing them to agents. In Version 1, these chats were initiated manually. The chatbot journey has since evolved with backend integration and strategic automation changes.

**Analysis of the Phase 1 data:** https://docs.google.com/spreadsheets/d/1AmW89zKxMjXp8NncwI2rkYkIrcftDpC4XGOA_ZbaAW4/edit?usp=sharing

**Progress Updates: As on 12th Aug 2025**

- The WATI probing chatbot has been **replaced by Volt’s backend probing chatbot** using WhatsApp webhooks, resulting in reduced automation but improved backend control.
- From **15th July to 1st August**, chats were monitored in **shadow mode** to assess the performance of various AI models.
- AI-generated responses are currently being **reviewed**, and feedback will be shared to enhance the **knowledge base** and refine **prompt engineering**.
- During **non-business hours**, Volt’s backend chatbot is managing conversations, leading to **cost savings** by eliminating reliance on the WATI chatbot.
- The **Samadhan API** is now live for both **LMS and LOS flows** as part of **Phase 1**.

**Current Limitations – Phase 1:**

- No auto-closure mechanism for **inactive chats** is in place.
- **Customer nudges** to prompt responses have not been implemented.
- The AI model remains in **shadow mode** and is not actively responding to customers.
- Handling of **complex queries** is limited due to dependencies on the evolving knowledge base.

**Plans for Phase 2:**

1. **Probing Chatbot Enhancements:**
    - Continue with the current backend probing chatbot.
    - Introduce **customer nudges** to improve engagement.
    - Enable **auto-closure** of inactive chats (either soft close or agent assignment) after **30 minutes** of no response.
2. **Faulty/Broadcast Message Handling:**
    - Implement auto-closure for chats triggered by **broadcast messages** or **faulty replies** (e.g., “Thank you for reaching out!!” or auto-replies like “I will maintain balance”).
    - Targeting a **20% reduction** in overall message volume.
    - Ongoing mapping of **keywords** used in broadcast messages and customer-configured auto-replies.
3. **AI Response Analysis:**
    - Continue running AI in **shadow mode**.
    - Post feedback and prompt/knowledge base improvements, plan for gradual transition to active response mode.

**Action items Taken for Phase 2:** 

| **S. No.** | **Description** | **Impact Type** | **Impact** |  |
| --- | --- | --- | --- | --- |
| 1 | 5% of the chats are blacklisted messages. In these chats, the agents has to manually close the tickets by assigning them to themselves and then closing the ticket. In this, Agents does not require to send any closing or CSAT messages. | Improvement | 5% Chat |  |
| 2 | Currently, if customer sends a message other than the options provided, the bot does not acknowledge the message but follows the hard path ruining the customer experience. - Short term fix: Acknowledge that customer didn't select a valid option and sent a message, so we are directly assigning the chat to the agent- Long term fix: Nudge the customer to select the option, if still he/she does not respond, assing the chat to agent | Customer Experience |  |  |
| 3 | The Customer support team is not disabling the chats manually which results in ambigous behaviour.The count is not measurable because of the ambigous results. | Bug Fix |  |  |
| 4 | Update the blacklisted messages list as few keywords like "Satisfied", "Not Satisfied" & other buttons offered through campaign initiates the chat.In these chats, no agent or customer intervention is needed apart from closing the chat.This can be automated. | Improvement |  |  |
| 5 | Team has to manually check the chats that entered non-business hours and send a communication to re-initiate the chat, before closing it.- Why we need to do it? Because these customers can route to different mediums like call, etc.- Long term fix? To reinitiate the chat in business hours and assign the chat to the agent. | Improvement | ~16% |  |
| 6 | Team has to manually close the chats that do not respond to the bot.**Current SOP**: Wait for 30 minutes of no response from customer and manually disable the chat. Then nudge the customer to respond to human agent. On no response, the agents close the chats.**Issue**: Agents do not manually disable. The 30 minute check is not followed.**Solution**: Nude the customer on no response in 30 minutes window and self close the chat. | Improvement | ~60% | piority 1 redice the |

**Feedback shared with shellkode team to improve AI Responses:**

1. Each response contained too many examples. Examples should only be included when absolutely necessary.
2. The agent is summarising the customer’s message, which is not required. We should directly answer the customer’s query.
3. Responses should be concise, with a maximum length of 50–80 characters.
4. The responses from the Knowledge Base feel like direct copy-paste. Can we explore an approach where AI uses the KB to understand the content and craft a reply tailored to the customer’s specific query?
5. Is the Samadhan API integrated?
6. The agent is attempting to respond to messages with no meaningful content. In such cases, we can either provide the customer support number or politely decline to respond.

# **Phase 2 Documentation:**

1. Probing Chatbot Enhancements:
    1. Customer Nudges:
        1. For customer nudges, we will prompt the customer to respond to the probing chatbot in case they forget or remain inactive:
        - **1st nudge** → sent **5 minutes** after the last message if there is no response.
        - **2nd nudge** → sent **10 minutes** after the first nudge.
        - **3rd nudge** → sent **15 minutes** after the second nudge.
        - If the customer still does not respond after the third nudge, the chat will be **soft closed**.
    
    The Excepted behaviour with the nudges are as below:
    
    1. That customer continues with interacting with bot
    2. Generic messages that can be applied anywhere.
    3. First Message: soft nudge; Second message: Hard nudge; Third message: Chat closure

**Nudges:**

**At 5 Minutes :** Just checking in—could you share the details of the issue so we can help resolve it quickly?

**At 15 Minutes :** We’re here to assist you. Please share the details of the issue so we can move forward.

**At 25 Minutes – Final Closure :** As we haven’t received the details, we’ll keep this conversation on hold. You can reply anytime, and we’ll be ready to assist you.

1. **Faulty/Broadcast Message Handling:**
    1. For faulty message handling, we will use **predefined keywords and broadcast responses** to detect irrelevant or auto-generated customer replies.
    2. These responses will be filtered out, and the chats will be **auto-closed** accordingly.
    
    **Currently configured broadcast responses for filtering include:**
    
    - **Satisfied**
    - **Not Satisfied / I'll maintain balance**
    
    **Associated auto-responses:**
    
    - *“Thank you for contacting us”*
    - *“How can we help you?”*