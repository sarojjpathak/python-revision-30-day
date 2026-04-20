#  problem 1: move all zero to end of array
#input = [0,1,0,3,12]
#output = [1,3,12,0,0]
input = [0,1,0,3,12]
x = []
y = []
for n in input:
    if n != 0:
        x.append(n)
    else:
        y.append(n)
x.extend(y)
print(x)



#another way 
inputis = (input("enter a list"))
inputis = list(int(inputis))
for i in range(len(inputis)):
    if inputis[i] == 0:
        inputis.append(inputis.pop(i))

print(inputis)



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

a = {1,2,3,4,5}
saroj_set.add(a)
print(saroj_set)
