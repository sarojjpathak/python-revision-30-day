import math



print("hello , my name is Saroj Pathak")
#python executing the code line by line and then it will print the result of that code. In this case it will print "hello , my name is Saroj Pathak"
print("0_____~")
print(" || ||")


print("*"*10)

#at first  python interpreter will execute the code in the parenthesis and then it will print the result of that code. In this case it will print 10 stars.
#variables in python

#after we declare a variable  computer or interpreter will allocate some memory to store the value of that variable. We can use that variable to store any type of data like numbers, strings, lists, etc. value of variables are converted into binary format and stored in the memory. We can use variables to perform various operations like arithmetic operations, string operations, etc. We can also use variables to store the result of an operation and use it later in the program.

#variables are used to store data in a program. We can use variables to store any type
price = 20 
print(price)
floating_number = 3.14
print(floating_number)
#we can also change the value of a variable
price = 30
print(price)

#python is case sensitive language. So, price and Price are two different variables.

is_sold = True
print(is_sold) 
#boolean variables can only have two values True or False. 
name = "saroj pathak"
age = 22
is_student = True
print("my name is "+ name + " and I am " + str(age)+ " years old. I am a student: " + str(is_student))

#how to take input from user in python
# name = input("what is your name? ")
#to take input from user we can use input() function. It will take the input from user and store it in a variable. By default, input() function takes the input as a string. If we want to take input as a number we need to convert it into the desired type using int() or float() function.
# age = int(input("what is your age? "))
# print("my name is "+ name + " and I am " + str(age)+ " years old.")


# birth_year = int(input("what is your birth year? "))

#as birth_year is converted into integer using int() function we can perform arithmetic operation on that variable to calculate the age of the user. 

# current_year = int(input("what is the current year? "))
# age = int(current_year) - birth_year
# print("your age is: " + str(age))

#using type() function we can check the type of a variable. It will return the type of the variable.
print(type(name))
print(type(age))


print('hello "world" wow how can we use double quotes inside a string?')
#we can use single quotes to define a string if we want to use double quotes inside the string and vice versa. In this case we are using single quotes to define the string and we can use double quotes inside the string without any problem.

msg = '''  
hi saroj ,
 this is a multi line string. We can use triple quotes to define a multi line string. 
 
 thank you'''
print(msg)

print('''  
            ________________
           |                |
           |      SAROJ     |
           |      PATHAK    |
           |________________|''')
bachelor_degree = "bachelor in information technology"
print(bachelor_degree.upper())
print(bachelor_degree[-11])
print(bachelor_degree[0:8])
#this will print the characters from index 0 to index 7. The character at index 8 will not be included in the output. In this case it will print "bachelor"
#bachelor_degree[:] will print the entire string as it will start from index 0 and end at the last index of the string. In this case it will print "bachelor in information technology"
print(bachelor_degree[1:-1]) 
#this will print from index 1 to index -2


#formated string
name = "saroj"
age = 22
print(f"my name is {name} and I am [{age}] years old.")
#with formated string we can directly use the variables inside the string without using concatenation. We need to prefix the string with 'f' and then we can use curly braces {} to include the variables inside the string. In this case it will print "my name is saroj and I am [22] years old."


#different functions to manipulate strings
print(bachelor_degree.lower())
print(bachelor_degree.capitalize())
print(bachelor_degree.title())
print(bachelor_degree.replace("information", "IT"))
print(bachelor_degree.find("information"))
#the find() function will return the index of the first occurrence of the specified substring. In this case it will return the index of the first occurrence of "information" in the string "bachelor in information technology". If the substring is not found it will return -1.
print(bachelor_degree.count("a"))
print(bachelor_degree.startswith("bachelor"))
#passes boolean
print(bachelor_degree.endswith("technology"))
print(bachelor_degree.split())
print(bachelor_degree.split("i"))
#the split() function will split the string into a list of substrings based on the delimiter provided. In this case it will split the string into a list of words based on the space character. If we provide "i" as the delimiter it will split the string into a list of substrings based on the character "i".
print(bachelor_degree.strip())
print(bachelor_degree.strip("bachelor, technology"))
#the strip() function will remove the specified characters from the beginning and end of the string. In this case it will remove "bachelor" and "technology" from the beginning and end of the string. If we don't provide any characters it will remove the whitespace characters from the beginning and end of the string.
a = "##@saroj@##"
print(a.strip("#@"))
#strip("#@") means:
# Remove any combination of # and @ from the start and end of the string. either ##@ or @## or #@# or @#@ will be removed from the start and end of the string. In this case it will remove ##@ from the start and @## from the end of the string, leaving us with "saroj".
print(len(bachelor_degree))
print("bachelor" in bachelor_degree)
#the in operator is used to check if a substring is present in a string. It will return True if the substring is present in the string and False if it is not present. In this case it will return True as "bachelor" is present in the string "bachelor in information technology".



#ARITHMETIC OPERATORS
#operators are used to perform various operations on variables and values. In Python, we have the following operators:
#rules for operators in python:
# precedence of operators:
    # Parentheses
    # Exponentiation then Multiplication and Division then Addition and Subtraction then Comparison operators then Logical operators then Assignment operators then Identity operators then Membership operators
    # Associativity of operators:
    # Direction	Operators
# Left → Right	+ - * / // %, comparisons, and, or
# Right → Left	**, assignment (=), unary (-x)
# '+' is used for addition
# '-' is used for subtraction
# '*' is used for multiplication
# '/' is used for division
# '//' is used for floor division
# for ceiling division we can use math.ceil() function from math module. It will return the smallest integer greater than or equal to the result of the division.  print(10/3) # this will return 4
# '%' is used for modulus
# '**' is used for exponentiation
# '=' is used for assignment
# '==' is used for equality comparison
# '!=' is used for inequality comparison
# '>' is used for greater than comparison
# '<' is used for less than comparison
# '>=' is used for greater than or equal to comparison
# '<=' is used for less than or equal to comparison
# 'and' is used for logical AND operation
# 'or' is used for logical OR operation
# 'not' is used for logical NOT operation
# 'in' is used for membership testing
# 'not in' is used for membership testing
# 'is' is used for identity testing
# 'is not' is used for identity testing
#'+' operator can also be used for string concatenation. In this case it will concatenate two strings and return a new string. For example:
first_name = "saroj"
last_name = "pathak"
full_name = first_name + " " + last_name
print(full_name)



# MATH FUNCTIONs

x = 2.9
print(round(x))
x = -2.9
print(abs(round(x)))

#we can also use math module to perform various mathematical operations. We need to import the math module to use its functions.  for this we import math module and then we can use math.ceil() function to perform ceiling division and similarly other function also


x = 23.4324
print(math.ceil(x))
print(math.floor(x))   # round down
print(math.trunc(x))   # remove decimal
print(math.fabs(x))    # absolute value     this cannot calculate  value for complex number whereas abs() function can calculate absolute value for complex number also as that is inbuilt function in python. math.fabs() function can only calculate absolute value for real numbers.
print(math.sqrt(x))    # square root
y = 3
print(math.pow(x, y))  # x^y
print(math.exp(x))     # e^x
print(math.log(x))     # natural logarithm
print(math.log10(x))   # logarithm base 10
print(math.sin(x))     # sine of x
#print(math.acos(x))     # arc cosine of x
print(math.degrees(x)) # convert radians to degrees
print(math.radians(x)) # convert degrees to radians
#etc. there are many more functions in math module that we can use to perform various mathematical operations. We can refer to the official documentation of math module for more information about the functions available in math module.
   


   # if statements

is_hot = True
is_cold = False
if is_hot:
    print("*-------------------------*")
    print("|    it is a hot day      |")
    print("|   drink plenty of water |")
    print("*-------------------------*")
elif is_cold:
    print("*------------------------*")
    print("it is a cold day")
    
    print("wear warm clothes")
    print("*------------------------*")
else:
    print("*------------------------*")
    print("   its amazing day")
    print("enjoy")
    print("*------------------------*")



#question price if house is 20 lkh  if buyer has good credit then they need to pay 10% of the price as down payment otherwise they need to pay 20% of the price as down payment. print the down payment and the house price should be  with unit at the end such as  L for lakh C for crore and K for thousand  and you have to convert that to integer and calculate .


house_price =  "20C"
has_good_credit = True
h_unit = house_price[-1]

hp = int(house_price.strip("LKC"))
if (h_unit == "L"):
    final_house_price = hp * math.pow(10, 5)
elif (h_unit == "K"):
    final_house_price = hp * math.pow(10, 3)
elif (h_unit == "C"):
    final_house_price = hp * math.pow(10, 7)
else:
    final_house_price = hp

# here we converted the house price from string to integer and then we calculated the final house price based on the unit provided in the input. We used math.pow() function to calculate the power of 10 based on the unit provided in the input. Finally, we calculated the down payment based on whether the buyer has good credit or not and printed the down payment.


if has_good_credit:
    downpayment = final_house_price * 0.1
else:
    downpayment = final_house_price * 0.2

print(f"house price: {final_house_price} ")
print("The down payment amount is :")
print("*-----------------------------*")
print(f"|  down payment: {downpayment}   |")
print("*-----------------------------*")