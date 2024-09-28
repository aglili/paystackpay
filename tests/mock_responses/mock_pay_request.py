mock_create_pay_request = {
  "status": True,
  "message": "Payment request created",
  "data": {
    "id": 3136406,
    "domain": "test",
    "amount": 42000,
    "currency": "NGN",
    "due_date": "2020-07-08T00:00:00.000Z",
    "has_invoice": True,
    "invoice_number": 1,
    "description": "a test invoice",
    "line_items": [
      {
        "name": "item 1",
        "amount": 20000
      },
      {
        "name": "item 2",
        "amount": 20000
      }
    ],
    "tax": [
      {
        "name": "VAT",
        "amount": 2000
      }
    ],
    "request_code": "PRQ_1weqqsn2wwzgft8",
    "status": "pending",
    "paid": False,
    "metadata": None,
    "notifications": [],
    "offline_reference": "4286263136406",
    "customer": 25833615,
    "created_at": "2020-06-29T16:07:33.073Z"
  }    
}

mock_fetch_pay_request = {
  "status": True,
  "message": "Payment request retrieved",
  "data": {
    "transactions": [],
    "domain": "test",
    "request_code": "PRQ_53s49t73kq6qmsq",
    "description": "a test invoice",
    "line_items": [
      {
        "name": "item 1",
        "amount": 20000
      },
      {
        "name": "item 2",
        "amount": 20000
      }
    ],
    "tax": [
      {
        "name": "VAT",
        "amount": 2000
      }
    ],
    "amount": 42000,
    "discount": None,
    "currency": "NGN",
    "due_date": "2020-07-08T00:00:00.000Z",
    "status": "pending",
    "paid": False,
    "paid_at": None,
    "metadata": None,
    "has_invoice": True,
    "invoice_number": 1,
    "offline_reference": "4286263136406",
    "pdf_url": None,
    "notifications": [],
    "archived": False,
    "source": "user",
    "payment_method": None,
    "note": None,
    "amount_paid": None,
    "id": 3136406,
    "integration": 428626,
    "customer": {
      "transactions": [],
      "subscriptions": [],
      "authorizations": [],
      "first_name": "Damilola",
      "last_name": "Odujoko",
      "email": "damilola@example.com",
      "phone": None,
      "metadata": {
        "calling_code": "+234"
      },
      "domain": "test",
      "customer_code": "CUS_xwaj0txjryg393b",
      "risk_action": "default",
      "id": 25833615,
      "integration": 428626,
      "createdAt": "2020-06-29T16:06:53.000Z",
      "updatedAt": "2020-06-29T16:06:53.000Z"
    },
    "createdAt": "2020-06-29T16:07:33.000Z",
    "updatedAt": "2020-06-29T16:07:33.000Z",
    "pending_amount": 42000
  }    
}

mock_list_pay_request = {
  "status": True,
  "message": "Payment requests retrieved",
  "data": [
    {
      "id": 3136406,
      "domain": "test",
      "amount": 42000,
      "currency": "NGN",
      "due_date": "2020-07-08T00:00:00.000Z",
      "has_invoice": True,
      "invoice_number": 1,
      "description": "a test invoice",
      "pdf_url": None,
      "line_items": [
        {
          "name": "item 1",
          "amount": 20000
        },
        {
          "name": "item 2",
          "amount": 20000
        }
      ],
      "tax": [
        {
          "name": "VAT",
          "amount": 2000
        }
      ],
      "request_code": "PRQ_1weqqsn2wwzgft8",
      "status": "pending",
      "paid": False,
      "paid_at": None,
      "metadata": None,
      "notifications": [],
      "offline_reference": "4286263136406",
      "customer": {
        "id": 25833615,
        "first_name": "Damilola",
        "last_name": "Odujoko",
        "email": "damilola@example.com",
        "customer_code": "CUS_xwaj0txjryg393b",
        "phone": None,
        "metadata": {
          "calling_code": "+234"
        },
        "risk_action": "default",
        "international_format_phone": None
      },
      "created_at": "2020-06-29T16:07:33.000Z"
    }
  ],
  "meta": {
    "total": 1,
    "skipped": 0,
    "perPage": 50,
    "page": 1,
    "pageCount": 1
  }    
}

mock_verify_pay_request = {
  "status": True,
  "message": "Payment request retrieved",
  "data": {
    "id": 3136406,
    "domain": "test",
    "amount": 42000,
    "currency": "NGN",
    "due_date": "2020-07-08T00:00:00.000Z",
    "has_invoice": True,
    "invoice_number": 1,
    "description": "a test invoice",
    "pdf_url": None,
    "line_items": [
      {
        "name": "item 1",
        "amount": 20000
      },
      {
        "name": "item 2",
        "amount": 20000
      }
    ],
    "tax": [
      {
        "name": "VAT",
        "amount": 2000
      }
    ],
    "request_code": "PRQ_53s49t73kq6qmsq",
    "status": "pending",
    "paid": False,
    "paid_at": None,
    "metadata": None,
    "notifications": [],
    "offline_reference": "4286263136406",
    "customer": {
      "id": 25833615,
      "first_name": "Damilola",
      "last_name": "Odujoko",
      "email": "damilola@example.com",
      "customer_code": "CUS_xwaj0txjryg393b",
      "phone": None,
      "metadata": {
        "calling_code": "+234"
      },
      "risk_action": "default",
      "international_format_phone": None
    },
    "created_at": "2020-06-29T16:07:33.000Z",
    "integration": {
      "key": "pk_test_xxxxxxxx",
      "name": "Paystack Documentation",
      "logo": "https://s3-eu-west-1.amazonaws.com/pstk-integration-logos/paystack.jpg",
      "allowed_currencies": [
        "NGN",
        "USD"
      ]
    },
    "pending_amount": 42000
  }    
}

mock_send_notification = {
  "status": True,
  "message": "Notification sent"    
}