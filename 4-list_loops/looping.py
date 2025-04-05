# LOOPING is creating repetitive line for each item on the list!!!
# "FOR" looping example from book:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

gifts = ['flowers', 'cologne', 'chocolate', 'diamond']
print("\n# looping example:")
for gift in gifts:
    # repetitive code
    print(f"\nI want to give {gift} for you on March 8th with love!")
    print(f"{gift} cost me a lot:)")
    print("------------------------")
print("Do not worry they all are nothing all I need is you.") # looping stopped!

# looping continues until you stop indentation
# for var_name in list_name :
# do not forget to indent, requires at least one line to repeat

print("=============================================================")
print("# 4-1")
pizzas = ['cheese', 'pepperoni', 'neapolitan']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("\nI really love pizza!")
print("\n# 4-2")
animals = ['fish', 'dog', 'cat']
for animal in animals:
    print(f"A {animal} would make a great pet")
print("\nAny of these animals would make a great pet!")

print(gifts)
print(f"removing the element from the list: {gifts.pop()}")
print(gifts)
print(f"")
