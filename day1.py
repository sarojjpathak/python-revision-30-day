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
print(bachelor_degree.count("a"))
print(bachelor_degree.startswith("bachelor"))
print(bachelor_degree.endswith("technology"))
print(bachelor_degree.split())
print(bachelor_degree.split("i"))
#the split() function will split the string into a list of substrings based on the delimiter provided. In this case it will split the string into a list of words based on the space character. If we provide "i" as the delimiter it will split the string into a list of substrings based on the character "i".
print(bachelor_degree.strip())
print(bachelor_degree.strip("bachelor, technology"))
#the strip() function will remove the specified characters from the beginning and end of the string. In this case it will remove "bachelor" and "technology" from the beginning and end of the string. If we don't provide any characters it will remove the whitespace characters from the beginning and end of the string.
a = "##@saroj@##"
print(a.strip("#@"))
print(len(bachelor_degree))