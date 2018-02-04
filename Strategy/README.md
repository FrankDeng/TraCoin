# TraCoin strategy

```
strategy/
    |---- strategy_class.py
    |
    |---- strategy_xxx/
    |        |---- strategy_xxx.py
    |        |---- strategy_xxx_constants.py
    |        |---- strategy_xxx_utils.py
    |
    |----......
```

### abstract base class

The `Strategy` class in `strategy_class.py` provides an abstract base class as interface to a certain trading strategy.

Each strategy is encapsulated as a derived class from `Strategy`, with methods required to be implemented

1. `get_data`: a generic method to fetch required data for signal generation through an instance of `DataHandler`
2. `generate_positions`: generate target positions in form of ticker-percentage pairs
