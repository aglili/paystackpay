mock_initialize_transactions = {
  "status": True,
  "message": "Authorization URL created",
  "data": {
    "authorization_url": "https://checkout.paystack.com/3ni8kdavz62431k",
    "access_code": "3ni8kdavz62431k",
    "reference": "re4lyvq3s3"
  }
}

mock_verify_transaction = {
  "status": True,
  "message": "Verification successful",
  "data": {
    "id": 4099260516,
    "domain": "test",
    "status": "success",
    "reference": "mko157u44s",
    "receipt_number": None,
    "amount": 40333,
    "message": None,
    "gateway_response": "Successful",
    "paid_at": "2024-08-22T09:15:02.000Z",
    "created_at": "2024-08-22T09:14:24.000Z",
    "channel": "card",
    "currency": "NGN",
    "ip_address": "197.210.54.33",
    "metadata": "",
    "log": {
      "start_time": 1724318098,
      "time_spent": 4,
      "attempts": 1,
      "errors": 0,
      "success": True,
      "mobile": False,
      "input": [],
      "history": [
        {
          "type": "action",
          "message": "Attempted to pay with card",
          "time": 3
        },
        {
          "type": "success",
          "message": "Successfully paid with card",
          "time": 4
        }
      ]
    },
    "fees": 10283,
    "fees_split": None,
    "authorization": {
      "authorization_code": "AUTH_uh8bcl3zbn",
      "bin": "408408",
      "last4": "4081",
      "exp_month": "12",
      "exp_year": "2030",
      "channel": "card",
      "card_type": "visa ",
      "bank": "TEST BANK",
      "country_code": "NG",
      "brand": "visa",
      "reusable": None,
      "signature": "SIG_yEXu7dLBeqG0kU7g95Ke",
      "account_name": None
    },
    "customer": {
      "id": 181873746,
      "first_name": None,
      "last_name": None,
      "email": "demo@test.com",
      "customer_code": "CUS_1rkzaqsv4rrhqo6",
      "phone": None,
      "metadata": None,
      "risk_action": "default",
      "international_format_phone": None
    },
    "plan": None,
    "split": {},
    "order_id": None,
    "paidAt": "2024-08-22T09:15:02.000Z",
    "createdAt": "2024-08-22T09:14:24.000Z",
    "requested_amount": 30050,
    "pos_transaction_data": None,
    "source": None,
    "fees_breakdown": None,
    "connect": None,
    "transaction_date": "2024-08-22T09:14:24.000Z",
    "plan_object": {},
    "subaccount": {}
  }    
}

mock_list_transactions = {
  "status": True,
  "message": "Transactions retrieved",
  "data": [
    {
      "id": 4099260516,
      "domain": "test",
      "status": "success",
      "reference": "re4lyvq3s3",
      "amount": 40333,
      "message": None,
      "gateway_response": "Successful",
      "paid_at": "2024-08-22T09:15:02.000Z",
      "created_at": "2024-08-22T09:14:24.000Z",
      "channel": "card",
      "currency": "NGN",
      "ip_address": "197.210.54.33",
      "metadata": None,
      "log": {
        "start_time": 1724318098,
        "time_spent": 4,
        "attempts": 1,
        "errors": 0,
        "success": True,
        "mobile": False,
        "input": [],
        "history": [
          {
            "type": "action",
            "message": "Attempted to pay with card",
            "time": 3
          },
          {
            "type": "success",
            "message": "Successfully paid with card",
            "time": 4
          }
        ]
      },
      "fees": 10283,
      "fees_split": None,
      "customer": {
        "id": 181873746,
        "first_name": None,
        "last_name": None,
        "email": "demo@test.com",
        "phone": True,
        "metadata": {
          "custom_fields": [
            {
              "display_name": "Customer email",
              "variable_name": "customer_email",
              "value": "new@email.com"
            }
          ]
        },
        "customer_code": "CUS_1rkzaqsv4rrhqo6",
        "risk_action": "default"
      },
      "authorization": {
        "authorization_code": "AUTH_uh8bcl3zbn",
        "bin": "408408",
        "last4": "4081",
        "exp_month": "12",
        "exp_year": "2030",
        "channel": "card",
        "card_type": "visa ",
        "bank": "TEST BANK",
        "country_code": "NG",
        "brand": "visa",
        "reusable": True,
        "signature": "SIG_yEXu7dLBeqG0kU7g95Ke",
        "account_name": None
      },
      "plan": {},
      "split": {},
      "subaccount": {},
      "order_id": None,
      "paidAt": "2024-08-22T09:15:02.000Z",
      "createdAt": "2024-08-22T09:14:24.000Z",
      "requested_amount": 30050,
      "source": {
        "source": "merchant_api",
        "type": "api",
        "identifier": None,
        "entry_point": "transaction_initialize"
      },
      "connect": None,
      "pos_transaction_data": None
    }
  ],
  "meta": {
    "next": "dW5kZWZpbmVkOjQwMTM3MDk2MzU=",
    "previous": None,
    "perPage": 50
  }    
}

mock_fetch_transactions = {
  "status": True,
  "message": "Transaction retrieved",
  "data": {
    "id": 4099260516,
    "domain": "test",
    "status": "success",
    "reference": "re4lyvq3s3",
    "receipt_number": None,
    "amount": 40333,
    "message": None,
    "gateway_response": "Successful",
    "helpdesk_link": None,
    "paid_at": "2024-08-22T09:15:02.000Z",
    "created_at": "2024-08-22T09:14:24.000Z",
    "channel": "card",
    "currency": "NGN",
    "ip_address": "197.210.54.33",
    "metadata": "",
    "log": {
      "start_time": 1724318098,
      "time_spent": 4,
      "attempts": 1,
      "errors": 0,
      "success": True,
      "mobile": False,
      "input": [],
      "history": [
        {
          "type": "action",
          "message": "Attempted to pay with card",
          "time": 3
        },
        {
          "type": "success",
          "message": "Successfully paid with card",
          "time": 4
        }
      ]
    },
    "fees": 10283,
    "fees_split": None,
    "authorization": {
      "authorization_code": "AUTH_uh8bcl3zbn",
      "bin": "408408",
      "last4": "4081",
      "exp_month": "12",
      "exp_year": "2030",
      "channel": "card",
      "card_type": "visa ",
      "bank": "TEST BANK",
      "country_code": "NG",
      "brand": "visa",
      "reusable": True,
      "signature": "SIG_yEXu7dLBeqG0kU7g95Ke",
      "account_name": None
    },
    "customer": {
      "id": 181873746,
      "first_name": None,
      "last_name": None,
      "email": "demo@test.com",
      "customer_code": "CUS_1rkzaqsv4rrhqo6",
      "phone": None,
      "metadata": {
        "custom_fields": [
          {
            "display_name": "Customer email",
            "variable_name": "customer_email",
            "value": "new@email.com"
          }
        ]
      },
      "risk_action": "default",
      "international_format_phone": None
    },
    "plan": {},
    "subaccount": {},
    "split": {},
    "order_id": None,
    "paidAt": "2024-08-22T09:15:02.000Z",
    "createdAt": "2024-08-22T09:14:24.000Z",
    "requested_amount": 30050,
    "pos_transaction_data": None,
    "source": {
      "type": "api",
      "source": "merchant_api",
      "identifier": None
    },
    "fees_breakdown": None,
    "connect": None
  }    
}

mock_charge_authorization = {
  "status": True,
  "message": "Charge attempted",
  "data": {
    "amount": 35247,
    "currency": "NGN",
    "transaction_date": "2024-08-22T10:53:49.000Z",
    "status": "success",
    "reference": "0m7frfnr47ezyxl",
    "domain": "test",
    "metadata": "",
    "gateway_response": "Approved",
    "message": None,
    "channel": "card",
    "ip_address": None,
    "log": None,
    "fees": 10247,
    "authorization": {
      "authorization_code": "AUTH_uh8bcl3zbn",
      "bin": "408408",
      "last4": "4081",
      "exp_month": "12",
      "exp_year": "2030",
      "channel": "card",
      "card_type": "visa ",
      "bank": "TEST BANK",
      "country_code": "NG",
      "brand": "visa",
      "reusable": True,
      "signature": "SIG_yEXu7dLBeqG0kU7g95Ke",
      "account_name": None
    },
    "customer": {
      "id": 181873746,
      "first_name": None,
      "last_name": None,
      "email": "demo@test.com",
      "customer_code": "CUS_1rkzaqsv4rrhqo6",
      "phone": None,
      "metadata": {
        "custom_fields": [
          {
            "display_name": "Customer email",
            "variable_name": "customer_email",
            "value": "new@email.com"
          }
        ]
      },
      "risk_action": "default",
      "international_format_phone": None
    },
    "plan": None,
    "id": 4099490251
  }    
}

mock_transaction_timeline = {
  "status": True,
  "message": "Timeline retrieved",
  "data": {
    "start_time": 1724318098,
    "time_spent": 4,
    "attempts": 1,
    "errors": 0,
    "success": True,
    "mobile": False,
    "input": [],
    "history": [
      {
        "type": "action",
        "message": "Attempted to pay with card",
        "time": 3
      },
      {
        "type": "success",
        "message": "Successfully paid with card",
        "time": 4
      }
    ]
  }    
}

mock_transaction_totals = {
  "status": True,
  "message": "Transaction totals",
  "data": {
    "total_transactions": 42670,
    "total_volume": 6617829946,
    "total_volume_by_currency": [
      {
        "currency": "NGN",
        "amount": 6617829946
      },
      {
        "currency": "USD",
        "amount": 28000
      }
    ],
    "pending_transfers": 6617829946,
    "pending_transfers_by_currency": [
      {
        "currency": "NGN",
        "amount": 6617829946
      },
      {
        "currency": "USD",
        "amount": 28000
      }
    ]
  }    
}

mock_export_transactions = {
  "status": True,
  "message": "Export successful",
  "data": {
    "path": "https://s3.eu-west-1.amazonaws.com/files.paystack.co/exports/463433/transactions/Integration_name_transactions_1724324423843.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAI7CL5IZL2DJHOPPA%2F20240822%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20240822T110023Z&X-Amz-Expires=60&X-Amz-Signature=40525f4f361e07c09a445a1a6888d135758abd507ed988ee744c2d94ea14cf1e&X-Amz-SignedHeaders=host",
    "expiresAt": "2024-08-22 11:01:23"
  }    
}

mock_partial_debit = {
  "status": True,
  "message": "Charge attempted",
  "data": {
    "amount": 50000,
    "currency": "NGN",
    "transaction_date": "2024-08-22T11:13:48.000Z",
    "status": "success",
    "reference": "ofuhmnzw05vny9j",
    "domain": "test",
    "metadata": "",
    "gateway_response": "Approved",
    "message": None,
    "channel": "card",
    "ip_address": None,
    "log": None,
    "fees": 10350,
    "authorization": {
      "authorization_code": "AUTH_uh8bcl3zbn",
      "bin": "408408",
      "last4": "4081",
      "exp_month": "12",
      "exp_year": "2030",
      "channel": "card",
      "card_type": "visa ",
      "bank": "TEST BANK",
      "country_code": "NG",
      "brand": "visa",
      "reusable": True,
      "signature": "SIG_yEXu7dLBeqG0kU7g95Ke",
      "account_name": None
    },
    "customer": {
      "id": 181873746,
      "first_name": None,
      "last_name": None,
      "email": "demo@test.com",
      "customer_code": "CUS_1rkzaqsv4rrhqo6",
      "phone": None,
      "metadata": {
        "custom_fields": [
          {
            "display_name": "Customer email",
            "variable_name": "customer_email",
            "value": "new@email.com"
          }
        ]
      },
      "risk_action": "default",
      "international_format_phone": None
    },
    "plan": 0,
    "requested_amount": 50000,
    "id": 4099546180
  }    
}