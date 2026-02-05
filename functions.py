def greet(): print("Hello World")
greet()

#Check weather
def check_weather():
    temperature = int(input("What's the temperature?"))
    if temperature <= 17: print("Cold")
    elif temperature > 17 and temperature <=26: print("Pleasant")
    else: print("Hot")

check_weather()

# Calculate total price including tax
def total_price():
    mrp = int(input("Enter MRP of a product"))
    tax = 18/100
    total_mrp = mrp + (tax * mrp)
    return total_mrp

total_price()

#Functions with parameters
def greet(name): print(f"Hello {name}")
greet("Abhishek")

def temperature(temp):
    if temp > 26: print("Hot")
    else: print("Cold")

temperature(25)

def name(first,last):
    print(f"Your firstName is {first} and lastName is {last}")

name("Abhishek","Y")

def greet(name, prefix = "Mr."):
    print(f"Hello {prefix} {name}")

greet("Abhishek")

def greet(first="Abhi", last="shake", prefix = "Mr."):
    print(f"Hello {prefix} {first} {last}")

greet()
greet(last="shek")

#return highest number of the two.
def highest(a,b):
    if a > b: return a
    else: return b

highest(1,2)

def highest(a,b):
    return max(a,b)

#Accept n number of parameters and find the highest of the lot
def highest(*args):
    return max(args)

highest(1,2,3,4,5,10,15,20)

#Returning multiple values from a function
def simple():
    num = [1,2,3,4,5]
    first = num[0]
    last = num[-1]
    return first, last

a, b = simple()
