# Comms config

: Ranjan kumar Singh
Created time: February 18, 2025 9:17 AM
Status: Not started
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

Customer loan renewals

```json
{
  "LOAN_RENEWAL_REMINDER_1ST": {
    "eventInFiltering": {
      "customerChannel": [
        "B2C",
        "B2B",
        "B2B2C"
      ],
      "customerPlatform": [
        "PHONEPE",
        "PHONEPE",
        "VOLT_MOBILE_APP",
        "VOLT_PARTNER_ANDROID_APP",
        "VOLT_WEB_APP",
        "BHARAT_NXT",
        "BharatNxt1",
        "VOLT_API_UAT"
      ]
    },
    "eventOutFiltering": {},
    "communicationMedium": [
      "WHATSAPP",
      "MAIL"
    ],
    "triggerTime": {},
    "templateConfig": {
      "WHATSAPP": {
        "templateId": "loan_renewal_1st_day_of_month_v1",
        "overrideTemplates": [
          {
            "customerPlatform": [
              "PHONEPE",
              "PHONEPE",
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Bajaj"
            ],
            "templateId": "loan_renewal_1st_day_of_month_v1"
          },
          {
            "customerPlatform": [
              "PHONEPE",
              "PHONEPE",
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Tata"
            ],
            "templateId": "loan_renewal_1st_day_of_month_v1"
          }
        ],
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "loan_expiry_date",
          "contactnumber"
        ]
      },
      "MAIL": {
        "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb",
        "overrideTemplates": [
          {
            "customerPlatform": [
              "PHONEPE",
              "PHONEPE",
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Bajaj"
            ],
            "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb"
          },
          {
            "customerPlatform": [
              "PHONEPE",
              "PHONEPE",
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Tata"
            ],
            "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb"
          }
        ],
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "loan_expiry_date",
          "loan_renewal_landing_page_link",
          "contactnumber"
        ]
      }
    },
    "isActive": true
  },
  "LOAN_RENEWAL_REMINDER_2ND": {
    "eventInFiltering": {
      "customerChannel": [
        "B2B",
        "B2C",
        "B2B2C"
      ],
      "customerPlatform": [
        "VOLT_MOBILE_APP",
        "VOLT_PARTNER_ANDROID_APP",
        "VOLT_WEB_APP",
        "PHONEPE",
        "PHONEPE",
        "BHARAT_NXT",
        "BharatNxt1",
        "VOLT_API_UAT"
      ]
    },
    "eventOutFiltering": {},
    "communicationMedium": [
      "WHATSAPP",
      "MAIL"
    ],
    "triggerTime": {},
    "templateConfig": {
      "WHATSAPP": {
        "templateId": "15th_day_of_loan_expiry_v1",
        "overrideTemplates": [
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Bajaj"
            ],
            "templateId": "15th_day_of_loan_expiry_v1"
          },
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Tata"
            ],
            "templateId": "15th_day_of_loan_expiry_v1"
          },
        ],
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "days_left",
          "contactnumber"
        ]
      },
      "MAIL": {
        "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de",
        "overrideTemplates": [
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Bajaj"
            ],
            "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de"
          },
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Tata"
            ],
            "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de"
          }
        ],
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "days_left",
          "loan_renewal_landing_page_link",
          "contactnumber"
        ]
      }
    },
    "isActive": true
  },
  "LOAN_RENEWAL_REMINDER_LAST_WEEK_DUE": {
    "eventInFiltering": {
      "customerChannel": [
        "B2B",
        "B2C",
        "B2B2C"
      ],
      "customerPlatform": [
        "VOLT_MOBILE_APP",
        "VOLT_PARTNER_ANDROID_APP",
        "VOLT_WEB_APP",
        "PHONEPE",
        "PHONEPE",
        "BHARAT_NXT",
        "BharatNxt1",
        "VOLT_API_UAT"
      ]
    },
    "eventOutFiltering": {},
    "communicationMedium": [
      "WHATSAPP",
      "MAIL"
    ],
    "triggerTime": {},
    "templateConfig": {
      "WHATSAPP": {
        "templateId": "20days_to_last_day_amount_due",
        "overrideTemplates": [
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Bajaj"
            ],
            "templateId": "20days_to_last_day_amount_due"
          },
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Tata"
            ],
            "templateId": "20days_to_last_day_amount_due"
          }
        ],
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "days_left",
          "outstanding_amount",
          "contactnumber"
        ]
      },
      "MAIL": {
        "templateId": "d-78f7acdde85248798dfda7f480312e31",
        "overrideTemplates": [
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Bajaj"
            ],
            "templateId": "d-78f7acdde85248798dfda7f480312e31"
          },
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Tata"
            ],
            "templateId": "d-78f7acdde85248798dfda7f480312e31"
          }
        ],
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "days_left",
          "outstanding_amount",
          "loan_renewal_landing_page_link",
          "contactnumber"
        ]
      }
    },
    "isActive": true
  },
  "LOAN_RENEWAL_REMINDER_LAST_WEEK_NO_DUE": {
    "eventInFiltering": {
      "customerChannel": [
        "B2B",
        "B2C",
        "B2B2C"
      ],
      "customerPlatform": [
        "VOLT_MOBILE_APP",
        "VOLT_PARTNER_ANDROID_APP",
        "VOLT_WEB_APP",
        "PHONEPE",
        "PHONEPE",
        "BHARAT_NXT",
        "BharatNxt1",
        "VOLT_API_UAT"
      ]
    },
    "eventOutFiltering": {},
    "communicationMedium": [
      "WHATSAPP",
      "MAIL"
    ],
    "triggerTime": {},
    "templateConfig": {
      "WHATSAPP": {
        "templateId": "20days_to_last_day_amount_not_due",
        "overrideTemplates": [
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Bajaj"
            ],
            "templateId": "20days_to_last_day_amount_not_due"
          },
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Tata"
            ],
            "templateId": "20days_to_last_day_amount_not_due"
          }
        ],
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "days_left",
          "contactnumber"
        ]
      },
      "MAIL": {
        "templateId": "d-56ac6c99ba2d4e8382c826b457d0751b",
        "overrideTemplates": [
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Bajaj"
            ],
            "templateId": "d-56ac6c99ba2d4e8382c826b457d0751b"
          },
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Tata"
            ],
            "templateId": "d-56ac6c99ba2d4e8382c826b457d0751b"
          }
        ],
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "days_left",
          "loan_renewal_landing_page_link",
          "contactnumber"
        ]
      }
    },
    "isActive": true
  },
  "LOAN_RENEWAL_REMINDER_LAST_DAY_NO_DUE": {
    "eventInFiltering": {
      "customerChannel": [
        "B2B",
        "B2C",
        "B2B2C"
      ],
      "customerPlatform": [
        "VOLT_MOBILE_APP",
        "VOLT_PARTNER_ANDROID_APP",
        "VOLT_WEB_APP",
        "PHONEPE",
        "PHONEPE",
        "BHARAT_NXT",
        "BharatNxt1",
        "VOLT_API_UAT"
      ]
    },
    "eventOutFiltering": {},
    "communicationMedium": [
      "WHATSAPP",
      "MAIL"
    ],
    "triggerTime": {},
    "templateConfig": {
      "WHATSAPP": {
        "templateId": "last_day_of_loan_expiry_amount_not_due_v2",
        "overrideTemplates": [
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Bajaj"
            ],
            "templateId": "last_day_of_loan_expiry_amount_not_due_v2"
          },
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Tata"
            ],
            "templateId": "last_day_of_loan_expiry_amount_not_due_v2"
          }
        ],
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "contactnumber"
        ]
      },
      "MAIL": {
        "templateId": "d-c5421e5370ac4ef0adea00a5e760a076",
        "overrideTemplates": [
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Bajaj"
            ],
            "templateId": "d-c5421e5370ac4ef0adea00a5e760a076"
          },
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Tata"
            ],
            "templateId": "d-c5421e5370ac4ef0adea00a5e760a076"
          }
        ],
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "loan_renewal_landing_page_link",
          "contactnumber"
        ]
      }
    },
    "isActive": true
  },
  "LOAN_RENEWAL_REMINDER_LAST_DAY_DUE": {
    "eventInFiltering": {
      "customerChannel": [
        "B2B",
        "B2C",
        "B2B2C"
      ],
      "customerPlatform": [
        "VOLT_MOBILE_APP",
        "VOLT_PARTNER_ANDROID_APP",
        "VOLT_WEB_APP",
        "PHONEPE",
        "PHONEPE",
        "BHARAT_NXT",
        "BharatNxt1",
        "VOLT_API_UAT"
      ]
    },
    "eventOutFiltering": {},
    "communicationMedium": [
      "WHATSAPP",
      "MAIL"
    ],
    "triggerTime": {},
    "templateConfig": {
      "WHATSAPP": {
        "templateId": "last_day_of_loan_expiry_month_amount_due",
        "overrideTemplates": [
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Bajaj"
            ],
            "templateId": "last_day_of_loan_expiry_month_amount_due"
          },
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Tata"
            ],
            "templateId": "last_day_of_loan_expiry_month_amount_due"
          }
        ],
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "outstanding_amount",
          "contactnumber"
        ]
      },
      "MAIL": {
        "templateId": "d-86dd391e69d94fb8a3caf119ce5a5154",
        "overrideTemplates": [
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Bajaj"
            ],
            "templateId": "d-86dd391e69d94fb8a3caf119ce5a5154"
          },
          {
            "customerPlatform": [
              "VOLT_MOBILE_APP",
              "VOLT_PARTNER_ANDROID_APP",
              "VOLT_WEB_APP",
              "PHONEPE",
              "PHONEPE",
              "BHARAT_NXT",
              "BharatNxt1",
              "VOLT_API_UAT"
            ],
            "lenderPlatform": [
              "Tata"
            ],
            "templateId": "d-86dd391e69d94fb8a3caf119ce5a5154"
          }
        ],
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "outstanding_amount",
          "loan_renewal_landing_page_link",
          "contactnumber"
        ]
      }
    },
    "isActive": true
  },
  "LOAN_RENEWAL_REMINDER_1ST_NO_DUE": {
    "eventInFiltering": {
      "customerChannel": [
        "B2B",
        "B2C",
        "B2B2C"
      ],
      "customerPlatform": [
        "VOLT_MOBILE_APP",
        "VOLT_PARTNER_ANDROID_APP",
        "VOLT_WEB_APP",
        "PHONEPE",
        "PHONEPE",
        "BHARAT_NXT",
        "BharatNxt1",
        "VOLT_API_UAT"
      ]
    },
    "eventOutFiltering": {},
    "communicationMedium": [
      "WHATSAPP",
      "MAIL"
    ],
    "triggerTime": {},
    "templateConfig": {
      "WHATSAPP": {
        "templateId": "loan_expired_amount_not_due_v1",
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "contactnumber"
        ]
      },
      "MAIL": {
        "templateId": "d-203fa301d72846ed84ecf4dc151056fc",
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "loan_renewal_landing_page_link",
          "contactnumber"
        ]
      }
    },
    "isActive": false
  },
  "LOAN_RENEWAL_REMINDER_1ST_WEEK_DUE": {
    "eventInFiltering": {
      "customerChannel": [
        "B2B",
        "B2C",
        "B2B2C"
      ],
      "customerPlatform": [
        "VOLT_MOBILE_APP",
        "VOLT_PARTNER_ANDROID_APP",
        "VOLT_WEB_APP",
        "PHONEPE",
        "PHONEPE",
        "BHARAT_NXT",
        "BharatNxt1",
        "VOLT_API_UAT"
      ]
    },
    "eventOutFiltering": {},
    "communicationMedium": [
      "WHATSAPP",
      "MAIL"
    ],
    "triggerTime": {},
    "templateConfig": {
      "WHATSAPP": {
        "templateId": "loan_expired_amount_due",
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "outstanding_amount",
          "contactnumber",
          "penal_charges",
          "sell_of_date"
        ]
      },
      "MAIL": {
        "templateId": "d-95ec8ebdd82f46968e7b11994e113cba",
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "outstanding_amount",
          "loan_renewal_landing_page_link",
          "contactnumber",
          "penal_charges",
          "sell_of_date"
        ]
      }
    },
    "isActive": false
  },
  "LOAN_RENEWAL_REMINDER_AFTER_WEEK_DUE": {
    "eventInFiltering": {
      "customerChannel": [
        "B2B",
        "B2C",
        "B2B2C"
      ],
      "customerPlatform": [
        "VOLT_MOBILE_APP",
        "VOLT_PARTNER_ANDROID_APP",
        "VOLT_WEB_APP",
        "PHONEPE",
        "PHONEPE",
        "BHARAT_NXT",
        "BharatNxt1",
        "VOLT_API_UAT"
      ]
    },
    "eventOutFiltering": {},
    "communicationMedium": [
      "WHATSAPP",
      "MAIL"
    ],
    "triggerTime": {},
    "templateConfig": {
      "WHATSAPP": {
        "templateId": "loan_expired_amount_due_7_v3",
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "outstanding_amount",
          "contactnumber",
          "lendername"
        ]
      },
      "MAIL": {
        "templateId": "d-22acf1e891c744ad89e777d6ee44c0bb",
        "variables": [
          "customername",
          "brand_name",
          "credit_limit",
          "outstanding_amount",
          "loan_renewal_landing_page_link",
          "contactnumber",
          "lendername"
        ]
      }
    },
    "isActive": false
  }
}
```