from data.gemini.gemini import GeminiData
from data.gdax.gdax import GDAXData

MODEL_MAPPING = {
    'gemini': GeminiData,
    'gdax': GDAXData,
}
