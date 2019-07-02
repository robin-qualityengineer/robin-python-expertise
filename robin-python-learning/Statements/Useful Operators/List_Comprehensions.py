myString = 'hello'
myList = []

for letter in myString:
    myList.append(letter)
    print(myList)

#breaking down the code
myList = [letter for letter in myString]
print(myList)

#Another way
myList = [variable_name for variable_name in 'word']
print(myList)

#Nested Loops
myList = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        myList.append(x*y)
        print(myList)

#best way
myList = [x*y for x in [2,4,6] for y in [1, 10, 1000]]
print(myList)

#Using range function in these List comprehensions
myList = [variable_number for variable_number in range(0,11)]
print(myList)

#Using range function in these List comprehensions and getting the square values
myList = [variable_number**2 for variable_number in range(0,11)]
print(myList)

#Using range function in these List comprehensions and getting the even values
myList = [variable_number for variable_number in range(0,11) if variable_number%2==0]
print(myList)

myList = [variable_number if variable_number%2==0 else 'ODD' for variable_number in range(0,11)]
print(myList)

#Using range function in these List comprehensions and getting the temperature by converting celcius into farenhite
myCelciusList = [0, 10, 20, 34.5]
fahrenhite = []
for temp in myCelciusList:
    fahrenhite.append((9/5)*temp + 32)

    #Best way to write same code.
fahrenhite = [((9/5)*temp + 32) for temp in myCelciusList]
print(fahrenhite)