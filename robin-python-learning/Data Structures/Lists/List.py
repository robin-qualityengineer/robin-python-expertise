myList = ['One', 'Two' , 'Three', 'Four', 'Five']
addList = ['Six', 'Seven', 'Eight' , 'Nine', 'Ten']
alphabeticList = ['a', 'e', 'b', 'd' ,'c']
numericList = [1, 3, 5, 2, 4]

#Concatenate Two List Values
concatenatedList = myList + addList
print(concatenatedList)

#Length of Lists
myList_lengthList =  len(myList)
print(myList_lengthList)

addList_lengthList =  len(addList)
print(addList_lengthList)

concatenatedList_lengthList =  len(concatenatedList)
print(concatenatedList_lengthList)

#Slicing of Lists
sliceList = myList[1:]
print(sliceList)

#Append Value in List
appendList = myList.append('Eleven')
print(myList)

#Pop List Values
poppedList = myList.pop()
print(myList)

poppedIndexList = myList.pop(1)
print(myList)

#Sort List Values
sortAlphabets = alphabeticList.sort()
print(alphabeticList)

numericList.sort()                                       #Another Way To Sort
sortNumeric = numericList
print(sortNumeric)

#Reverse List Values
reverseAlphabets = alphabeticList.reverse()
print(alphabeticList)