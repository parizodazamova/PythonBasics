# 4-10
pizzas = ['cheese', 'vegetarian', 'pepperoni', 'chicken bbq', 'margarita']
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nThe first three pizzas in the list are:")
print(pizzas[:3])

print("\nThe pizzas from the middle of the list are:")
middle_list = len(pizzas) // 2-1
print(pizzas[middle_list:middle_list+3])

print("\nThe last three pizzas in the list are:")
print(pizzas[-3:])

# 5-1

car = 'subaru'

print("Is car 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car 'audi'? I predict False.")
print(car == 'audi')

color = 'blue'
print("\nIs color 'blue'? I predict True.")
print(color == 'blue')

print("\nIs color 'green'? I predict False.")
print(color == 'green')

age = 25
print("\nIs age greater than 20? I predict True.")
print(age > 20)

print("\nIs age less than 18? I predict False.")
print(age < 18)

city = 'Cleveland'
print("\nIs city 'Cleveland'? I predict True.")
print(city == 'Cleveland')

print("\nIs city 'New York'? I predict False.")
print(city == 'New York')

temperature = 70
print("\nIs temperature above 65? I predict True.")
print(temperature > 65)

print("\nIs temperature below 50? I predict False.")
print(temperature < 50)
