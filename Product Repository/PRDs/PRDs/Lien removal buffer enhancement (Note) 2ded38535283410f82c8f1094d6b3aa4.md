# Lien removal buffer enhancement (Note)

: Vaibhav Arora
Created time: August 10, 2024 2:16 PM
Status: Not started
Last edited: August 10, 2024 3:51 PM

[Bajaj buffer handling for lien removal](https://app.notion.com/p/Bajaj-buffer-handling-for-lien-removal-90fa191a67ec4f38b2bff1cfe6d99a98?pvs=21)

For Bajaj, we had placed a buffer of 5% on total outstanding when users raise collateral removal requests to handle NAV changes. Collateral removal requests take 1-2 working days to be processed by the lender and hence to ensure requests are not cancelled this buffer is maintained.

Due to high volatility in markets our requests are still getting rejected despite the 5% buffer. We need to solve for the cancellations. 

One proposed method by the business team is to increase the buffer to 10% however that impacts customer experience. Need solutioning for the same.