# TraCoin
```
TraCoin/
    |---- data/
    |        |---- data_class.py
    |        |---- cryptocompare/
    |        |---- gemini/
    |        |---- ib/
    |---- generate_data.py
    |
    |---- api/
    |        |---- api_class.py
    |        |---- gemini/
    |        |---- ib/
    |
    |---- trader/
    |        |---- trader_class.py
    |        |---- strat_1.py
    |        |---- strat_2.py
    |        |---- ......
    |
    |---- constants.py
    |---- logger.py
    |---- models.py
    |---- settings.py
    |---- utils.py
```

### data module

Data module provides interfaces to several data source APIs.

###### commands

```shell
# create all tables and drop existing ones
python generate_data --create --drop
```

### api module

API module wraps exchange APIs for account information query and trading execution.

### trader module

Trader module provides a wrapped trading runner/executioner for each active strategy.

### auxiliary modules

1. `constants` includes some frequently queried constant values
2. `logger` records all the logs at various levels: INFO, DEBUG, WARNING, ERROR; logs are printed on the screen and also saved into local log files
3. `models` defines ORM through SQLALchemy for interaction between database and program
4. `settings` defines environment configuration constant variables, e.g. database URI, log directory, etc.
5. `utils` implements several commonly used utility functions, e.g. database connection and insert, etc.