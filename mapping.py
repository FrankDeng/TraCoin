from data.gemini.gemini import Gemini
from data.gdax.gdax import GDAX

MODEL_MAPPING = {
    'gemini': Gemini,
    'gdax': GDAX,
}
