# 8. A) Make a class called Restaurant. The __init__() method for Restaurant should store two
# attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant()
# that prints these two pieces of information, and a method called open_restaurant() that prints a
# message indicating that the restaurant is open. Make an instance called restaurant from your
# class. Print the two attributes individually, and then call both methods.
# B) Make a class called User. Create two attributes called first_name and last_name, and then
# create several other attributes that are typically stored in a user profile. Make a method called
# describe_user() that prints a summary of the user’s information. Make another method called
# greet_user() that prints a personalized greeting to the user. Create several instances representing
# different users, and call both method for each user.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.restaurant_name + " serves " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.restaurant_name + " is open."
        print("\n" + msg)


restaurant = Restaurant('Harsh', 'Burger')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
