# /problems

To effectively document the problems you’re facing with **Wati**, **Exotel**, **Zendesk**, and 

**1. Wati (WhatsApp Integration)**

**Problem**: Lack of visibility and tracking of WhatsApp communications

•	**Details**: Wati handles a high volume of inbound customer queries, but there is no systematic way to track query status (open, pending, resolved). This leads to issues where agents miss or forget to follow up on important customer queries.

•	**Impact**: Queries often go unresolved, causing delays in customer service and frustrating customers, particularly MFDs who rely on quick resolutions to onboard and serve their clients.

•	**User Story**: *As an agent, I am overwhelmed by the volume of WhatsApp messages coming in. There is no mechanism to mark whether I’ve responded to a message or if it’s still unresolved, which leads to missed follow-ups and unhappy customers.*

**2. Exotel (Call Management)**

**Problem**: Inefficient call tracking and follow-up system

•	**Details**: Exotel manages inbound calls, currently there is a manul batch process to send the list of the customer with missed calls to support team to reachout  through Exotell portal. we need more real time way to track whether queries have been resolved after a missed calls.  Agents cannot easily see if the customer issue requires follow-up or if it has been addressed fully during the initial call.

•	**Impact**: Critical customer issues often require additional attention but get lost after the first call, resulting in unresolved problems, repeat calls, and customer dissatisfaction.

•	**User Story**: *As an agent, I receive many customer calls, but there’s no system to track whether their issues were fully resolved. Without follow-up reminders or logs, important cases are forgotten, and customers have to call back multiple times.*

**3. Zendesk (Ticketing System)**

**Problem**: Fragmented ticketing and lack of SLA tracking

•	**Details**: While Zendesk manages tickets across multiple channels (email, chat, etc.), it does not integrate well with other tools like Wati or Exotel. This leads to fragmented reporting and ticketing, where some queries are logged in Zendesk but others (from WhatsApp or calls) are not. Additionally, there is no clear tracking of SLAs for different customer segments (e.g., MFDs vs. direct customers).

•	**Impact**: Incomplete visibility of customer queries and SLA breaches result in delays, lost tickets, and poor prioritization of high-value customers.

•	**User Story**: *As a service manager, I cannot track SLAs for different customer types, which leads to some high-priority issues being neglected. Additionally, not all customer queries (e.g., from WhatsApp) are reflected in Zendesk, creating gaps in service records.*

**4. Periscope (Group Chat Management)**

**Problem**: No tracking and visibility of group chat resolution

•	**Details**: Periscope is used for managing group chats between RMs and MFDs, but there is no system in place to track the status of the conversations. This makes it difficult to know whether a query has been addressed or if follow-ups are required. Additionally, it’s hard to measure the performance of these interactions across different MFDs.

•	**Impact**: Queries from MFDs may go unresolved or require multiple follow-ups because there’s no tracking system, resulting in a lack of accountability and slow responses.

•	**User Story**: *As an RM, I manage multiple MFDs through Periscope, but there is no way to track whether each query is resolved. I often miss follow-ups, and MFDs are dissatisfied with the response times.*

MFD would like to see the status of the there request , or ticket 

Core servicing 

- actual problems