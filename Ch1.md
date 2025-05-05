Ch1 Python

# Introduction
    Python is a high-level, easy-to-read programming language used to build websites, software, automate tasks, analyze data, and more.

# Why Python?
    Easy to learn
    Versatile: Used in alot of domains
    Huge Community
    Cros-Platform
    High Job Demand
    Free and Open Source
    Lots of libraries help in easy development
    Very readable and portable code
    
# Virtual Environment in Python
    A virtual environment is like a separate folder where you install Python tools just for one project, so they don’t mess with other projects. 
    
    ## Why use it?
        Keeps dependencies of a project separate
        Prevents version conflicts between different projects
        Makes your projects easier to share and maintain
        
    ## How to create and initialize a Virtual Environment:
        ```
        python -m venv myenv
        source  myenv/bin/activate ( For Linux based systems)
        myenv\Scripts\activate ( For Windows )
        ```

# Writing Comments
    Comments are notes in your code that the compiler ignores.
    
    Types of Comments:
    1. Single Line
        # This is a comment
        
    2. Multi-line Comment
        '''
        This is a 
        comment
        too.
        '''

# Indentations
    Indentations means spaces at the beginning of a line.
    It is compulsory to have proper indentations in Python.
    It defines blocks of code, and without it, python throws an error.
    
    eg: 
    ```
    if age<18:
        print("You are a minor")
    ```

    The space before print is indentation.
    
# Tokens
    They are the smallest elements of code that has meanings. All statements and instructions are built with tokens.
    
    There are various types of tokens:
    
    1. Keywords: 
        - words having special meanings
        - can't be used as variable names
        - used for their special features
        - python has 33 keywords
        
        eg: if, elif, for, while, try, True, False etc.   
 
    2. Identifiers:
        - names given to any variables, functions, class, lists, etc for their identification
        - case sensitive i.e. apple and Apple are different
        - can start only with alphabets and _
        - special characters and whitespaces are forbidden
        - keywords are forbidden
        
        eg: name = "Rhythm"
        Here, name is an identifier
        
    3. Literals: 
        - fixed values or constants 
        - python supports various types of literals:
        
        a. string:
            name = "Rhythm"
            "Rhythm" is a string literal
            
        b. character: 
            grade = "a"
            "a" is a character literal
            
        c. numeric:
            - can be integer, float or complex
            
            eg of int: 
                age = 18
            
            eg of float:
                price = 69.9
            
            eg of complex:
                smth = 3 + 4j
                
        d. boolean:
            - True, False
            
        e. special:
            - None
            
            eg: 
                smth = None
                
        f. collections:
            - lists, sets, dictionaries, tuples 
            
            
    4. Operators:
        - tokens to perform operations
        - can be unary or binary
        
    5. Punctuators:
        - symbols used to organize structures
        - {},(),@, etc.
         
# Variables and Constants
    - Variables store data that can change while your program runs
    - constants stores data that should not change once set
    
    eg of variables:
        ```
        name = "Rhythm"
        ```
    
    eg of constants:
        ```
        PI = 3.14
        MAX_USERS = 60
        ```
        
    NOTE: PYTHON DOES NOT HAVE ACTUAL CONSTANTS. THEY ARE CONSTANTS BY NAMING CONVENTION ONLY
    
# Operators
    Types:
    
    1. Arithmetic
        +, -, *, /, %
    
    2. Comparision
        <, >, ==, !=, <=, >=
        
    3. Logical
        and, or, not
        
    4. Bitwise
        &, |, ~, ^, >>, <<
        
    5. Assignment
        =, +=, -=, *=, /=
       
    6. Identity
        is, is not
        
    7. Membership
        in, not in
        
    8. Ternary
        - shortcut for if-else
        
        [vaalue_if_true] if [condition] else [value_if_false]
        
        eg: 
        ```
        status = "adult" if age>18 else "minor"
        ```
        
# id() function
    - returns a unique identifier for an object in memory
    - helps you know if two objects are actually same or if they just have the same value
    
    ```
    id(object)
    ```
    
    eg:
    ```
    a = 10
    print(id(a))
    ```
    Prints the memory address where a is stored
    


