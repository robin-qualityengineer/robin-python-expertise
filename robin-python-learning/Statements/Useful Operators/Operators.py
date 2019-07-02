#Input Operator
result = input("What is your name?")              #Note: Everything in input operator is considered as String. To convert it to another type, you may need to change its type as shown below

result = float(input("What is your age? "))

#Range Operator

myList = [1,2,3]
for num in range(2, 10, 2):           #range(Sart From, Till (-1), Steps (jumps))
    print(num)

print(list(range(0,11,2)))

#Enumerate Operator
index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count+=1

word = 'abcde'
for index, letter in enumerate(word):                      #enumerate gets the data in tuple format
    print(index)
    print(letter)
    print('\n')

#Zip Operator
myList = [1,2,3]
myList2 = ['a','b','c']
myList3 = [100, 200, 300]
#for item in zip(myList, myList2, myList3):
   # print(item)
print(list(zip(myList, myList2)))

#In Operator
print('x' in [1, 2, 3])
print('x' in ['x', 'y', 'z'])
print('a' in 'aphabets')
print('regid' in {'regid':12345})
d = {'regid':12345}
print(12345 in d.keys())
print(12345 in d.values())

#Min value
print(min(myList))

#Max value
print(max(myList))

#Random Library - Shuffle
from random import shuffle
myListValue = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(myListValue)
print(myListValue)

#Random Library - Randint
from random import randint
print(randint(0,100))
