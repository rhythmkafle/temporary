'''
Ch2 Python: Control Statements
'''

'''
Introduction
    - dictates the flow of execution of a program based on certain conditions
'''

'''
Selection Statements
    1. If Statements
'''

age = 18
if age < 18:
    print("You are a minor")

# If-else

if age < 18: 
    print("Minor")
else:
    print("Major? Lol")

# If-elif ladder

num = 69
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

'''
Selection statements
    2. Match-case Statements
        - similar to swich case statements. Python has a way of adopting stuffs and making them it's own 
        - default is denoted by an underscore
        - There is no need of a "break" keyword, Python does that for you
'''

day = "Sunday"
match day:
    case "Sunday":
        print("First day")
    case "Monday":
        print("Second day")
    case _:
        print("Idk, Some day in some calender, i guess")

'''
Using If-else as a ternary operator
'''

age = 18
status = "Adult" if age > 18 else "Minor"
print("You are a %s" % status)  # There are many ways to print, I prefer this one. It's just printing, nothing else


'''
Looping Statements
    1. For Loops
        - used to repeat a block of code for each item in a collection
'''

letters = ['a','b','c']
for characters in letters:
    print(characters)

# To loop through a range of numbers:
for i in range(10):
    print(i)

'''
Looping Statements
    2. While Loops
        - repeats a block of code for as long as its true
'''

while True:
    print("Infinite loop! Don't run without break")
    break

# A simpler while loop
i = 0
while i < 10:
    print(i)
    i = i + 1

'''
Else Clause after a for or while loop
    - runs only after the loop has finished executing
    - runs only if the loop completes on itself, i.e. no break statements should be executed    
'''

for i in range(10):
    print(i)
else:
    print("Loop finished without breaks")

# In a while loop
i = 0
while i <5:
    print(i)
    i = i+ 1
else:
    print("While loop finished without interruption")



'''
Break and continue statements
    - special keywords used inside loops to control their flow
    - break stops the loop immediately even if the condition is still true
    - continue skips the current loop and jumps to the next one
'''

# Break demonstration
for i in range(5):
    if i == 3:
        break
    print(i)

# Output: 0 1 2

# Now for continue

for i in range(5):
    if i == 3:
        continue
    print(i)

# Output: 0 1 2   4   


'''
Pass Statement
    - used as a placeholder for a code block when you don't yet have any code
    - prevents an error
    - Ellipsis(...) also does the same, but is not as safe as pass
'''

def pass_demonstrate():
    pass
