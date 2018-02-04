from data.gemini.gemini import GeminiData
from data.gdax.gdax import GDAXData

DATA_MODELS = {
    'gemini': GeminiData,
    'gdax': GDAXData,
}
