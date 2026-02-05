class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} can eat")

    def sleep(self):
        print(f"{self.name} can sleep")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} can bark")

dog = Dog("Mark")

dog.eat() # Method present in parent but instance is of child class
dog.sleep() # Method present in parent but instance is of child class
dog.bark() # Method present in child


