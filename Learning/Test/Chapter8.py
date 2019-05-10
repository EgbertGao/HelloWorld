'''
#8-1 打印一个句子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。
def display_message(self):
    print('我在本章学的是{}！'.format(self))

display_message('函数')

#8-2
def favorite_book(title):
    print('One of my favorite books is {}.'.format(title))

favorite_book('Alice in Wonderland')


#8-3
def make_shirt(size, type):
    print('This T-shirt size is {}-inches, write {} on it.'.format(size, type))

make_shirt(20, 'Fat')

#8-4
def make_shirt(size = 'big', type = 'I love Python'):
    print('This T-shirt size is {}-inches, write {} on it.'.format(size, type))

make_shirt()
make_shirt('medium')
make_shirt(type = 'Vehicle')

#8-5
def describe_city(name = 'Reykjavik', country = 'China'):
    print('{1} is in {0}.'.format(country, name.title()))

describe_city()
describe_city('chengdu')
describe_city('shenzhen')



# 8-6
def city_country(name, country):
    print(name.title(), ',', country.title())

city_country('chengdu', 'china')

#8-7
def make_album(singer, album):



#8-9
magicians = ['a', 'b', 'c', 'd']

def show_magicians(name):
    for magician in name:
        print('Welcome ' + magician + '!')

show_magicians(magicians)


# 8-10

magicians = ['a', 'b', 'c', 'd']

def make_great(persons_old, persons_new):
    for person in persons_old:
        name = 'the Great ' + person
        persons_new.append(name)
    show_magicians(persons_new)

def show_magicians(name):
    print('The following magician is:')
    for magician in name:
        print('Welcome ' + magician + '!')

make_great(magicians, magicians[:])
# for magician in magicians:
#     print('Welcome ' + magician + '!')
'''

