# Analytics requirement: Revocation request

|  | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Number of revocation requests | (count of total revocation requests made today) |  |  |  |  |  |  |  |  |
| Number of revocation requests automatically closed | (count of requests made and settled today) |  |  |  |  |  |  |  |  |
| Number of revocation pending closure | (Count of requests made today but pending closure) |  |  |  |  |  |  |  |  |
|  | **Today** | **This week** | **This month** |  |  |  |  |  |  |
| Average closure TAT | For requests closed today avg(closed_on - created_on) - difference of hours |  |  |  |  |  |  |  |  |
| % requests settled automatically | % of requests that were settled closed today (identify requests settled manually via admin action) |  |  |  |  |  |  |  |  |

## Tables and Important fields:

### Table:

Credit_applications.default.revocationrequests

### Field:

revocationrequest: created_on - When payment was created

revocationrequest: settled_on - When payment was settled automatically

revocation requests status (If equals to closed - request was closed either using admin action or automatically)

### Table:

admin_action_audit

admin action name: CLOSE_REVOCATION_REQUEST

To identify which requests were closed manually

Format: Email with CSV attached

Recipients:

@Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava