# Product Note : Post limit fetch optimisation

# Objective

- This is **post-credit limit fetch, pre-KYC**.
- User already knows eligibility → now reviewing loan terms.
- Goal: Maximise conversion from this page to KYC initiation.

# Current journey

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image.png)

# Funnel metrics

## Overall Funnel [Only Eligible Users]

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%201.png)

## First time success rate

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%202.png)

## Median time to convert of overall funnel

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%203.png)

## P75t and P90th conversion time

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%204.png)

## MF Fetch Anchor Page Analysis

## Median time to convert from step 1 to 2

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%205.png)

### No. of users who clicked on ‘Mutual Funds Fetched Card’

In LOS i.e new users

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%206.png)

In LOS + LMS combined

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%207.png)

### No. of users to clicked on back button after being eligible

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%208.png)

-

### No. of users to clicked on back from ‘fetched mutual funds page’

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%209.png)

### No. of users who clicked on refresh portfolio from ‘fetched mutual funds page’

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2010.png)

### No. of users who refreshed portfolio from ‘fetched mutual funds page’ and moved ahead to set credit limit and loan offer

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2011.png)

### Refresh portfolio on MFC Anchor page

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2012.png)

## Set Credit Limit Page Analysis

## Median time to convert from step 2 to 3

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2013.png)

## No of users who clicked on edit limit pencil icon

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2014.png)

## Loan Offer Page Analysis

## Median time to convert from step 3 to 4

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2015.png)

### Loan offer page CTA clicked

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2016.png)

### No. of users who clicked prepayment expanded

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2017.png)

### No. of users who clicked withdrawal and repayment expanded

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2018.png)

### No. of users who clicked charges expanded

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2019.png)

### No. of users who clicked info icon on loan tenure

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2020.png)

### No. of users who clicked info icon on interest rate

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2021.png)

### No. of users who clicked info icon on credit limit

![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2022.png)

## WATI Chats queries

[https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system)

---

# Insights

**Step 1 → Step 2 (Eligibility → Credit Limit) is the biggest drop off point**.

- Users get eligibility but hesitate at credit limit setup
- Around 28% of the users who land on the anchor page go and click ‘fetched mutual funds’ button to view their mutual funds.
    - Image
        
        ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2023.png)
        
- Rest refresh portfolio(~6-7%) and some hit back button.
- While median conversion time of the entire funnel is ~1min, p75th and p90th conversion time is anywhere from 1hr to 14hrs

**Possible reasons of the drop-offs**

- WATI chats show users asking questions like what is the interest rate, why is my portfolio amount less, what are the charges, what will the EMI be? this shows we need to communicate at least the following this more clearly on this page
- Non-eligible funds
- Clarity on how the credit line is calculated.
- Understanding on how the repayment of the loan is expected. EMI-Free is one way to do this since most folks understand personal loans better.
- Quotes ”This matches the WATI queries about *“Why only 25k shown?”*, *“What are charges?”*, *“Explain EMI”*

**First time success rate is not great**

- For **first-time users**, leakage is **higher** — nearly 2 out of 3 drop before reaching loan offer.~35%
- No of people who visit page more than 1nce is more than please who visit is once.
- 23% visit is once others visit it more than once.

# Data Summary

1. Overall conversion rate is ~50% (Across Channels) with the highest drop is the first 2 steps. 
2. First time success rate is around 36%, However a chunk of remaining users visit the page multiple times and with every consecutive visit has a higher chance of converting
3. While median conversion time of the entire funnel is ~1min, p75th and p90th conversion time is anywhere from 1-2hrs.
4. Based on WATI chats most users expected to see a solid EMI(Saying things like, How much EMI will get cut), Details of interest rate, and How much was processing fees. This could be because we don’t show these details until loan offer page. 
5. Around 28% of the users who land on the anchor page go and click ‘fetched mutual funds’ button to view their mutual funds. 
6. If users visit the ‘fetched mutual funds page’ their conversion reduces by 50% to ‘Set credit limit page’. 
7. Out of the 100% of **New Users** who land of Loan Offer Page, 34% go to check fetched mutual funds, 18% these users end up clicking of set credit limit.  

# Hypothesis

- Users drop off when they don’t see their entire portfolio value.
- Users don’t understand the ‘Flexi repay’ construct of this loan type.
    - They have questions around EMI which shows that we need to explain this better.
- Users show a lack of trust, hesitation combined with concern about what will happen to the their mutual funds.
    - As communicated through calls made, their questions are around will the mutual funds be locked, and stop growing.
- Users compare other loans with us
    - Power users compare loans, illustrated by the fact that they ask about interest rates and visit the app multiple times.
- The final leg of the process after fetch limit is not clear and concise
    - The users spend 8 secs on the Anchor Page, followed by a median time of ~14-16s on Set credit limit page, and 20s on the loan offer page.
    - This is also corroborated by the fact that they have asked supporting questions on Wati, although the data is available on the page which include process fee and interest rates.
- To be Verified
    - Users don’t understand the process of fetching funds and often get confused about the limit that they have received (To be Verified)
        - Showcased by the fact that a lot of people visit FAQs to learn about the 45% LTV ratio
    - Users may recognise the funds they own but not remember exact values. Showing mutual fund **logos** adds instant **visual confirmation**, making it easier to differentiate funds, improving **scannability**. As a result, users are likely to **spend less time hunting for details**, leading to a faster experience.