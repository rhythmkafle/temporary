'''
Ch5 - OOP in Python

Introduction
    - OOP is a programming paradigm that organizes code into classes and objects, allowing developers to model real-world entities within resuable and modular structures
    

Classes and Objects
    - class is a blueprint or template used to create objects
    - object is an instance of a class, which represents a real-world entity created using the class blueprint
'''

class Car:
    def __init__(self, brand):  # __init__ is a constructor
        self.brand = brand

    def drive(self):    # all functions within a class will contain "self" keyword
        print(f"The {self.brand} is driving")   # self keyword is similar to this keyword in JS and Java

my_car = Car("Toyota")
my_car.drive() # Output: The Toyota is driving

# Note: self keyword is required to be the first parameter in any method inside a class. It does not need to be called "self". You can also call it "abc", "123", "your_name" etc.

# If the class is empty, you can use the "pass" keyword, as discussed in previous chapters


'''
Encapsulation
    - OOP principle of bundling data and methods into a single unit i.e. class
    - restricts direct access for security and control
''' 

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Creating an object
account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300

# Trying to access private variable directly (won’t work)
# print(account.__balance)  # This will raise an error

# There is no true private values in python, its just a convention as mentioned in previous chapters

'''
Inheritance
    - OOP principle where one class (child) can inherit the attributes and methods from another class (parent)
    - allows code reuse and extension
    - syntax: class Child_class(Parent_class):

    - Types: single level, multi level, multiple, hierarchial
'''
# single level inheritance
class Animal:  # Parent class
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Child class
    def bark(self):
        print("Dog barks")

d = Dog()   # instantiating an object
d.speak()  # Inherited from Animal
d.bark()   # Own method


# Hierarchil Inheritance - basically the same as single level, but instead of just one class inheriting from parent, multiple classes inherit from the same parent
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
d.sound()  # Inherited from Animal
d.bark()

c = Cat()
c.sound()  # Inherited from Animal
c.meow()



# multi level inheritance
class Grandparent:
    def greet(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

c = Child()
c.greet()



# multiple inheritance
class Father:
    def skills(self):
        print("Driving")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()  # Calls Father.skills() due to order



# Super keyword - makes the child class inherit all the methods and properties from its parents
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname, "is amazing")

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)  # this is calling it's parents constructor, and all other functions that the parent has. This way, no need to write same functions over and over again

x = Student("Mike", "Olsen")
x.printname()   # Output: Mike Olsen is amazing


'''
Polymorphism:
    - many forms 
    - refers to methods/functions/operators with the same name that can be executed on many objects or classes
    - for eg: let's see the polymorphism using len() function in python
'''

greet = "Hello World!"
print(len(greet)) # Output: 12

my_tups = ("apple", "ball", "cat")
print(len(my_tups)) # Output: 3

'''
Here, when used on a string, len returns total character in that string. But when used in a tuple, then it will return number of items in that tuple. This is polymorphism in work in python. The same len() function can be used in one way while using with a string, and another way when used with a tuple


Class Polymorphism
    - having multiple classes, with the same method name
    - in the example below, all three classes have a method called move()
'''

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

# Output: Drive!    Sail!   Fly!

'''
Compile Time vs Run-Time Polymorphism
    - compile time is function overloading whereas runtime is function overriding
    - compile time is faster than runtime
    - compile time is less flexible than runtime

    - method overloading is not supported in python
'''


'''
Abstraction
    - OOP principle about hiding internal implementations of a process or a method from user
    - to declare an abstract class, first import the abc module
'''

from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def sound(self):  # Abstract method
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()  # Output: Bark

# Note: You can't make objects of abstract classes directly. They just define a structure


f'''
Defining a Class
    1. Adding Instance Variables 
        - defined using self keyword
        - stored in each object

    2. Adding Instance methods
        - operates on instance variables
        - always takes "self" as the first argument
        
    3. Adding Class Variables
        - shared by all instances
        - defined directly in the class body

    4. Adding Class Methods
        - works with class variables
        - use @classmethod and cls as the first argument

    5. Adding Static methods
        - does not require to instantiate an object 
        - can be acccessed directly

Example code:
'''
class Person:
    species = "Human"  # Class variable

    def __init__(self, name, age):
        self.name = name          # Instance variable
        self.age = age

    def greet(self):              # Instance method
        print(f"Hi, I'm {self.name} and I'm {self.age}.")

    @classmethod
    def show_species(cls):        # Class method
        print(f"Species: {cls.species}")

    @staticmethod
    def is_adult(age):            # Static method
        return age >= 18

p = Person("Alice", 20)
p.greet()
Person.show_species()
print(Person.is_adult(17))  # Output: False


'''
Constructors
    - special method called automatically when an object is instantiated
    - defined using __init__()
'''
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s = Student("Tom", "A")
print(s.name)   # Output: Tom
print(s.grade)  # Output: A


'''
Method Overloading
    - defining multiple methods with the same name but different arguments
    - python doesn't support it directly, but we can mimic it using *args
'''
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(1, 2))         # Output: 3
print(calc.add(1, 2, 3, 4))   # Output: 10

# Here, *args will take any number of argument, and hence mimics method overloading


'''
Method Overriding
    - when a child class defines a method with the same name and parameters as one in its parent class, replacing its behavior
'''
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):  # Overrides the parent method
        print("Dog barks")

d = Dog()
d.sound()  # Output: Dog barks


'''
Access Modifiers
    - control visibility of class members (variables/methods)
    - Python uses naming conventions, not strict rules.
'''

class Person:
    def __init__(self):
        self.name = "Public"       # Public
        self._age = 21             # Protected
        self.__salary = 50000      # Private

    def show(self):
        print(self.__salary)       # Accessible inside class

p = Person()
print(p.name)      # ✅ Works
print(p._age)      # ⚠️ Works (by convention, "protected"), works only in inherited classes if the rules were strict
# print(p.__salary)  ❌ Error


'''
Operator Overloading (remember the definition, example might not come in exam)
    - lets you change how operators like +, -, * work with your custom objects.
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overload +
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Output: (4, 6)


'''
Magic Methods
    - special methods that let you define how built-in operators and functions behave with your custom objects
    - all methods in the form __name__ are magic methods, eg: __init__, __str__ etc
'''
# Remembering only __init__ and __str__ is fine. __str__ will print a custom value when printing the object
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return abs(self.x) + abs(self.y)

p1 = Point(3, 4)
p2 = Point(1, 2)

print(p1)            # Output: Point(3, 4)  , this is due to __str__
print(p1 + p2)       # Output: Point(4, 6)
print(p1 == p2)      # Output: False
print(len(p1))       # Output: 7



'''
Exception Handling
    - deal with exceptions in a controlled way
    - it's like setting up a safety net, so that the code does not fail
'''
# Basic Syntax:
try:
    # Code that might throw an error
    risky_code()
except SomeException as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
else:
    # Code that runs if no exception occurs
    print("No errors!")
finally:
    # Code that runs no matter what (optional)
    print("This will run anyway.")


# Example
try:
    num = int(input("Enter a number: "))  # Might cause ValueError
    result = 10 / num  # Might cause ZeroDivisionError
except ValueError:
    print("Oops! That’s not a valid number.")
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")
else:
    print(f"The result is {result}")
finally:
    print("This block runs no matter what!")


'''
Custom Exceptions 
    - to create custom exceptions, first we need to inherit from the "Exception" class
    - this allows you to create your own type of error 
'''
# making the custom class
class CustomZeroDivisionError(Exception):
    def __init__(self, message="Cannot divide by zero!"):
        self.message = message
        super().__init__(self.message)  # necessary to remember

def divide(a, b):
    if b == 0:
        raise CustomZeroDivisionError("You cannot divide by zero!") # calling our custom exceptions
    return a / b

result = divide(10, 0)


'''
Modules and Packages
    - A module is simply a file containing Python code, such as functions, classes, and variables, that can be imported and reused in other Python programs.
    - A package is a collection of related modules grouped together in a directory. It allows you to organize and manage multiple modules.
    - This python code here ( Ch5.py ) is a module, all these python codes together ( Ch2.py ... Ch5.py )can be considered a package

    - package structure
        my_package/
            __init__.py
            module1.py
            module2.py
    
    - package must consist of a __init__.py file
    - We can use import keyword to bring in functionality from modules and packages
'''


'''
Enumeration
    - symbolic name for a set of values
    - we can use Enum class from enum module to create your own enumerations
'''
from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Accessing Enum values
print(Day.MONDAY)      # Output: Day.MONDAY
print(Day.MONDAY.name) # Output: 'MONDAY'
print(Day.MONDAY.value) # Output: 1
print(Day.TUESDAY.value) # Output: 2

'''
Why use Enums?
    - readability
    - prevents error as invalid values cannot occur, we are restricted to the set of defined names
    - maintainability as it helps in managing sets of related constants in a single place
'''


'''
Finished!!!
'''