#    1       pass statement
#In Python, pass is a do-nothing statement.   PASS

# It is used when Python expects some code, but you don’t want to write anything yet.
for i in range(5):
    pass
x = 11
if x > 10:
    pass  # will write code later

# if True:
#     # error ❌ after we write a loop we have write the statement

# 2 Match
#The Python Match Statement
# Instead of writing many if..else statements, you can use the match statement.

# The match statement selects one of many code blocks to be executed.

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:   #default
    print("invalid day")

#Default Value
#Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:

#Combine Values
#Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")



#If Statements as Guards
#You can add if statements in the case evaluation as an extra condition-check:
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")


#as switch cant do that this match is more powerful then switch case
point = (0, 0)
place = "down"

match point:
    case (0, 0) if place =="up":
        print("Origin_up")
    case (0, 0) if place =="down":
        print("Origin_down")
    case (x, 0):
        print("On X axis")
    case (0, y):
        print("On Y axis")
    case _:
        print("Somewhere else")