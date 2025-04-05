# 4-3
for value in range(1,21):
    print (value)
print("=====================================")
# 4-4
for value in range(1,1000001):
    print (value)
print("=====================================")

# 4-5
numbers = list(range(1,1000001))
print(f"\nMinimum number:", min(numbers))
print(f"\nMaximum number:", max(numbers))
print(f"\nSum of all numbers:", sum(numbers))
print("=====================================")

# 4-6
odd_numbers = list(range(1,20,2))
for number in odd_numbers:
    print(number)
print("=====================================")

# 4-7
threes = list(range(3,31,3))
for number in threes:
    print(number)
print("=====================================")

# 4-8
cubes = []
for number in range (1,11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)
print("=====================================")

# 4-9
cubes = [number**3 for number in range(1,11)]
for cube in cubes:
    print(cube)
