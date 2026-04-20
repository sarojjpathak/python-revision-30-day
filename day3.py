# TUPLE is also one of the in built data type of python. It is a collection which is ordered and unchangeable. It allows duplicate members.
#the tuple is defined by using parentheses () and the items are separated by commas.
#one of the main difference between list and tuple is that list is mutable (can be changed) while tuple is immutable (cannot be changed).
#creating a tuple


a = ("apple", "Banana", "cherry")
def sorttuple(a):
    return  a.lower()



print(a)
#accessing tuple items
print(a[0]) #accessing the first item
print(a[1]) #accessing the second item
# Note: Tuples are immutable, so the following line would cause an error
# a.sort(reverse=True)
# print(a)
#if we want the reverse then we can use the reversed() function
b = sorted(a,reverse=False,key=sorttuple)#as banana is capital then it will come first in the sorted list to solve this we can use the key parameter in the sorted() function to ignore the case sensitivity
print(list(b))


#to determine the length of tuple we can use the len() function
print(f"The length of the tuple is: {len(a)}")

b = ("apple")
print(type(b)) #this will print <class 'str'> because it is not a tuple, it is a string. To create a tuple with one item we need to add a comma after the item.
c = ("apple",)
print(type(c)) #this will print <class 'tuple'> because it is a tuple with one item.



####It is also possible to use the tuple() constructor to make a tuple.
d = tuple(("apple", "Banana", "cherry")) # note the double round-brackets
print(d)


a = tuple("hello")
print(a)#Output:('h', 'e', 'l', 'l', 'o')
x = tuple()
print(x) #Output:() this is an empty tuple


#IMP 
thistuple = tuple(("apple"))
print(thistuple) #Output:('a', 'p', 'p', 'l', 'e') this is not a tuple with one item, it is a tuple with 5 items because the string "apple" is iterable and it is treated as a sequence of characters. To create a tuple with one item we need to add a comma after the item.


#to access the items in a tuple we can use the index number, just like we do with lists. The index starts from 0.

thistuple = tuple(("apple",))
print(thistuple) #Output:('apple',) this is a tuple with one item because we have added a comma after the item.
x= (1, 2, 3, 4, 5, 6)
#to access the items in a tuple we can use the index number, just like we do with lists. The index starts from 0.
print(x[::2]) #Output:(1, 3, 5) 
print(x[::-1]) #Output:(6, 5, 4, 3, 2, 1) this is the reverse of the tuple because we have used the step -1 in the slicing. The step -1 means that we want to go through the tuple in reverse order. [start:stop:step] the start and stop are optional, if we don't specify them then it will take the default values. The default value of start is 0 and the default value of stop is the length of the tuple. The step is also optional, if we don't specify it then it will take the default value of 1.







# we cant update or change the items in a tuple because it is immutable. But we can convert the tuple into a list, change the list and then convert it back to a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) #Output:('apple', 'kiwi', 'cherry') this is the updated tuple after converting it to a list and then back to a tuple.












#unpacking a tuple is when we assign the values of a tuple to a variable. We can unpack a tuple by using the assignment operator = and the variable names on the left side of the operator and the tuple on the right side of the operator.
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits # we can do unpacking  in list as well but here we are doing it in a tuple. The number of variables on the left side of the operator must be equal to the number of items in the tuple on the right side of the operator, otherwise we will get an error.

print(green)
print(yellow)
print(red)
#output: apple
#banana
#cherry

# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits   

print(green)
print(yellow)
print(red)

#we can write * in middle of the variables as well  if * variable is in  the second last then last variable without star will be assigned with last item in list or tuple and the variable with star will be assigned with the rest of the items in the list or tuple before last variable

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(a, *b, c) = fruits
print(a) #Output: apple
print(b) #Output: ['banana', 'cherry', 'strawberry'] this is the list of items between the first and last item in the tuple because we have used the star variable in the middle of the variables.
print(c) #Output: raspberry this is the last item in the tuple because we have used the star variable in the middle of the variables and the last variable without star will be assigned with the last item in the tuple.



thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


for x in thistuple:
    print(list(x))




#one of the min difference betweeen list and typle in joining is that in tuple we use addition operator to join and we dont have the extend() method like in list. In tuple we can use the + operator to join two or more tuples. The + operator will create a new tuple that is the concatenation of the two tuples.
#here we dont have join() method like in list .

tuple1 = ("a", "b" , "c")
print(tuple1.index("b")) #Output: 1

a = ("apple",)
print(a.count("a")) #Output: 0 because the item "a" is not in the tuple, it is a string "apple" that is in the tuple. If we want to count the number of times the item "apple" is in the tuple then we can use the count() method like this:
a = ("appleadfgwsaa")
print(a.count("a")) #Output: 4 because the item "a" is in the string "appleadfgwsaa" 4 times. The count() method



#


#SET

#Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

# * Note: Set items are unchangeable, but you can remove items and add new items.

# Sets are written with curly brackets.



saroj_set = {"saroj","sameer"}
saroj_set.add("sujan")
print(saroj_set) #Output: {'sameer', 'sujan', 'saroj'} the order of the items in the set is not guaranteed to be the same as the order in which they were added, because sets are unordered.
#the order in which it is shown is not the order in which it was added, because sets are unordered. The items in the set are stored in a way that allows for fast membership testing and efficient use of memory, but it does not maintain any particular order. So, when we print the set, the items may be displayed in a different order than they were added.

saroj_set.remove("sameer")
print(saroj_set)


#Note : the value 1 and True and 0 and False is consider same in set and as duplucate is not allowes one will be removed
a = {2,3,True,1,False,"saroj"}
print(a)

# as true and 1 has same hash value hash(true ) hash(1) so which one came at first will be in set other one will be removed 


#to add item in sset

a.add("hello")
print(a) #output

b = {"cat","dog"}

#to add another set to current set 
#To add items from another set into the current set, use the update() method.
a.update(b)
print(a)


#to remove
thisset = {"apple", "banana", "cherry"}
print("------------LEARNING DISCARD-------------")
print(f"thisset items :{thisset}")

thisset.discard("banana")
print("after discard")

print(f"thisset items :{thisset}")# If the item to remove does not exist, discard() will NOT raise an error.



#pop the return value of pop is the value which have been removed 
thisset = {"apple", "banana", "cherry"}
print("------------------LEARNING_POP-----------")
print(thisset)
print(f" the value which is poped out is :{thisset.pop()}") 
print(thisset)


#clear function is used to clear the item in set
print("------------------LEARNING_clear-----------")
print(f"thisset items :{thisset}")
thisset.clear()
print("after clear ")
print(f"thisset items :{thisset}")



#delete
#The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

# print(thisset) thisset is not defined
