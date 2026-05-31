# Sample PMR transactions

Status: Done

## CDSL (Lien marking): Pledge marking

| Date | BO ID | ISIN | ISIN Description | Pledged Quantity | Pledgee Name | Status | Pledge Type | Remarks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01-Jul-2025 | 1201916305123456 | INE018A01030 | RELIANCE EQ | 100 | DSP Finance Pvt Ltd | Confirmed | Margin | Pledge created successfully |

## CDSL (Lien revocation): Pledge closure

| Date | BO ID | ISIN | ISIN Description | Closed Quantity | Pledgee Name | Status | Closure Date | Remarks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 05-Jul-2025 | 1201916305123456 | INE018A01030 | RELIANCE EQ | 100 | DSP Finance Pvt Ltd | Released | 05-Jul-2025 | Pledge closed successfully |

### CDSL: (Lien invocation)

| Date | BO ID | ISIN | ISIN Description | Invoked Quantity | Pledgee Name | Status | Invocation Date | Remarks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 07-Jul-2025 | 1201916305123456 | INE018A01030 | RELIANCE EQ | 50 | DSP Finance Pvt Ltd | Invoked | 07-Jul-2025 | Partial invocation triggered |

### NSDL (Lien marking): Pledge marking

| Execution Date | Client ID | ISIN | ISIN Description | Pledged Quantity | Pledgee | Pledge Type | Margin Pledge | Status | Agreement No. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01-Jul-2025 | 41111111 | INE018A01030 | RELIANCE EQ | 100 | DSP1234 | Margin | Yes | Confirmed | AGMT-56789 |

### NSDL (Lien revocation) Pledge closure

| Closure Date | Client ID | ISIN | ISIN Description | Closed Quantity | Pledgee | Status | Lock-In Reason | Remarks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 05-Jul-2025 | 41111111 | INE018A01030 | RELIANCE EQ | 100 | DSP1234 | Released | NA | Closure on user request |

### NSDL (Lien invocation)

| Execution Date | Client ID | ISIN | ISIN Description | Invoked Quantity | Pledgee | Status | Remarks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 07-Jul-2025 | 41111111 | INE018A01030 | RELIANCE EQ | 50 | DSP1234 | Invoked | Auto-invoked due to LTV breach |

[CDSL_PMR_Sample.csv](Sample%20PMR%20transactions/CDSL_PMR_Sample.csv)

[NSDL_PMR_Sample.csv](Sample%20PMR%20transactions/NSDL_PMR_Sample.csv)