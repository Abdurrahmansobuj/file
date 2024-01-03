# # str1 = '-----------Hello world------------'
# #
# #
# # print(str1.lstrip('-'))
# #
# # str1 = '-----------Hello world------------'
# #
# #
# # print(str1.rstrip('-'))
#
# str1 = '-----------Hello world------------'
#
# print(str1.strip('-'))



# print(str1.split())
# print(str1.split(','))
# print(str1.split(',',maxsplit=1))

# print(str1.splitlines())
#print(str1.splitlines(False))

# print(str1.index('e'))
# print(str1.rindex('e'))
#
# print(str1.find('o'))
# print(str1.rfind('o'))

# str1 = 'sobuj'
#
# # print(str1.strip('-'))
# # print(str1.lstrip('-'))
# # print(str1.rstrip('-'))
#
# print(str1.count('o'),4)

# linl = 'hello python'
#
#
# print(linl.startswith('he'))

# linl = 'hello python'
#
# print(linl.endswith('n'))

# linl = 'hello python'
#
# print(linl.index('o'))
# print(linl.rindex('o'))

# linl = 'hello python'
#
# print(linl.find('p'))
# print(linl.rfind('h'))
#
# linl = 'hello python'
#
# print(linl.split())
# print(linl.split(' '))
# print(linl.split(','))
# print(linl.split(',',maxsplit=1))
#
# print(linl.split(',',maxsplit=1))
# print(linl.split(','))

# print(linl.splitlines())

# name = 'hello, sobuj im\n23 years old'
#
# print(name.split())
# print(name.split(','))
# print(name.split(',',maxsplit=1))
# print(name.splitlines(True))
# print(name.splitlines(False))

# str1 = 'Sobuj islam '
# #
# str2 = 'Md sobuj \tislam'
#
# str3 = ['Hello', 'world']




# print(str1.center(29,'*'))
# print(str1.ljust(20,'*'))
# print(str1.rjust(40,'*'))


# print(str2.expandtabs(8))


# print(str4[3:15])
#
# str4 = 'my, name\'s sobuj'
#
# print(str4.split())
# print(str4.split(','))
# print(str4.split(',',maxsplit=1))

# str1 = '1234567890'
# str2 = 'hfiunguwi'
# str3 = 'hf46g,4di38b'
#
# print(str1.isdigit())
# print(str1.isnumeric())
# print(str1.isdecimal())
# print(str1.isalnum())
# print(str2.isalpha())
# print(str1.isascii())
# print(str3.isprintable())
#
# str1 = 'ABDUR RAHMAN'
#
# str2 = 'Sobuj'
#
# str3 = 'sobuj'
#
# str4 = 'Abdur Rahman Sobuj'
#
# str5 = 'sOBUJ'
#
# print(str1.isupper())
# print(str2.istitle())
# print(str3.islower())

# str1 = 'sobuj'
#
# print(str1.upper())
#
# str2 = 'SOBUJ'
#
# print(str2.lower())
# print(str2.casefold())
#
# str3 = 'soByrs'
#
# print(str3.capitalize())
#
# str4 = 'Abdur RAHMNA'
#
# print(str4.swapcase())
#
# str5 = ' '
#
# print(str5.isspace())
#
# str1 = 'Abdur Rahman is a good student'
#
# substring = 'a'
#
# print(str1.count(substring))
#
# person = {'name':'sobuj', 'age':19}
#
# print('my name\'s is {name} and age is {age}'.format_map(person))
#
#
# person = {'name': 'sobuj', 'age': 20}
#
# print('my name is {name} my age {age}'.format_map(person))

# num1 = '2'
#
# print(num1.zfill(5))
#
# users = [
#     {
#         'name':'sobuj',
#         'username':'sobujislam',
#         'email':'sobujislam@gmail.com',
#         'address':{
#             'streer':'tangail'
#         },
#     },
#
#     {
#         'name':'abdur rahman',
#         'username':'abdurrahman',
#         'email':'abdurrahman@gmail.com',
#         'address':{
#             'streer':'tangail'
#         },
#     }
# ]
#
# for user in users:
#     name = user.get('name')
#     username = user.get('username')
#     email = user.get('email')
#     streer = user.get('address').get('streer')
#     sentence = f'This is {name} He mail adrress {email} and mail username {username} he was reside {streer}'
#     print(sentence)

# st1 = '2'
#
# print(st1.zfill(5))
#
# str1 = 'Md SObuj Islam'
#
# lass = str1.casefold()
#
# print(lass.replace(' ','-'))

# str1 = '--------sobuj-----'
#
# print(str1.lstrip('-'))
# print(str1.rstrip('-'))
# print(str1.strip('-'))


# str1 = 'Abdur rahman sobuj'
#
# # print(str1.split())
# # print(str1.split(maxsplit=1))
#
# print(str1.isprintable(50))

# str1 = 'Abdur Rahman \tSobuj'
#
# print(str1.expandtabs(10))

# str2 = 'Sobuj'
#
# print(str2.center(10,'*'))

# str1 = 'Abdur Rahman'
#
# str2 = 'Sobuj Islam'

# str3 = 'Abdur Rahman Sobuj'
#
#
# # print(str1.center(20,' '))
# # print(str2.center(100,'*'))
# print(str3.center(50,'*'))
#
# str1 = 'Abdur Rahman SObuj'
#
# print(str1.center(300,' '))