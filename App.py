# # Strings use quotes when declared
# name="Taylor"
# # integers don't use quotes when being declared
# age = 26

# print(name+' is a boy')
# # int must use comma, string can use either
# print(name+' is', age)
# print(name+' is from Idaho')

# print('Hi. \nHow are you?')
# name ='Taylor'
# print(name.upper())
# print(name.lower())
# isupper() and islower() are for bools

# # length of string
# print(len(name))

# print(name.index('a'))
# print(name.replace('T', 'B'))

#NOTE  NUMBERS
# print(78+22)

# print(20%6)
# number = 55
# number2 = str(number)
# print(number2)

# print(abs(-5))
# print(max(4,1))

# from math import *
# print(sqrt(100))


# NOTE GETTING USERS INPUT
# name = input('Input your name: ')
# age = int(input('Input your age: '))
# print('Your name is ' + name + ' and you are', age , 'years old')

# sentence = input('Enter your sentence: ')
# print(sentence)
# word1= input('Enter the word to replace: ')
# word2 = input('Enter the word to replace it with: ')
# print(sentence.replace(word1,word2))

# NOTE lists in python
# countries = ['USA', 'united kingdom', 'Ghana', 'Nigeria']
# print(countries[1:3])

# countries = list(('Nigeria', 34, True))
# print(countries)

# NOTE List Methods
list1=[5,2,3,6,9,4]
list2=['banana', 'apples', 'mangos', 'oranges']

# list1.extend(list2)
# print(list1)
# list2.append('cherry')
# list2.insert(1,'cherry')
# list2.remove('banana')

# print(list2.count('mangos'))
# list1.sort()
# list2.reverse()
# list3 = list2.copy()
# print(list3)
list2.pop()
print(list2)