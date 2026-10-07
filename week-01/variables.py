import sys
print(sys.version) #Checks the python version of the editor

# use the 'end' parameter to avoid the new line after the print statement
print("Hello, I am learning Python.",end=" ")
print(" This will be printed on the same line as the previous print statement.")

# You can do math inside the print statement
print(3+8)  #This will print 11

# Mix Text and Numbers
print("I am", 20, "years old.")

#  Python variables
x = 5
y = "Hello, Teressa!"
print(x)
print(y)
# variables do not need to be declared with any particular type.
x = 16
x ="Python  is easy to learn."
print(x)
# casting 
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
# getting data type of a variable
x= 5
y = "Hello, Teressa!"
print(type(x))
print(type(y))

# Case sensitive
a = 12
A = "Python is case sensitive." #a and A are different variables
print(a)
print(A)

# VariableNames
#Camel Case (Each word, except the first, starts with a capital letter)
myVariableName = "Felix Awere"
# Pascal Case (Each word starts with a capital letter)
MyVariableName = "Felix Odhiambo"
# Snake Case (Each word is separated by an underscore character)
my_variable_name = "Felix Awere Odhiambo"

# Assigning values to multiple variables in one line
x, y, z = 5, "Hello, Teressa!", 3.14
print(x)
print(y)
print(z)
#One value to multiple variables
x=y=z= "Orange"

print(x)
print(y)
print(z)
#Unpacking a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
a = "Python"
b = "is"
c ="awesome"
print(a, b, c)

#Global variables
#  Are created outside of a function and can be used inside a function
x = "Teresia"

def myfunc():
  print("My name is " + x)

myfunc()

# Local variables
# Are created inside a function and can only be used inside that function
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#Global keyword
# The 'global' keyword is used to create a global variable inside a function
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
# Variable Exercises
