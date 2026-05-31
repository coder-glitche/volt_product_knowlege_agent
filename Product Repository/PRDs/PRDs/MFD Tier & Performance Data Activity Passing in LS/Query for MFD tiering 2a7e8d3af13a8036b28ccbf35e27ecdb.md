# Query for MFD tiering:

WITH partnet_cte AS (
SELECT
vdl_audit_partneraccounts.accountid AS partner_account_id,
max(NULLIF(partnername,'nan')) as partner_name,
MAX(NULLIF(accountholderphonenumber,'nan')) AS partner_phone_number,
MAX( COALESCE(NULLIF(accountholderphonenumber, 'nan'),NULLIF(pa_sub.pa_alt_phonenumber, 'nan'))) AS partner_phone_number,
max(case when address = 'nan' then null else json_extract_scalar(REPLACE(address, '''', '"'), '$.city') end) as partner_city,
MAX(partnercode) AS partnercode,
MAX(CASE
WHEN partnerprofiledetails IS NOT NULL
THEN json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.arnNo')
END) AS partner_arn,
MAX(CASE
WHEN partnerprofiledetails IS NOT NULL
THEN json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.companyName')
END) AS companyName,
MAX(NULLIF(accountholderemail,'nan')) AS partner_email,
MIN(CASE
WHEN lastupdatedtimestamp LIKE '%Z' THEN
cast(from_iso8601_timestamp(lastupdatedtimestamp) as TIMESTAMP)
ELSE
CAST(lastupdatedtimestamp AS TIMESTAMP)
END) + INTERVAL '330' MINUTE AS registered_date,
MIN(
CASE
WHEN accountholderemail IS NOT NULL THEN
CASE
WHEN lastupdatedtimestamp LIKE '%Z' THEN
cast(from_iso8601_timestamp(lastupdatedtimestamp) as TIMESTAMP)
ELSE
CAST(lastupdatedtimestamp AS TIMESTAMP)
END
END
)+ INTERVAL '330' MINUTE AS emplanelement_date
FROM "volt-audit-data-lake"."vdl_audit_partneraccounts"
left join (select accountid,coalesce(accountholderphonenumber,json_extract_scalar(partnerprofiledetails, '$.partnerAlternateMobileNumber')) as pa_alt_phonenumber from "volt-data-lake"."vdl_partneraccounts") pa_sub on pa_sub.accountid = vdl_audit_partneraccounts.accountid
GROUP BY vdl_audit_partneraccounts.accountid

UNION

- - PART 2: From Partner Table not present in Audit
SELECT
partner.accountid AS partner_account_id,
NULLIF(partnername, 'nan') AS partner_name,
COALESCE(NULLIF(accountholderphonenumber, 'nan'), json_extract_scalar(partnerprofiledetails, '$.partnerAlternateMobileNumber')) AS partner_phone_number,
json_extract_scalar(REPLACE(address, '''', '"'), '$.city') as partner_city,
partnercode,
json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.arnNo') AS partner_arn,
json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.companyName') AS companyName,
NULLIF(accountholderemail, 'nan') AS partner_email,
(
CASE
WHEN lastupdatedtimestamp LIKE '%Z' THEN cast(from_iso8601_timestamp(lastupdatedtimestamp) AS TIMESTAMP)
ELSE CAST(lastupdatedtimestamp AS TIMESTAMP)
END
) + INTERVAL '330' MINUTE AS registered_date,
(
CASE
WHEN accountholderemail IS NOT NULL THEN
CASE
WHEN lastupdatedtimestamp LIKE '%Z' THEN cast(from_iso8601_timestamp(lastupdatedtimestamp) AS TIMESTAMP)
ELSE CAST(lastupdatedtimestamp AS TIMESTAMP)
END
END
) + INTERVAL '330' MINUTE AS emplanelement_date
FROM "volt-data-lake"."vdl_partneraccounts" partner
LEFT JOIN (
SELECT DISTINCT accountid
FROM "volt-audit-data-lake"."vdl_audit_partneraccounts"
) audit_check
ON partner.accountid = audit_check.accountid
WHERE audit_check.accountid IS NULL
),
customer_cte AS (
select partner_account_id,date(first_created_on) as partner_active_date_application_first_created_on,partner_partially_active_date,partner_active_date,dhanda_activity_date from (
SELECT
partner_account_id,
first_created_on,
MIN(date(first_created_on)) OVER (PARTITION BY partner_account_id) AS partner_partially_active_date,
MIN(date(completed_on)) OVER (PARTITION BY partner_account_id) AS partner_active_date,
MAX(date(completed_on)) OVER (PARTITION BY partner_account_id) AS dhanda_activity_date,
ROW_NUMBER() OVER (PARTITION BY partner_account_id ORDER BY completed_on ASC) AS rn
FROM "volt-analytics"."primary_application_full_info"
-- WHERE partner_account_id = '072f9922-abe0-4c79-9883-1b26044767b8'
) sub
where rn=1
),
partner_customer_detail_cte as (
select count(distinct application_id) as total_no_of_completed_applications,sum(app_pledged_credit_limit) as toal_pledged_credit_limit,partner_account_id,max(business_channel) as business_channel ,max(operating_channel) as operating_channel,max(platform_name) as platform_name from "volt-analytics"."primary_application_full_info" where current_step_id='COMPLETED'
group by partner_account_id
),
final_cte as (
select p.*,
c.partner_active_date_application_first_created_on,
c.partner_partially_active_date,
c.partner_active_date,
c.dhanda_activity_date,
pc.total_no_of_completed_applications,
pc.toal_pledged_credit_limit,
pc.business_channel,
pc.operating_channel,
pc.platform_name
from partnet_cte p left join customer_cte c on p.partner_account_id=c.partner_account_id
left join partner_customer_detail_cte pc on p.partner_account_id=pc.partner_account_id
),
volt_cte as (
select *,CASE
WHEN percentile_completed_cases <= 0.10 -- and percentile_pledged_limit <= 0.10
THEN 'Super Gold'
WHEN percentile_completed_cases > 0.10 and percentile_completed_cases <= 0.22
OR percentile_pledged_limit > 0.10 and percentile_pledged_limit <= 0.22
THEN 'Gold'
WHEN percentile_completed_cases > 0.22 and percentile_completed_cases <= 0.40
OR percentile_pledged_limit > 0.22 and percentile_pledged_limit <= 0.40
THEN 'Silver'
ELSE 'Bronze'
END AS tier
from (select *,
PERCENT_RANK() OVER (ORDER BY total_no_of_completed_applications DESC) AS percentile_completed_cases,
PERCENT_RANK() OVER (ORDER BY toal_pledged_credit_limit DESC) AS percentile_pledged_limit
from final_cte
where business_channel='B2B2C'
and operating_channel ='MFD_Direct'
) volt_sub
),
redvision_cte as (
select *,CASE
WHEN percentile_completed_cases <= 0.10 -- and percentile_pledged_limit <= 0.10
THEN 'Super Gold'
WHEN percentile_completed_cases > 0.10 and percentile_completed_cases <= 0.22
OR percentile_pledged_limit > 0.10 and percentile_pledged_limit <= 0.22
THEN 'Gold'
WHEN percentile_completed_cases > 0.22 and percentile_completed_cases <= 0.40
OR percentile_pledged_limit > 0.22 and percentile_pledged_limit <= 0.40
THEN 'Silver'
ELSE 'Bronze'
END AS tier
from (select *,
PERCENT_RANK() OVER (ORDER BY total_no_of_completed_applications DESC) AS percentile_completed_cases,
PERCENT_RANK() OVER (ORDER BY toal_pledged_credit_limit DESC) AS percentile_pledged_limit
from final_cte
where business_channel='B2B2C'
and platform_name ='Redvision Technologies') red_sub
),
investwell_cte as (
select *,CASE
WHEN percentile_completed_cases <= 0.10 -- and percentile_pledged_limit <= 0.10
THEN 'Super Gold'
WHEN percentile_completed_cases > 0.10 and percentile_completed_cases <= 0.22
OR percentile_pledged_limit > 0.10 and percentile_pledged_limit <= 0.22
THEN 'Gold'
WHEN percentile_completed_cases > 0.22 and percentile_completed_cases <= 0.40
OR percentile_pledged_limit > 0.22 and percentile_pledged_limit <= 0.40
THEN 'Silver'
ELSE 'Bronze'
END AS tier
from (select *,
PERCENT_RANK() OVER (ORDER BY total_no_of_completed_applications DESC) AS percentile_completed_cases,
PERCENT_RANK() OVER (ORDER BY toal_pledged_credit_limit DESC) AS percentile_pledged_limit
from final_cte
where business_channel='B2B2C'
and platform_name ='Investwell SDK') invest_sub
),
union_cte as (
select * from volt_cte
union all
select * from redvision_cte
union all
select * from investwell_cte
)select * from union_cte