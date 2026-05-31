# Comms config - OTP

: Ranjan kumar Singh
Created time: November 7, 2025 12:41 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# What problem are we solving?

We have experienced multiple instances of **SMS service provider outages**, which have **impacted critical business operations**. Since SMS was our **only channel** for sending OTPs used in **login and transaction verification**, we introduced **WhatsApp** as a **backup channel** to ensure continuity.

However, SMS service disruptions are **intermittent**, and we want to maintain SMS as the **primary channel** for OTP delivery while using **WhatsApp and Email** as **secondary fallback channels** during downtime. This approach will help ensure **seamless user experience** and **uninterrupted transaction processing**.

To enable this flexibility, we need to **move OTP channel configuration from the code level to AWS Config**, allowing dynamic control over which channels are active without requiring a code deployment.

# What is the solutions:

OTP delivery settings will be **event-driven** and **fully configurable** through AWS Config, allowing dynamic control without requiring code-level changes.

### **a. Event-Based Configuration**

- OTP configurations will be defined for specific events such as:
    - **Login**
    - **Disbursal**
    - **Lien Removal**
    - **Foreclosure**
- Each event will support enabling or disabling OTP delivery across multiple communication channels (SMS, WhatsApp, Email).

### **b. Channel-Level Control**

- Channels can be selectively activated per event. For example:
    - **Login OTP:** Enabled only on **SMS**
    - **Disbursal OTP:** Enabled on both **SMS** and **WhatsApp**
- This setup ensures flexibility in managing costs and fallback strategies while maintaining a consistent user experience.

### **c. Business Channel–Based Configuration**

- Configurations can be **filtered based on business partners or channels**.
- Example: Separate OTP templates or channel preferences can be defined for each business partner (e.g., Volt Platform, Lark).

### **d. Dynamic Updates**

- All configurations can be updated dynamically via AWS Config without any application deployment.
- This allows **real-time adjustments** during outages or provider-specific issues, minimizing business disruption.

**Sample config:**

```json
{
  "LOGIN_OTP_CUSTOMERCUSTOMER_LOGIN_OTP": {
    "eventInFiltering": {},
    "eventOutFiltering": {},
    "communicationMedium": ["WHATSAPP", "MAIL", "SMS"],
    "triggerTime": {},
    "templateConfig": {
      "WHATSAPP": {
        "templateId": "otpv6",
        "overrideTemplates": [
          {
            "customerPlatform": ["LARK", "TATA"],
            "templateId": "otpv7"
          }
        ],
        "variables": ["1"]
      },
      "MAIL": {
        "templateId": "to_added",
        "overrideTemplates": [
          {
            "customerPlatform": ["LARK", "TATA"],
            "templateId": "345678ihgfghjklkjhv"
          }
        ],
        "variables": ["1"]
      },
      "SMS": {
        "templateId": "to_add",
        "overrideTemplates": [
          {
            "customerPlatform": ["LARK", "TATA"],
            "templateId": "{VAR is the OTP to LOGIN}"
          }
        ],
        "variables": ["otp"]
      }
    },
    "isActive": true
  },

  "LOGIN_OTP_PARTNER_DASHBOARDPARTNER_DASHBOARD_LOGIN_OTP
  ": {
    "eventInFiltering": {
      "customerChannel": ["B2B", "B2C", "B2B2C"],
      "customerPlatform": []
    },
    "eventOutFiltering": {},
    "communicationMedium": ["SMS"],
    "triggerTime": {},
    "templateConfig": {
      "WHATSAPP": {
        "templateId": "otpv6",
        "variables": ["1"]
      },
      "MAIL": {
        "templateId": "to_added",
        "variables": ["1"]
      },
      "SMS": {
        "templateId": "to_add",
        "variables": ["otp"]
      }
    },
    "isActive": true
  },

  "DISBURSAL": {
    "eventInFiltering": {
      "customerChannel": ["B2B", "B2C", "B2B2C"],
      "customerPlatform": []
    },
    "eventOutFiltering": {},
    "communicationMedium": ["WHATSAPP", "SMS", "MAIL"],
    "triggerTime": {},
    "templateConfig": {
      "WHATSAPP": {
        "templateId": "otpv6",
        "overrideTemplates": [
          {
            "customerPlatform": ["LARK", "TATA"],
            "templateId": "otpv7"
          }
        ],
        "variables": ["1"]
      },
      "MAIL": {
        "templateId": "to_added",
        "overrideTemplates": [
          {
            "customerPlatform": ["LARK", "TATA"],
            "templateId": "345678ihgfghjklkjhv"
          }
        ],
        "variables": ["1"]
      },
      "SMS": {
        "templateId": "to_add",
        "overrideTemplates": [
          {
            "customerPlatform": ["LARK", "TATA"],
            "templateId": "{VAR is the OTP to LOGIN - SALTER}"
          }
        ],
        "variables": ["otp"]
      }
    },
    "isActive": true
  },

  "LIEN_REMOVAL": {
    "eventInFiltering": {
      "customerChannel": ["B2B", "B2C", "B2B2C"],
      "customerPlatform": []
    },
    "eventOutFiltering": {},
    "communicationMedium": ["WHATSAPP", "SMS", "MAIL"],
    "triggerTime": {},
    "templateConfig": {
      "WHATSAPP": {
        "templateId": "otpv6",
        "variables": ["1"]
      },
      "MAIL": {
        "templateId": "to_added",
        "overrideTemplates": [
          {
            "customerPlatform": ["LARK", "TATA"],
            "templateId": "345678ihgfghjklkjhv"
          }
        ],
        "variables": ["1"]
      },
      "SMS": {
        "templateId": "to_add",
        "variables": ["otp"]
      }
    },
    "isActive": true
  },

  "FORECLOSURE": {
    "eventInFiltering": {
      "customerChannel": ["B2B", "B2C", "B2B2C"],
      "customerPlatform": []
    },
    "eventOutFiltering": {},
    "communicationMedium": ["WHATSAPP", "SMS", "MAIL"],
    "triggerTime": {},
    "templateConfig": {
      "WHATSAPP": {
        "templateId": "otpv6",
        "variables": ["1"]
      },
      "MAIL": {
        "templateId": "to_added",
        "overrideTemplates": [
          {
            "customerPlatform": ["LARK", "TATA"],
            "templateId": "345678ihgfghjklkjhv"
          }
        ],
        "variables": ["1"]
      },
      "SMS": {
        "templateId": "to_add",
        "variables": ["otp"]
      }
    },
    "isActive": true
  }
}

```