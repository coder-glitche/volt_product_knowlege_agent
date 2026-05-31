# MFD Login data

"total_partner_users": 77588,
"never_logged_in": 12310,
"first_login_mobile": 4978,
"first_login_web": 31789,
"first_login_other": 28511,
"total_mobile_users": 24608,
"total_web_users": 37813,
"used_both_platforms": 21165,
"used_only_other_platforms": 24028,
"never_logged_in_percent": 15.87,
"mobile_adoption_percent": 31.72,
"web_adoption_percent": 48.74,
"both_platforms_percent": 27.28

query 

```jsx
WITH first_logins AS (
    SELECT 
        user_id,
        MIN(created_date_time) as first_login_date,
        -- Get the platform of their first login
        platform as first_platform
    FROM user_login_audits
    WHERE created_date_time = (
        SELECT MIN(created_date_time)
        FROM user_login_audits ua2 
        WHERE ua2.user_id = user_login_audits.user_id
    )
    GROUP BY user_id, platform
),
platform_usage AS (
    SELECT DISTINCT
        rutpm.user_id,
        fl.first_login_date,
        fl.first_platform,
        CASE 
            WHEN EXISTS (SELECT 1 FROM user_login_audits ua 
                        WHERE ua.user_id = rutpm.user_id 
                        AND ua.platform = 'VOLT_MOBILE_APP') THEN 1 
            ELSE 0 
        END as has_used_mobile,
        CASE 
            WHEN EXISTS (SELECT 1 FROM user_login_audits ua 
                        WHERE ua.user_id = rutpm.user_id 
                        AND ua.platform = 'VOLT_WEB_APP') THEN 1 
            ELSE 0 
        END as has_used_web
    FROM relationship_user_to_partner_main rutpm
    LEFT JOIN first_logins fl ON rutpm.user_id = fl.user_id
)
SELECT 
    -- Total Users with Partners
    COUNT(*) as total_partner_users,
    
    -- Users who have never logged in
    COUNT(CASE WHEN first_login_date IS NULL THEN 1 END) as never_logged_in,
    
    -- First Platform Distribution
    COUNT(CASE WHEN first_platform = 'VOLT_MOBILE_APP' THEN 1 END) as first_login_mobile,
    COUNT(CASE WHEN first_platform = 'VOLT_WEB_APP' THEN 1 END) as first_login_web,
    COUNT(CASE WHEN first_platform NOT IN ('VOLT_MOBILE_APP', 'VOLT_WEB_APP') 
               AND first_platform IS NOT NULL THEN 1 END) as first_login_other,
    
    -- Platform Usage Distribution
    COUNT(CASE WHEN has_used_mobile = 1 THEN 1 END) as total_mobile_users,
    COUNT(CASE WHEN has_used_web = 1 THEN 1 END) as total_web_users,
    COUNT(CASE WHEN has_used_mobile = 1 AND has_used_web = 1 THEN 1 END) as used_both_platforms,
    COUNT(CASE WHEN has_used_mobile = 0 AND has_used_web = 0 
               AND first_login_date IS NOT NULL THEN 1 END) as used_only_other_platforms,
    
    -- Calculate percentages
    ROUND(100.0 * COUNT(CASE WHEN first_login_date IS NULL THEN 1 END)::numeric / COUNT(*), 2) as never_logged_in_percent,
    ROUND(100.0 * COUNT(CASE WHEN has_used_mobile = 1 THEN 1 END)::numeric / COUNT(*), 2) as mobile_adoption_percent,
    ROUND(100.0 * COUNT(CASE WHEN has_used_web = 1 THEN 1 END)::numeric / COUNT(*), 2) as web_adoption_percent,
    ROUND(100.0 * COUNT(CASE WHEN has_used_mobile = 1 AND has_used_web = 1 THEN 1 END)::numeric / COUNT(*), 2) as both_platforms_percent
FROM platform_usage;

```

---

**Subject:** Empanelment Funnel & Landing Page Data (/partner)

Hi Shivansh,

Here’s the data for the initial landing page views of **/partner** and the subsequent steps in the empanelment journey.

**Limitations:**

- This data is for the **first two weeks of April** only.
- Note: `/signup` and `/signup/` both refer to the empanelment flow.

---

**Page Views (Apr 1–14, from Google Analytics)**

| Page URL | Unique Visitors |
| --- | --- |
| /partner | 1,026 |
| /partner/signup | 1,563 |
| /partner/signup/ | 2,413 |

---

**Funnel Data (April, from DB)**

| Step | Count |
| --- | --- |
| Partner created (OTP verified) | 800 |
| Email provided | 474 |
| Name provided | 473 |
| ARN provided | 281 |
| PAN provided (not asked in flow) | 173 |
| Partial activated | 215 |
| Fully activated | 141 |

Let me know if you need a comparison with past months or a visual funnel summary.

Best,

Naman

---

Want me to combine this with the Android app usage data into a summary report or deck slide for easier review?