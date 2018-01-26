# TraCoin api

```
api/
    |---- api_class.py
    |
    |---- gemini/
    |        |---- gemini_auth.py
    |        |---- gemini.py
    |
    |----......
```

### abstract base class

The `Api` class in `api_class.py` provides an abstract base class as interface to a certain exchange. The base class implements

1. `save_data`, which writes the data into database

### exchange authentication class

Exchanges require auth/signature to use the private API. The exchange auth class defines the AuthBase derived class used for GET request authentication.

### exchange class

Each exchange source are encapsulated as a derive class from `Api`, with methods required to be implemented

1. `query_account`: query account summary information, e.g. balance, position
2. `query_order`: query order information, either for all active orders or specify order id
3. `send_limit_order`: place a new limit order
4. `send_market_order`: place a new market order
5. `cancel_order`: cancel an order with order id specified or cancel all active orders
