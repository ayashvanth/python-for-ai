import os

import pandas
from dotenv import load_dotenv

print(type(pandas))  # Packages - find under .venv/lib
print(type(os))  # module - system-path

print(os.__file__)
# /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/os.py

# Reading the .env file
load_dotenv()

api_key = os.environ.get("API_KEY")
debugMode = os.environ.get("DEBUG")

print(api_key)
print(debugMode)
