# def multipul_num(*args):
#     total = 0
#
#     for number in args:
#         total +=number
#     return total
# los = multipul_num(1,2,3,4,5,6,7,8,9,10,11)
#
# print(los)

# def num(*args):
#     total = 0
#
#     for number in args:
#         total += number
#     return total
# los = num(23, 45, 67, 43 )
#
# print(los)

# def num(*args):
#     total = 0
#
#     for number in args:
#         total += number
#     return total
# print(num(12,34,5,64,35,4,3))
#
# def num(*args):
#     total = 0
#
#     for number in args:
#         total += number
#     return total
# print(num(12,34,5,6,78,9,23))
#
# def multiple(a, b):
#     result = a + b
#     po = a - b
#     rt = a * b
#
#     return result, po, rt
# los = multiple(7, 2)
#
# print(los)
#
# def number(a, b):
#     x = a + b
#     y = a - b
#     z = a * b
#     return x, y, z
#
# x,y,z = number(3, 8)
#
# print(x)
# print(y)
# print(z)
#
# def num(*args):
#     result = 0
#     for number in args:
#         result += number
#     return result
# print(num(12,34,56,78,90,12))
#
# def num(a, b):
#     result = a + b
#     sab = a - b
#     return result, sab, a, b
# test = num(8, 2)
#
# test_list = list(test)
#
# test_list[3] = 11
#
# test = tuple(test_list)
# print(test)

# def num(a,b):
#     result = a + b
#     volume = a -b
#     return result, volume
# print(num(9, 3))

# def num(*args):
#     result = 0
#     for number in args:
#         result+= number
#     return result
#
# print(num(1,2,3,4,5,6,7,8,910,10))
#
# def num(a, b,):
#     result = a + b
#     volume = a - b
#     return result, volume,a,b
#
# test = num(67,98)
# list_con = list(test)
# list_con[0] = 23
# test = list_con
# print(test)
#
# def agurment(*args):
#     result = 0
#     for number in args:
#         result += number
#     return result
# print(agurment(1,2,34,5))
#
# def numb(*args):
#     total = 0
#     for number in args:
#         total += number
#     return total
# los = numb(27,30,845,12,3,5,76,7,9)
#
# print(los)
#
# def num(a, b):
#     result = a + b
#     volume = a - b
#     x = a * b
#     y = a / b
#     return result, volume,x,b
#
# print(num(876, 234))

# def num(*args):
#     result = 0
#     for number in args:
#         result += number
#     return result
# print(num(23,45,67,8,9))

# def num(a,b):
#     result = a + b
#     volume = a * b
#     return result, volume,a,b
# los = num(34,98)
#
# list_los = list(los)
# list_los[2] = 50
# los = list_los
# print(los)
#
# def sulgify(taxt):
#     result = taxt.strip().lower().replace(' ','-')
#     while '--' in result:
#         result = result.replace('--','-')
#     return result
# title = 'This is a Laptops'
#
# los = sulgify(title)
# print(los)

# def num(a, b,):
#     result = a + b
#     volume = a - b
#     return result, volume
#
# los = num(5, 2)
#
# # print(los)
#
# def number(a, b):
#     x = a + b
#     y = a / b
#     return x, y
# test = number(4, 2)
# list_test = list(test)
# list_test[1] = 10
# test = list_test
# print(test)
#
# def number(*args):
#     result = 0
#     for number in args:
#         result +=  number
#     return result
# los = number(23,45,67,8,10)
# print(los)
#
# import random
# num = 1, 2, 3, 4, 5, 6, 7,8, 9
# computer_number = random.choice(num)
# i = 0
# while i < computer_number:
#     number = int(input('Enter number: '))
#     if computer_number == number:
#         print('Goood')
#         break
#
# i += 1
#
# import random
# number = 1, 2, 3, 4, 5, 6, 7, 8, 9,
# computer_number = number
#
# computer_number = random.choice(number)
#
# i = 0
#
# while i < computer_number:
#     number = int(input('Enter number: '))
#     if computer_number == number:
#         print('Clear')
#         break
# i += 1

# users = [
#     {
#         'name':'sobuj',
#         'username':'sobujislam',
#         'email':'sobujislam@gamil.com',
#         'address':{
#             'street':'tangail',
#             'village':'chana khola',
#             'zipcode':'1912'
#         },
#         'phone':'019835642',
#         'website':'abcd.com',
#         'company':'debal dekar',
#         'gender':'man'
#     },
#
#     {
#         'name':'abdurrahman',
#         'username':'abdurrahman',
#         'email':'abdurrahman@gamail.com',
#         'address':{
#             'street':'tangail',
#             'village':'phatrail',
#             'zipcode':'1253'
#         },
#         'phone':'012836454',
#         'website':'abcd.oxy',
#         'company':'w#shoocle',
#         'gender':'man'
#     },
#
#     {
#         'name':'Tisha',
#         'username':'abdubakar',
#         'email':'abubakar@gmail.com',
#         'address':{
#             'street':'dhaka',
#             'village':'katghora',
#             'zipcode':'1382'
#         },
#         'phone':'0198545323',
#         'website':'netbook.com',
#         'company':'netbook',
#         'gender':'woman'
#     }
# ]
#
# for user in users:
#     name = user.get('name')
#     username = user.get('username')
#     email = user.get('email')
#     gender = user.get('gender')
#     if gender == 'man':
#         pronoun = 'His'
#     else:
#         pronoun = 'Her'
#     street = user.get('address').get('street')
#     village = user.get('address').get('village')
#     zipcode = user.get('address').get('zipcode')
#     phone = user.get('phone')
#     website = user.get('website')
#     company = user.get('company')
#
#     sentence = (f'This is {name} he is a programmer {pronoun}\nHas a company it {pronoun} {company} & {website} name\'s'
#                 f'\nIt\'s {pronoun} personal number Her was bron {street} {pronoun} village name {village} '
#                 f'and zip number {zipcode}\nit\'s username of website {username} {pronoun} gender {gender}')
#
#     print(sentence)