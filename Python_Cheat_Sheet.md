# PYTHON CHEAT SHEET

## CONTENTS

### [[BASICS]](#-basics)
- Print
- Input
- Comments
- Variables
- The += Operator

### [[DATA TYPES]](#-data-types)

- Integers
- Floating Point Numbers
- Strings
- String Concatenation
- Escaping a String
- F-Strings
- Converting Data Types
- Checking Data Types

### [[MATHS]](#-maths)

- Arithmetic Operators
- The += Operator
- The Modulo Operator

### [[ERRORS]](#-errors)

- Syntax Error
- Name Error
- Zero Division Error

### [[FUNCTIONS]](#-functions)

- Creating Functions
- Calling Functions
- Functions with Inputs
- Functions with Outputs
- Variable Scope
- Keyword Arguments

### [[CONDITIONALS]](#-conditionals)
- If
- Else
- Elif
- and
- or
- not
- comparison operators

### [[LOOPS]](#-loops)

- For Loop
- _ in a For Loop
- break
- continue
- Infinite Loops

### [[LIST METHODS]](#-list-methods)

- Adding Lists Together
- Adding an Item to a List
- List Index
- List Slicing

### [[BUILT-IN FUNCTIONS]](#-built-in-functions)

- Range
- Randomisation
- Round
- abs

### [[MODULES]](#-modules)

- Importing
- Aliasing
- Importing from modules
- Importing Everything

### [[CLASSES & OBJECTS]](#-classes--objects)

- Creating a Python Class
- Creating an Object from a Class
- Class Methods
- Class Variables
- The __init__ method
- Class Properties
- Class Inheritance

---

## ✅ BASICS

### Print

    print("Hello World")

Prints a string into the console.

### Input

    input("What's your name")

Prints a string into the console, and asks the user for a string input.

### Comments

    # This is a comment
    print("This is code")

Adding a # symbol in font of text lets you make comments on a line of code. <br>
The computer will ignore your comments.

### Variables

    my_name = "Angela"
    my_age = 12

A variable give a name to a piece of data. <br>
Like a box with a label, it tells you what's inside the box.

### The += Operator

    my_age = 12
    my_age += 4
    # my_age is now 16

This is a convenient way of saying: <br>
"take the previous value and add to it."

---

## ✅ DATA TYPES

### Integers

    my_number = 354

Integers are whole numbers.

### Floating Point Numbers

    my_float = 3.14159

Floats are numbers with decimal places.<br>
When you do a calculation that results in a fraction 
<br>e.g. 4 ÷ 3 the result will always be a floating point number.

### Strings

    my_string = "Hello"

A string is just a string of characters.<br>
It should be surrounded by double quotes.

### String Concatenation

    "Hello" + "Angela"
    # becomes "HelloAngela"

You can add strings to string to create a new string.<br>
This is called concatenation.<br>
It results in a new string.

### Escaping a String

    speech = "She said: \"Hi\""
    print(speech)
    # prints: She said: "Hi"

Because the double quote is special, it denotes a string, <br>
if you want to use it in a string, you need to escape it with a "\"

### F-Strings

    days = 365
    print(f"There are {days} in a year")

You can insert a variable into a string using f-strings.<br>
The syntax is simple, just insert the variable in-between a set of curly braces {}.

### Converting Data Types

    n = 354
    new_n = float(n)
    print(new_n)  # result 354.0

You can convert a variable from 1 data type to another. <br>
Converting to float:<br>
float()<br>
Converting to int:<br>
int()<br>
Converting to string:<br>
str()

### Checking Data Types

    n = 3.14159
    type(n)  # result float

You can use the type() function to check what is the data type of particular variable.

---

## ✅ MATHS

### Arithmetic Operators

    3+2  # Add
    4-1  # Subtract
    2*3  # Multiply
    5/2  # Divide
    5**2  # Exponent

You can do mathematical calculations with Python as long as you know the right operators.

### The += Operator

    my_number = 4
    my_number += 2
    # result is 6

This is a convenient way to modify a variable.<br>
It takes the existing value in a variable and adds to it.<br>
You can also use any of the other mathematical operators e.g. -= or *=

### The Modulo Operator

    5 % 2
    # result is 1

Often you'll want to know what is the remainder after a division.<br>
e.g. 4 ÷ 2 = 2 with no remainder<br>
but 5 ÷ 2 = 2 with 1 remainder<br>
The modulo does not give you the result of the division, just the remainder.<br>
It can be really helpful in certain situations,<br>
e.g. figuring out if a number is odd or even.

---

## ✅ ERRORS

### Syntax Error

    print(12 + 4))
        File "<stdin>", line 1
            print(12 + 4))
                         ^
    SyntaxError: unmatched ')'

Syntax errors happen when your code does not make any sense to the computer.<br>
This can happen because you've misspelt something or there's too many brackets or a missing comma.

### Name Error

    my_number = 4
    my_Number + 2
    Traceback (most recent call last): File "<stdin>", line 1,
    NameError: name 'my_Number' is not defined

This happens when there is a variable with a name that the computer does not recognise.<br>
It's usually because you've misspelt the name of a variable you created earlier.<br>
Note: variable names are case sensitive!

### Zero Division Error

    5 % 0
    Traceback (most recent call last): File "<stdin>", line 1,
    ZeroDivisionError: integer division or modulo by zero

This happens when you try to divide by zero.<br>
This is something that is mathematically impossible so Python will also complain.

---

## ✅ FUNCTIONS

### Creating Functions

    def my_function():
        print("Hello")
        name = input("Your name:")
        print("Hello")

This is the basic syntax for a function in Python.<br>
It allows you to give a set of instructions a name, so you can trigger it multiple times without having to re-write or copy-paste it.<br>
The contents of the function must be indented to signal that it's inside.

### Calling Functions

    my_function()
    my_function()
    # The function my_function will run twice.

You activate the function by calling it.<br>
This is simply done by writing the name of the function followed by a set of round brackets.<br>
This allows you to determine when to trigger the function and how many times.

### Functions with Inputs

    def add(n1, n2):
        print(n1 + n2)

    add(2, 3)

In addition to simple functions, you can give the function an input.<br>
This way, each time the function can do something different depending on the input.<br>
It makes your function more useful and re-usable.

### Functions with Outputs

    def add(n1, n2):
        return n1 + n2

    result = add(2, 3)

In addition to inputs, a function can also have an output.<br> 
The output value is proceeded by the keyword "return".<br>
This allows you to store the result from a function.

### Variable Scope

    n = 2
    def my_function():
        n = 3
        print(n)

    print(n)  # Prints 2
    my_function()  # Prints 3

Variables created inside a function are destroyed once the function has executed.<br>
The location (line of code) that you use a variable will determine its value.<br>
Here n is 2 but inside my_function() n is 3.<br>
So printing n inside and outside the function will determine its value.

### Keyword Arguments

    def divide(n1, n2):
        result = n1 / n2

    # Option 1:
    divide(10, 5)

    # Option 2:
    divide(n2=5, n1=10)

When calling a function, you can provide a keyword argument or simply just the value.<br>
Using a keyword argument means that you don't have to follow any order when providing the inputs.

---

## ✅ CONDITIONALS

### If

    n = 5
    if n > 2:
        print("Larger than 2")

This is the basic syntax to test if a condition is true.<br>
If so, the indented code will be executed, if not it will be skipped.

### Else

    age = 18
    if age > 16:
        print("Can drive")
    else:
        print("Don't drive")

This is a way to specify some code that will be executed if a condition is false.

### Elif

    weather = "sunny"
    if weather == "rain":
        print("bring umbrella")
    elif weather == "sunny":
        print("bring sunglasses")
    elif weather == "snow":
        print("bring gloves")

In addition to the initial If statement condition, you can add extra conditions to test if the first condition is false.<br>
Once an elif condition is true, the rest of the elif conditions are no longer checked and are skipped.

### and

    s = 58
    if s < 60 and s > 50:
    print("Your grade is C")

This expects both conditions either side of the and to be true.

### or

    age = 12
    if age < 16 or age > 200:
        print("Can't drive")

This expects either of the conditions either side of the or to be true.<br>
Basically, both conditions cannot be false.

### not

    if not 3 > 1:
        print("something")
    # Will not be printed.

This will flip the original result of the condition.<br>
e.g. if it was true then it's now false.

### comparison operators

    > Greater than
    < Lesser than
    >= Greater than or equal to
    <= Lesser than or equal to
    == Is equal to
    != Is not equal to

These mathematical comparison operators allow you to refine your conditional checks.

---

## ✅ LOOPS

    n = 1
    while n < 100:
        n += 1

This is a loop that will keep repeating itself until the while condition becomes false.

### For Loop

    all_fruits = ["apple", "banana", "orange"]

    for fruit in all_fruits:
        print(fruit)

For loops give you more control than while loops.<br>
You can loop through anything that is iterable.<br>
e.g. a range, a list, a dictionary or tuple.

### _ in a For Loop

    for _ in range(100):
        # Do something 100 times.

If the value your for loop is iterating through,<br>
e.g. the number in the range, or the item in the list is not needed,<br>
you can replace it with an underscore.

### break

    scores = [34, 67, 99, 105]

    for s in scores:
        if s > 100:
            print("Invalid")
            break
        print(s)

This keyword allows you to break free of the loop.<br>
You can use it in a for or while loop.

### continue

    n = 0

    while n < 100:
        n += 1
        if n % 2 == 0:
            continue
        print(n)

    # Prints all the odd numbers

This keyword allows you to skip this iteration of the loop and go to the next.<br>
The loop will still continue, but it will start from the top.

### Infinite Loops

    while 5 > 1:
        print("I'm a survivor")

Sometimes, the condition you are checking to see if the loop should continue never becomes false.<br>
In this case, the loop will continue for eternity (or until your computer stops it).<br>
This is more common with while loops.

---

## ✅ LIST METHODS

### Adding Lists Together

    list1 = [1, 2, 3]
    list2 = [9, 8, 7]

    new_list = list1 + list2
    list1 += list2

You can extend a list with another list by using the extend keyword, or the + symbol.

### Adding an Item to a List

    all_fruits = ["apple", "banana", "orange"]

    all_fruits.append("pear")

If you just want to add a single item to a list, you need to use the .append() method.

### List Index

    letters = ["a", "b", "c"]

    letters[0]
    # Result:"a"

    letters[-1]
    # Result: "c"

To get hold of a particular item from a list you can use its index number.<br>
This number can also be negative, if you want to start counting from the end of the list.

### List Slicing

    # list[start:end]

    letters = ["a","b","c","d"]

    letters[1:3]
    # Result: ["b", "c"]

Using the list index and the colon symbol you can slice up a list to get only the portion you want.<br>
Start is included, but end is not.

---

## ✅ BUILT-IN FUNCTIONS

### Range

    # range(start, end, step)
    for i in range(6, 0, -2):
        print(i)

    # result: 6, 4, 2
    # 0 is not included.

Often you will want to generate a range of numbers.<br>
You can specify the start, end and step.<br>
Start is included, but end is excluded:<br>
start <= range < end

### Randomisation

    import random

    # randint(start, end)

    n = random.randint(2, 5)
    # n can be 2, 3, 4 or 5.

The random functions come from the random module which needs to be imported.<br>
In this case, the start and end are both included<br>
start <= randint <= end

### Round

    round(4.6)
    # result 5

This does a mathematical round.<br>
So 3.1 becomes 3, 4.5 becomes 5 and 5.8 becomes 6.

### abs

    abs(-4.6)
    # result 4.6

This returns the absolute value.<br>
Basically removing any -ve signs.

---

## ✅ MODULES

### Importing

    import random

    n = random.randint(3, 10)

Some modules are pre-installed with python<br>
e.g. random/datetime<br>
Other modules need to be installed from pypi.org

### Aliasing

    import random as r

    n = r.randint(1, 5)

You can use the as keyword to give your module a different name.

### Importing from modules

    from random import randint

    n = randint(1, 5)

You can import a specific thing from a module.<br>
e.g. a function/class/constant<br>
You do this with the from keyword.<br>
It can save you from having to type the same thing many times.

### Importing Everything

    from random import *

    list = [1, 2, 3]
    choice(list)

    # More readable/understood
    # random.choice(list)

You can use the wildcard (*) to import everything from a module.<br>
Beware, this usually reduces code readability.

---

## ✅ CLASSES & OBJECTS

### Creating a Python Class

    class MyClass:
        # define class

You create a class using the class keyword.<br>
Note, class names in Python are PascalCased.<br>
So to create an empty class.

### Creating an Object from a Class

    class Car:
        pass

    my_toyota = Car()

You can create a new instance of an object by using the class name + ()

### Class Methods

    class Car:
        def drive(self):
            print("move")

    my_honda = Car()
    my_honda.drive()

You can create a function that belongs to a class, this is known as a method.

### Class Variables

    class Car:
        colour = "black"

    car1 = Car()
    print(car1.colour)  # black

You can create a varaiable in a class.<br>
The value of the variable will be available to all objects created from the class.

### The __init__ method

    class Car:
        def __init__(self):
            print("Building car")

    my_toyota = Car()

    # You will see "building car" printed.

### Class Properties

    class Car:
        def __init__(self, name):
            self.name = "Jimmy"

You can create a variable in the init() of a class so that all objects created from the class has access to that variable.

### Class Inheritance

    class Animal:
        def breathe(self):
            print("breathing")

    class Fish(Animal):
        def breathe(self):
            super().breathe()
            print("underwater")

    nemo = Fish()
    nemo.breathe()

    # Result:
    # breathing
    # underwater

When you create a new class, you can inherit the methods and properties of another class.

---