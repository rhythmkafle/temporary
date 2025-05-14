'''
Ch8 - Advanced Topics

Working with Database and SQL statements    
    - we will use SQLite3 for simplicity
'''
# Importing and connecting
import sqlite3
conn = sqlite3.connect('example.db')

# Creating a cursor and a table
c = conn.cursor()
c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

'''
A cursor is an object used to interact with a database. It allows you to execute SQL queries and fetch results.
'''

# Inserting Records
c.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25)) # Alice is set in the first ?,  25 in the second ?. This is called prepare and bind and helps in secure coding

# Fetching Records
c.execute("SELECT * FROM users")
print(c.fetchall())

# committing and closing
conn.commit()
conn.close()


# Proper example: to perform CRUD operations and print employees with salary > 25000: ( 10 marks )
import sqlite3

# Connect to database (or create it)
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    salary REAL
)
''')

# ------------------- CRUD OPERATIONS -------------------

# Create (Insert)
cursor.execute("INSERT INTO employees (name, age, salary) VALUES (?, ?, ?)", ("Alice", 30, 30000))
cursor.execute("INSERT INTO employees (name, age, salary) VALUES (?, ?, ?)", ("Bob", 25, 22000))
cursor.execute("INSERT INTO employees (name, age, salary) VALUES (?, ?, ?)", ("Charlie", 35, 27000))

# Read (Select)
print("\nEmployees with salary > 25000:")
cursor.execute("SELECT * FROM employees WHERE salary > 25000")
for row in cursor.fetchall():
    print(row)

# Update
cursor.execute("UPDATE employees SET salary = 28000 WHERE name = 'Bob'")

# Delete
cursor.execute("DELETE FROM employees WHERE name = 'Charlie' AND salary < 26000")

# Commit changes and close
conn.commit()
conn.close()


'''
Basics of GUI Programming 
    - we use tkinter for GUI programming
    - we need to import it to use it
'''

import tkinter as tk

'''
Creating the main window
'''
root = tk.Tk()  # creates the main application window
root.title("User Form") # sets the window's title
root.geometry("400x500")    # sets the window size

'''
Adding Entry Fields
'''
name = tk.StringVar() # helps store and retrieve text from input fields easily 

tk.Label(root, text="Name").pack()  # displays field names
tk.Entry(root, textvariable=name_var).pack()    # textbox where users can enter values
# the textvariable " binds the user entered value to a variable

'''
Adding radio buttons
'''
gender = tk.StringVar()

tk.Label(root, text="Gender").pack()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack()
# The .Radiobutton makes sure only one choice can be selected, all three Radiobuttons have the same "variable", value is what gets assigned

'''
Adding Check boxes
'''
python_var = tk.BooleanVar()
java_var = tk.BooleanVar()
js_var = tk.BooleanVar()

tk.Label(root, text="Skills").pack()
tk.Checkbutton(root, text="Python", variable=python_var).pack()
tk.Checkbutton(root, text="Java", variable=java_var).pack()
tk.Checkbutton(root, text="JavaScript", variable=js_var).pack()

# Checkbutton helps pick multiple values, each checkbox uses Boolean to store True or false value

'''
Submit and clear buttons
'''
def submit():
    name = name_var.get()   # get the value entered in name field
    gender = gender_var.get()   # get the value entered in gender radio
    skills = [] # list to store all skills

    # Check if skills have been selected or not
    if python_var.get(): skills.append("Python")
    if java_var.get(): skills.append("Java")
    if js_var.get(): skills.append("JavaScript")
    
    # The message that will be passed after clicking the submit button
    message = f"Name: {name}\nImage: {image}\nGender: {gender}\nSkills: {', '.join(skills)}"
    messagebox.showinfo("Submitted Info", message)

def clear():
    name_var.set("")    # clear the value in the name field
    gender_var.set("")  # clear the value in the gender field
    python_var.set(False)   # uncheck the checkbox
    java_var.set(False) # uncheck the checkbox
    js_var.set(False)   # uncheck the checkbox

tk.Button(root, text="Submit", command=submit).pack(pady=5) # command=submit will call the submit function, and the form gets submitted
tk.Button(root, text="Clear", command=clear).pack(pady=5)   # command=clear will call the clear funciton, and the form gets cleared, reset


'''
Starting the application
'''
root.mainloop() # runs the GUI until the user closes it


'''
The question that came in exam:
Full code:
'''
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("User Form")
root.geometry("400x500")

# Variables
name_var = tk.StringVar()
email_var = tk.StringVar()
website_var = tk.StringVar()
image_var = tk.StringVar()
gender_var = tk.StringVar()

python_var = tk.BooleanVar()
java_var = tk.BooleanVar()
js_var = tk.BooleanVar()

# Form Fields
tk.Label(root, text="Name").pack()
tk.Entry(root, textvariable=name_var).pack()

tk.Label(root, text="Email").pack()
tk.Entry(root, textvariable=email_var).pack()

tk.Label(root, text="Website").pack()
tk.Entry(root, textvariable=website_var).pack()

tk.Label(root, text="Image Link").pack()
tk.Entry(root, textvariable=image_var).pack()

tk.Label(root, text="Gender").pack()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack()

tk.Label(root, text="Skills").pack()
tk.Checkbutton(root, text="Python", variable=python_var).pack()
tk.Checkbutton(root, text="Java", variable=java_var).pack()
tk.Checkbutton(root, text="JavaScript", variable=js_var).pack()

# Functions
def submit():
    name = name_var.get()
    email = email_var.get()
    website = website_var.get()
    image = image_var.get()
    gender = gender_var.get()
    skills = []
    if python_var.get(): skills.append("Python")
    if java_var.get(): skills.append("Java")
    if js_var.get(): skills.append("JavaScript")
    
    message = f"Name: {name}\nEmail: {email}\nWebsite: {website}\nImage: {image}\nGender: {gender}\nSkills: {', '.join(skills)}"

def clear():
    name_var.set("")
    email_var.set("")
    website_var.set("")
    image_var.set("")
    gender_var.set("")
    python_var.set(False)
    java_var.set(False)
    js_var.set(False)

# Buttons
tk.Button(root, text="Submit", command=submit).pack(pady=5)
tk.Button(root, text="Clear", command=clear).pack(pady=5)

# Run App
root.mainloop()



'''
Basics of Web Development
    - we can use Flask for Web Dev
    - flask is a light weight web framework
    - lets you build websites and APIs using python
    - it is beginner friendly and flexible
'''
from flask import Flask
app = Flask(__name__)

@app.route('/') # / means the home page of the website
def home(): # it's simply a function
    return "Hello, World!"

'''
Routing and Pages
    - a route helps connect a URL to a Python function 
'''
@app.route('/about') # www.website.com/about
def about():
    return "This is the About page."

'''
Templates with HTML
    - we can render HTML pages using render_template() method

    - let's say we have an index.html file which contains the following code:

        <!DOCTYPE html>
        <html>
        <body>
            <h1>Hello from Flask</h1>
        </body>
        </html>

    - now, to run (render) this code:
'''
@app.route('/index')
def index():
    return render_template('index.html')


'''
Handling Form Data
'''
@app.route('/submit', methods=['POST']) # accepts only POST requests
def submit():
    name = request.form['name']
    email = request.form['email']
    return render_template('success.html', name=name, email=email)  # passes the name and email values to success.html

'''
success.html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Success</title>
    </head>
    <body>
        <h2>Thank You!</h2>
        <p>Name: {{ name }}</p>
        <p>Email: {{ email }}</p>
    </body>
    </html>
'''


'''
Django Intro
    - high level Python framework that lets you build secure, full-featured websites quickly
    - follows the Model-Template-View architecture


    -MTV(Model Template View)
        - model handles databases and data
        - template is the website layout. it displays HTML pages for us to see
        - view connects model and templates, it handles logic

    - eg: 
        - view gets data from model
        - sends it to template
        - template shows it to browser
'''