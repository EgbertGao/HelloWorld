'''alien_0={}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0['color'])

# 6-1 用字典储存一个熟人的信息
people = {}
people['first_name'] = '马'
people['last_name'] = '萌萌'
people['age'] = 30
people['city'] = '深圳'
print(people)


# 6-2 每个人喜欢的数字
loved_nums = {
    'gao': '8',
    'ma': '6',
    'chen' : '7'}
for name in loved_nums:
    print(name.title())

# 6-5 词汇表
rivels = {
    'Nile' : 'Egypt',
    'Amazon' : 'America',
    'Changjiang' : 'China'
}

for name, value in rivels.items():
    print('The ' + name.title() + ' runs through ' + value.title() + '.\n')


# 6-6 调查
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

people_numbers = ['jen', 'phil', 'egbert', 'hebe']
for name in people_numbers:
    if name in favorite_languages.keys():
        print(name.title() + ', thank you for your participate!')
    else :
        print(name.title() + ', please take our poll!')

# 6-7 用字典储存3个熟人的信息

people_0 = {
    'first_name' : '马',
    'last_name' : '萌萌',
    'age' : 30,
    'city' : '深圳'
}
people_1 = {
    'first_name' : '马',
    'last_name' : '宝宝',
    'age' : 12,
    'city' : '武汉'
}
people_2 = {
    'first_name' : '马',
    'last_name' : '呆呆',
    'age' : 50,
    'city' : '广州'
}
persons = [people_0, people_1, people_2]
for person in persons:
    print(person)


#6-8 多个字典输出宠物名称
mammal = {
    'cats' : 'John',
    'dogs' :'Egbert'
}
fish ={
    'grass crap' : 'Sharon'
}
birds = {
    'Hawk' : 'Flavia'
}
amphibians = {
    'frog' : 'Ken'
}
reptiles = {
    'snake' : 'Anna'
}

pets = [mammal, fish, birds, amphibians, reptiles]
for pet in pets:
    print(pet)


# 6-9 需重做
favorite_places = {
    'Anna': 'Beijing',
    'Anna': 'Tianjin',
    'Anna': 'Shanghai',
    'Egbert': 'Wuhan',
    'Egbert': 'Changsha',
    'Egbert': 'Xi an',
    'Ken': 'Xinjiang',
    'Ken': 'xi zang',
    'Ken': 'Guangzhou'
}
for name, value in favorite_places.items():
     if favorite_places[name] == 'Anna':
        print('\nname:' + name)
        print('\nvalue:' +value)
'''

#6-11 城市，用3个城市名用作键，每座城市创造一个字典
cities = {
    'shenzhen' : {
        'province' : 'GuangDong',
        'population' : '1000w',
        'fact' : 'People like running outside.'
    },

    'tianjin' : {
        'province': 'HeBei',
        'population': '500w',
        'fact': 'People like enjoying themselves.'
    },

    'chengdu' : {
        'province': 'Sichuan',
        'population': '600w',
        'fact': 'People like eating spicy food.'
    }
}
for city, city_info in sorted(cities.items()):
    print('This city is ' + city.title() + '.')
    country = city_info['province']
    people_num = city_info['population']
    fact = city_info['fact']
    print("It's in " + country.title() + '.')
    print('The population there is about ' + people_num + '.')
    print(fact +'\n')