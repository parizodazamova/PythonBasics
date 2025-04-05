# class - bluprint (model of real-world thing)
class Dog:
    """General representation of real-world dog."""

    #attributes
    name = 'Willie'
    age = 2

    #behaviour
    def sit(self):
        print(f"{self.name} is sitting.")

    def roll_over(self):
        print(f"{self.name} is rolling over {self.age} times because it is {self.age} years old.")

# creating the object - instantiation
my_dog = Dog() # my_dog is the object, i.e. my_dog is the instance of Dog class
my_dog.sit()

friend_dog = Dog()
# Updating the value of class attribute for each object
friend_dog.name = 'Roksi' 
friend_dog.age = 3

friend_dog.sit = Dog()
my_dog.sit()
my_dog.roll_over()
friend_dog.roll_over()