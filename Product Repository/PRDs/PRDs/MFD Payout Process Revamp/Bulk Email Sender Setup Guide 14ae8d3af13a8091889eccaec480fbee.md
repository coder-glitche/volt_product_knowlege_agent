# Bulk Email Sender Setup Guide

## Prerequisites

1. Python 3.8 or higher
2. SendGrid account with API key
3. Dynamic email template set up in SendGrid with variables:
Template should use these variables:
    
    ```
    Subject: Volt: GST Invoice for {{invoice_month}} - {{invoice_number}}
    
    ```
    
    - {{current_date}}
    - {{partner_id}}
    - {{invoice_month}}
    - {{partner_name}}
    - {{file_link}}
    - {{submission_link}}
    - {{deadline_date}}
    - {{invoice_number}}

## Setup Steps

### 1. Environment Setup

```bash
# Create a new directory
mkdir email-sender
cd email-sender

# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows:
venv\\Scripts\\activate
# For Mac/Linux:
source venv/bin/activate

# Install required packages
pip install pandas python-dotenv sendgrid

```

### 2. File Structure

```
email-sender/
├── venv/
├── .env
├── emailsender.py
├── invoices.csv
└── logs/

```

### 3. Environment Variables

Create a `.env` file with these variables:

```
SENDGRID_API_KEY=<REDACTED>
FROM_EMAIL=no-reply@voltmoney.in
TEST_MODE=False
CSV_PATH=invoices.csv
TEMPLATE_ID=d-5a90b23aa1214f3d87f817bffb91ebd9 
BATCH_SIZE=100
DELAY=1.0
MAX_RETRIES=3

```

### 4. Input CSV Format

Create `invoices.csv` with these columns:

```
email_ID,invoice_date,partner_id,invoice_month,partner_name,file_link,Pre-filled Form URL,invoice_number
example@company.com,2024-03-01,PART001,March 2024,John Doe,<https://link-to-file>,<https://form-link>,INV-2024-001

```

## Running the Script

1. **Test Mode First**
    
    ```bash
    # Keep TEST_MODE=True in .env
    python emailsender.py
    
    ```
    
    Check logs folder for email_log_[timestamp].csv
    
2. **Live Mode**
    
    ```bash
    # Change TEST_MODE=False in .env
    python emailsender.py
    
    ```
    

## Output & Logs

- Script creates a `logs` folder
- Each run generates a CSV file: `email_log_YYYYMMDD_HHMMSS.csv`
- Log contains:
    - Timestamp
    - Email status (SUCCESS/FAILED)
    - Retry attempts
    - Error messages if any
    - All email details

## Troubleshooting

1. **Common Issues**
    - "Missing required environment variables": Check .env file
    - "API key invalid": Verify SendGrid API key
    - "Template not found": Check template_id in .env
2. **SendGrid Template**
    - Ensure all variables are properly defined
    - Test template in SendGrid dashboard first
3. **CSV Issues**
    - Check CSV encoding (should be UTF-8)
    - Verify all required columns are present
    - No empty rows/cells in required fields

## Best Practices

1. **Before Sending**
    - Run in TEST_MODE first
    - Verify template with test data
    - Check log file format
2. **Production Use**
    - Start with small batches
    - Monitor logs actively
    - Keep DELAY=1.0 to avoid rate limits

## Support

For issues:

- Check SendGrid logs for delivery status
- Review email_log CSV for error messages
- Ensure all template variables match CSV data

## Security Notes

- Keep .env file secure
- Don't commit .env to version control
- Use verified sender emails only