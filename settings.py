import os

# database URI
SQL_URI = 'postgres://localhost:5432/tracoin'

# exchange access key
GEMINI_KEY = os.environ.get('GEMINI_KEY')
GEMINI_SECRET = os.environ.get('GEMINI_SECRET')
