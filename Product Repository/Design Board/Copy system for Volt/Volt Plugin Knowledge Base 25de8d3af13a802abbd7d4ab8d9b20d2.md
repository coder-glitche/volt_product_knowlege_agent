# Volt Plugin Knowledge Base

# Introduction

This project aims to build a unified UX writing system for Volt based on fintech best practices. The goal is to have a unified, brand-aligned tone of voice across screens, touchpoints, and teams.

## Problem

- Right now we handle error case copies differently throughout the app.
- Different writers/designers use different tones, leading to a fragmented experience.
- No shared rules for writing error messages, CTAs, success screens, etc.
- Designers or PMs often write placeholder text or inconsistent copy due to lack of writing support & time constraints.

## Solution

A self-serve figma plugin where anyone can write first version of the copy that’s on-brand, on-tone, and compliant without needing support 

## Approach

- Align stakeholders on a unified brand voice
- Setup brand voice guidlines (Tone) for cases like success, error, New features and so on.
- Present guidelines that will be used as the first config for the figma app
- Create the figma plugin with the help of Devs
- Present a working model, to stakeholders
- Take feedback and iterate if necessary
- Replace copy throughout app using the figma plugin

## Brand Voice

Based on the conversation with Lalit this is what volt stands for. based on these I want to define what the tone of language we want through out the app. 

- Call with Lalit on volt brand
    1. If volt was a person how would you describe it?
        1. Supportive
        2. Reliable and Fast to help
        3. Motivating
        4. Enabler to achieve your financial needs
        5. A saviour when you need most 
    2. Describe Volt in 3-4 words
        1. Transparent, Trustworthy, Easy, Fast
    

<aside>
💡

**Interacting with Volt should feel like:**

Interacting with Volt should feel like interacting with a modern, banking savvy friend/ RM — someone who guides me towards my goals and makes everything feel simple, supportive, and effortless.

- **Like a smart, supportive money guide**
- **Your effortless, goal-driven money companion**
</aside>

Voice: **Smart, Supportive, Calm, and Clear.**

<aside>
💡

Volt speaks like a modern financial guide — someone who knows money inside out, and explains it with warmth & clarity, not jargon.

</aside>

## Scenarios / Possible Usecases

- Error like PAN verification failed, No CKYC data found and so on
- Success like Completion of Payment, Loan application, Increase limit and so on
- Onboarding like App screenshots and Onboarding or flash screens
- Process like Increase limit process, Loan application process etc
- Educational like FAQs
- Feature explanation  like New feature of ‘Foreclosure, Increase limit, Unpledge funds, Interest calculator’ and so on.

## Content Type

(All type of content across multiple touchpoints with our users )

- Navigation like Bottom nav, Profile section labels and so on
- Buttons and CTAs like Continue journey, Verify, Unlock limit and Add documents
- Headers like “PAN Verification failed, Invalid PAN, Unlock additional limit upto 5Cr and so on
- Sub-headers “ Pledge additional funds to unlock a higher limit in under 2 minutes”
- Descriptions - “Higher limits mean you never have to scramble for cash, whether it’s planned or unexpected.”

# Volt UX Copy Matrix by Scenario

Prompts for the LLM for copy based on scenario and content type.

## Brand Voice

**Smart, Supportive, Calm, and Clear**

---

## 1. ERROR SCENARIO

### Headers

- **Tone**: Clear, reassuring, specific
- **Voice Application**: Smart identification of the problem. Clear communication that maintains calm. (Clear communication that clearly states the error that has occured in User Friendly Words)
- **Character Range**: 20-45
- **Examples**: We couldn’t verify your PAN | Please check your internet | Something went wrong on our end
- **Guidelines**: Clear about what happened, reassuring, action-oriented. Lead with the issue.
- **Avoid**: Technical error codes, blame language, vague problems

### Sub-headers

- **Tone**: Supportive, next-action focused
- **Voice Application**: Supportive guidance that shows the path forward. Calm reassurance.
- **Character Range**: 30-60
- **Examples**: Please check your PAN details and try again | Try checking your internet connection
- **Guidelines**: Provide clear next steps. Reassuring tone that builds confidence.
- **Avoid**: Overwhelming information, technical jargon, panic language

### Descriptions

- **Tone**: Clear reason first, action next. Supportive, avoids blame
- **Voice Application**: Smart explanation of the issue. Supportive solution guidance. Clear next steps.
- **Character Range**: 50-120
- **Examples**: We couldn't verify your PAN. Double-check the number matches your documents exactly and try again. Need help? Contact support.
- **Guidelines**: Explain what happened, provide solution, reassure. Follow inverted pyramid - issue, solution, support.
- **Avoid**: Technical details, panic-inducing language, blame on user

### Buttons and CTAs

- **Tone**: Calm & supportive
- **Voice Application**: Supportive CTAs that give confidence. Smart suggestions for next steps.
- **Character Range**: 8-20
- **Examples**: Try Again | Update Details | Get Help
- **Guidelines**: Clear corrective action, specific, Reassuring without minimizing issue.
- **Avoid**: Vague instructions, blame language, pressure tactics

---

## 2. SUCCESS SCENARIO

### Buttons and CTAs

- **Tone**: Celebratory, brief
- **Voice Application**: Supportive CTAs that build on achievement. Smart suggestions for growth.
- **Character Range**: 10-25
- **Examples**: View My Growth | Continue Journey | Explore More
- **Guidelines**: Positive action, outcome-focused. Build on success feeling.
- **Avoid**: Neutral language, missed celebration, immediate hard sells, Wordy CTAs

### Headers

- **Tone**: Clear, celebratory
- **Voice Application**: Smart acknowledgment of achievement. Clear celebration that feels genuine.
- **Character Range**: 20-50
- **Examples**: Limit Increased Successfully! | Payment Complete | Application Approved!
- **Guidelines**: Celebratory, acknowledges achievement, forward-looking. Lead with the success.
- **Avoid**: Bland confirmations, technical language, over-excitement

### Sub-headers

- **Tone**: Calm encouragement, next steps
- **Voice Application**: Supportive confirmation with smart next step guidance. Calm confidence building.
- **Examples**: You can use your new ₹5L limit right away | | Your application was processed in under 2 minutes
- **Character Range**: 30-70
- **Guidelines**: Confirm the outcome, set expectations for what's available now.
- **Avoid**: Overly excited tone, unclear outcomes, missing key details

### Descriptions

- **Tone**: Restate achievement first, then offer actionable next steps
- **Voice Application**: Smart summary of achievement. Supportive guidance for leveraging success.
- **Examples**: Your limit has increased to ₹5L. Start exploring offers in your portfolio or continue building your financial goals.
- **Character Range**: 50-120
- **Guidelines**: Celebrate success, confirm details, set expectations. Achievement first, then possibilities.
- **Avoid**: Bland confirmations, missing key details, immediate pressure

---

## 3. ONBOARDING SCENARIO

### Buttons and CTAs

- **Tone**: Supportive, motivating
- **Voice Application**: Supportive CTAs that reduce barriers. Smart onboarding that feels personal.
- **Character Range**: 10-25
- **Examples**: Get Started | Tell Us Your Goals | Continue Setup
- **Guidelines**: Gentle guidance, personal focus. Encouraging without pressure.
- **Avoid**: Demanding tone, complex requests, high-pressure tactics

### Headers

- **Tone**: Friendly, inviting, clear
- **Voice Application**: Smart welcome that builds confidence. Clear journey mapping.
- **Examples**: Welcome to Volt | Let's Build Your Future | Setup Your Profile
- **Character Range**: 20-45
- **Guidelines**: Welcoming, journey-focused, encouraging. Set positive expectations.
- **Avoid**: Overwhelming information, complex terms, assumption of knowledge

### Sub-headers

- **Tone**: Quick benefit, simple action
- **Voice Application**: Smart benefit communication. Supportive time estimates that reduce anxiety.
- **Examples**: Grow your wealth safely and smartly | This takes less than 3 minutes
- **Character Range**: 25-60
- **Guidelines**: Brief intro/benefit, then time expectation. Remove barriers to entry.
- **Avoid**: Complex promises, overwhelming detail, unrealistic timelines

### Descriptions

- **Tone**: Brief intro/benefit, then explanation. No jargon
- **Voice Application**: Smart introduction to value. Supportive explanation that builds confidence.
- **Examples**: Build your financial future with Volt. We make investing accessible and easy to understand, starting with just ₹100.
- **Character Range**: 50-120
- **Guidelines**: Reassuring, educational, removes barriers. Benefit first, then how.
- **Avoid**: Assumptions about knowledge, overwhelming detail, jargon without explanation

---

## 4. PROCESS SCENARIO

### Buttons and CTAs

- **Tone**: Clear, supportive
- **Voice Application**: Smart CTAs that maintain momentum. Supportive guidance through complex processes.
- **Examples**: Continue | Verify Now | Upload Documents | Complete Setup
- **Character Range**: 10-25
- **Guidelines**: Clear action for each step. Supportive progression through process.
- **Avoid**: Vague actions, overwhelming next steps, technical terms

### Headers

- **Tone**: Specific, step-oriented
- **Voice Application**: Smart step identification. Clear communication of progress.
- **Examples**: Increase Your Limit | Verify Your Identity | Upload Documents
- **Character Range**: 15-40
- **Guidelines**: Clear about current step. Action-oriented without pressure.
- **Avoid**: Vague processes, overwhelming information, technical steps

### Sub-headers

- **Tone**: Calm instruction, hint at next step
- **Voice Application**: Supportive progress tracking. Smart time estimates that reduce anxiety.
- **Examples**: Step 2 of 5: Verify your PAN | This usually takes under 2 minutes
- **Character Range**: 25-60
- **Guidelines**: Show progress, set time expectations. Calm reassurance about process.
- **Avoid**: Overwhelming steps, unclear progress, unrealistic timelines

### Descriptions

- **Tone**: Step 1 first. Clear instructions. Less is more, but offer details
- **Voice Application**: Smart explanation of requirements. Supportive guidance through each step.
- **Examples**: To increase your limit, we need to verify your PAN. Enter your details below and we'll process it instantly.
- **Character Range**: 50-120
- **Guidelines**: Clear reason for step, simple instructions. Support available if needed.
- **Avoid**: Complex requirements, overwhelming detail, hidden reasons

---

## 5. EDUCATIONAL SCENARIO

### Buttons and CTAs

- **Tone**: Relevant, clear
- **Voice Application**: Supportive learning CTAs. Smart optional depth for different knowledge levels.
- **Examples**: Learn More | Got It | See Example
- **Character Range**: 8-20
- **Guidelines**: Clear learning actions. Optional depth without pressure.
- **Avoid**: Forced learning, overwhelming options, technical progression

### Headers

- **Tone**: Direct, clear
- **Voice Application**: Smart topic identification. Clear educational focus that welcomes all knowledge levels.
- **Examples**: What is Foreclosure? | Understanding Interest Rates | How Limits Work
- **Character Range**: 15-45
- **Guidelines**: Clear question or topic. Direct and approachable language.
- **Avoid**: Overwhelming topics, assumption of knowledge, intimidating language

### Sub-headers

- **Tone**: Supportive, context if needed
- **Voice Application**: Supportive framing that reduces learning anxiety. Smart complexity communication.
- **Examples**: Understanding your options | The basics explained simply
- **Character Range**: 20-50
- **Guidelines**: Set expectation for learning level. Reassuring about complexity.
- **Avoid**: Intimidating framing, assumption of prior knowledge, overwhelming scope

### Descriptions

- **Tone**: State answer/definition first, then break down the 'why'
- **Voice Application**: Smart educational structure. Supportive learning that builds from basics.
- **Examples**: Foreclosure lets you pay off your loan early and save on interest. Here's when it makes sense and how to do it step-by-step.
- **Character Range**: 50-150
- **Guidelines**: Clear definition first, then practical application. No jargon without explanation.
- **Avoid**: Complex theory first, unexplained jargon, overwhelming detail

---

## 6. FEATURE EXPLANATION SCENARIO

### Buttons and CTAs

- **Tone**: Smart, actionable
- **Voice Application**: Smart CTAs that highlight feature value. Supportive encouragement to try.
- **Character Range**: 10-25
- **Examples**: Try Feature | Unlock Now | Calculate Interest | Unpledge Funds
- **Guidelines**: Clear action, benefit-implied. Encouraging trial without pressure.
- **Avoid**: Pushy language, overwhelming features, unclear benefits

### Headers

- **Tone**: Clear, benefit-first
- **Voice Application**: Smart benefit communication. Clear feature value that connects to user needs.
- **Examples**: Unpledge Funds Easily | Calculate Your Interest | Unlock Higher Limits
- **Character Range**: 20-50
- **Guidelines**: Lead with benefit or outcome. Clear value proposition.
- **Avoid**: Technical feature names, vague benefits, overwhelming capabilities

### Sub-headers

- **Tone**: Descriptive, reinforces use
- **Voice Application**: Supportive benefit reinforcement. Smart outcome communication that motivates use.
- **Character Range**: 30-70
- **Guidelines**: Specific benefit or outcome. Reinforces practical use case.
- **Examples**: Get access to your money anytime | See exactly what you'll save | Up to ₹5Cr available instantly
- **Avoid**: Vague benefits, technical descriptions, unrealistic promises

### Descriptions

- **Tone**: What/why first, how/when next. Emphasize simplicity and user benefit
- **Voice Application**: Smart feature explanation that emphasizes user control. Supportive simplicity communication.
- **Examples**: Unpledge your funds instantly when you need cash. No hassle, no long waits - your money is ready when you are.
- **Character Range**: 50-120
- **Guidelines**: Clear benefit first, then ease of use. Practical application focus.
- **Avoid**: Technical explanations first, complex processes, hidden limitations

---

## 7. LEGAL, COMPLIANCE AND CONSENT COPY

### Descriptions (Detailed, Inverted Pyramid)

- **Tone**: Clear, Calm, Smart, Supportive
- **Voice Application**: Calms concerns by being explicit, supportive, and precise.
- **Character Range**: 50-120
- **Guidelines**:
    - Always make the action and parties clear (“by proceeding”, “I accept”, “I authorize sharing KYC with ___”).
    - Avoid dense or ambiguous language.
    - Pair every action with a visible path to review “T&C”, “Privacy Policy”, or “Learn more”.
- **Examples**:
    - By proceeding, you accept the T&C and Privacy Policy.
    - By continuing, you authorize sharing KYC with DSP Finance Pvt. Ltd.
    - By submitting, I allow Volt to process my identity documents.
    - I agree to the processing of my information by Volt.
- **Avoid**: Dense blocks of legal text, ambiguous conditions, confusing disclaimers.