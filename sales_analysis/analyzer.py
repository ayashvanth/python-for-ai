import os

# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "data/sales.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")

#---------------------#

import os

# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "../data/paris_weather.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")

#---------------------#

#Reading a csv file
with open("data/sales.csv","r") as file:
    content = file.read()

#---------------------#

import sys
print(sys.path)

#---------------------#


