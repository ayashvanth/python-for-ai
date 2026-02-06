#Variables
age = 32
print(age)

power = 5 ** 5
print("Answer = " + str(power))

userName = "Abhishek"

long_string = """
This is a big comment 
getting stored as a string
"""

#DataTypes
firstName = "Abhishek"
lastName = "Y"
fullName = firstName + " " + lastName

fullName = firstName + lastName # No Space

dash = "-"
longDash = dash * 30
len(longDash)

userInput = input("Enter your Name")
print("Your name is", userInput)

age = 18
can_vote = age>=18

age = 20
has_license = True
can_drive = age >= 18 and has_license
print(can_drive)

age = 19
has_license = True
drunk = True
can_be_penalized = age <= 18 and has_license and not drunk
print(can_be_penalized)

#F-strings (Formatted String Literals)
name = input("Please provide your name: ")
print(f"Hi {name}! What can I do for you?")

name = "NaVya"
name.lower()
name.upper()
name.title()

name = "python program"
name.title()

sentence = """
Python programming is a good programming language.
It is easy and good for beginners to learn.
It is good for designing AI models.
"""

print(sentence.count("good"))
sentence.find("good")

newSentence = sentence.replace("good","bad")
print(newSentence)

#formatted string liberals
name = input("Enter name: ")
age = input("Enter age: ")
print(f"Your name is {name} and your age is {age}")

# if-elif condition
marks = int(input("Enter your marks: "))
if marks > 35:
    print("Pass")
elif marks == 35:
    print("Re-evalution")
else:
    print("Fail")

#Single line condition
marks = 35
result = "Pass" if marks > 35 else "Re-evaluation" if marks == 35 else "Fail"
print(result)

a = 100
print("Yes" if a == 20 else "No")

#Driver licence and age criteria to drive
has_license = True
age = 18
print("Can drive" if age > 18 and has_license else "Cannot drive")

temperature = int(input("What is the temperature in your region?"))
if temperature < 18:
    print("It's cold")
elif temperature >= 18 and temperature < 28:
    print("Pleasant weather")
else: 
    print("It's hot")

# for loop
for i in range(5): print(i)
for i in range(1,6): print(i)
for i in range(0,10,2): print(i)
for i in range(0,10,3): print(i)

#List
my_list = ["Navya", 30, True]
name = my_list[0]; print(name)
age = my_list[1]; print(age)
has_license = my_list[2]; print(has_license)
has_license = my_list[-1]; print(has_license)
name = my_list[-3]; print(name)
new_list = my_list[0:1]; print(new_list)
new_list = my_list[1:2]; print(new_list)

numbers = [1,2,3,4,5,10]
numbers[1:2]
numbers.append(6)
numbers
numbers.insert(1,0)
numbers.remove(0)
numbers[:2]
numbers[0] = 0
numbers.remove(0)
numbers.insert(0,0)
del numbers[3]
last = numbers.pop(); last

dry_fruits = ["Almonds", "Cashew", "Raisins", "Walnut", "Pista"]
dry_last = dry_fruits.pop()
dry_fruits
dry_last
dry_fruits.index("Almonds")

names = ["Abhi", "ABhi", "Abhi", "Navya", "NavyA"]
names.count("Abhi")
names.index("NavyA")
names.index("Abhi")

num = [3,4,1,6,2,0]
num.sort()
num.reverse()

list1 = [1,2,3]
list2 = list1
list2.append(4)
print(list1)

#Dictionary
person = {"name":"Abhishek","age":32,"city":"Mysore"}
person["name"] #remember it's not person[name] but person["name"]
person["name"] = "Abhishek"

person.keys()
person.values()
person.items()
person

for key, value in person.items():
    print(f"{key}:{value}")

person.clear()
person.update({"name":"Navya","age":30})


#Tuples
colours = ('red','green','blue')
colours[-3]
colours[1:2]
rgb = ["red","green","blue"]
rgb[1:2]
rgb[2]

single = (42)
type(single) #int

single = (42,)
type(single) #tuple

#Set
empty_set1=set()
empty_set2={}
scores = {1,1,1,2,3,4,5,5}
my_list = [1,1,1,2,4,"Abhishek",32,32]
unique = set(my_list)
unique

colours = {'red','green'}
colours.add('blue')
colours
colours.remove("yellow") #Error if not found
colours.discard("yellow") #No Error if not found
colours.discard("red")

"""
I need to define 2 functions with the same name "double". The first function should take only 1 argument and double it. The second function should take 2 arguments and multiply the values and return. If I pass double(2) it should give me 4 and double(2,3) should give me 6. Is it possible in python?
"""
def double(*args):
    if len(args) == 1:
        return args[0] * 2
    elif len(args) == 2:
        return args[0] * args[1]
    else:
        raise ValueError("Need to pass either 1 or 2 parameters")
    
double(2)
double(2,3)
double(2,3,4)


"""
list = [1,0,2,3,5,2,0,3,4,6]
Remove all zeros and append it at the end of the list
"""

list = [1,0,2,3,5,2,0,3,4,6]

for item in list:
    if item == 0:
        list.remove(item)
        list.append(item)

print(list)

"""
Create a list 1,2,3,4 using range function
"""

list = []

for item in range(1,5):
    list.append(item)

print(list)