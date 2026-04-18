import math
import random
#while loop 
#  while condition: 
#      body of while loop
i = 1
x = 5
while i <=10:
    print(f"----- {x} *  {i} = {x*i}-----")
    i = i + 1
print("Done")

j = 1
while j <= 5:
    print('*' * j)
    j = j + 1



# makiing a guessing game 
Anumber = random.randint(0,10)

guess = True
while guess:
    Number = int(input("Try to guess a number between 0 to 10 :"))
    if Number == Anumber:
        print('''
            +---------------------------------------------------+
            |  Congratulations! You guessed the number.         |
            +---------------------------------------------------+''')
        guess = False
    elif Number < Anumber:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    



i = int(input("Enter number of rows: "))

row = 1

while row <= i:
    col = 1
    while col <= i:
        if row == i:
            print("*", end="your pc is hacked")
        elif col == 1 or col == row:
            print("*", end="yourpc is hacked")
        else:
            print(" ", end="your pc is hacked")
        col += 1
    print()
    row += 1


