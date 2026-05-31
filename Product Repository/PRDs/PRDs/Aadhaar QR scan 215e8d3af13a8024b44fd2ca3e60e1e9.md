# Aadhaar QR scan

: Surya Ganesh
Created time: June 17, 2025 5:25 PM
Status: Not started
Last edited: June 26, 2025 11:33 AM

1. Perfios Walk-through completed:
    
    SDK includes:
    
    1. Scan QR (scanner)
    2. Upload QR
    3. Fetches and displays the data
    4. To verify the email and phone, the customer has to enter email and phone 
    
    Steps:
    
    1. Scan QR/ Upload QR
    2. Perfios de-codes the data on the QR 
    3. Fetches the data from UIDAI 
    4. Verify the email and phone
    
    Downside of SDK: Cannot be used for web-app (MFD portal)
    
    Perfios gave a walk through for the OCR KYC Plus:
    
    1. Upload the Aadhaar
    2. Scans the QR itself
    3. Gives the address as the outputD

1. Bureau ID gave the following demo:
    1. Upload the Aadhaar QR of the customer
    2. It provides:
        1. Adhaar last 4 digits
        2. careOf
        3. District
        4. DOB
        5. gender
        6. location
        7. landmark
        8. mobile number registered?
        9. email registered?
        10. name of the customer
        11. signature base64
        12. state
        13. street
        14. sub district
    
    But when I gave it my black and white aadhaar and another coloured aadhaar card photo, they could not process it. 
    
    They provide an API based solution thus it can be used across for web-app and mobile-app usage.