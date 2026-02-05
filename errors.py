# This will crash if the file doesn't exist
with open('data.txt', 'r') as f:
    content = f.read()
print("Done!")

# -------------------- #

# This keeps running even if file doesn't exist
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Could not find data.txt")
    content = "default data"
print("Done!")  # Always reaches here  # Never reaches here if file missing

# -------------------- #

try:
    age = int(input("Enter your age: "))
    print(f"In 10 years, you'll be {age + 10}")
except ValueError:
    print("Please enter a number")

# -------------------- #

import os
print(os.getcwd())

try:
    with open('data/paris_weather.csv', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
else:
    # This only runs if the file was opened successfully
    print(f"File has {len(data)} characters")