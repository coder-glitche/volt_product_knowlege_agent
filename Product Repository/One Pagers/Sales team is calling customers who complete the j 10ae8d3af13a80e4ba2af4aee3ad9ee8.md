# Sales team is calling customers who complete the journey on their own

To maximize the efficiency of our sales team and ensure that our limited resources are used effectively, we aim to distinguish between customers who genuinely need assistance and those who can self-serve. By enabling our sales team to focus on "struck" customers—those facing difficulties in the application or onboarding process—we can optimize our support efforts, increase customer satisfaction, and drive higher conversion rates.

## Strategy:

We are building a **customer classifier** that will automatically detect whether a customer is "stuck" in the journey or can self-serve. This will allow our CRM to prioritize customers based on their likelihood to convert or their need for human assistance. By focusing on high-priority leads, we can drive better performance with the same resources.

### Key Steps:

1. **Develop a Classifier**:
    - Build a mechanism that identifies "struck" customers based on their interaction with the platform. This classifier will be able to distinguish between users who are struggling and those who can proceed independently.
2. **Highlight in CRM**:
    - Integrate the classifier with our CRM system to ensure that sales representatives are notified in real-time when a customer is identified as "stuck." The CRM should highlight these customers, offering the sales team clear, actionable insights.
3. **Update Sales Incentives**:
    - Modify the incentive structure for sales executives to align with the new system, rewarding them for focusing on and resolving cases where their intervention is truly needed.

## Identifying "Struck" Applicants:

To accurately identify struck customers, we will deploy the following tactics:

- **Telemetry on Errors**:
    - Implement error tracking throughout the customer journey. If a customer encounters a technical problem (e.g., form submission fails, API error), they will be flagged as "struck."
- **Abandoned Journey**:
    - Monitor customer activity in real-time. If a user abandons a critical stage of the application process (e.g., KYC, loan application) for more than 30 minutes, they will be marked as "stuck."
- **Custom Rules**:
    - We will determine additional logic based on further data analysis and customer feedback to enhance the classifier.

### Classifier Logic:

The classifier's logic will be based on a combination of:

- **User behavior telemetry** (e.g., error reports, time spent on a task).
- **Abandonment tracking** (e.g., inactivity beyond a defined threshold).
- **Data-driven insights** (e.g., patterns in customers’ prior journeys that lead to successful or failed conversions).

### CRM Integration:

Once the classifier is fully defined, the CRM must be modified to:

- **Highlight Struck Customers**: The CRM interface should automatically flag struck customers in the sales pipeline, using a visual indicator (e.g., a high-priority marker or a red flag) and assigning a lead quality score that reflects the customer's need for support.
- **Prioritize Leads Based on Urgency**: Leads will be prioritized in real-time based on their need for help, ensuring the sales team can focus on resolving urgent cases.

### Incentive Alignment:

To motivate the sales team to focus on the most critical customers:

- **New Incentive Structures**: The incentive plan will need to shift from a volume-based model (total number of customers helped) to a value-driven model. Sales executives should be rewarded based on:
    - The number of struck customers successfully assisted and converted.
    - Overall improvement in lead quality scores after intervention.

This change ensures that the team is not just incentivized to increase the volume of calls or interactions but to focus on meaningful, high-impact interventions.

## Technical Requirements:

To achieve the desired results, the following system updates are necessary:

- **Classifier Development**: Build the backend logic that flags struck customers based on real-time data.
- **CRM Modification**: Integrate the classifier output into the CRM, highlighting struck leads and assigning appropriate lead quality scores.
- **Database Changes**: Ensure that the database is structured to store telemetry data, abandonment timestamps, and error logs for accurate classification.

## Objectives:

- **Improve Sales Efficiency**: Enable the sales team to prioritize customers who genuinely need their help, ensuring their efforts are focused on high-value interactions.
- **Increase Conversion Rates**: By focusing on struck customers, we can reduce friction in the user journey and increase the likelihood of successful conversions.
- **Reduce Support Costs**: By filtering out customers who can self-serve, we can reduce unnecessary sales and support interventions, optimizing resource allocation.

## Next Steps:

- **Finalize Classifier Logic**: Define the final criteria and thresholds for marking customers as struck.
- **Implement CRM Changes**: Collaborate with the technical team to integrate the classifier and make the necessary CRM updates.
- **Update Sales Processes**: Communicate changes to the sales team and align new incentive structures with the revised processes.

By implementing these steps, we will empower our sales team to work smarter, reduce operational inefficiencies, and improve customer outcomes.