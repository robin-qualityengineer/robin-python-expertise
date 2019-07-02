myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_sum = 0

#Print LIst Contents
for myVariable in myList:
    print(myVariable)


#Print Hello in iteratively
for myVariable in myList:
    print("Hello")


#Print Even Numbers
for myVariable in myList:
    if  myVariable % 2 == 0:
        print(f' Even Number : {myVariable}' )
    else:
        print(f' Odd Number : {myVariable}' )

#Print Addition of All Numbers
for num in myList:
    list_sum = list_sum + num
print(list_sum)
   
#Print letters in String
myString = "Hello World"
for letter in myString:
    print(letter)

#Print values in Tuple
tup = (1, 2, 3)
for item in tup:
    print(item)

#Print List values which contains Tuples
myListTuple  = [(1,2),(3,4),(5,6),(7,8)]
print(len(myListTuple))
for a,b in myListTuple:
    print(b)

#Print List values containing Tuples with three array   
myListTupleArray = [(1,2, 3),(4, 5, 6),(7, 8, 9)]
print(len(myListTupleArray))
for a,b,c in myListTupleArray:
    print(b)

#Print Dictionary Key Data
myDictionary = {'k1':1, 'k2':2, 'k3':3}
for key in myDictionary:
    print(key)

#Print Dictionary Key and its Values
for key, value in myDictionary.items():
    print(value)
