# 1. Write a function called myfunc that prints the string 'Hello World'?

def myfunc():
    print('Hello World')

myfunc() #Calling Function


# 2. Define a function called myfunc that takes in a name, and prints 'Hello Name'
 
def myfunc2(name):
    print("Hello " + name)

myfunc2('Robin') #Calling Function


# 3.  Define a function called myfunc that takes a Boolean value (True or False). If True, return 'Hello', and if False, return 'Goodbye'

def myfunc3(myValue):
    if myValue == True:
        print('Hello')
        return "Hello"
    else:
        print('Goodbye')
        return "Goodbye"

myfunc3(False) #Calling Function

# 4. Define a function called myfunc that takes three arguments, x, y and z. If z is True, return x, If z is false, return y.

def myfunc4(x, y, z):
    if z==True:
        print(x)
        return x
    else:
        print(y)
        return y

myfunc4(True, 'y', 'z') #Calling Function

# 5. Define a function called myfunc that takes in two arguments and returns their sum.

def myfunc5(value1, value2):
    return value1 + value2

result = myfunc5(5,10)  #Calling Function
print(result)

# 6. Define a function called is_even that takes in one argument, and returns True if the passed-in value is even, False if it is not.

def is_even(value):
    if value%2==0:
        print('True')
        return True
    else:
        print('False')
        return False

is_even(2)   #Calling Function

# 7.  Define a function called is_greater that takes in two argument, and returns True if the first value is greater than the second, False if it is less than or equal to the second.

def is_greater(value1, value2):
    if value1>value2:
        print("True")
        return True
    elif value1<=value2:
        print("False")
        return False

is_greater(1,2)    #Calling Function

# 8. Define a function called myfunc that takes in an arbitary number of arguments, and return the sum of those arguments.

def myfunc8(*args):
    print(sum(args))
    return sum(args)

myfunc8(10, 20, 30)    #Calling Function

# 9. Define a function called myfunc that takes in an arbitary number of arguments, and return a list containing only those arguments that are even.

def myfunc9(*args):
     return [n for n in args if n%2==0]

result = myfunc9(1,2,3,4,5,6)
print(result)

# 10. Define a function called myfunc that takes in a String, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. 
# Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation.
#The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.

def myfunc10(word):
    result=""
    for index, letter in enumerate(word):
        if(index % 2 == 0):
            result += letter.lower()
        else:
            result += letter.upper()
        index +=1
    print(result)


myfunc10('letter')

            





