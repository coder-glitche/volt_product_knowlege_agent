# Analytics requirement: Repayment

|  | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Number of repayments | (count of total repayments made today) |  |  |  |  |  |  |  |  |
| Number of transactions automatically settled | (count of repayments made and settled today) | yesterday |  |  |  |  |  |  |  |
| Number of transactions pending settlement | (Count of repayments made today but pending settlement) |  |  |  |  |  |  |  |  |
| Average settlement TAT | For payments settled today avg(settled_on - created_on) - difference of hours |  |  |  |  |  |  |  |  |
| % repayments settled automatically | % of payments that were settled automatically today (identify payments settled manually via admin action) |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |

## Tables and Important fields:

### Table:

Credits.default.collections

### Field:

Collections: created_on - When payment was created

Collections: settled_on - When payment was settled automatically

Payment_status (If equals to settled - payment was settled either using admin action or automatically)

### Table:

admin_action_audit (Credits)

admin action name: UPDATE_COLLECTION_STATUS

To identify which collections were settled manually

Format: Email with CSV attached

Sample query:

```sql
SELECT CAST(collections.created_on AS DATE) as transaction_date,collection_status,count(*)
FROM collections 
LEFT JOIN credits ON collections.credit_id = credits.credit_id
WHERE lending_partner_id = 'Bajaj'
  AND CAST(collections.created_on AS DATE) <= current_date - INTERVAL '2' DAY
  AND CAST(collections.created_on AS DATE) >= current_date - INTERVAL '30' DAY
  AND collection_status not in ('REQUESTED','CANCELLED','FAILED')
group by collection_status,CAST(collections.created_on AS DATE)
order by 1,2
```

Recipients:

@Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava