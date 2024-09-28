mock_create_customer_response = {
  "status": True,
  "message": "Customer created",
  "data": {
    "email": "test@example.com",
    "integration": 100032,
    "domain": "test",
    "customer_code": "CUS_ng9mw56ma4cx6x9",
    "id": 1173,
    "identified": False,
    "identifications": None,
    "createdAt": "2016-03-29T20:03:09.584Z",
    "updatedAt": "2016-03-29T20:03:09.584Z"
  }    
}

mock_update_customer_response = {
  "status": True,
  "message": "Customer updated",
  "data": {
    "integration": 100032,
    "first_name": "UpdatedFirstName",
    "last_name": "UpdatedLastName",
    "email": "bojack@horsinaround.com",
    "phone": None,
    "metadata": {
      "photos": [
        {
          "type": "twitter",
          "typeId": "twitter",
          "typeName": "Twitter",
          "url": "https://d2ojpxxtu63wzl.cloudfront.net/static/61b1a0a1d4dda2c9fe9e165fed07f812_a722ae7148870cc2e33465d1807dfdc6efca33ad2c4e1f8943a79eead3c21311",
          "isPrimary": True
        }
      ]
    },
    "identified": False,
    "identifications": None,
    "domain": "test",
    "customer_code": "CUS_ng9mw56ma4cx6x9",
    "id": 1173,
    "transactions": [],
    "subscriptions": [],
    "authorizations": [],
    "createdAt": "2016-03-29T20:03:09.000Z",
    "updatedAt": "2016-03-29T20:03:10.000Z"
  }
}

mock_list_customer_response = {
  "status": True,
  "message": "Customers retrieved",
  "data": [
    {
      "integration": 463433,
      "first_name": None,
      "last_name": None,
      "email": "dom@gmail.com",
      "phone": None,
      "metadata": None,
      "domain": "test",
      "customer_code": "CUS_c6wqvwmvwopw4ms",
      "risk_action": "default",
      "id": 90758908,
      "createdAt": "2022-08-15T13:46:39.000Z",
      "updatedAt": "2022-08-15T13:46:39.000Z"
    },
    {
      "integration": 463433,
      "first_name": "Okiki",
      "last_name": "Sample",
      "email": "okiki@sample.com",
      "phone": "09048829123",
      "metadata": {},
      "domain": "test",
      "customer_code": "CUS_rki2ccocw7g8lsj",
      "risk_action": "default",
      "id": 90758301,
      "createdAt": "2022-08-15T13:42:52.000Z",
      "updatedAt": "2022-08-15T13:42:52.000Z"
    },
    {
      "integration": 463433,
      "first_name": "lukman",
      "last_name": "calle",
      "email": "lukman@calle.co",
      "phone": "08922383034",
      "metadata": {},
      "domain": "test",
      "customer_code": "CUS_hpxsz8c1if90quo",
      "risk_action": "default",
      "id": 90747194,
      "createdAt": "2022-08-15T12:31:13.000Z",
      "updatedAt": "2022-08-15T12:31:13.000Z"
    }
  ],
  "meta": {
    "next": "Y3VzdG9tZXI6OTAyMjU4MDk=",
    "previous": None,
    "perPage": 3
  }    
}

mock_fetch_customer_response = {
  "status": True,
  "message": "Customer retrieved",
  "data": {
    "transactions": [],
    "subscriptions": [],
    "authorizations": [
      {
        "authorization_code": "AUTH_ekk8t49ogj",
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
      }
    ],
    "first_name": None,
    "last_name": None,
    "email": "test@example.com",
    "phone": None,
    "metadata": None,
    "domain": "test",
    "customer_code": "CUS_c6wqvwmvwopw4ms",
    "risk_action": "default",
    "id": 90758908,
    "integration": 463433,
    "createdAt": "2022-08-15T13:46:39.000Z",
    "updatedAt": "2022-08-15T13:46:39.000Z",
    "created_at": "2022-08-15T13:46:39.000Z",
    "updated_at": "2022-08-15T13:46:39.000Z",
    "total_transactions": 0,
    "total_transaction_value": [],
    "dedicated_account": None,
    "identified": False,
    "identifications": None
  }    
}