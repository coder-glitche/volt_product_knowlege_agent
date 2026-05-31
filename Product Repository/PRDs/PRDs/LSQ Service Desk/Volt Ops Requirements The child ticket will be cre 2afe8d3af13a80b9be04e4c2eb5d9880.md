# Volt Ops Requirements

The child ticket will be created and assigned to Volt Ops.

Ticket Schema:
The ticket can be replicated with a click using the option of Capture properties from parent ticket.

Additional Tags required are as follows, and the mapping against the parent tags:

| **Parent Tag** | **Child Tag** |
| --- | --- |
| account_opening | 1. pending_account_opening2. account_opening_/_lodgement_delayed |
| lodgement | 1. pending_lodgement2. lodgement3. lodgement_issue4. account_opening_/_lodgement_delayed |
| enhancement | 1. pending_account_enhancement
2. pending_enhancement |
| disbursal | 1. pending_disbursal2. withdrawal_issue3. withdrawal_rejected4. unable_to_place_withdrawal5. manual_manual_disbursement |
| foreclosure | 1. unable_to_submit_foreclosure2. foreclosure3. foreclosure_pending4. foreclosure_success_but_account_not_closed5. expired_loan |
| lien_removal | 1. foreclosure_success_but_lien_not_removed2. lien_removal3. unable_to_submit_lien_removal4. lien_removal_pending5. lien_removal_success_but_lien_not_removed |
| repayment | 1. repayment_issue2. repayment_not_accounted3. offline_repayment4. repayment_screen_not_opening |
| service_request | 1. servicerequest-others2. service_request3. interest_certificate4. interest_calculation5. noc6. excess_refund |
| details_update | 1. details_update2. customer_details_update3. bank_account_update4. email_id_update5. phone_number_update |
| voluntary_sell_off | 1. voluntary_sell_off2. sell_off_dispute3. sell-off_request |
| customer_drop_off | 1. customer_dropoff2. customer_doesn_t_want_to_continue |
| shortfall | 1. sell_off_dispute2. shortfall_issue3. short_fall |
| interest | 1. interest_/_charge_dispute
2. interest_amount_incorrect
3. interest_and_charges |
| renewal | 1. renewal |