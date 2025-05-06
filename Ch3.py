'''
Ch 3
Built-in Data Types
'''

'''
Numeric Types
    - int, float, complex
'''

age = 21    # int
price = 69.96   # float
smth = 3 + 4j   # complex

print(age, price, smth) # Output : 21 69.96 (3+4j)


'''
Methods available for these types:
    1. for Int and Float
        abs(x) → absolute value
        round(x) → rounded value
        pow(x, y) → x raised to y
        divmod(x, y) → returns (x // y, x % y)
        int() / float() → type conversion

    2. for complex
            .real → real part
            .imag → imaginary part
            abs(complex_num) → magnitude
'''


'''
String 
    - sequence of characters surrounded by single or double quotes
'''

name = "Rhythm"
for i in name:
    print(i)

''' Output: Letters of my name in differen lines
    R
    h
    y
    t
    h
    m
'''


'''
Common methods is String
    .lower() -> converts all to lower
    .upper() -> to upper
    .strip() -> removes spaces from both ends
    .split(delimeter) -> splits the string to a list based on a delimeter(, space etc)
    .startswith() / .endswith() 
'''

'''
String slicing
    - returning only a small part of the entire string
'''

text = "Hello baby"
print(text[2:5]) # Output: llo, start at index 2...end at index 5
print(text[:5]) # Output: Hello, start at index 0...end at index 5
print(text[7:]) # Output: aby, start at index 7...end at last index
print(text[-6:-2]) # Output: o ba, start at index -6...end at index -2


'''
String Formatting
    - we can combine strings and numbers using f-strings or the format() method

F-Strings:
    - put f before the string, add curly brackets where you want to insert code/values
'''

name = "Rhythm"
age = 22
print(f"Hello, I am {name} and I am {age} years old.")


print(f"The price of 5 kg paneer is: {1100 * 5} rupees")


'''
Escape Sequence
    - special characters combinations used to represent characters that are difficult to type or that has special meanings

    \n -> New line
    \r -> Carriage return
    \t -> tab
    \b -> backspace
    \' -> '
    \\ -> \
    \'\' -> ''
'''

print("This will have \n \btwo lines")


'''
Boolean
    - data type that represents either True or False
    
    Common Boolean Operations:
    and, or, not
'''

x = 10
y = 9
print(x<y) # False
print(x==y) # False
print(not(x < y)) # True


'''
Lists
    - ordered mutable collection of items that can hold elements of different data types
'''

subjects = ["python", "IS", "AI", "Marketing", "SDAD"]
print(subjects[1]) # prints the element at index 1 i.e. IS

'''
Lists Slicing
    - done in the same way string slicing is done
    - list[start_index:end_index]
'''

print(subjects[1:3]) # OutputL IS, AI (start from 1, till 3-1th positon)
print(subjects[:3]) # Output python, IS, AI
print(subjects[3:]) # Output Marketing, SDAD

'''
Changing List Items
    - we can replace list items by simply calling the index of the list and assigning a new value
'''

subjects[1] = "Security"
print(subjects) # Output: ['python', 'Security', 'AI', 'Marketing', 'SDAD'], Here, IS is replaced by Security

subjects.append("a new subject") # This will add to the end of the subjects list
print(subjects) # Output: ['python', 'Security', 'AI', 'Marketing', 'SDAD', 'a new subject']

# You can also insert new values at a specific index
subjects.insert(1, "I Dont know")
print(subjects) # ['python', 'I Dont know', 'Security', 'AI', 'Marketing', 'SDAD', 'a new subject'], "I dont know" was inserted in index 1

'''
You can also add one list onto another
'''
list1 = ['random', 'list', '1']
list2 = ['another', 'random', 'list']
list1.extend(list2)
print(list1) # Output: ['random', 'list', '1', 'another', 'random', 'list']

# You can also use extend method to add tuples an dictionaries

'''
Removing List Items
'''
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

fruits.pop(1) # removes the item in index 1, If index is not specified, the last item will be removed

del fruits[0] # also removes the item in index 0, if no index is given, deletes the entire list

fruits.clear() # clears all the items in a list

'''
Looping a list
    - can be used to print all the items in a list
'''
animals = ["ape", "bear", "cat"]

#Using For loop
for animal in range(len(animals)):
    print(animal)

#Using While loop
i = 0
while i < len(animals):
    print(animals[i])
    i = i + 1

#Using List Comprehension
[print(x) for x in animals] # Syntax: [expression for item in list if condition == True], Here, we have not given condition, not necessary

'''
Sorting in Lists
'''
num_list = [5,4,3,2,1,0]
num_list.sort() # automatically sorts the whole list
num_list.sort(reverse=True) # Sorts in descending

num_list.reverse() # does not sort in descending order, just reverses how the list is right now

'''
Copying in lists
'''
list1 = ["I", "dont", "know"]
list2 = list1.copy()
list3 = list(list1)
list3 = list1[:]

'''
Joining Lists
'''
list1 = ["I", "dont", "know"]
list2 = ["he", "he", "he"]

# Method 1, use '+' sign
list3 = list1 + list2

# Method 2, loop through the list and append the values
for i in list2:
    list1.append(i)

# Method 3, extend method
list1.extend(list2)



'''
Tuples
    - ordered, immutable lists of objects
    - written with round brackets
    - tuple allows duplicate values
'''

mytuple = ("apple", "banana", "cherry")

'''
Accessing Tuples
    - accessing tuples is same as accessing lists, use index values to access
    - you can also use slicing in tuples, just like in lists
'''
print(mytuple[1])
print(mytuple[1:3])

'''
Updating Tuples
    - Tuples can't be changed easily
    - They first have to be changed to lists, and only then can they e updated
    - After being changed to lists, all the methods used in tuples are the same as a list
'''
x = (1,2,3)
x2 = list(x)
#Now, you can update the tuple values

'''
Unpacking Tuples
    - you can assign the values of tuple to different variables all at the same time
'''
a, b, c = (1,2,3) # 1 is assigned to a, 2 to b and 3 to c

fruits = ("apple", "ball", "cat")
fruit1, fruit2, fruit3 = fruits # apple to fruit1, ball to fruit2 anf cat to fruit3

'''
If the number of variable is less that no. of items, then an asterisk sign is used
'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

'''
Loop through a tuple
    - same way as you would loop through a list
'''
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 

#Using the index value:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i]) 


'''
Joining Tuples
    - by using +
'''

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2

print(tuple3)




'''
Sets in Python
    - unordered, immutable, unindexed collection of data
    - you cannot access sets using index as there is no index
    - written with curly brackets
    - duplicate values are not allowed i.e. same value cannot be written more than once
'''

myset = {"apple", "ball", "cat"}
print(myset)
print(len(myset))

'''
    - Just like previous lists and tuples, set can be of any type
    - set can contain any type of data
'''
set1 = {"abc", 34, True, 40, "male"} 

'''
    - Just like previously, you can also create a set by using a constructor (eg: list())
'''

set2 = set(("apple","ball"))

'''
Accessing set items
    - You cannot access items in a set by referring to an index or a key.
    - But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
'''

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

'''
Adding items in a set
    - using .add()
    - using .update()

'''

# .add()
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# .update() - this adds the items of one list to another. Similar to .extend() function learnt previously
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

'''
Removing items in a set
    - using .remove()
    - using .discard()
    - using .pop()
    - using .clear()
    - using del


    - this is same as done previously
'''

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
thisset.discard("apple")
print(thisset) 
#Others are same as previous
#Note: Sets are unordered, so you don't know which element will be removed while using .pop()

'''
Looping set is same as previous
for x in myset:
    # Do whatever you want here
'''

'''
Set operations
    - union, intersection, difference, symmetric difference
'''

# Union - joins both the sets
set1 = {"a", "b", "c"} 
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) 

# Intersection - only the common elements
set4 =set1.intersection(set2)
print(set4)

# difference - keeps the items from the first set that are not in the other set
set5 = set1.difference(set2)
print(set5) # Output: {'c', 'b', 'a'}

# Symmetric differences - only keeps the elements that are NOT PRESENT IN BOTH THE SETS i.e. that are NOT COMMON IN BOTH THE SETS
set6 = set1.symmetric_difference(set2)
print(set6) # OUtput: {1, 2, 3, 'a', 'b', 'c'} , this may seem like union, but it is not


'''
Frozen Sets in python
    - they are an immutable version of a set
    - once created, it cannot be updated
    - they can be created using the frozenset() function
    - you cannot perform any updates, however, you can use Set Operations (union, intersection,...) to it
'''

animals = frozenset(["cat", "dog", "lion"])
animals2 = frozenset(["human", "dog", "tiger"])

animals3 = animals.intersection(animals2)
print(animals3) # Output: frozenset({'dog'})




'''
Dictionaries in Python
    - ordered collection of key value pairs
    - does not allow duplicates
    - written with curly brackets, and key-value pairs 
    - just like all other collections we have learnt(lists, sets, tuples), dictionary can contain any data types
    - can also be made using the dict() keyword
'''
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(len(thisdict))

#using dict() keyword
thisdict = dict(name = "John", age = 36, country = "Norway")

'''
Accessing Items in Dictionaries
    - by referring key
    - using .get() method
    - using .keys() method
    - using .values() method
    - using .items() method
'''
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# by referring key
print(thisdict["model"]) # output: Mustang

# using .get() method
print(thisdict.get("model")) # output: Mustang

# using .keys() - returns list of all the keys in the dictionary
print(thisdict.keys()) # OUtput: dict_keys(['brand', 'model', 'year'])

# using .values() - returns list of all the values in the dictionary
print(thisdict.values()) # output: dict_values(['Ford', 'Mustang', 1964])

# using .items() - returns all keys and values, as tuples in a list 
print(thisdict.items()) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

'''
Changing values in a dictionary:
    - by referring to it's key
    - by using the .update() method
'''

# by referring to its key
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018 # changes the year to 2018

# by using .update() method
thisdict.update({"year": 2020})

'''
Updating values in a dictionary
    - same way as changing the values, by referring to key and using the update method
'''

# By referring to a key
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["owner"] = "Rhythm" # adds a key owner, with the value Rhythm

# Using the .update() method
thisdict.update({"owner": "Rhythm"})

'''
Deleting the items in a dictionary
    - using .pop()
    - using .popitem()
    - using del keyword
    - using .clear() method
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "owner": "Rhythm"
}

# using .pop() - removes the item with the specified keyname
thisdict.pop("year")

# using .popitem() - removes the last inserted item (in our case, removes "owner": "Rhythm")
thisdict.popitem()

# Using del keyword - removes the item with the specified keyname
del thisdict["model"]

# using .clear() method - empties the whole dictionary
thisdict.clear()

'''
Looping through a dictionary
    - using .values()
    - using .keys()
    - using .items()
'''

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# using .values() - returns only the values
for x in thisdict.values():
    print(x, end=" ") # output: Ford Mustang 1964

# using .keys() - returns only the keys
for x in thisdict.keys():
    print(x, end=" ") # output: brand model year

# using .items() - returns both keys and values
for x, y in thisdict.items():
    print(x, y) 
    ''' Output: 
                brand Ford
                model Mustang
                year 1964
    '''


'''
Copying dictionaries
    - using .copy() method
    - using dict() constructor
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# using .copy()
new_dict = thisdict.copy()

# using dict()
new_dict = dict(thisdict)



'''
Binary Types in Python
    - we can work with bits and bytes in python too using the binary types
    - if you add a 'b' before any string, it is no longer a string. It now becomes a byte
'''

this_is_a_byte = b'hello'
print(this_is_a_byte) # Output: b'hello'

'''
Bitwise operations
    - |, &, ^, >>, <<
'''


'''
None Types in Python
    - there is only one None type object during a code execution, and hence it is called as singleton object
    - None is not zero
    - None is not empty string
    - None is not False
    - when a variable does not have any meaningful initial value, you can assign it as None
'''

state = None
if state is None:
    state = "start"

print(state) # since state did not have any meaningful initial value, we initialized it as None


'''
Ch2 Finished!!!
'''