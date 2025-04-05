# defining the function
def greet_user():
    """
    Displays general greeting, 'Hello'
    """

    print("Hello!")

def greet_user_by_name(user_name): # function has parameter, user_name is the parameter
    """
    Prints Hello along with username. Function has parameter,
    user_name  is parameter
    :param user_name: it is a username
    :return: None
    """
    print(f"Hello {user_name.title()}!")

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My" + animal_type + "'s name is " + pet_name.title() + ".")

# Calling the Function
greet_user()

# greet_user_by_name()
# TypeError: greet_user_by_name() missing 1 required positional argument: 'user_name'

greet_user_by_name('john') # needs argument, 'john' is an argument
greet_user_by_name('jane') # needs argument, 'john' is an argument
greet_user_by_name('kylian') # needs argument, 'john' is an argument

# print("today", 'is Sunday', 2+2, 'is 5', False)
# print("today", 'is Sunday', 2+2, 'is 5', False, sep="|",
#       end="<3@@@")
# print("abc")
print("****** positional argument ******")
describe_pet('horse', 'maximus')
print("****** keyword argument ******")
describe_pet(pet_name='maximus', animal_type='horse')

print("******* positional arguments ***********")
describe_pet('horse', 'maximus')

print("******** keyword arguments **********")
describe_pet(pet_name='maximus', animal_type='horse')

print("******* Way of execution: positional arguments ***********")
describe_pet('horse', 'maximus')
# describe_pet_with_default('dog', 'markus')
# describe_pet_with_default('cat', 'lazy', 2)

print("******** Way of execution: keyword arguments **********")
describe_pet(pet_name='maximus', animal_type='horse')
# describe_pet_with_default(pet_name='markus', animal_type='dog')
# describe_pet_with_default(age=2, pet_name='lazy', animal_type='cat')

# describe_pet_with_default(age=2, animal_type='cat')
# TypeError: describe_pet_with_default() missing 1 required positional argument: 'pet_name'
# H/w: 8-3, 8-4, 8-5