import os
from dotenv import load_dotenv

# Reading the .env file
load_dotenv()

api_key = os.environ.get('API_KEY')
debugMode = os.environ.get('DEBUG')

print(api_key)
print(debugMode)