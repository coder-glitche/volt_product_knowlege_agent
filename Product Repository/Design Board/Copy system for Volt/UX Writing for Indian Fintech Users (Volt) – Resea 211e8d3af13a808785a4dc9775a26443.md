# UX Writing for Indian Fintech Users (Volt) – Research & Guidelines

# Introduction

Designing a UX writing system requires a deep understanding of **local users**, **financial regulations**, and **effective copy practices**.  Every label, message, and CTA must inspire confidence and clarity, since

<aside>
💡

> *Fintech content design and UX writing is all about building user trust, and it couldn’t matter more when we’re dealing with people’s money.*

 https://uxcontent.com/ux-writing-in-the-fintech-industry/#:~:text=Fintech%20content%20design%20and%20UX,we%E2%80%99re%20dealing%20with%20people%E2%80%99s%20money
> 
</aside>

## Understanding the Indian Fintech User

### **Trust is paramount**

Indian users, especially first-time investors and borrowers, tend to be cautious with new financial services. 

<aside>
💡

A McKinsey report found that *trust is the primary factor influencing customer adoption and engagement with fintech services* [thence.co](https://www.thence.co/blogs/building-trust-in-fintech-ux-key-psychological-factors-for-user-confidence#:~:text=User%20confidence%20is%20the%20degree,and%20engagement%20with%20fintech%20services) 

</aside>

Users need to feel their money and data are safe. UX copy should therefore reassure at every step (e.g. using phrases like “securely powered by XYZ bank” or highlighting RBI oversight) to strengthen this trust foundation.

### **Broad, diverse audience**

Volt’s target users include salaried professionals investing in mutual funds, stocks, insurance, bonds, etc. Many are financially savvy to an extent, but there’s a **wide range of literacy** Some may be first-time investors from Tier-2 cities (as seen with apps like Groww), while others are seasoned market participants. Copy must hit a sweet spot where **both novices and experts can understand it easily**

<aside>
💡

As one UX guide advises, F*intech UX should prioritize clear, simple language that can be easily understood by both newbies and experts alike*

https://www.thence.co/blogs/building-trust-in-fintech-ux-key-psychological-factors-for-user-confidence#:~:text=Problem%3A%20The%20financial%20language%20can,to%20understand%20for%20many%20users

</aside>

This means avoiding heavy jargon and explaining necessary terms in plain language. For example, instead of “lien marking your mutual fund units,” Volt’s app explains it as

*“mark your mutual funds as a security with a trusted lender”* immediately clarifying the action.

### Friendly, guiding tone

 A friendly tone humanizes complex financial tasks – it’s like having a helpful friend explain things rather than a formal banker. However, the tone should also reflect **professionalism** to build credibility; a balance of *professional yet approachable* works well, as Razorpay’s content team describes: their fintech UX writing maintains a *“consistent tone – professional yet approachable”* to serve users dealing with high-stakes transactions

### Attention span and mobile behaviour

Remember that Indian users predominantly access fintech services on mobile (Volt is **mobile-first**, as noted). Mobile users skim and scan due to small screens and on-the-go usage. Studies show people read only ~20–28% of text on screens, often scanning in an “F”-pattern.

### User psychology and guidance

**Overwhelm is a risk** – if we dump too much info on a user (like lengthy terms and conditions or dense FAQs), they might disengage. Instead, structure content step-by-step (onboarding flows, form field hints, etc.) so that users get information *just when they need it*.

Bottom line: make every piece of text feel like it’s helping the user move forward confidently, not confusing or stopping them.

## Complete Framework for Building Your Copy System

Based on extensive fintech UX writing research and best practices, I've created a comprehensive framework for Volt's copy system that addresses your specific user base and requirements. This framework provides the foundation for your Figma plugin while ensuring consistent, accessible, and trustworthy communication across your product.

## Key Framework Components

## Four-Level Tone System

The framework establishes **four distinct tone levels** that correspond to different user contexts and emotional states:

**Level 1: Critical/Security** - For error states, security alerts, and legal requirements. This tone is formal yet reassuring, providing clear next steps without causing panic.

**Level 2: Friendly Professional** - For general descriptions, feature explanations, and onboarding. This strikes the perfect balance for your diverse user base, being conversational yet trustworthy.

**Level 3: Celebratory/Success** - For completions and positive confirmations. This tone acknowledges user achievements while maintaining professionalism.

**Level 4: Patient Guidance** - For instructions and educational content. This tone is supportive and anticipates user concerns, particularly important for first-time investors.

## Content Type Guidelines

The framework provides specific guidance for each content scenario you mentioned:

**Error Messages** follow a clear structure: what happened (without blame), why it matters, what to do next, and how to get help. For example, instead of "Invalid input detected," use "We couldn't process your transaction. Your payment details may need updating. Please check your card information and try again."

**Success Messages** celebrate user achievements while providing clear next steps. They acknowledge completion, confirm outcomes, and suggest relevant follow-up actions.

**Consent and Legal Text** prioritize transparency while maintaining accessibility. They provide plain language summaries before legal text and highlight key user rights clearly.

## Jargon Translation System

The framework addresses your core challenge of serving both novice and experienced users by implementing a systematic approach to financial terminology. Every complex term follows the pattern: **Jargon term** → **Plain explanation**. For example:

- "SIP (Systematic Investment Plan) - automated monthly investments"
- "NAV (Net Asset Value) - the current price per unit of your fund"
- "Lien marking - temporarily securing your mutual funds as collateral"

# User psychology and guidance

### Regulatory and Compliance Considerations

In India, fintech copy must heed certain **regulatory guidelines (RBI, SEBI, etc.)** to ensure transparency and fairness. The Reserve Bank of India, in its digital lending directives, stresses that loan offerings should be presented with *full transparency and without bias or misleading content*[economictimes.indiatimes.com](https://economictimes.indiatimes.com/industry/banking/finance/banking/rbi-issues-new-guidelines-for-loan-service-providers-to-ensure-transparency-in-multi-lender-loan-offers/articleshow/121033211.cms?from=mdr#:~:text=Reserve%20Bank%20of%20India%20released,biased%20content%20and%20misleading%20tactics)[economictimes.indiatimes.com](https://economictimes.indiatimes.com/industry/banking/finance/banking/rbi-issues-new-guidelines-for-loan-service-providers-to-ensure-transparency-in-multi-lender-loan-offers/articleshow/121033211.cms?from=mdr#:~:text=RBI%20emphasised%20that%20the%20content,is%20prohibited%2C%20the%20RBI%20said). This has direct implications for UX writing in Volt:

- **Disclose key loan details clearly:** Always mention the critical facts of credit products in plain terms. RBI’s guidelines mandate showing *key details such as lender name, loan amount, tenure, **annual percentage rate (APR)**, monthly EMI, and any penal charges* in the digital interface[economictimes.indiatimes.com](https://economictimes.indiatimes.com/industry/banking/finance/banking/rbi-issues-new-guidelines-for-loan-service-providers-to-ensure-transparency-in-multi-lender-loan-offers/articleshow/121033211.cms?from=mdr#:~:text=The%20regulator%20also%20said%20that,comparison%20between%20various%20loan%20offers). In practice, Volt’s UI copy should surface these in an easily readable format (e.g. a summary on the loan offer screen or a “Key Facts” section). Avoid burying essential info in fine print or lengthy footnotes.
- **“No hidden charges” – and mean it:** Transparency isn’t just legal, it’s a trust signal. If Volt charges fees, spell them out upfront. If not, explicitly say there are none. Volt’s own marketing copy already reflects this, stating *“Withdraw as per your need, and pay only as per usage. **No hidden charges.**”*[voltmoney.in](https://voltmoney.in/#:~:text=). Such straightforward statements should carry through in the product UI wherever costs or fees are involved (interest, processing fee, etc.). Users should never feel tricked by the wording; otherwise trust evaporates.
- **Impartial and compliant language:** RBI also warns against using **misleading tactics or content biases** – for example, UI copy that nudges users toward a particular option (a.k.a. dark patterns) is prohibited[economictimes.indiatimes.com](https://economictimes.indiatimes.com/industry/banking/finance/banking/rbi-issues-new-guidelines-for-loan-service-providers-to-ensure-transparency-in-multi-lender-loan-offers/articleshow/121033211.cms?from=mdr#:~:text=RBI%20emphasised%20that%20the%20content,is%20prohibited%2C%20the%20RBI%20said). The copy must maintain an objective, factual tone when presenting choices. If Volt lists multiple offers or actions, each should be described neutrally and accurately (e.g. not labeling one option as “Recommended” unless there is unbiased justification). All compliance-related info (like risk disclosures for mutual fund investments or legal terms for loans) should be clearly accessible and written in plain language. For instance, if Volt needs to include the classic SEBI mutual fund disclaimer (“Mutual fund investments are subject to market risks…”), it can be phrased in a user-friendly way and placed at appropriate touchpoints (e.g. on an offer screen or in FAQs), ensuring users are informed without being scared off by all-caps legalese.
- **Avoiding costly miscommunication:** Beyond satisfying regulators, clear copy prevents misunderstandings that could harm the business. A Vice report highlighted how one fintech’s poor phrasing allegedly *tricked users into signing up for unwanted credit cards*, damaging their credit scores and leading to lawsuits[uxcontent.com](https://uxcontent.com/ux-writing-in-the-fintech-industry/#:~:text=As%20digital%20banking%20becomes%20the,even%20hurting%20their%20credit%20scores). This cautionary tale underlines the importance of **unambiguous, honest messaging**. Every prompt or offer in Volt should accurately represent the action’s consequences. For example, if tapping a button will actually initiate a loan disbursal, label it clearly (“**Withdraw ₹50,000 Now**”) rather than something vague (“Get Funds” could confuse users if they don’t realize it’s an actual withdrawal). By being precise and truthful, Volt not only stays compliant but also earns user respect.

### **Volt Money Tone Matrix**

| **User Scenario** | **User Emotion / Need** | **Volt Principle to Prioritize** | **Tone Guidance** | **Example Copy** |
| --- | --- | --- | --- | --- |
| **User onboarding (first visit)** | Curious but unsure; evaluating trust | *Simplicity*, *Transparency* | Friendly, clean, and confidence-building. Avoid financial jargon. Be upfront about what’s offered. | “Welcome to Volt. Let’s get your credit set up — no hidden steps or fees.” |
| **Explaining lien / pledging MF/stocks** | Confused, anxious about asset safety | *Helpful*, *Transparency* | Calm, explanatory, non-jargony. Build trust and ensure clarity about safety and control. | “You keep ownership — we’re just securing your investments while you borrow.” |
| **Eligibility success (credit approved)** | Excited, optimistic | *Speed*, *Thematic* | Celebratory, crisp, and direct. Let delight shine but stay on-brand — no overhype. | “You’re eligible for ₹5,00,000 credit. Set it up now in under 5 minutes.” |
| **Eligibility failure / no credit offered** | Disappointed, uncertain | *Helpful*, *Accessibility* | Empathetic, respectful, encouraging. Offer clarity and next step (retry, or improve portfolio). | “Not eligible just yet. You can try again in 15 days or grow your investments.” |
| **PAN input + KYC screens** | Focused, slightly nervous about data safety | *Transparency*, *Simplicity* | Reassuring, polite, minimal. Mention purpose and security where needed. | “Enter your PAN to fetch your portfolio securely. We don’t share this with anyone.” |
| **Error: invalid PAN / input mismatch** | Frustrated, stuck | *Helpful*, *Simplicity* | Polite, blame-free, short + action-based. Avoid guilt-tripping or technical terms. | “Hmm, that PAN doesn’t look right. Please double-check and try again.” |
| **Error: max attempts / temporary lockout** | Impatient, blocked | *Helpful*, *Transparency* | Calm, clear on timeframes, encourage retry. No alarmist language. | “We’ll pause for now. You can try again in 15 minutes.” |
| **Success: pledge / withdraw / repay** | Relieved, satisfied | *Speed*, *Trust-building* | Confident, positive, concise. Reinforce control and next steps. | “All done! Your funds are secured and credit is ready to use.” |
| **Tooltips / info explainer** | Curious, cautious | *Helpful*, *Accessibility* | Concise, precise, non-jargony. Prioritize clarity over charm. | “This lets us calculate your credit based on your mutual fund value.” |
| **Loan summary screen / EMI breakdown** | Calculating, verifying, comparing options | *Transparency*, *Simplicity* | Factual, crystal-clear, no hidden meanings. Make numbers readable and digestible. | “Interest: 10.5% per annum. You only pay for what you use. No extra charges.” |
| **Reminder (repayment due, lien expiring)** | Distracted, might postpone | *Speed*, *Helpful* | Crisp, motivating, polite urgency. Avoid threats or dry statements. | “Your repayment is due in 2 days. Clear it now to unlock your investments.” |
| **Push: feature nudge (e.g. insurance unlock)** | Passive, mildly interested | *Thematic*, *Simplicity* | Light, crisp benefit-first nudge. Respect user's mental load. | “You can now get credit on your insurance too. Check your updated limit.” |
| **Exit intent / session time-out** | Uncertain, hesitant | *Accessibility*, *Helpful* | Reassure continuity, encourage return. Avoid guilt or pressure. | “You can resume anytime. Your progress is saved securely.” |

# Notes form Nicely Said

**Good UX writing = Designing with words, it’s about helping users take action without confusion.**

**Voice** is **consistent** (like Volt’s personality), **Tone** is **situational** (changes with emotion or context).

- Success? Empowering & celebratory.
- Error? Calm and reassuring.
- Empty state? Supportive and motivating.

Think of voice as *who you are*, tone as *how you sound depending on the moment*.

Volt’s personality 

1. Supportive
2. Reliable and Fast to help
3. Motivating
4. Enabler to achieve your financial needs
5. A saviour when you need most 

Aligning every word with *Supportive*, *Reliable*, *Empowering*, and *Effortless*.

Describe Volt in 3-4 words

**Transparent, Trustworthy, Easy, Fast**

### Purpose

**What happened + What to do next + Reassurance (if needed)**

- **What does the user need to do here?**
    
    → E.g., "Link a bank account," "Set up autopay," "Check credit eligibility."
    
- **What might they feel?**
    
    → Confused? Nervous? Curious? This affects your tone.
    
- **What’s your job as the writer?**
    
    → Reduce friction. Build trust. Empower the user.
    

### Understand your voice

For Volt, your audience:

- Is **financially aware**, but not always confident
- May be **anxious about trust and security**
- Wants to **save time**, avoid jargon, and stay in control

Sound like a **smart friend guiding you**

### Inverted Pyramid

- **Goal first**: “Add your bank account”
- **Details next**: “This helps us set up auto-pay.”
- **Reassurance optional**: “You can change this later.”

![image.png](UX%20Writing%20for%20Indian%20Fintech%20Users%20(Volt)%20%E2%80%93%20Resea/image.png)

### **Core Rules for Writing Usefully**

- Write for scanning
- Only say what matters right now
- Every word must do work

## ✳️ 5-Part Framework for Effective Error Messages

### 1. **State What Happened**

### 2. **Explain Why (if possible)**

> Be helpful, not technical.
> 
> 
> ❌ “NSDL validation failed”
> 
> ✅ “Your PAN doesn’t match with what NSDL has on record”
> 

### 3. **Suggest a Clear Next Step**

> Avoid dead ends.
> 
> 
> ✅ “Try again with the PAN linked to your mutual funds”
> 
> ✅ “You can reattempt in 15 minutes”
> 

### 4. **Use Reassuring Tone**

> Reduce panic. Sound supportive.
> 
> 
> ✅ “No worries. These things happen.”
> 
> ✅ “Still stuck? We’re here to help.”
> 

### 5. **Follow Brand Voice (Volt: Supportive + Reliable + Effortless)**

> Keep it short, but not cold.
> 
> 
> ✅ “Let’s fix this together.”
> 

## 📋 Error Message Template for Volt

> Header: What happened (short)
> 
> 
> **Body**: Why + what next (1–2 lines)
> 
> **Optional CTA**: Try again / Contact support / Retry later
> 

<aside>
💡

**Interacting with Volt should feel like:**

Interacting with Volt should feel like interacting with a modern, banking savvy friend/ RM — someone who guides me towards my goals and makes everything feel simple, supportive, and effortless.

- **Like a smart, supportive money guide**
- **Your effortless, goal-driven money companion**
</aside>

## Users should feel

Supportive, Effortless, Empowering and Safe

Voice: **Smart, Supportive, Calm, and Clear.**

Volt speaks like a modern financial guide — someone who knows money inside out, but explains it with warmth and clarity, not jargon.

### Tone

- **Voice** is **consistent** (like Volt’s personality).
    
    E.g., Volt is always clear, helpful, and warm.
    
- **Tone** is **situational** (changes with emotion or context).

### Situations [Scenarios]

- Error like PAN verification failed, No CKYC data found and so on
- Success like Completion of Payment, Loan application, Increase limit and so on
- Onboarding like App screenshots and Onboarding or flash screens
- Process like Increase limit process, Loan application process etc
- Educational like FAQs
- Feature explanation  like New feature of ‘Foreclosure, Increase limit, Unpledge funds, Interest calculator’ and so on.

### Content Type

1. Navigation like Bottom nav, Profile section labels and so on
2. Buttons and CTAs like Continue journey, Verify, Unlock limit and Add documents
3. Headers like “PAN Verification failed, Invalid PAN, Unlock additional limit upto 5Cr and so on
4. Sub-headers “ Pledge additional funds to unlock a higher limit in under 2 minutes”
5. Descriptions - “Higher limits mean you never have to scramble for cash, whether it’s planned or unexpected.” 

# Volt UX Copy Matrix by Scenario

## Brand Voice

**Smart, Supportive, Calm, and Clear**

---

## 1. ERROR SCENARIO

### Navigation

- **Examples**: Support | Try Again | Go Back
- **Character Range**: 4-12
- **Tone**: Calm & direct
- **Guidelines**: Simple action words, familiar terms. Stay calm and supportive.
- **Voice Application**: Clear navigation that doesn't add stress. Smart labels that guide users to solutions.
- **Avoid**: Complex phrases, technical terms, panic-inducing language

### Buttons and CTAs

- **Examples**: Try Again | Update Details | Get Help
- **Character Range**: 8-20
- **Tone**: Calm & supportive
- **Guidelines**: Clear corrective action, specific requirement. Reassuring without minimizing issue.
- **Voice Application**: Supportive CTAs that give confidence. Smart suggestions for next steps.
- **Avoid**: Vague instructions, blame language, pressure tactics

### Headers

- **Examples**: PAN Verification Failed | Connection Issue | Unable to Process
- **Character Range**: 20-45
- **Tone**: Clear, reassuring, specific
- **Guidelines**: Clear about what happened, reassuring, action-oriented. Lead with the issue.
- **Voice Application**: Smart identification of the problem. Clear communication that maintains calm.
- **Avoid**: Technical error codes, blame language, vague problems

### Sub-headers

- **Examples**: Please check your PAN details and try again | We're here to help you resolve this
- **Character Range**: 30-60
- **Tone**: Supportive, next-action focused
- **Guidelines**: Provide clear next steps. Reassuring tone that builds confidence.
- **Voice Application**: Supportive guidance that shows the path forward. Calm reassurance.
- **Avoid**: Overwhelming information, technical jargon, panic language

### Descriptions

- **Examples**: We couldn't verify your PAN. Double-check the number matches your documents exactly and try again. Need help? Tap Support.
- **Character Range**: 50-120
- **Tone**: Clear reason first, action next. Supportive, avoids blame
- **Guidelines**: Explain what happened, provide solution, reassure. Follow inverted pyramid - issue, solution, support.
- **Voice Application**: Smart explanation of the issue. Supportive solution guidance. Clear next steps.
- **Avoid**: Technical details, panic-inducing language, blame on user

---

## 2. SUCCESS SCENARIO

### Navigation

- **Examples**: Portfolio | Continue | Explore
- **Character Range**: 4-12
- **Tone**: Calm & positive
- **Guidelines**: Clear destinations, positive actions. Guide to logical next steps.
- **Voice Application**: Smart navigation to capitalize on success momentum. Clear next destinations.
- **Avoid**: Confusing labels, negative framing, overwhelming options

### Buttons and CTAs

- **Examples**: View My Growth | Continue Journey | Explore More
- **Character Range**: 10-25
- **Tone**: Celebratory, brief
- **Guidelines**: Positive action, outcome-focused. Build on success feeling.
- **Voice Application**: Supportive CTAs that build on achievement. Smart suggestions for growth.
- **Avoid**: Neutral language, missed celebration, immediate hard sells

### Headers

- **Examples**: Limit Increased Successfully! | Payment Complete | Application Approved!
- **Character Range**: 20-50
- **Tone**: Clear, celebratory
- **Guidelines**: Celebratory, acknowledges achievement, forward-looking. Lead with the success.
- **Voice Application**: Smart acknowledgment of achievement. Clear celebration that feels genuine.
- **Avoid**: Bland confirmations, technical language, over-excitement

### Sub-headers

- **Examples**: You can use your new ₹5L limit right away | Your application was processed in under 2 minutes
- **Character Range**: 30-70
- **Tone**: Calm encouragement, next steps
- **Guidelines**: Confirm the outcome, set expectations for what's available now.
- **Voice Application**: Supportive confirmation with smart next step guidance. Calm confidence building.
- **Avoid**: Overly excited tone, unclear outcomes, missing key details

### Descriptions

- **Examples**: Your limit has increased to ₹5L. Start exploring offers in your portfolio or continue building your financial goals.
- **Character Range**: 50-120
- **Tone**: Restate achievement first, then offer actionable next steps
- **Guidelines**: Celebrate success, confirm details, set expectations. Achievement first, then possibilities.
- **Voice Application**: Smart summary of achievement. Supportive guidance for leveraging success.
- **Avoid**: Bland confirmations, missing key details, immediate pressure

---

## 3. ONBOARDING SCENARIO

### Navigation

- **Examples**: Next | Skip | Help
- **Character Range**: 4-12
- **Tone**: Clear, familiar
- **Guidelines**: Progress-focused, flexible options. Don't force progression.
- **Voice Application**: Smart navigation that respects user pace. Clear progress indicators.
- **Avoid**: Forced progression, unclear steps, overwhelming options

### Buttons and CTAs

- **Examples**: Get Started | Tell Us Your Goals | Continue Setup
- **Character Range**: 10-25
- **Tone**: Supportive, motivating
- **Guidelines**: Gentle guidance, personal focus. Encouraging without pressure.
- **Voice Application**: Supportive CTAs that reduce barriers. Smart onboarding that feels personal.
- **Avoid**: Demanding tone, complex requests, high-pressure tactics

### Headers

- **Examples**: Welcome to Volt | Let's Build Your Future | Setup Your Profile
- **Character Range**: 20-45
- **Tone**: Friendly, inviting, clear
- **Guidelines**: Welcoming, journey-focused, encouraging. Set positive expectations.
- **Voice Application**: Smart welcome that builds confidence. Clear journey mapping.
- **Avoid**: Overwhelming information, complex terms, assumption of knowledge

### Sub-headers

- **Examples**: Grow your wealth safely and smartly | This takes less than 3 minutes
- **Character Range**: 25-60
- **Tone**: Quick benefit, simple action
- **Guidelines**: Brief intro/benefit, then time expectation. Remove barriers to entry.
- **Voice Application**: Smart benefit communication. Supportive time estimates that reduce anxiety.
- **Avoid**: Complex promises, overwhelming detail, unrealistic timelines

### Descriptions

- **Examples**: Build your financial future with Volt. We make investing accessible and easy to understand, starting with just ₹100.
- **Character Range**: 50-120
- **Tone**: Brief intro/benefit, then explanation. No jargon
- **Guidelines**: Reassuring, educational, removes barriers. Benefit first, then how.
- **Voice Application**: Smart introduction to value. Supportive explanation that builds confidence.
- **Avoid**: Assumptions about knowledge, overwhelming detail, jargon without explanation

---

## 4. PROCESS SCENARIO

### Navigation

- **Examples**: Back | Profile | Support
- **Character Range**: 4-12
- **Tone**: Calm, step-based
- **Guidelines**: Simple navigation that supports the process flow. Clear escape routes.
- **Voice Application**: Smart navigation that supports user confidence in multi-step processes.
- **Avoid**: Complex phrases, confusing back-tracking, dead ends

### Buttons and CTAs

- **Examples**: Continue | Verify Now | Upload Documents | Complete Setup
- **Character Range**: 10-25
- **Tone**: Clear, supportive
- **Guidelines**: Clear action for each step. Supportive progression through process.
- **Voice Application**: Smart CTAs that maintain momentum. Supportive guidance through complex processes.
- **Avoid**: Vague actions, overwhelming next steps, technical terms

### Headers

- **Examples**: Increase Your Limit | Verify Your Identity | Upload Documents
- **Character Range**: 15-40
- **Tone**: Specific, step-oriented
- **Guidelines**: Clear about current step. Action-oriented without pressure.
- **Voice Application**: Smart step identification. Clear communication of progress.
- **Avoid**: Vague processes, overwhelming information, technical steps

### Sub-headers

- **Examples**: Step 2 of 5: Verify your PAN | This usually takes under 2 minutes
- **Character Range**: 25-60
- **Tone**: Calm instruction, hint at next step
- **Guidelines**: Show progress, set time expectations. Calm reassurance about process.
- **Voice Application**: Supportive progress tracking. Smart time estimates that reduce anxiety.
- **Avoid**: Overwhelming steps, unclear progress, unrealistic timelines

### Descriptions

- **Examples**: To increase your limit, we need to verify your PAN. Enter your details below and we'll process it instantly.
- **Character Range**: 50-120
- **Tone**: Step 1 first. Clear instructions. Less is more, but offer details
- **Guidelines**: Clear reason for step, simple instructions. Support available if needed.
- **Voice Application**: Smart explanation of requirements. Supportive guidance through each step.
- **Avoid**: Complex requirements, overwhelming detail, hidden reasons

---

## 5. EDUCATIONAL SCENARIO

### Navigation

- **Examples**: FAQs | Learn | Back
- **Character Range**: 4-12
- **Tone**: Neutral, direct
- **Guidelines**: Clear educational categories. Easy navigation through learning content.
- **Voice Application**: Smart organization of educational content. Clear learning paths.
- **Avoid**: Complex categorization, overwhelming options, unclear paths

### Buttons and CTAs

- **Examples**: Learn More | Got It | See Example
- **Character Range**: 8-20
- **Tone**: Relevant, clear
- **Guidelines**: Clear learning actions. Optional depth without pressure.
- **Voice Application**: Supportive learning CTAs. Smart optional depth for different knowledge levels.
- **Avoid**: Forced learning, overwhelming options, technical progression

### Headers

- **Examples**: What is Foreclosure? | Understanding Interest Rates | How Limits Work
- **Character Range**: 15-45
- **Tone**: Direct, clear
- **Guidelines**: Clear question or topic. Direct and approachable language.
- **Voice Application**: Smart topic identification. Clear educational focus that welcomes all knowledge levels.
- **Avoid**: Overwhelming topics, assumption of knowledge, intimidating language

### Sub-headers

- **Examples**: Understanding your options | The basics explained simply
- **Character Range**: 20-50
- **Tone**: Supportive, context if needed
- **Guidelines**: Set expectation for learning level. Reassuring about complexity.
- **Voice Application**: Supportive framing that reduces learning anxiety. Smart complexity communication.
- **Avoid**: Intimidating framing, assumption of prior knowledge, overwhelming scope

### Descriptions

- **Examples**: Foreclosure lets you pay off your loan early and save on interest. Here's when it makes sense and how to do it step-by-step.
- **Character Range**: 50-150
- **Tone**: State answer/definition first, then break down the 'why'
- **Guidelines**: Clear definition first, then practical application. No jargon without explanation.
- **Voice Application**: Smart educational structure. Supportive learning that builds from basics.
- **Avoid**: Complex theory first, unexplained jargon, overwhelming detail

---

## 6. FEATURE EXPLANATION SCENARIO

### Navigation

- **Examples**: Try It | Learn More | Close
- **Character Range**: 4-12
- **Tone**: Approachable
- **Guidelines**: Clear feature exploration options. Low-pressure trial.
- **Voice Application**: Smart feature navigation that encourages exploration without pressure.
- **Avoid**: Forced trial, overwhelming options, unclear exits

### Buttons and CTAs

- **Examples**: Try Feature | Unlock Now | Calculate Interest | Unpledge Funds
- **Character Range**: 10-25
- **Tone**: Smart, actionable
- **Guidelines**: Clear action, benefit-implied. Encouraging trial without pressure.
- **Voice Application**: Smart CTAs that highlight feature value. Supportive encouragement to try.
- **Avoid**: Pushy language, overwhelming features, unclear benefits

### Headers

- **Examples**: Unpledge Funds Easily | Calculate Your Interest | Unlock Higher Limits
- **Character Range**: 20-50
- **Tone**: Clear, benefit-first
- **Guidelines**: Lead with benefit or outcome. Clear value proposition.
- **Voice Application**: Smart benefit communication. Clear feature value that connects to user needs.
- **Avoid**: Technical feature names, vague benefits, overwhelming capabilities

### Sub-headers

- **Examples**: Get access to your money anytime | See exactly what you'll save | Up to ₹5Cr available instantly
- **Character Range**: 30-70
- **Tone**: Descriptive, reinforces use
- **Guidelines**: Specific benefit or outcome. Reinforces practical use case.
- **Voice Application**: Supportive benefit reinforcement. Smart outcome communication that motivates use.
- **Avoid**: Vague benefits, technical descriptions, unrealistic promises

### Descriptions

- **Examples**: Unpledge your funds instantly when you need cash. No hassle, no long waits - your money is ready when you are.
- **Character Range**: 50-120
- **Tone**: What/why first, how/when next. Emphasize simplicity and user benefit
- **Guidelines**: Clear benefit first, then ease of use. Practical application focus.
- **Voice Application**: Smart feature explanation that emphasizes user control. Supportive simplicity communication.
- **Avoid**: Technical explanations first, complex processes, hidden limitations

---

## Implementation Notes

### Inverted Pyramid Method

All content follows the inverted pyramid structure:

1. **Most Important Information First** - Lead with the key message, outcome, or action needed
2. **Supporting Details Second** - Provide context, explanation, or next steps
3. **Background/Context Last** - Additional information, help options, or detailed explanations

### Brand Voice Application

- **Smart**: Use intelligent, informed language that respects user knowledge while explaining complexities
- **Supportive**: Always provide help, reassurance, and clear next steps
- **Calm**: Maintain steady, reassuring tone even in error states
- **Clear**: Use simple, direct language with specific examples and outcomes

### Character Range Guidelines

- Navigation: 4-12 characters (1-2 words max)
- Buttons/CTAs: 8-25 characters (action-focused)
- Headers: 15-50 characters (clear, specific)
- Sub-headers: 20-70 characters (supporting context)
- Descriptions: 50-150 characters (detailed explanation)