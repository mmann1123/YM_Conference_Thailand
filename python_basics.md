# Python Basics

In this tutorial, you'll learn the basics of Python programming, including variables, and loops. Python is a versatile and powerful programming language that is widely used in various fields, including data science, web development, and automation as well as of course geography.

## Table of Contents

1. [The Python Console in QGIS](#console)
2. [Python Tutorial: Understanding Variables](#variables)
3. [Mastering For Loops](#loops)
4. [Introduction to Python Modules](#modules)


## The Python Console in QGIS <a name="console"></a>

To get started with Python in QGIS, you first need to access the Python console. Here’s how you can do it:

1. **Open QGIS**: Start by launching the QGIS application on your computer.
2. **Open the Python Console**: Look for a button on the toolbar that resembles a Python logo or go to the menu bar and select `Plugins` -> `Python Console`. This will open a small scripting window at the bottom or side of your QGIS workspace.

The Python console in QGIS is split into two main parts:

- **The command line**: This is where you can type single lines of Python code and execute them immediately.

- **The editor**: Here, you can write more complex scripts, save them, and run them as needed.

This dual setup allows you to quickly test small pieces of code and develop more extensive scripts for automating tasks.

## QGIS Python Console

The console is a Python interpreter that allows you to execute Python commands. Modules from QGIS (analysis, core, gui, server, processing, 3d) and Qt (QtCore, QtGui, QtNetwork, QtWidgets, QtXml) as well as Python's math, os, re, and sys modules are already imported and can be used directly.

The interactive console is composed of a toolbar, an input area, and an output area.
![The Python Console](https://github.com/qgis/QGIS-Documentation/blob/master/docs/user_manual/plugins/img/python_console.png?raw=true)

## QGIS Editor 

The editor is a Python script editor that allows you to write and execute Python scripts. It is composed of a toolbar, an input area, an output area, and a dockable code editor.

![The Python Editor](https://github.com/qgis/QGIS-Documentation/blob/master/docs/user_manual/plugins/img/python_console_editor.png?raw=true)

This editor is a full-featured Python editor that provides syntax highlighting, code completion, and error checking. It also allows you to save and load scripts, as well as run them directly from the editor.

### Toolbar

The toolbar proposes the following tools:
- Clear Console ![clearConsole](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/iconClearConsole.png?raw=true) to wipe the output area;

- Run Command ![start](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/mActionStart.png?raw=true) available in the input area: same as pressing Enter;

- Show Editor ![showEditorConsole](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/iconShowEditorConsole.png?raw=true): toggles console editor visibility;

- Options... ![options](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/mActionOptions.png?raw=true): opens a dialog to configure console properties;

- Help... ![helpContents](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/mActionHelpContents.png?raw=true) provides a menu to access various documentation:
  - [Python Console Help](https://docs.qgis.org/latest/en/docs/user_manual/plugins/python_console.html)
  - [PyQGIS API documentation](https://qgis.org/api/)
  - [PyQGIS Cookbook](https://docs.qgis.org/latest/en/docs/pyqgis_developer_cookbook/)

Dock Code Editor ![dock](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/dock.png?raw=true) to dock or undock the panel in QGIS interface.


## Python Tutorial: Understanding Variables <a name="variables"></a>

Welcome to this tutorial on Python variables. In this guide, we'll cover the basics of how variables work in Python, the execution flow of code, and the concept of variable overwriting. By the end of this tutorial, you'll have a solid understanding of how to define and manipulate variables in Python.

### What is a Variable?

In Python, a variable is a named location used to store data in the memory. A variable is created the moment you first assign a value to it, and it gets destroyed when the program ends.

Python executes code from top to bottom, line by line. This execution order is important because it affects how values are assigned to variables and how they are updated throughout the script.

### Creating and Using Variables

The syntax to create a variable is straightforward:

```python
variable_name = value
```

Here, `variable_name` is the identifier you're assigning the value to, and `value` can be any data type.

#### Example 1: Simple Variable Assignment

```python
# Creating variables
name = "John Doe"  # A string variable
age = 25           # An integer variable
```

In this example, `name` stores a string, and `age` stores an integer. These variables can be used later in the program to access or manipulate the stored data.

For instance maybe we want to print the name and age of John Doe:

```python
# Using variables
print("Our user's name is", name, "and their age is", age)
```

### Variable Overwriting

Since Python executes code line by line, a variable can be overwritten by simply assigning a new value to it. This means that the content of the variable can change throughout the execution of the program.

#### Example 2: Overwriting a Variable

```python
# Initial assignment
message = "Hello, world!"
print("Initial message:", message)

# Overwriting the variable
message = "Goodbye, world!"
print("Updated message:", message)
```

Paste these lines into the Python console in QGIS to see the output and press ![start](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/mActionStart.png?raw=true)

- **Output**

```
Initial message: Hello, world!
Updated message: Goodbye, world!
```

In this example, the variable `message` is first set to `"Hello, world!"` and then overwritten with `"Goodbye, world!"`. Each `print` statement outputs the content of `message` at the time it is called.

### Interactive Guessing Game: Variable Content

Now, let's have an interactive exercise. Read the following code snippet and guess what the final content of the variable `number` will be before running the code.

```python
number = 10
number = 20
number = number + 5
number = number - 2
print("Final number:", number)
```


Try to figure out the content of `number` at the end of the script. This exercise helps illustrate how Python handles variable assignment and manipulation sequentially, from top to bottom.

Paste these lines into the Python console in QGIS to see the output and press ![start](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/mActionStart.png?raw=true)

### Variables Conclusion

Understanding how variables work in Python is fundamental to becoming proficient in the language. By mastering variable assignment and the concept of overwriting, you can manipulate data effectively within your programs. Remember, variables are essential for storing information that your program can manipulate, so knowing how to use them efficiently is crucial for any Python programmer.

---

## Mastering For Loops <a name="loops"></a>

In this guide, you'll learn how to use `for` loops effectively, including understanding their structure, the importance of indentation, and how Python executes these loops line by line, allowing for variable modification within the loop.

### Introduction to For Loops

A `for` loop in Python is used to iterate over a sequence, which could be a list, a tuple, a dictionary, a set, or even a string. This type of loop allows you to execute a block of code multiple times, which is especially useful for tasks that require repetitive actions.

### Structure of a For Loop

The basic structure of a `for` loop is as follows:

```python
for variable in sequence:
    # Block of code
```

- **`variable`**: This is the iterator variable that takes the value of the item inside the sequence on each iteration.
- **`sequence`**: This is the collection that you are iterating over.

### Importance of Indentation

Indentation is critical in Python, particularly for defining the block of code associated with `for` loops. The code that you want to repeat in each iteration should be indented under the `for` statement.

#### Example 1: Basic For Loop

Let's start with a simple example to print each item in a list:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("No more fruits")
```

Paste these lines into the Python console in QGIS to see the output and press ![start](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/mActionStart.png?raw=true)

- **Output**

```
apple
banana
cherry
No more fruits
```

Each `print(fruit)` statement is executed one at a time for each fruit in the list. Notice how the `print` statement is indented under the `for` line, indicating that it is the code to execute for each iteration.

The final `print("No more fruits")` statement is not indented under the `for` loop, so it is executed only once after the loop has completed.

##### Challange 1: Nested For Loops 

In the following example, work with your friends to figure out what the output will be before running the code.

> Note: Onces a loop has started it will run all the indented code below it before moving to the next step in the loop.

```python
for i in ['A', 'B', 'C']:
    for j in [1,2,3]:
        print(i, j)
```
*After your try* see the answer [here](https://mmann1123.github.io/YM_Conference_Thailand/loop_answer.html)

### Counting with For Loops

Python executes code line by line, which means that variables defined in a loop can be overwritten with each iteration. This behavior allows for dynamic changes to the variable within the loop's body. Importantly, this means we can easily count or sum values within a `for` loop.

#### Example 2: Overwriting Variables

```python
numbers = [1, 2, 3, 4, 5]
sum = 0  # Initialize a variable to store the sum
for number in numbers:
    sum = sum + number  # Update the sum variable in each iteration
    print("Current sum:", sum)

print("Final sum:", sum)
```
Paste these lines into the Python console in QGIS to see the output and press ![start](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/mActionStart.png?raw=true)

- **Output**

```
Current sum: 1
Current sum: 3
Current sum: 6
Current sum: 10
Current sum: 15
Final sum: 15
```

In this example, the `sum` variable is updated in each iteration, showing how variables can be dynamically modified and used to store intermediate results in loops.

### Conclusion

`For` loops are a fundamental aspect of Python that allows you to iterate over sequences efficiently. Understanding how to structure these loops, the significance of proper indentation, and the implications of line-by-line execution helps in creating robust and dynamic Python scripts.

By mastering `for` loops, you enhance your capability to handle repetitive tasks in programming, making your code more efficient and your programming tasks easier to manage.

## Introduction to Python Modules <a name="modules"></a>

In Python, a module is a file containing Python code that defines functions, classes, or variables, which can be accessed and utilized in other Python scripts. 

Python has a vast standard library of modules that you can use for various tasks, from mathematical operations to handling internet data. Additionally, third-party modules can be installed and used in your projects, greatly extending Python's capabilities.

### Importing Modules in Python

To use a module in Python, you need to import it into your script using the `import` statement. Once a module is imported, you can call its functions or access its classes and variables using the dot notation.

For example, to import the Python `math` module, you would write:

```python
import math
```

Now you can use functions within the `math` module:

```python
result = math.sqrt(25)  # Computes the square root of 25
print(result)
```

Paste these lines into the Python console in QGIS to see the output and press ![start](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/mActionStart.png?raw=true)

---

> This tutorial continues in the next section [Introduction to Python in QGIS](https://mmann1123.github.io/YM_Conference_Thailand/QGIS_python.html)