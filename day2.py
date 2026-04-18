# import math
# import random
# #while loop 
# #  while condition: 
# #      body of while loop
# i = 1
# x = 5
# while i <=10:
#     print(f"----- {x} *  {i} = {x*i}-----")
#     i = i + 1
# print("Done")

# j = 1
# while j <= 5:
#     print('*' * j)
#     j = j + 1



# # makiing a guessing game 
# Anumber = random.randint(0,10)

# guess = True
# while guess:
#     Number = int(input("Try to guess a number between 0 to 10 :"))
#     if Number == Anumber:
#         print('''
#             +---------------------------------------------------+
#             |  Congratulations! You guessed the number.         |
#             +---------------------------------------------------+''')
#         guess = False
#     elif Number < Anumber:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")
    



# i = int(input("Enter number of rows: "))

# row = 1

# while row <= i:
#     col = 1
#     while col <= i:
#         if row == i:
#             print("*", end="your pc is hacked")
#         elif col == 1 or col == row:
#             print("*", end="yourpc is hacked")
#         else:
#             print(" ", end="your pc is hacked")
#         col += 1
#     print()
#     row += 1

      


#-------------------------------------------------------------- |^|



#FOR LOOPS IN PYTHON 
# for variable in sequence:
course = "python"
for letter in course :
    print(letter)


for item in range(2,6):
    #here 6 is not included in thr range only 2 ,3 ,4 ,5 are included
    print(item)
for item in range(0 ,10,2):
    #here 10 is not included in the range only 0,2,4,6,8 are included
    print(item)



prices = [10, 20, 30]
total = 0
for p in prices:
    total += p

print(f"Total: {total}")


# we can use a break statement to exit a loop when a certain condition is met
#we can use a continue statement to skip the current iteration of a loop and move on to the next one
for item in range(10):
    if item == 5:
        break
    print(item)
for item in range(10):    
    if item % 2 == 0:
        continue
    print(item)


for item in [2, 2, 5, 4, 1,8,9,3]:
    print ("*"*item)






#LISTS 
# a list is a collection of items that are ordered and changeable.
#list allow duplicate values and can contain different data types.
#intrestingly lists are defined using square brackets [] and items are separated by commas.
#facts about lists is that they are mutable, which means you can change their content after they have been created.
my_list = [1, 2, 3, 4, 5]
print(my_list[0]) # Output: 1
print(my_list[1:4]) # Output: [2, 3, 4]
my_list.append(6) # Adds 6 to the end of the list
print(my_list) # Output: [1, 2, 3, 4, 5, 6]
my_list.insert(0, 0) # Inserts 0 at index 0
print(my_list) # Output: [0, 1, 2, 3, 4, 5, 6]
my_list.remove(3) # Removes the first occurrence of 3
print(my_list) # Output: [0, 1, 2, 4, 5, 6]


my_list[1:2] = [10, 20, 30] # Replaces the element at index 1 with 10, 20, and 30 know the list is [0, 10, 20, 30, 2, 4, 5, 6]
# if the number of items assigned is less then the number of items being replaced, the list will be shortened. If the number of items assigned is greater than the number of items being replaced, the list will be extended.
print(my_list) # Output: [0, 10, 20, 30, 2, 4, 5, 6]
my_list[1:4] = [] # Removes the elements at index 1, 2, and 3
print(my_list) # Output: [0, 2, 4, 5, 6]


# to add a item in a list we use append method and that will append the item at the end of the list and if we want to add a item at a specific index we can use insert method and that will insert the item at the specified index and shift the other items to the right.

a = [1, 2, 3]
a.append(4)# Output: [1, 2, 3, 4]
a.insert(0, 0) # Output: [0, 1, 2, 3, 4]
a.insert(2, 1.5) # Output: [0, 1, 1.5, 2, 3, 4]


#if we want to add multiple items to a list we can use the extend method and that will add the items to the end of the list from another list or any iterable.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)

 #The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")#this is a tuple and we can use extend method to add the items of the tuple to the list
thislist.extend(thistuple)
print(thislist) # Output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']



#to remove an item from a list we can use the remove method and that will remove the first occurrence of the item from the list and if we want to remove an item at a specific index we can use the pop method and that will remove the item at the specified index and return it.

my_list = [0, 1, 2, 4, 5, 6,3,4]
my_list.remove(4) # Output: [0, 1, 2, 5, 6, 3, 4] # if there are multiple occurence of the item remove in list then first occurrence will be removed

#The pop() method removes the specified index.
my_list.pop(2) # Output: [0, 1, 5, 6, 3, 4] # removes the item at index 2 which is 2 and returns it
#If you do not specify the index, the pop() method removes the last item.
my_list.pop() # Output: [0, 1, 5, 6, 3] # removes the last item which is 4 and returns it

li = [1, 2, 3, 4, 5,4,6,88,64,7,4]
#find the largest number from the list
largest = li[0] 
smallest = li[0]
for num in li:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print(f"The largest number in the list is: {largest}")
print(f"The smallest number in the list is: {smallest}")