#  All string method for KVS PGT
str = "hello world"
print('|----------------------------------------------|')
print('|   String we are working on is : ', str, '|')
print('|----------------------------------------------|')
#|-------------len()---------------|
# len() method
# Syntax
# len(string|list|tuple|dictionary) // return length of given string|list|tuple|dictionary
print('|---------len()-----------|')
print('\n')
print('output for len() method ---->', len(str))  # output: 11
print('\n')
# |-------------capitalise()---------------|
# capitalize() method
# Syntax
# string.capitalize() // return capitalized string(make first letter capital))
print('|---------capitalize()-----------|')
print('\n')
print('output for the string.capitalize() method ---->',
      str.capitalize())  # output: Hello world
print('\n')
# |-------------titile()---------------|
# titile() method
# Syntax
# string.title() // return title string (make all first letter of each word capital)
print('|---------title()-----------|')
print('\n')
print('output for the string.title() method ---->',
      str.title())  # output: Hello World
print('\n')
# |-------------upper()---------------|
# upper() method
# Syntax
# string.upper() // return upper case string(make all letter capital)
print('|---------upper()-----------|')
print('\n')
print('output for the string.upper() method ---->',
      str.upper())  # output: HELLO WORLD
print('\n')
# |-------------lower()---------------|
# lower() method
# Syntax
# string.lower() // return lower case string(make all letter small)
print('|---------lower()-----------|')
print('\n')
print('output for the string.lower() method ---->',
      str.lower())  # output: hello world
print('\n')
# |-------------count()---------------|
# count() method
# Syntax
# string.count(value,startIndex,endIndex) // return count of given value in given string
# By default startIndex is 0 and endIndex is length of string
# if provided only one params value
print(
  '|---------count()-----------|')  # count() method
print('\n')
print(
    '1. output for the string.count(val) method (here provided val present inside string) val = l ---->',
    str.count('l'))  # output: 3
# if provided value not found in string will return 0
print(
    '2. output for the string.count(val) method (here provided val not present inside string) val = a ---->',
    str.count('a'))  # output: 0
# if provided all three params value
print(
    '3. output for the string.count(val,startIndex,endIndex) method (here provided val present inside string) val=l startIndex = 6 and endIndex = 11 ---->',
    str.count('l', 6, 11))  # output: 1
print('\n')
# |-------------find()---------------|
# find() method
# Syntax
# string.find(value,startIndex,endIndex) // return index of given value in given string
# By default startIndex is 0 and endIndex is length of string
# if provided only one params value
print('|---------find()-----------|')
print('\n')
print(
    '1. output for the string.find(val) method (here provided val present inside string) val = l ---->',
    str.find('l'))  # output: 2
# if provided value not found in string will return -1
print(
    '2. output for the string.find(val) method (here provided val not present inside string) val = a ---->',
    str.find('a'))  # output: -1
print('\n')
