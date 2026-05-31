# Check eligibility overhaul

# **What problem are we solving?**

In context of Check limit page we are solving the following problems

1. UI/UX Problems: 
    1. CTA copy signifies that this is an eligibility test which means not everyone is eligible for loan. 
    2. The main headline occupies too much space. Pushes the form down and deviates user attention from the form. The current headline conveys very little. 
    3. Too much space on the main scroll is left unused. Nothing except the form and headline is visible in the first fold. Pushes trust markers and education content down. 
    4. CTAs that are of now use to user at this stage populate the header and confuse the user. 
    5. Overall space utilisation on the page is unoptimised. Blank spaces + images occupying to much space. 
    6. Submission of PAN upfront is problematic because of the following reasons:
        1. Users are uncomfortable sharing both phone number and PAN at once. 
        2. PAN is not that accessible for all users and may lead to the user dropping off before us capturing a lead.
    7. Form needs various UI + copy fixes. 
    8. Post limit check information on how the limit is calculated given can be made better.  
    9. Post limit check users have surface level understanding of what part of their portfolio is eligible. No fund level information is available. (Check analytics - Before vs After)
    10. User have no visibility on how much their interest only EMI will be.
    11. For cases where the user has no/insufficient portfolio there should be no continue CTA. 
    12. The progress bar says that this may take upto 20 seconds which is not inline with the 15 seconds claim prior. 
2. Education Problems:
    1. We do not educate the user on what exactly is LAMF. Embedded video and written material that explains key concepts like interest only EMI, OD, etc is missing. 
    2. Content that eases user anxiety regarding what will happen to you mutual funds throughout the process is missing. 
    3. Comparisons with other products/players is not available. Why Volt communication can be made better with the comparisons.  
    4. Few use cases where LAMF makes sense aren’t available right now. 
3. Absence of adequate trust markers:
    1. Current trust markers very generic and most users might not understand them. 
    2. No social proofing. No testament of scale. 
    3. On desktop no space that shows that we have highly rated apps on Android and App store. On mobile web view even though the download button is there, high app ratings is missing. App rating is extremely important trust marker. (Source: Tushar’s LLA call insights)
    4. Press trust markers don’t have hyperlink on the icon so that the user can go and check the article themselves. 
4. Absence of tools that can engage users: 
    1. Tools to engage users and make decision such as sell vs lien calculator (regret calculator is missing).
    2. Slider for understanding OD. Pay interest on only what you withdraw.

---

# **How do we measure success?**

---

# **How are others solving this problem?**

### Benchmarking discussions:

1. Finzzy LAMF landing page: 
    1. Video on the landing page to explain 

---

# **What is the solution?**

## Preliminary solutions

| Problem | Possible solutions | Impact | Effort | Priority |
| --- | --- | --- | --- | --- |
| 1.a | - Change the copy to something that signifies limit check over eligibility, is more contextual, and let go of in 15s. Few options are:
  1. Calculate your credit limit
  2. Find your credit limit (smallcase)
  3. Discover your credit limit
 | Medium | Low |  |
| 1.b | - Make the heading smaller. 
- Change the copy. Current copy has two parts, following is the problem with each of them. 
  1. Get loan against mutual funds: Loan focus should be downplayed, put focus on mf is not sold. 
  2. Free eligibility check in 15 seconds: Free taken from Free credit score check but the case is completely different for us. This info can be given in the form only to avoid repetition. 
  Heading copy suggestions: 
   1. Unlock cash against your mutual funds without selling them! 
   2. Cash-in your mutual funds without selling them! 
   3. Access cash against your mutual funds without selling them!  | Medium | Low |  |
| 1.c | - Make the form smaller to make way for Interest comparison as ROI is the main comparison metric (Source: Tushar’s LLA calls) | High | Medium |  |
| 1.d | - On desktop view: Remove check eligibility in 15s from top menu. Move all the other existing CTA except sign in to a hamburger menu (Or remove them). Introduce CTAs like “What is LAMF?”, “Why Volt?”, “Redeem vs Volt calculator”
- On Mobile view only Download app CTA should be there along with hamburger menu filled with same suggested CTAs as above.  | High | Medium |  |
| 1.f | - Separate the mobile number submission and PAN submission step. It should solve the following problems:
  1. Phone number as verification step and PAN to fetch portfolio might make the completion look easier, OTP on both stages might make the user feel more secure. 
  2. Users who drop off with just the phone number will be captured as leads.  | Very high | High |  |
| 1.g | - Remove the box and free float the components on web page.
- Change the copy of the form title (Which will act as the sub-heading to the headline) to “Calculate your credit limit in 15 seconds”. 
- Other UI changes | Medium | High |  |
| 1.h | - Point wise + with example explanation similar to smallcase. 
How is the credit limit calculated?
One can avail upto
- 75% of the net asset value for debt mutual funds
- 45% of the net asset value for equity mutual funds
Lets say you have ₹2L in debt fund and ₹1L in equity funds. Your eligible loan amount will be
= (0.75 × ₹2L) + (0.45 × ₹1L)
= ₹1.95L
While the above holds true for most funds, the loan to value percentage can sometimes vary scheme wise.
Only non demat mutual funds are supported for a loan at this moment.
The loan amount might get lowered during the application in case you have the following
- Investments in mutual funds blacklisted by the lender/AMC
- Mutual funds that are currently pledged
- Mutual funds held in a demat account
- ELSS funds that are currently locked in | High | Low |  |
| 1.i | A version of this was previously there, discuss on why it was removed.  |  |  |  |
| 1.j | - Post limit check, show the EMI for 100% utilization. This will help users in understanding the construct of interest only EMIs.  | High | Low |  |
| 1.k | - CTA should be changes to “Understood” or “Got it”.  | Low | Low |  |
| 2.a | - Easy explanation of what is LAMF through as many visuals as possible link snippets of content from previous explanations from creators and old + new blogs for understanding of different components of LAMF. This will also help with secondary research input as users see atleast two videos before forming a opinion. (Source: Tushar’s LLA call insights) | Very high | High |  |
| 2.b | - Create process of applying for LAMF with special emphasis on how their MFs are safe. These videos/blogs should not take user away from the page. | High | High |  |
| 2.c | - Content for LAMF vs Personal loan, LAMF vs Business loan, LAMF vs Gold loan etc.  | High | High |  |
| 2.d | - Use cases where LAMF makes most sense can be listed in a section. Example include, business capital, house renovation, etc. A good example of a direct competitor is [https://finezzy.com/loan-against-mutual-funds/](https://finezzy.com/loan-against-mutual-funds/) | Medium | Low |  |
| 3.a | - Influencers act as better trust markers than CAMS, KFIN etc. Take snippet from what they said about volt along with their subscribers/views across YT and other platforms.  | Very high | Low |  |
| 3.b | - Social proofing should be used both in the form and as a separate section. 
  In form and journey:
  1. Below PAN input box: 2345 users have checked their credit limit in last 24 hours. 
  2. During MFC fetching: Volt money AUM crossed Xcr+ in Feb 2024, Y+ Users have pledged Rs.z+ worth of MFs with Volt, etc. 
  A section on testament of scale: Key metrics like AUM, loan disbursed, etc can be shown in this particular section.  | Very high | Medium |  |
| 3.c | - Current homepage section of app download actually looks fine except for no mention of app ratings. Add app ratings, optimize copy and that can be used as a section. 
- Add app rating in the download CTA. | High | Low |  |
| 3.d | - Link the particular links of media with the logo of publishers. | Low | Low |  |
| 4.a | - A sample tool has been created here: https://docs.google.com/spreadsheets/d/1xZxkhUo9XP3KawyFkWMsNWGsgw0bLfVxMWXjAW84L-E/edit?usp=sharing | High | Medium |  |
| 4.b | - A simple slider, along with changing instalment amount can be made.  | High | Low |  |

## Requirements overview (optional)

## User stories / User flow

## Requirements

---

# **Design**

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

Should we make an influencer specific version? This will solve for user’s trust as influencer endorsement is a major trust marker. (As per Tushar’s LLA calls). I have seen this in places like [https://surfshark.com/influencer/mrwhosethebosshttps://surfshark.com/influencer/mrwhosetheboss](https://surfshark.com/influencer/mrwhosetheboss)

Can we have a time specific reward from influencer or will that be overkill? The landing page will have a timer as well. This will ensure that more users activate the credit limit right now, might use later.

Should we revamp the landing page itself and make check eligibility a pop up like small case is currently doing?