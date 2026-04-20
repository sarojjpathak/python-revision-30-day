#python join methods
#There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.



#UNION ()
#The union() method returns a new set with all items from both sets.
a = {"a","b","c"}
b = {"c","d"}

c = a.union(b)
print(c)#output is : a b c d 


#intersection 


intersection = a.intersection(b)
print(intersection)
#You can use the & operator instead of the intersection() method, and you will get the same result.
#Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
intersection = a & b
print(f"this is new set {intersection}")

#we can join multiple set also we just have to include sets inside parenthesis after join and seprated by comma
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)



#update method
#The update() method inserts all items from one set into another.

#the update() changes the original set, and does not return a new set.


#NOTE we should understand that while updatind or joining if there are two same items then that will became  1 if set a has aa and set b also has aa in its item then if we join them or update set a with b then there will be only one aa


#Difference
#the  difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

#Note with intersection and difference we can apply this method with any type of built in datatype of python such as list tuple but "&"  and "-" for difference can only be applied with set


a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9,10}
c=(3,4,5,6,7,8,9,10)


aa = a - b
print(f"aa: {aa}")

aaa = a & b
print(f"aaa= {aaa}")

#aaaa = a - c #this is not valid as c is tuple 



#The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.



set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)



#Symmetric Differences
#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
print(set3)

#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(f"symmetric diff update{set1}")




#FROZEN SET
#set Can use .add(), .remove(), .pop()     but frozen set	No modification methods available as this in imutable

# Standard Set
numbers = {1, 2, 3}
numbers.add(4)  # Works perfectly

# Frozenset
frozen_numbers = frozenset([1, 2, 3])
# frozen_numbers.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'


#Hashable = Has a permanent "ID number" so Python can find it instantly in a dictionary or set.

#Unhashable = Can change, so it’s not allowed to have a permanent ID number.
#To understand hashability at an expert level, you have to look at how Python manages memory and data retrieval via Hash Tables.In a standard list, searching for an item is an $O(n)$ operation—you might have to check every single element. In a dictionary or set, searching is $O(1)$, or "constant time." This near-instant lookup is only possible because of hashability.1. The Hash Function and DeterminismAt the architectural level, a hashable object must implement a __hash__() method that satisfies determinism. This means that for the entire lifetime of the object, hash(obj) must return the same integer.$$H(x) = y$$If the internal state of $x$ changes (like adding an item to a list), the resulting $y$ would change. If $y$ changes, the object’s location in the underlying hash table array becomes "lost," as the index is derived directly from that hash value:$$\text{index} = \text{hash}(\text{object}) \pmod{\text{array\_size}}$$2. The Contract of EqualityHashability is strictly tied to Equality ($==$). Python enforces a contract:If a == b, then hash(a) must equal hash(b).However, the reverse is not necessarily true (this is called a hash collision). If two different objects produce the same hash, Python resolves this using "Open Addressing," checking the next available slot in the memory array. For this resolution to work, the objects must be comparable. This is why hashable objects must also implement __eq__()


# Frozenset Methods
# Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.

# Method	Shortcut	             Description	
# copy()	 	                     Returns a shallow copy	
# difference()    	-	          Returns a new frozenset with the difference	
# intersection()	          	          Returns a new frozenset with the intersection	
# isdisjoint()	 	                       Returns whether two frozensets have an intersection	
# issubset()	        <= / <	          Returns True if this frozenset is a (proper) subset of another	
# issuperset()	         >= / >	          Returns True if this frozenset is a (proper) superset of another	
# symmetric_difference()  ^	          Returns a new frozenset with the symmetric differences	
# union()	|	                       Returns a new frozenset containing the union	

# Note When you use a method (like .union() or .intersection()), the type of the result is determined by the object on the left side of the operation.

