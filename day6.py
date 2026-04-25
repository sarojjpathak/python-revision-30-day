#Functions in Python
#Python Functions
#A function is a block of code which only runs when it is called.
#A function can return data as a result.
#A function helps avoiding code repetition.




# Function names follow the same rules as variable names in Python:

# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)

def greet(name):
    print(f"goodmorning {name}")
 #we need to leave two line after function, this is good practice

greet("saroj")
greet("sameer")

#-------------------------------------------------------------------------------------

def multiply(a = 2,b = 3):   #we add the default value
    return a*b

print(f"Multiplication of 12 and 43 is :{multiply(32)}")


#-------------------------------------------------------------------------------------
#pass

#Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
 
 #-------------------------------------------------------------------------------------
# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the actual value that is sent to the function when it is called.


#if func is defined with two parameters then two arguments should be passed otherwise the program willshow error tosolve this problem you can set default value if required num of arguments didnt came the function will use that default argument




#-------------------------------------------------------------------------------------

# Keyword Arguments
# You can send arguments with the key = value syntax.

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")
my_function( name = "buddy",animal = "dog") #using keyword arguments doesnot required the order of arg


#-------------------------------------------------------------------------------------
# Positional Arguments
# When you call a function with arguments without using keywords, they are called positional arguments.

# Positional arguments must be in the correct order:

#------------------------------------------------------------------------------------
# Mixing Positional and Keyword Arguments
# You can mix positional and keyword arguments in a function call.

# However, positional arguments must come before keyword arguments:
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", age = 5, name = "Buddy")

#---------------------------------______________________________----------------------------
# Passing Different Data Types
# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).

# The data type will be preserved inside the function:

#===========================================================================================
# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments.

# To specify positional-only arguments, add , / after the arguments:
def my_function(animal, name, age,/):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", "Buddy",3)#if we pass keyword then it will show syntax error




#------------------------------------------------------------------------------------
# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*,animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function(animal="dog", age = 5, name = "Buddy")#if we try to type positional arguments then it will show error


#-------------------------------------------------------------------------------------
# Combining Positional-Only and Keyword-Only
# You can combine both argument types in the same function.

# Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)


#-------------------------------------------------------------------------------
# *args
# Collects positional arguments
# Stored as a tuple
# Used when you don’t know how many values will be passed

def marks(*args):
    return sum(args)

print(marks(80, 75, 90))  

#-------------------------------------------------------------------------------
# **kwargs
# Collects keyword arguments (name=value)
# Stored as a dictionary
#Used when you don’t know how many named values will be passed
def student_info(**kwargs):
    return kwargs

print(student_info(name="Saroj", age=20))



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def profile(*skills, **details):                                        
    print("Skills:", skills)
    print("Details:", details)

profile(
    "Python", "C++", "DSA",
    name="Saroj",
    country="Nepal",
    # "java",#possitional arguments follow keyword arguments 
    favorite_player="Ronaldo"
)



# def profile( **details,*skills,):     this is completely wrong because possitional arguments should be in first and only after that keyword arguments                                   
#     print("Skills:", skills)
#     print("Details:", details)

# profile(
    
#     name="Saroj",
#     country="Nepal",
#     # "java",#possitional arguments follow keyword arguments 
#     favorite_player="Ronaldo",
#     "Python", "C++", "DSA",
# )



#NOTE
# 
# Correct order:

# normal parameters
# *args
# **kwargs


# * unpacking
nums = [1, 2, 3]
print(*nums)#output is : 1 2 3


#------------------------------------------
# rule 3: ** unpacking
info = {"name": "Saroj", "age": 20}
# print(**info)  # ❌ invalid directly

# ✔️ Correct use:
info = {"name": "Saroj", "age": 20}
def show(name, age):
    print(name, age)

show(**info) # here argu will became show(name = "saroj", age = 22) #this is how unpacking works  we cant directly unpack dict
