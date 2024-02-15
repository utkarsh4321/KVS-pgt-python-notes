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
# if provided all three params value
print(
    '3. output for the string.find(val,startIndex,endIndex) method (here provided val present inside) val=l, startIndex = 6 and endIndex = 11 ---->',str.find('l',6,11)) #output: 9
print('\n')
# |-------------index()---------------|
# index() method
# Syntax
# string.index(value,startIndex,endIndex) // return index of given value in given string
# By default startIndex is 0 and endIndex is length of string
# if provided only one params value
print('|------index()---------|')
print('\n')
print('1. output for the string.index(val) here val = l --->',str.index('l')) # output: 2
# if provided value not found in string will return value error
# print('2. output for the string.index(val) here val = a return value error because val not present in given string --->',str.index('a')) # output: value error substring not found
#if provided all three params value
print(
    '3. output for the string.index(val,startIndex,endIndex) here val = l startIndex = 6,endIndex = 11 --->',str.index('l', 6, 11))  # output: 9
print('\n')
# |-------------ends with()---------------|
# endswith() method
# Syntax
# string.endswith(value,startIndex,endIndex) // return true if given string ends with given value
# By default startIndex is 0 and endIndex is length of string
# if provided only one params value
print('|------endswith()---------|')
print('\n')
print('1. output for the string.endswith(val) here val = l --->',str.endswith('l')) # output: False
# Becusse hello world is not ends with l
# if provided value not found in string will return False
print('2. output for the string.endswith(val) here val = a --->',str.endswith('a')) # output: False
# if provided all three params value
print('3. output for the string.endswith(val,startIndex,endIndex) here val = l, startIndex="6",endIndex="10" --->',str.endswith('l',6,10)) # output: True"
print('\n')
# |-------------starts with()---------------|
# startswith() method
# Syntax
# string.startswith(value,startIndex,endIndex) // return true if given string starts with given value
# By default startIndex is 0 and endIndex is length of string
# if provided only one params value
print('|------startswith()---------|')
print('\n')
print('1. output for the string.startswith(val) here val = he --->',str.startswith('he')) #output: True
#if provide all three params value
print('2. output for the string.startswith(val,startIndex,endIndex) here val = wor, startIndex=6,endIndex=11 --->',str.startswith('wor',6,11)) #output: True
print('\n')
# |-------------isalnum()---------------|
# isalnum() method
# Syntax
# string.isalnum() // return true if string is alphanumeric
print('|------isalnum()---------|')
print('\n')
print('1. output for the string.isalnum() here string =\'123\' --->','123'.isalnum()) #output: True
print('2. output for the string.isalnum() here string =\'123abc\' --->','123abc'.isalnum()) #output: True
# When string contains any other character like whitespace or special character it will return false
print('3. output for the string.isalnum() here string =\'123 abc\' when --->','123 abc'.isalnum()) #Output:False
print('4. output for the string.isalnum() here string =\'abc\' when --->','123@abc'.isalnum()) #Output: False
print('\n')
# |-------------isalpha()---------------|
# isalpha() method
# Syntax
# string.isalpha() // return true if string is alphabetic,no number, whitespace, special character accepted
print('|------isalpha()---------|')
print('\n')
print('1. output for the string.isalpha() here string =\'123\' --->','123'.isalpha()) #Output: False
print('2. output for the string.isalpha() here string =\'123abc\' --->','123abc'.isalpha()) #Output: False
# When string contains any number, whitespace, special character it will return false
print('3. output for the string.isalpha() here string =\'123 abc\' when --->','123 abc'.isalpha()) #Output: False
print('4. output for the string.isalpha() here string =\'abc\' when --->','abc'.isalpha()) #Output: True
print('\n')
# |-------------isdigit()---------------|
# isdigit() method
# Syntax
# string.isdigit() // return true if string is digit,no alphabet, whitespace, special character accepted
print('|------isdigit()---------|')
print('\n')
print('1. output for the string.isdigit() here string =\'123\' --->','123'.isdigit()) #Output True
print('2. output for the string.isdigit() here string =\'123abc\' --->','123abc'.isdigit()) #Output: False
print('3. output for the string.isdigit() here string =\'123 abc\' when --->','123 abc'.isdigit()) #Output : False

print('4. output for the string.isdigit() here string =\'abc\' when --->','abc'.isdigit()) #Output: False
print('\n')
# |-------------islower()---------------|
# islower() method
# Syntax
# string.islower() // return true if string is lower case all the characters should be in lower case
print(
    '|------islower()---------|')
print('\n')
print('1. output for the string.islower() here string =\'hello\' --->','hello'.islower()) #Output: True
print(
    '2. output for the string.islower() here string =\'Hello\' when --->','Hello'.islower()) #Output: False
print(
    '3. output for the string.islower() here string =\'hello world\' when --->','hello world'.islower()) #Output: True
print('\n')
# |-------------isupper()---------------|
# isupper() method
# Syntax
# string.isupper() // return true if string is upper case all the characters should be in upper case
print('|------isupper()---------|')
print('\n')
print('1. output for the string.isupper() here string =\'HELLO\' --->','HELLO'.isupper()) #Output: True
print('2. output for the string.isupper() here string =\'Hello\'  --->','Hello'.isupper()) #Output: False
print('3. output for the string.isupper() here string =\'Hello World\' --->','Hello World'.isupper()) #Output: False
print('\n')
# |-------------isspace()---------------|
# isspace() method
# Syntax
# string.isspace() // return true if string containing only space no any other thing like number,alphabet,special character are not accepted
print('|------isspace()---------|')
print('\n')
print('1. output for the string.isspace() here string =\'\' empty string --->',''.isspace()) #Output: False
print('2. output for the string.isspace() here string =\' \t\' string with whitespace --->',' '.isspace()) #Output: True
print('3. output for the string.isspace() here string =\'hello world\' --->','hello world'.isspace()) #Output: False
print('\n')
# |-------------lstrip()---------------|
# lstrip() method
# Syntax
# string.lstrip(value) // if value provided then remove all the leading characters of string which are same as value. If value not present then by default remove all the leading whitespaces from left side of string
print('|------lstrip()---------|')
print('\n')
print('1. output for the string.lstrip(value) here string =\'hello world\' value=hell --->','hello world'.lstrip('hell')) #Output: o world
# If no any value provided then by default remove all the leading whitespaces from left side of string
print('2. output for the string.lstrip() here string =\' hello world\' value not provided --->','hello world'.lstrip()) #Output: hello world remove white space from left side of string
print('\n')
# |-------------rstrip()---------------|
# rstrip() method
# Syntax
# string.rstrip(value) // if value provided then remove all the trailing characters of string which are same as provide value from right side of string. If value not present then by default remove all the trailing whitespaces from right side of string.
print('|------rstrip()---------|')
print('\n')
print('1. output for the string.rstrip(value) here string =\'hello world\' value=world --->','hello world'.rstrip('world')) #Output:hello
# If no any value provided then by default remove all the trailing whitespaces from right side of string.
print('2. output for the string.rstrip() here string =\'hello world    \' value not provided --->','hello world  '.rstrip()) #Output: hello world
print('\n')
# |-------------strip()---------------|
# strip() method
# Syntax
# string.strip(value) // if value provided then remove all the leading and trailing characters of string which are same as provided value.If no any value provided then by default remove all the trailing whitespaces from both side of string.
print('|------strip()---------|')
print('\n')
print('1. output for the string.strip(value) here string =\'hello world\' value=world --->',
      'hello world'.strip('world'))  # Output:hello
# If no any value provided then by default remove all the trailing whitespaces from both side of the string
print('2. output for the string.strip() here string =\'   hello world    \' value not provided --->','   hello world    '.strip()) #Output: hello world
print('\n')
#



