mock_create_plans = {
  "status": True,
  "message": "Plan created",
  "data": {
    "name": "Monthly Platinum Session",
    "amount": 10000,
    "interval": "monthly",
    "integration": 100032,
    "domain": "test",
    "plan_code": "PLN_gx2wn530m0i3w3m",
    "send_invoices": True,
    "send_sms": True,
    "hosted_page": False,
    "currency": "NGN",
    "id": 28,
    "createdAt": "2016-03-29T22:42:50.811Z",
    "updatedAt": "2016-03-29T22:42:50.811Z"
  }    
}
mock_list_plans = {
  "status": True,
  "message": "Plans retrieved",
  "data": [
    {
      "subscriptions": [
        {
          "customer": 63,
          "plan": 27,
          "integration": 100032,
          "domain": "test",
          "start": 1458505748,
          "status": "complete",
          "quantity": 1,
          "amount": 100000,
          "subscription_code": "SUB_birvokwpp0sftun",
          "email_token": "9y62mxp4uh25das",
          "authorization": {
            "authorization_code": "AUTH_6tmt288t0o",
            "bin": "408408",
            "last4": "4081",
            "exp_month": "12",
            "exp_year": "2020",
            "channel": "card",
            "card_type": "visa visa",
            "bank": "TEST BANK",
            "country_code": "NG",
            "brand": "visa",
            "reusable": True,
            "signature": "SIG_uSYN4fv1adlAuoij8QXh",
            "account_name": "BoJack Horseman"
          },
          "easy_cron_id": None,
          "cron_expression": "0 0 * * 0",
          "next_payment_date": "2016-03-27T07:00:00.000Z",
          "open_invoice": None,
          "id": 8,
          "createdAt": "2016-03-20T20:29:08.000Z",
          "updatedAt": "2016-03-22T16:23:52.000Z"
        }
      ],
      "integration": 100032,
      "domain": "test",
      "name": "Satin Flower",
      "plan_code": "PLN_lkozbpsoyd4je9t",
      "description": None,
      "amount": 100000,
      "interval": "weekly",
      "send_invoices": True,
      "send_sms": True,
      "hosted_page": False,
      "hosted_page_url": None,
      "hosted_page_summary": None,
      "currency": "NGN",
      "id": 27,
      "createdAt": "2016-03-21T02:44:14.000Z",
      "updatedAt": "2016-03-21T02:44:14.000Z"
    },
    {
      "subscriptions": [],
      "integration": 100032,
      "domain": "test",
      "name": "Monthly retainer",
      "plan_code": "PLN_gx2wn530m0i3w3m",
      "description": None,
      "amount": 50000,
      "interval": "monthly",
      "send_invoices": True,
      "send_sms": True,
      "hosted_page": False,
      "hosted_page_url": None,
      "hosted_page_summary": None,
      "currency": "NGN",
      "id": 28,
      "createdAt": "2016-03-29T22:42:50.000Z",
      "updatedAt": "2016-03-29T22:42:50.000Z"
    }
  ],
  "meta": {
    "total": 2,
    "skipped": 0,
    "perPage": 50,
    "page": 1,
    "pageCount": 1
  }
}

mock_fetch_plan = {
  "status": True,
  "message": "Plan retrieved",
  "data": {
    "subscriptions": [],
    "integration": 100032,
    "domain": "test",
    "name": "Monthly retainer",
    "plan_code": "PLN_cfd3s2sdmqxravk",
    "description": None,
    "amount": 50000,
    "interval": "monthly",
    "send_invoices": True,
    "send_sms": True,
    "hosted_page": False,
    "hosted_page_url": None,
    "hosted_page_summary": None,
    "currency": "NGN",
    "id": 28,
    "createdAt": "2016-03-29T22:42:50.000Z",
    "updatedAt": "2016-03-29T22:42:50.000Z"
  }
}

mock_update_plan = {
  "status": True,
  "message": "Plan updated. 1 subscription(s) affected"    
}