'''
Chapter 4 - Functions 
    - function is a block of reusable code that performs a specific task
    - defined using the def keyword


Benefits of using Function
    - Reusability of code
    - Readability of code
    - Maintainability of code
    - Organization of code
    - Modularity i.e. breaking big problems into small tasks


Creating and calling functions 
    - to create functions, we use the def keyword
    - to call a function, we write its name followed by a parantheses
'''

# defining a func
def say_hello():
    print("Hello there!")

# calling a func
say_hello() 

'''
Passing arguments in a function
    - arguments are the values you pass to a function while calling it
    - parameters are variables inside a function that receives a value
'''

# defining function with parameters
def say_hello(name):
    print(f"Hello {name}!")

# Passing arguments while passing a function
say_hello("Rhythm")

# Passing Multiple arguments
def say_hello(name, age):
    print(f"Hello {name} who is {age} years old.")

say_hello("Rhythm", 21)

'''
Default Arguments
    - if no arguments are passed, then we can set default arguments
    - in case of no arguments being passed, the parameter will be assigned the default value
'''
def say_hello(name="Rhythm", age=21):
    print(f"Hello {name} who is {age} years old")

say_hello() # Even if we don't pass any arguments, it is not an error as defult arguments have been passed

'''
Keyword Arguments
    - you can also pass an argument by specifying the variable names while calling a function
'''
def say_hello(name, age):
    print(f"Hello {name} who is {age} years old")

say_hello(name="Rhythm", age=21)

'''
*args and **kwargs
    - *args takes any number of values passed by the user
    - **kwargs takes any number of keys and values, that is dictionary styled data
'''

# demo of args
def demo_args(*args):
    print(args) # output: (1, 2, 3, 4, 'Hello', 'Infinityyy')

demo_args(1,2,3,4,"Hello", "Infinityyy")

# demo of kwargs
def demo_kwargs(**kwargs):
    print(kwargs) # Output: {'a': 1, 'b': 2, 'name': 'rhythm', 'age': 21}

demo_kwargs(a=1,b=2,name="rhythm",age=21)


'''
Packing and Unpacking arguments
    - packing is collecting multiple values to a single variable
    - unpacking is the breaking a collection into individual variables or arguments
    - we achieve this using *args, **kwargs, tuples an dictionaries
'''
# packing demonstration using args and tuples
def demopack_args(*args):
    print(args)

data = (1,2,3,4,"apple","ball")
demopack_args(data) # we are sending a tuple called data into the function, where *args will read all the value and store it. This is packing with tuples

#unpacking demo using tuples
def unpack_demo():
    tups = (1,2,3)
    return tups

a,b,c = unpack_demo() # (1,2,3) is returned from the function, and they will be unpacked into a, b, c respectively. a=1, b=2 and c=3 after this


'''
Return values and returning multiple values
    - uses the return keyword
    - we can return multiple values using a tuple ( same as unpacking )
'''
def calc(a, b):
    return (a + b, a * b)  # Returns a tuple

result = calc(2, 3) # creates a tuple result
print(result)           # output: (5, 6)

sum_, product = calc(2, 3)  # Unpacking and storing on individual values
print(sum_, product)        # output: 5 6

'''
Recursive Function
    - it is a function that calls itself to solve smaller parts of a problem
    - it works until a base case is satisfied

    - given below are some questions that may come in exam
'''

# factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # Output: 5

# sum of natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

print(sum_natural(5))  # Output: 15 (1 + 2 + 3 + 4 + 5)

# gcd
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))  # Output: 6

# prime or not
def is_prime(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor - 1)

print(is_prime(11))  # Output: True
print(is_prime(10))  # Output: False


'''
Lambda Functions
    - small anonymous function defined using the lambda keyword
    - it can take any number of arguments, but can only have one expression
    - can be used as a shorthand for a regular function
''' 

# a regular function
def add(a,b):
    return a + b

# a lambda function
add_lambda = lambda x, y: x+y # here, x ,y before : are parameters, and x + y after : is being returned and stored in add_lambda variable

'''
Finished!!!
'''