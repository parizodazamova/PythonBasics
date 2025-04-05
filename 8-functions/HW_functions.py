print ("***** 8-3 *****")
def make_shirt(size='small', message='Be Yourself'):
    """Displays the size of the t-shirt and the message on the t-shirt."""
    print(f'I have a {size} t-shirt and it says "{message}"')

print("***** positional argument *****")
make_shirt(size='medium', message='Be Strong!')

print("\n***** keyword argument *****")
make_shirt(message="Don't Give Up!")

print ("\n***** 8-4 *****")
def make_shirt(size='large', message='I love Python!'):
    """Displays the shirt in different  sizes with the specific message."""
    print(f"The t-shirt I made is {size}.")
    print("It will say " '"' + message + '"'" on the back of the t-shirt.\n")
make_shirt()
make_shirt(size='medium')
make_shirt('x-small', 'Test Automation')

print ("\n***** 8-5 *****")
def describe_city(city, country='spain'):
    """Information about the city."""
    msg = (city.title() + ' is in ' + country.title() + ".")
    print(msg)
describe_city('barcelona')
describe_city('madrid')
describe_city('paris', 'france')