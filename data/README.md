# TraCoin data

```
data/
    |---- data_class.py
    |
    |---- gemini/
    |        |---- gemini.py
    |
    |----......
```

### abstract base class

The `Data` class in `data_class.py` provides an abstract base class as interface to a certain data source. The base class implements

1. `save_data`, which writes the data into database

Each data source is encapsulated as a derived class from `Data`, with methods required to be implemented

1. `connect_data_api`: a generic method to connect to source API with certain parameters specified, e.g. url endpoint or headers
2. `fetch_data`: fetch all data wanted, save to database and return clean and jsonified data

### data sources

1. Gemini
   - historical data
     - 500 rows of recent trades
   - live data
     - current price
     - current order book information
2. Cryptocompare
   - TBD
3. Interactive Brokers
   - TBD