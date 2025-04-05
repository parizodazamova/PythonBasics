# HW 3-1, 3-2, 3-3
# 3-1
names = ['karen', 'joshua', 'angela', 'andrew', 'pam']

# 3-2
print(f"Hello {names[0].title()}! \nHow are you today?\n")
print(f"Hello {names[1].title()}! \nHow are you today?\n")
print(f"Hello {names[2].title()}! \nHow are you today?\n")
print(f"Hello {names[3].title()}! \nHow are you today?\n")
print(f"Hello {names[4].title()}! \nHow are you today?\n")

# 3-3
cars = ['race car', 'classic car', 'electric car']
print(f"I would like to own a {cars[0]}.")
print(f"I would like to drive a {cars[1]}.")
print(f"I do not want to own a {cars[0]}.")

# 3-4
guests = ['Angie', 'John', 'Nancy', 'Bob']
print(guests)

print(f"Greetings Mrs. {guests[0]}, \nWe would like to invite you to a dinner this weekend at our new house!\n")
print(f"Greetings Mr. {guests[1]}, \nWe would like to invite you to a dinner this weekend at our new house!\n")
print(f"Greetings Ms. {guests[2]}, \nWe would like to invite you to a dinner this weekend at our new house!\n")
print(f"Greetings Mr. {guests[3]}, \nWe would like to invite you to a dinner this weekend at our new house!\n")

# 3-5
print(f"Greetings Mrs. {guests[0]}, \nWe would like to invite you to a dinner this weekend at our new house!\n")
print(f"Sorry Mr. {guests[1]}, \nWill not be able to make it to the dinner.\n")
del(guests[1])
guests.insert(1, 'Tony')
print(f"Greetings Mr. {guests[1]}, \nWe would like to invite you to a dinner this weekend at our new house!\n")
print(f"Sorry Ms. {guests[2]}, \nWill not be able to make it to the dinner.\n")
del(guests[2])
guests.append('Charlie')
print(f"Greetings Mr. {guests[2]}, \nWe would like to invite you to a dinner this weekend at our new house!\n")
print(f"Greetings Ms. {guests[3]}, \nWe would like to invite you to a dinner this weekend at our new house!\n")

# 3-6
guests.insert(0, 'Karen')
guests.insert(2, 'Corey')
guests.append('Will')
print(f"Greetings Mrs. {guests[0]}, \nWe would like to invite you to a dinner this weekend at our new house!\n")
print(f"Greetings Mrs. {guests[1]}, \nWe would like to invite you to a dinner this weekend at our new house!\n")
print(f"Greetings Mr. {guests[2]}, \nWe would like to invite you to a dinner this weekend at our new house!\n")
print(f"Greetings Mr. {guests[4]}, \nWe would like to invite you to a dinner this weekend at our new house!\n")
print(f"Greetings Ms. {guests[5]}, \nWe would like to invite you to a dinner this weekend at our new house!\n")
print(f"Greetings Mr. {guests[6]}, \nWe would like to invite you to a dinner this weekend at our new house!\n")
