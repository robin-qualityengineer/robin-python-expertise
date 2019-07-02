
#Open Text File
myFile = open('D:\\Projects\\Research\\Python\\Study Lab\\robin-python-expertise\\robin-python-learning\\Files\\myFile.txt')

#Read Text File
#print(myFile.read())

#File  Locations
#For windows, you need to use double \ so python doesn't treat the second \ as an escape character, a file path is in the form:
#Windows: myFile = open('D:\\Projects\\Research\\Python\\Study Lab\\robin-python-expertise\\robin-python-learning\\Files\\myFile.txt')
#MAC and Linux: myFile = open('D:/Projects/Research/Python/Study Lab/robin-python-expertise/robin-python-learning/Files/myFile.txt')

# Close Text File
myFile.close()

#Open Text File in Another way
#Step1
myFile = open('D:\\Projects\\Research\\Python\\Study Lab\\robin-python-expertise\\robin-python-learning\\Files\\myFile.txt')
#Step2
with open('D:\\Projects\\Research\\Python\\Study Lab\\robin-python-expertise\\robin-python-learning\\Files\\myFile.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)

#Write in a File
with open('D:\\Projects\\Research\\Python\\Study Lab\\robin-python-expertise\\robin-python-learning\\Files\\myFile.txt', mode='w') as my_new_file: 
    contents = my_new_file.write('This is new data')

#ReadText File for the written contents
with open('D:\\Projects\\Research\\Python\\Study Lab\\robin-python-expertise\\robin-python-learning\\Files\\myFile.txt', mode='r') as my_new_file:
    contents = my_new_file.read()
    print(contents)

#Append Text File 
with open('D:\\Projects\\Research\\Python\\Study Lab\\robin-python-expertise\\robin-python-learning\\Files\\myFile.txt', mode='a') as my_new_file:
    contents = my_new_file.write('\nFour on Four')
    print(contents)
with open('D:\\Projects\\Research\\Python\\Study Lab\\robin-python-expertise\\robin-python-learning\\Files\\myFile.txt', mode='r') as my_new_file:
    contents = my_new_file.read()
    print(contents)
   
#Create New Text File
with open('D:\\Projects\\Research\\Python\\Study Lab\\robin-python-expertise\\robin-python-learning\\Files\\createdFile.txt', mode = 'w') as createdNewFile:
    createdNewFile.write('I created this file!')
with open('D:\\Projects\\Research\\Python\\Study Lab\\robin-python-expertise\\robin-python-learning\\Files\\createdFile.txt', mode = 'r') as createdNewFile:
    contents = createdNewFile.read()
print(contents)

     
