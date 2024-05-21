# Python Basics

In this tutorial, you'll learn the basics of Python programming, including variables, and loops. Python is a versatile and powerful programming language that is widely used in various fields, including data science, web development, and automation as well as of course geography.

## Table of Contents

1. [The Python Console in QGIS](#console)
2. [Python Tutorial: Understanding Variables](#variables)
3. [Mastering For Loops](#loops)
4. [Introduction to Python Modules](#modules)

Here’s a revised version to avoid plagiarism:
Here’s a revised version to avoid plagiarism:

## 1) Accessing the Python Console in QGIS <a name="console"></a>

To begin using Python within QGIS, follow these steps to access the Python console:

1. **Launch QGIS**: Open the QGIS application on your computer.
2. **Open the Python Console**: Click the toolbar button that looks like a Python logo or navigate to `Plugins` -> `Python Console` in the menu bar. This action opens a small scripting window at the bottom or side of your QGIS workspace.

The QGIS Python console consists of two primary components:

- **Command Line**: Here, you can enter and execute single lines of Python code.
- **Editor**: This area allows you to write, save, and run more complex scripts.

This setup is useful for both quickly testing small code snippets and developing larger scripts for task automation.

## Understanding the QGIS Python Console

The QGIS Python console is an interactive interpreter where you can run Python commands. It includes modules from QGIS (such as analysis, core, gui, server, processing, and 3d) and Qt (including QtCore, QtGui, QtNetwork, QtWidgets, and QtXml), along with Python's own math, os, re, and sys modules, which are all pre-imported for immediate use.

The console interface includes a toolbar, an input area, and an output area.
![The Python Console](https://github.com/qgis/QGIS-Documentation/blob/master/docs/user_manual/plugins/img/python_console.png?raw=true)

## Using the QGIS Editor

The editor within QGIS is a script editor for Python that lets you write and execute Python scripts. It features a toolbar, input and output areas, and a dockable code editor.

![The Python Editor](https://github.com/qgis/QGIS-Documentation/blob/master/docs/user_manual/plugins/img/python_console_editor.png?raw=true)

This editor offers full Python editing capabilities, including syntax highlighting, code completion, and error checking. You can save and load scripts and execute them directly from the editor.

### Toolbar Features

The toolbar in the Python console provides several useful tools:
- **Clear Console** ![clearConsole](https://github.com/mmann1123/YM_Conference_Thailand/blob/main/images/clear.png?raw=true): Clears the output area.
- **Run Command** ![start](https://github.com/mmann1123/YM_Conference_Thailand/blob/main/images/play.png?raw=true): Executes the command in the input area, equivalent to pressing Enter.
- **Show Editor** ![showEditorConsole](https://github.com/mmann1123/YM_Conference_Thailand/blob/main/images/editorbutton.png?raw=true): Toggles the visibility of the console editor.
- **Options...** ![options](https://github.com/mmann1123/YM_Conference_Thailand/blob/main/images/options.png?raw=true): Opens a dialog to configure console properties.
- **Help...** ![helpContents](https://github.com/mmann1123/YM_Conference_Thailand/blob/main/images/questionmark.png?raw=true): Provides access to various documentation:
  - [PyQGIS Cookbook](https://docs.qgis.org/latest/en/docs/pyqgis_developer_cookbook/)
  - [Python Console Help](https://docs.qgis.org/latest/en/docs/user_manual/plugins/python_console.html)
  - [PyQGIS API documentation](https://qgis.org/api/)

This should help you get started with the Python console and editor in QGIS, making your workflow more efficient and automated.

--- 

## 2) Python Tutorial: Understanding Variables <a name="variables"></a>

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

## 3) Mastering For Loops <a name="loops"></a>

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

---

## 4) Introduction to Python Modules <a name="modules"></a>

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