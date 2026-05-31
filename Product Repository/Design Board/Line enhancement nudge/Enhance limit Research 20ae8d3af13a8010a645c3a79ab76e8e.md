# Enhance limit Research

### Objective

1. **User Motivation:**
Why do people enhance their limit?
2. **Mental Models**
How do they currently think about credit lines?
    - Currently our users think about credit line like a personal loan, They only choose increase their credit limit if they are in need.
    - What we can work towards is building the mindset like a credit card where increased credit limit is something people go for even when they don’t feel the need for it.
    - Folks tried to
3. **Context of Use**
When do they increase limit?

- After a withdrawal (they see low balance)
- Utilisation > 70%
- If they see the value of their MF has increased.  . . 

4. **Flow Drop Offs**
Why do users abandon this?
    - Users who dropped out usually didn’t get the limit they wanted
    - They also were ineligible for the loan since there is a 10K limit 
    
    Unclear next steps.
    Lack of feedback
    Screen fatigue
5. **Purpose & Value**
Why does this feature matter to users?

> It’s a fast, low-effort way to access more cash without applying for a new loan. KYC, Mandate and Agreement not required (If new total limit is below SL)
> 

---

### Feedback from users

- No one complained of any difficulty, lack of information for dropping off.
- When asked “What’s one thing stopping you from increasing your limit right now?”
    - The answer always is they don’t have the need for it.
- Minimum 10K being the reason for drop-off.

---

### Segments of Users and Questionnaire

1. **Repeat Users (Used Top-Up More Than Once- Ideal Users)**
    - Why did you “Enhance Limit”?
    - What made you come back and do it again?
    - How easy or difficult was it to find the increase limit option?
    - Was anything unclear or unexpected in your experience?
    - Hindi
        - Aapne pehli baar limit enhance kyun kiya tha?
        - Aapne phir se kyun kiya?
        - Pura process aapko kaisa laga — easy ya confusing?
        - Koi ek step jo aapko helpful ya clear laga?
        - Aapko paise milne mein kitna time laga tha?
        - Kya koi cheez aisi thi jo alag thi ya samajh nahi aayi?
        - Aapko is process pe trust kyun hua?
        - Aapne jo extra limit mili uska use kaha kiya?
        - Kya kuch aisa hai jo aur better banaya ja sakta hai?
        - Kya aap yeh feature kisi aur ko recommend karenge? Kyun?
    
2. **>70% Utilisation Users**
    - Are you aware that your available credit is nearly exhausted?
    - Have you ever thought of increasing your limit?
    - Did you notice the “Enhance Limit” option in the app?
    - What do you think it does?
    - What would motivate you to explore more credit availability?
    - Are you worried about interest rate, credit score, or eligibility rules?
    - Do you prefer to wait until absolutely needed before seeking credit?
    - What’s one thing stopping you from increasing your limit right now?
    - Hindi
        - Kya aapko pata hai ki aapki limit kaafi use ho chuki hai?
        - Kya aapne kabhi socha hai ki aap apni limit badha sakte hain?
        - App mein ‘Enhance Limit’ ka option aapne dekha hai?
        - Aapke hisaab se ye option kya karta hoga?
        - Kis situation mein aap limit badhane ka decision lenge?
        - Kya aapko credit score ya paperwork ka concern hota hai?
        - Kya aapko pata hai ki mutual fund ki value se limit badh sakti hai?
        - Aap tab tak wait karte hain jab tak emergency na ho?
        - Agar app bolta ki “Aap ₹X zyada le sakte hain”, to kya aap try karte?
        - Abhi aapke liye sabse bada doubt ya rukawat kya hai?

1.  **Dropped-Off Users**
    - Why did you decide to start the limit enhancement process?
    - When you started, was there any information unclear or missing during the journey?
    - At what step did you feel confused or stuck?
    - Was it easy to find increase limit feature?
    - Hindi
        1. Aapne limit badhane ka process shuru kyun kiya tha?
        2. Aap kis step tak gaye the?
        3. Us samay aapko kya feel hua?
        4. Kya koi cheez samajh nahi aayi ya clear nahi thi?
        5. Kya aapko laga tha ki limit turant badh jaayegi?
        6. Aapne process ko complete kyun nahi kiya?
        7. Kya aapko wait time ya approval process ko lekar confusion tha?
        8. Agar hum kuch aur explain karte, to kya aap aage badhte?
        9. Kya aapne socha hai ki baad mein wapas aake complete karenge?
        10. Agar hum aapko ek simple tracker ya update dete, to kya aap wapas aate?

1. **Completed Successfully Users**
    - Why did you decide to start the limit enhancement process?
    - When you started, was there any information unclear or missing during the journey?
    - At what step did you feel confused or stuck?
    - Was it easy to find increase limit feature?
    

### Feedback on current flow from AI

### 🟢 **0:00–0:07 | Home Screen Entry**

**✅ What’s Working:**

- “Enhance Limit” button is visible on dashboard
- Simple UI with enough white space

**⚠️ Issues:**

- CTA label is vague: *“Enhance Limit”* doesn't say what the **user gains**
- No contextual reason *why* they should tap it — doesn’t reflect urgency or opportunity

**💡 Suggestions:**

- Change CTA to: **“Check ₹X More Credit”** or **“Get More Cash from Your MFs”**
- If user has >70% utilization or portfolio grew → trigger a dynamic card/banner

---

### 🟡 **0:08–0:20 | Portfolio Fetch + OTP**

**✅ What’s Working:**

- Uses mobile number → familiar for users
- Process feels quick so far

**⚠️ Issues:**

- No message setting user expectations (e.g., “We’re checking your eligibility...”)
- No indicator of trust: Is this secure? What data are we accessing?

**💡 Suggestions:**

- Add loader microcopy like: **“Verifying with your mutual fund provider...”**
- Add reassurance: **“Safe, 1-time verification. No impact on credit score.”**

---

### 🔴 **0:21–0:36 | Eligibility / Unlock Credit Limit**

**✅ What’s Working:**

- Shows the top-up eligibility amount clearly

**⚠️ Issues:**

- Zero emotional language: “You’re eligible for ₹X” doesn’t tell me *why it matters*
- No context on **why now?** Did my MF grow? Have I used 80% of my limit?
- Primary CTA is passive — “Proceed” lacks motivation

**💡 Suggestions:**

- Add line: **“Your mutual fund value qualifies you for ₹X more credit”**
- CTA: **“Unlock Now”** or **“Get My Extra ₹X”**
- Include assurance: “No docs, no CIBIL impact, takes 2 mins”

---

### 🟢 **0:37–0:48 | Pledge & Confirmation**

**✅ What’s Working:**

- Clean, simple UI
- Logical next step placement

**⚠️ Issues:**

- Still no **timeline** — when will they get the cash?
- No **feedback** on what’s being processed
- Emotionally flat — doesn’t feel like a "win" for the user

**💡 Suggestions:**

- Add a **progress indicator** or “We’ll notify you in 1–2 days”
- Add **success visual or celebration** once pledge is accepted

---

### 🟡 **0:49–End | Post-action State (Assumed)**

**Assumption:** User is done but isn’t told *what happens next*.

**⚠️ Issue:**

- No post-state: no tracker, confirmation message, or option to cancel

**💡 Suggestions:**

- Add **“You’re in! We’ll notify you when your limit is updated”**
- 
- Let’s **everyday language** (not “pledge MF”, but “use your mutual funds to unlock cash”)
- Avoid heavy visuals or jargon (LTV, NAV %, etc.)
- Add **trust signals** (No impact on CIBIL, secure process, etc.)

### UX Audit

[https://embed.figma.com/design/jYRvz34fgH47FywaqCrm25/Manage-Limit?node-id=840-4176&t=KEskHCXwVMsAzhxz-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/jYRvz34fgH47FywaqCrm25/Manage-Limit?node-id=840-4176&t=KEskHCXwVMsAzhxz-11&embed-host=notion&footer=false&theme=system)

### Behavioural Trigger Map

| **User State** | **Motivation Level** | **Trigger Opportunity** | **UX Nudge** | **Placement** |
| --- | --- | --- | --- | --- |
| **Has used 80%+ of credit limit** | High | 1. Withdrawal blocked or low balance screen
2. Homepage | “You’ve used most of your limit. Check if you can unlock ₹X more” | Post-withdrawal screen / banner |
| **Just completed a successful loan repayment** | Medium | 1. Passive nudge on repayment success page. | “Congrats on repayment. Want to boost your limit” | Post-repayment screen / banner / Toast / Pop-up |
| **New user, exploring for first time** | Low | 1. Refresh button on home. | Increase limit if they are eligible. | Button on main card. |
| **Clicked “Enhance Limit” but dropped off** | High (but interrupted) | 1. Home nudge | “Still need that extra credit? Complete in 2 mins — no extra docs needed.” | Home screen “Resume” card |
| **Eligible but hasn’t taken top-up** | Medium | Portfolio eligible + inactive 30+ days | “You’re eligible for a ₹X top-up. Get it in 2 taps.” | Push / email / manage limit tab |
| **Tried to pledge MF, fetch failed** | High–Frustrated | After failed attempt | “Still need that extra credit? Complete in 2 mins — no extra docs needed.” | Error screen with retry CTA |
| **High MF value, no limit utilized yet** | Low (curious) | Passive eligibility ping | “Your investments could unlock ₹X instantly. Want to check?” | Explore screen / MF tab |

### Journey Map Audit

| **Stage** | **User Goal** | **Touchpoint / Action** | **Emotion** | **Pain Points / Gaps** | **Opportunities** |
| --- | --- | --- | --- | --- | --- |
| **1. Enters App** | Access credit dashboard | Opens home screen | Neutral → hopeful | “Enhance Limit” button is visible, but has no motivation or clarity | Add benefit-led card: *“You may unlock ₹X more credit”* |
| **2. Clicks 'Enhance Limit'** | Check if more money is available | Taps CTA | Curious → slightly unsure | CTA is vague; no context given (Why now? Am I eligible?) | Use dynamic copy: *“Your MF grew. Check if you qualify for ₹X more”* |
| **3. OTP & MF fetch starts** | Authenticate MF provider & check eligibility | Inputs number → waits | Mild tension | No feedback on what’s happening, no timeline, no “why this step” | Add microcopy: *“Verifying via your MF provider (secure, one-time)”* |
| **4. Eligibility Result Displayed** | Know how much more credit is possible | Sees ₹ amount | Mild relief → confused | No reason given for eligibility, no time estimate, no emotional confirmation | Add celebratory tone + context: *“You’re eligible for ₹X more based on your MF portfolio”* |
| **5. Clicks Proceed / Pledge** | Complete top-up request | Begins next steps | Committed, but cautious | Still no ETA, success isn't clearly defined, zero feedback | Add “Step 2 of 3” + badge: *“No docs required. You’re almost done.”* |
| **6. Post-Action State (not shown)** | Know what happens next | Presumably dropped into dashboard | Anxious or confused | No confirmation, tracker, or follow-up | Show success screen: *“Request received. Limit will reflect in 1–2 days. We’ll notify you.”* |

### Funnel optimisation flow

[https://embed.figma.com/board/1GAwhiE76elEzujIjOycBZ/Servicing-jam-board?node-id=115-1847&t=rGLnBF4ryFua8xbc-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/board/1GAwhiE76elEzujIjOycBZ/Servicing-jam-board?node-id=115-1847&t=rGLnBF4ryFua8xbc-11&embed-host=notion&footer=false&theme=system)

### Object oriented UX

OOUX = **Object-Oriented UX** — a framework that helps you design **clarity-first** user experiences by identifying and structuring **core objects** that users interact with.

It was developed by Sophia Prater and is inspired by **object-oriented programming**, but applied to UX

## 🧠 Think of OOUX like this:

Most UX design starts with:

> “What does the screen look like?”
> 

OOUX flips it:

> “What are the things (objects) in your system that users care about?
> 
> 
> How do these things connect, change, and show up in the UI?”
> 

## 🛠 Example in Volt Money

Instead of designing the **Loan Details Page** as a standalone screen, you'd say:

> “Loan” is the object.
> 
> 
> Let me list all its **attributes**, **actions**, and **connections** to other objects.
> 

That way:

- You reduce inconsistencies across the app
- You build scalable UI patterns
- You align your design with what users mentally model

## Brainstorm

1. Why do people enhance limit?
    - Their limit is exhausted and they need additional limit for their work/emergency
    - They anticipate an upcoming need in the future
    - Why not, people.. .
2. How does this process relate to in daily life?
3. How do they currently think about loan/credit line people have?
4. Why do users abandon this flow?

What is the current conversion of this flow? we don’t have proper data on conversion of this flow

![Screenshot 2025-06-06 at 4.01.12 PM.png](Enhance%20limit%20Research/Screenshot_2025-06-06_at_4.01.12_PM.png)

What we can infer from data?

- Only 65% who see the increase limit page

What is the metaphor here from real life we can take?

- Top up.

- Is it increasing the % of pledged mutual fund NAV that can be loaned?
- Increase total disbursed loan value?
- 

Questions 

- When do users most often request a limit increase?
-