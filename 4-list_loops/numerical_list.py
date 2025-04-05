# range() functions

# range(start_number_inc, end_number, step) : default start_number_inc=0, step=1
# range(5, 10, 2) -> 5, 7, 9
# range(5, 10, 1) -> 5, 6, 7, 8, 9
# range(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (default start and default step)
print(list(range(10)))

for num in range(10):
    print(num)
print("---------------------------")
print("***** How do you loop only 3 times? *****")
for num in range(3):
    print(num)
print("***** How do you print even numbers from 20 to 30? *****")
for num in range(20,31,2):
    print(num)

print("***** Print numbers dividable by 5 between 60 to 93? *****")
for num in range(60,94,5):
    print(num)

print("***** Print square of numbers between 160 and 171? *****")
for num in range(160,172):
    print(f"Square of {num} is {num**2}.") # print(num*num)

print("***** Print cubes of numbers between 160 and 171? *****")
for num in range(160,172):
    print(f"Cube of {num} is {num**3}.") # print(num*num*num)

print(f"\n***** Print list of cubes of numbers between 160 and 171? Do not print individual numbers. *****")
cubes = []
for num in range(160, 171):
    cubes.append(num**3)
# List comprehension
cubes2 = [num**3 for num in range(160,171)]
print(f"\nCubes of the numbers:{cubes}")
print(f"\nCubes of the numbers:{cubes2}")

print(f"\n***** Print sum of numbers between 160 and 171? Do not print individual numbers. *****")
sum = 0
for num in range(160, 171):
    print(f"num is {num}")
    print(f"sum is {sum}")
    sum=sum+num # this keeps incrementing the value of sum
    print("******************************")
print(f"RESULT: {sum}")
