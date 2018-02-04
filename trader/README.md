# TraCoin trader

```
trader/
    |---- trader.py
    |---- risk_manager.py
```

### trader module

`trader` module implements two classes

1. `Trader`: trading execution
   - calls `Strategy` for signal generation and target position generation
   - calls `Backtester` for trading market value calculation
   - calls `Api` for order execution
2. `RiskManager`: portfolio risk evaluation
   - calculate performance and several risk metrics
   - perform actions like stop-loss or cancel order through `Api`
