'''
#9-1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant's name is {}.".format(self.restaurant_name))
        print("Restaurant's cooking style is {}.".format(self.cuisine_type))

    def open_restaurant(self):
        print('The restaurant {} now is opening!'.format(self.restaurant_name))

my_restaurant = Restaurant('Kongfu', 'spicy')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


#9-2
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant's name is {}.".format(self.restaurant_name))
        print("Restaurant's cooking style is {}.".format(self.cuisine_type))

    def open_restaurant(self):
        print('The restaurant {} now is opening!'.format(self.restaurant_name))

my_restaurant1 = Restaurant('Kongfu', 'spicy')
my_restaurant1.describe_restaurant()

my_restaurant2 = Restaurant('小青龙', '鲁菜')
my_restaurant2.describe_restaurant()

my_restaurant3 = Restaurant('流水人家', '东北菜')
my_restaurant3.describe_restaurant()


#9-3
class User():
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print("This person's brief introduction:")
        print('The name is {}{}, {} years old, {}'.format(self.first_name, self.last_name, self.age, self.gender))


first_person = User('陈', '振', 29, '男')
first_person.describe_user()
'''