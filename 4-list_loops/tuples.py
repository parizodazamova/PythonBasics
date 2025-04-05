# Tuple is immutable data structure, can not be modified, you can reset the value
# List is mutable, CRUD can be done

players = ['charles', 'marina', 'michael', 'florance', 'eli', 'john', 'mark', 'marie']

a = 12
b = 'hello'
names = ['john', 'jane', 12, True]
# type(variable) - returns the data type of the variable
print(type(players))
print(type(a))
print(type(b))
print(type(names))
print(type(names[0]))
print(type(names[-1]))

print("length", len(players))
print("first element", (players[0]))
print("length", (players[-1]))
print("length", (players))

players = ('charles', 'marina')