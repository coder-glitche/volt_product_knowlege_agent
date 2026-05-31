# Postman collection

{
"info": {
"_postman_id": "unique-postman-id",
"name": "Leegality UAT",
"schema": "[https://schema.getpostman.com/json/collection/v2.1.0/collection.json](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)"
},
"item": [
{
"name": "Inventory check",
"request": {
"method": "GET",
"header": [
{
"key": "X-Auth-Token",
"value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R",
"type": "text"
}
],
"url": {
"raw": "[https://sandbox.leegality.com/api/v3.0/series/list](https://sandbox.leegality.com/api/v3.0/series/list)",
"protocol": "https",
"host": [
"sandbox",
"leegality",
"com"
],
"path": [
"api",
"v3.0",
"series",
"list"
]
}
},
"response": []
},
{
"name": "E-sign request - copy to be sent to customer",
"request": {
"method": "POST",
"header": [
{
"key": "X-Auth-Token",
"value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R",
"type": "text"
}
],
"body": {
"mode": "raw",
"raw": "{\n  \"profileId\": \"mKJY8rA\",\n  \"file\": {\n    \"name\": \"string\",\n    \"file\": \"string\"\n  },\n  \"invitees\": [\n    {\n      \"name\": \"Saksham\",\n      \"email\": \"[saksham.srivastava@voltmoney.in](mailto:saksham.srivastava@voltmoney.in)\",\n      \"dscConfig\": {\n        \"verifyName\": false,\n        \"verifySmartName\": false,\n        \"verifyPincode\": \"string\",\n        \"verifyState\": \"string\"\n      }\n    }\n  ],\n  \"irn\": \"string\"\n}",
"options": {
"raw": {
"language": "json"
}
}
},
"url": {
"raw": "[https://sandbox.leegality.com/api/v3.0/sign/request](https://sandbox.leegality.com/api/v3.0/sign/request)",
"protocol": "https",
"host": [
"sandbox",
"leegality",
"com"
],
"path": [
"api",
"v3.0",
"sign",
"request"
]
}
},
"response": []
},
{
"name": "E-sign request - copy to be stamped and NBFC signed",
"request": {
"method": "POST",
"header": [
{
"key": "X-Auth-Token",
"value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R",
"type": "text"
}
],
"body": {
"mode": "raw",
"raw": "{\n  \"profileId\": \"GpqF8Tf\",\n  \"file\": {\n    \"name\": \"string\",\n    \"file\": \"string\"\n  },\n  \"stampSeries\": \"03\",\n  \"invitees\": [\n    {\n      \"name\": \"Saksham\",\n      \"email\": \"[saksham.srivastava@voltmoney.in](mailto:saksham.srivastava@voltmoney.in)\",\n      \"dscConfig\": {\n        \"verifyName\": false,\n        \"verifySmartName\": false,\n        \"verifyPincode\": \"string\",\n        \"verifyState\": \"string\"\n      }\n    }\n  ],\n  \"irn\": \"string\"\n}",
"options": {
"raw": {
"language": "json"
}
}
},
"url": {
"raw": "[https://sandbox.leegality.com/api/v3.0/sign/request](https://sandbox.leegality.com/api/v3.0/sign/request)",
"protocol": "https",
"host": [
"sandbox",
"leegality",
"com"
],
"path": [
"api",
"v3.0",
"sign",
"request"
]
}
},
"response": []
},
{
"name": "Sign on e-sign request",
"request": {
"method": "POST",
"header": [
{
"key": "X-Auth-Token",
"value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R",
"type": "text"
}
],
"body": {
"mode": "raw",
"raw": "{\n  \"signUrl\": \"string\",\n  \"profileId\": \"naq2t4g\",\n  \"consent\": \"By using this authenticated API and the ProfileID associated with this Document Signer Certificate, I agree that the Document Signer Certificate saved in this Account will be used to eSign documents for me. I also understand that recipients of such electronic documents will be able to see my signing details.\"\n}",
"options": {
"raw": {
"language": "json"
}
}
},
"url": {
"raw": "[https://sandbox.leegality.com/api/v3.0/sign/docSigner/invitation](https://sandbox.leegality.com/api/v3.0/sign/docSigner/invitation)",
"protocol": "https",
"host": [
"sandbox",
"leegality",
"com"
],
"path": [
"api",
"v3.0",
"sign",
"docSigner",
"invitation"
]
}
},
"response": []
},
{
"name": "Download document",
"request": {
"method": "GET",
"header": [
{
"key": "X-Auth-Token",
"value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R",
"type": "text"
}
],
"url": {
"raw": "[https://sandbox.leegality.com/api/v3.3/document/fetchDocument?documentId={{documentId}](https://sandbox.leegality.com/api/v3.3/document/fetchDocument?documentId=%7B%7BdocumentId%7D)}&documentDownloadType={{documentDownloadType}}",
"protocol": "https",
"host": [
"sandbox",
"leegality",
"com"
],
"path": [
"api",
"v3.3",
"document",
"fetchDocument"
],
"query": [
{
"key": "documentId",
"value": "{{documentId}}"
},
{
"key": "documentDownloadType",
"value": "{{documentDownloadType}}"
}
]
}
},
"response": []
},
{
"name": "Download document in base64",
"request": {
"method": "GET",
"header": [
{
"key": "X-Auth-Token",
"value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R",
"type": "text"
}
],
"url": {
"raw": "[https://sandbox.leegality.com/api/v3.1/document/details?documentId={{documentId}](https://sandbox.leegality.com/api/v3.1/document/details?documentId=%7B%7BdocumentId%7D)}&file=true",
"protocol": "https",
"host": [
"sandbox",
"leegality",
"com"
],
"path": [
"api",
"v3.1",
"document",
"details"
],
"query": [
{
"key": "documentId",
"value": "{{documentId}}"
},
{
"key": "file",
"value": "true"
}
]
}
},
"response": []
}
]
}