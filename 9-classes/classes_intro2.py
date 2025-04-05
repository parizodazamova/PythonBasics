# class - bluprint (model of real-world thing)
class Dog:
    """General representation of real-world dog."""

    # attributes
    # rewrite the constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #behaviour
    def sit(self):
        print(f"{self.name} is sitting.")

    def roll_over(self):
        print(f"{self.name} is rolling over {self.age} times because it is {self.age} years old.")

# creating the object - instantiation
my_dog = Dog("Willie", 2) # my_dog is the object, i.e. my_dog is the instance of Dog class
my_dog.sit()

friend_dog = Dog("Roksi", 3)
# Updating the value of class attribute for each object


friend_dog.sit
my_dog.sit()
my_dog.roll_over()
friend_dog.roll_over()

my_dog.age = 4 # reset the value of attributes
my_dog.roll_over()

my_dog.name = 'Charlie'
my_dog.roll_over()
print(f"my dog's name is {my_dog.name.upper()}.")