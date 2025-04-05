# 5-4 - ALIEN COLORS #2:
alien_color = 'green'

if alien_color == 'green':
    print("You green alien just earned 5 points!")
else:
    print("You just earned 10 points!")

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You yellow alien just earned 10 points!")

# 5-5 - ALIEN COLORS #3:
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You red alien just earned 15 points!")
print("=================================================")
# 5-6 - STAGES OF LIFE:
age = 29

if age < 2:
    print ("You are a baby!")
elif age < 4:
    print ("You are a toddler!")
elif age < 13:
    print ("You are a kid!")
elif age < 20:
    print ("You are a teenager!")
elif age < 65:
    print ("You are an adult!")
else:
    print("You are and elder!")
print("=================================================")

# 5-7 - Favorite Fruit:
favorite_fruits = ['strawberries', 'apples', 'pears']
if 'grapes' in favorite_fruits:
    print("You really like grapes!")
if 'pineapples' in favorite_fruits:
    print("You really like pineapples!")
if 'strawberries' in favorite_fruits:
    print("You really like strawberries!")
if 'mangoes' in favorite_fruits:
    print("You really like mangoes!")
if 'pears' in favorite_fruits:
    print("You really like pears!")
print("=================================================")

# 5-8 - Hello Admin
usernames = ['karen', 'bob', 'will', 'admin', 'eric']
for username in usernames:
    if username == 'admin':
        print('\nHello admin, would you like to see a status report?\n')
    else:
        print(f'Hello {username}, thank you for logging in again.')
print("=================================================")

# 5-9 - No Users
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print('\nHello admin, would you like to see a status report?\n')
        else:
            print(f'Hello {username}, thank you for logging in again.')
else:
    print("We need to find some users!")
print("=================================================")

# 5-10 - No Users
current_users = ['karen', 'bob', 'will', 'AdMin', 'Eric']
new_users = ['angie', 'William', 'BRYAN', 'nancy', 'karen']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")

