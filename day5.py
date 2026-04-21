#Dictionary   

#Dictionaries are used to store data values in key:value pairs. 
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


print(f"--------------DICTIONARY----------")
thisdict = {
  "brand": "apple",
  "model": "m5 air",
  "year": 2025
}
f"---------------------------------------------"
print(thisdict)


#if there is multiple key with same name then at that time latest value for key will be in 
 # with the help of key we can access the value for that key
 #if we want to print th value of brand then 

print(f"Value of key brand is : {thisdict['brand']}")


#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

thisdict["brand"] = "samsung"
print(f"Value of key brand  after changing the value is : {thisdict['brand']}")


#Dictionaries cannot have two items with the same key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#duplicates will be overwritten by latest



#Dictionary length
print(f"length of thisdict is {len(thisdict)}")   #output is 3

#The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"],
  "interior":{"black","white"}
}



# dictionary also have dic constructor

# Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


#Python - Access Dictionary Items
#we can access the value of dict by the dict name and alsong with the key name inside the [] .
#There is also a method called get() that will give you the same result:
x = thisdict["age"]
y = thisdict.get("age") #both of this give the same output


# what is the diff btwn get and normal method 
# in normal method if the key doesnot exists then the the program will show an error and crash but in get method we can set an default
a = {
    "aa":1,
    "bb":2
}
#print(a["cc"])#this will crash the program by showing key error but in get method we can set a default if there exists no key
print(f"{a.get("cc",0)}")  #here the output will be zero 0



#if we want to find all key in dict then we will use keys() method
print(f"key method for key : {a.keys()}")
#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
# No, keys() does NOT return a list

# It returns a special object called dict_keys

# d = {"a": 1, "b": 2}
# print(d.keys())

#  Output:

# dict_keys(['a', 'b'])
#  What is dict_keys then?
# It looks like a list
# But it is not actually a list
# It is a view object (dynamic)

# Meaning: if dictionary changes, it updates automatically




#Get Values
# The values() method will return a list of all the values in the dictionary.
print(f"values methood : {car.values()}")   #this will return a dist_values object


# to get all items we  use items method

#without items method
#The items() method will return each item in a dictionary, as tuples in a list.
d = {"a": 1, "b": 2}

for key in d:
    print(key, d[key])


    #with items
for key, value in d.items():
 print(key, value)


 #Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")



#Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018



#Update Dictionary      : "update will update the value if key exists and if key doesnot exists then it will add thast key and value"
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020,
                "month": "may",
                "brand":"student"})


#Adding Items
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict["saroj"] = "yes"



#The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
#The argument must be a dictionary, or an iterable object with key:value pairs.
print(thisdict.items())



#REmove items 
#pop() method

thisdict = {
  "brand": "hyundai",
  "model": "i20",
  "year": 2020
}
thisdict.pop("model")
print(thisdict)

#thisdict.pop() this is wrong in this we should use pop_item method before version 7.6 random item was removed but know last item will be removed


#popitem()
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
#The del keyword can also delete the dictionary completely:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#deleting the whole dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.



print("----------------------------------------------------------")
print("----------------------------------------------------------")
print("----------------------------------------------------------")



my_data = {
    "name": "Saroj Pathak",
    "country": "Nepal",
    "city": "Kathmandu",
    "language": ["Nepali", "English"],
    "field_of_study": "Computer Science",
    "subjects": ["Discrete Mathematics", "Microprocessor (8085)", "C++"],
    "skills": ["Python basics", "Problem solving"],
    "favorite_player": "Cristiano Ronaldo",
    "relationship_status": "In a relationship",
    "goal": "Improve programming skills and learn daily"
}


my_data.update({"name":"saroz pathak"})
print(my_data)
print("----------------------------------------------------------")
my_data["father"] = "devilal pathak"
print(my_data)
print("----------------------------------------------------------")
my_data.popitem();#this will remove last item
my_data.pop("subjects")
print(my_data)
del my_data["goal"]
print(my_data)


#clear () will make the dict empty

print("----------------------------------------------------------")
# to print all key from dict
for key,value in my_data.items():
 print(f"key of my data using items method{key}")
 print("----------------------------------------------------------")
 print(f"values of my data using items method{value}")

thisdict = {}



#this use extra loop for values so we use items method that reduce the loop so thats the good practice
for x in thisdict:
  print(x) # this will print all key of x
 #to print value we use indexing method
 
  print(thisdict[x])
  print("------------------------------------------------")
 # Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
print("------------------------------------------------")

#we can make copy using dict function also
a = dict(thisdict)
print(a)
print("------------------------------------------------")


#nested dictionary
#a dictionary can contain dictionary so that is called nested dict

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#how to access the nested dict


print(myfamily["child2"]["name"])


#loop in nested

for x in myfamily:
    for y in myfamily[x]:
      print(myfamily[x][y])




for x,y in myfamily.items():
  outter_key = x;
  for a,b in y.items():
    print(f"{a},{b}")
  


  #Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
keys = ["a", "b", "c"]
values = [1,2,3]

d = dict.fromkeys(keys, "default")
print(d)  #output {'a': 0, 'b': 0, 'c': 0}
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary






#In Python, pass is a do-nothing statement.   PASS
x=21
# It is used when Python expects some code, but you don’t want to write anything yet.
for i in range(5):
    pass
if x > 10:
    pass  # will write code later

# if True:
#     # error ❌ after we write a loop we have write the statement


#SYNTAX FOR DICTIONARY COMPREHENSION
#{key_expression: value_expression for element in iterable}

dict1 = {'nepal': 43 , 'india':36,'china':45}#this is dict with country temperature
dict_in_celcious = {key:  int(value-34*0.6) for key,value in dict1.items() }
print(dict_in_celcious)
