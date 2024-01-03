users = [
    {
        'name':'Abdur Rahman',
        'email':'abr@gmail.com',
        'PH':'019387534',
        'address':{
            'street':'Tangail',
            'village':'Chana-khola',
            'up':'phatrail'
        },

        'company':{
            'address':'Tangail',
            'cm_name':'AL-fafa',
            'cm_mail':'alfafa@gmail.com'
        },

        'website':'abc.com'
    },

    {
        'name':'Abu Bakar',
        'email':'abubakar@gmail.com',
        'Ph':'012837456',
        'address':{
            'street':'Dhaka',
            'village':"Katghora",
            'up':'Asulia'
        },

        'company':{
            'street':'Noya para, Asulia, Saver, Dhaka',
            'cm-name':'Agami apparals limited',
            'cm-mail':'Dekko Group'
        },

        'website':'dekko.com'
    },

    {
        'name':"Abdullah",
        'email':'Abdullha@gmail.com',
        'PH':'01928438456',
        'address':{
            'street':'Amtala',
            'village':'Amtala',
            'up':'Amtala'
        },

        'company':{
            'street':'Amtala',
            'cm-name':'Saine apparels',
            'cm-mail':'saine@gmail.com'
        },

        'website':'saine.com'
    }
]

for user in users:
    name = user.get('name')
    email = user.get('email')
    Phone = user.get('PH')
    street = user.get('address').get('street')
    village = user.get('address').get('village')
    up = user.get('address').get('up')
    cm_name = user.get('company').get('cm-name')
    cm_street = user.get('company').get('street')
    cm_mail = user.get('company').get('cm-mail')
    web = user.get('website')

    setence = (f'This is {name} He is owner of  {cm_name} it his company the company mail it {cm_mail}'
               f'\nThe company locad {cm_street} and web site address {web} his Ph no {Phone} his mail address if {email}'
               f'\n his street {street} he was bron {village} and it his present up {up}')

    print(setence)