mySet = set()

#Add value in Set
mySet.add(1)
print(mySet)

mySet.add(2)
print(mySet)

#Same values cannot be added again. Only unique values are accepted
mySet.add(2)
print(mySet)

#Converting/Casting List Values in Set
myList = [1,1,1,1,2,2,2,2,3,3,3,3]
print(set(myList))