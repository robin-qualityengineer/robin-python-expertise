#Print value in Iterative Mode
x=0
while x < 5:
    print(f' The current value of x is : {x}')
    x =x+1
    #x+=1
else:
    print(f' Current vallue is no more less than 5')

#Use of  Pass Keyword
myList=[1,2,3]
for item in myList:
    #comment
    pass                            #This helps us from syntax error, and you can paste your code later here

#Use of Continue Keyword
for letter in 'Sammy':
    if letter == 'a':
        continue
    print(letter)

#Use of Break Keyword
for letter in 'Sammy':
    if letter == 'a':
        break
    print(letter)

#Use of Continue Keyword in While Loop
y=0
while y < 5:
        if y==3:
            break
        print(y)
        y+=1


