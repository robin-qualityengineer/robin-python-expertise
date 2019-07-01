myDictonary = {'key1':'value1', 'key2':'value2'}
priceLookup = {'Apple':100, 'Mangoes':150, 'Banana':40}
interestingDictionary = {'k1':123, 'k2':[0, 1, 2], 'k3' : {'insideKey':100}}
vowelsDictionary = {'v1':'a', 'v2':'e', 'v3':'i',  'v4':'o', 'v5':'u'}

#Getting value by passing Key
print(myDictonary['key1'])
print(priceLookup['Apple'])

#Getting List value associated with Dictionary
print(interestingDictionary['k2'])

#Getting Index value of List associated with Dictionary
print(interestingDictionary['k2'][2])

#Getting Nested Key Value pair
print(interestingDictionary['k3']['insideKey'])

#Changing values to uppercase
uppercaseDictionary = vowelsDictionary['v1'][0].upper()
print(uppercaseDictionary)

#Addition of new key value pair
priceLookup['Grapes'] = 60
print(priceLookup)

#Modifying Values"
priceLookup['Grapes'] = 70
print(priceLookup)

#Getting all Key 
print(priceLookup.keys())

#Getting all Values 
print(priceLookup.values())

#Getting all Key-Value pair as Items
print(priceLookup.items())








