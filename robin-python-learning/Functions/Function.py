#Normal Function

def name_function():
    print("Hello")

name_function()

###################################################
#Parametrized Function

def say_hello(name):
    print("Hello " + name)

say_hello('Robin')


###################################################
#Function with Return Keyword 

def addition(num1, num2):
    return num1 + num2
    

result = addition(2,4)
print(result)
###################################################
#Find out if the word "dog" is in a string?

def word_check(myString):
    if 'dog' in myString.lower():
        print('Found word dog')
        return True
    else:
        print('Didnt found word dog')
        return False

#Another way for the same code is:
def easier_word_check(myString):
    return 'dog' in myString.lower()
print("Found Dog")


word_check('My Dog ran away')
easier_word_check('My Dog ran away')
####################################################
"""
PIG LATIN

- If the word starts with a vowel, add 'ay' to end
- If the word doesn't start with a vowel, put first letter at the end, then add 'ay'
examples:
word - ordway
apple - appleay
"""

def pig_latin(word):
    first_alphabet = word[0]
#check if a vowel
    if first_alphabet in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_alphabet + 'ay'  
        print(pig_word)
        return pig_word

pig_latin('Apple')

####################################################
#args (Arguments) and kwargs (Keyword Arguments)
def myfunc(*args):
    print(args)

myfunc(10, 20, 30) #You can pass as many arguments as you want, because we are using *args as parameter in function. It will return back a tuple value

#kwargs (Keyword Arguments)
def myfunc1(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice {}'.format(kwargs['fruit']))
    else:
        print('I do not find any fruit here')

myfunc1(fruit = 'apple', veggie = 'lettuce')

#args (Arguments) and kwargs (Keyword Arguments)

def myfunc2(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I like to have {} {}".format(args[0], kwargs['fruit']))

myfunc2(10, 20, 30, fruit = 'apple', snacks = 'maggie')