# Analytics Requirement: Name verification (TCL)

Query 1: (errors consolidation, distributed by providor)

Total applications initiated (unique)

Total 

Query 2: (Success rate 7 day window distributed by providor)

```jsx
select *,total_attempts/unique_attempts as number_of_attempts_per_user,
(successful_attempts*100)/unique_attempts AS success_rate_perc
from (select 'Digio' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts,
count(distinct(application_id)) as unique_attempts,
count(distinct(case when umrn is not null then application_id else null end)) as successful_attempts

from (select application_id,
bank_account_number,
created_date_time,
bank_ifsc_code,
umrn,
JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') AS npci_auth_failed_error,
JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') AS npci_auth_reject_reason,
CASE 
    WHEN umrn IS NOT NULL THEN 'COMPLETED'
    WHEN (
        JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') IS NOT NULL 
        OR JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') IS NOT NULL
    ) THEN 'FAILED'
    ELSE 'INVALID_REQUEST'
END AS status_mandate
from "credit_applications_data_audit_digio_mandate_sign" 
WHERE date(created_date_time) > date_add('day', -6, current_date)
) t 
group by date(created_date_time)

UNION ALL

select 
'Tata' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts,
count(distinct(application_id)) as unique_attempts,
count(distinct(case when status='Completed' then application_id else null end)) as successful_attempts

from (select application_id,
created_date_time,
bank_account_number,
bank_ifsc_code,
case when mandate_status='Finished' then 'Completed' else 'Failed' end as status,
JSON_EXTRACT(tata_mandate_data, '$.emandate_error_message') AS emandate_error_message,
JSON_EXTRACT(tata_mandate_data, '$.emandate_status') AS emandate_status
from "credit_applications_data_audit_tata_mandate"
where date(created_date_time) > date_add('day', -6, current_date)
and mandate_status!='In Progress'
) t2
group by date(created_date_time)

order by 2) ramesh
```

Format: Email with CSV attached

Recipients:

@Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava