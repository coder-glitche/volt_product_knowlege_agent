# Analytics requirement: Foreclosure

|  | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Number of foreclosure requests | (count of total requests made today) |  |  |  |  |  |  |  |  |
| Number of requests automatically closed | (count of requests made and closed today) |  |  |  |  |  |  |  |  |
| Number of requests pending closure | (Count of requests made today but pending closure) |  |  |  |  |  |  |  |  |
|  | **Today** | **This week** | **This month** |  |  |  |  |  |  |
| Average closure TAT | For requests closed today avg(settled_on - created_on) |  |  |  |  |  |  |  |  |
| % requests closed automatically | % of requests that were closed automatically today (identify requests closed manually via admin action) |  |  |  |  |  |  |  |  |

## Tables and Important fields:

### Table:

Credits.default.foreclosurerequests

### Field:

foreclosurerequests: created_on - When request was created

Collections: closed_on - When request was closed automatically

Request status 

### Table:

admin_action_audit

admin action name: 

To identify which requests were closed manually

Format: Email with CSV attached

Recipients:

@Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava