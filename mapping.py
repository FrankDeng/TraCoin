from models import CurrentPrice, OrderBook, RecentTrades, HistoricalPrices

from data.gemini.gemini import GeminiData
from data.gdax.gdax import GDAXData


DB_TABLES = {
    'cur': CurrentPrice,
    'ob': OrderBook,
    'trade': RecentTrades,
    'hist': HistoricalPrices,
}


DATA_MODELS = {
    'gemini': GeminiData,
    'gdax': GDAXData,
}
