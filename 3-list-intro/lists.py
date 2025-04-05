
# Data structure:
# - Create, Access the data (read), modify (update), delete (CRUD operations)
# 1. CREATE A LIST
students = []
teachers = list() # create list and converts to a list
engineers = ['adam', 'akmal', 'yuling', 'youssef']
numbers = [4, 55, 22, 1, -9, 0, 23]


# 2. ACCESS THE DATA (READ) IN A LIST
# what is index? index starts with D, index is not a count,
# last index is one less that total count
# index can also be negative number
print (f"Third element in the list: {engineers[2].title()}")
print (f"Third element in the list: {engineers[-2].title()}")
print(f"First element in the list: {engineers[0].title()}")
print(f"First element in the list: {engineers[-4].title()}")
print(f"Last element in the list: {engineers[3].title()}")
print(f"Last element in the list: {engineers[-1].title()}")


# IndexError: list index out of range
# print(f"last element in the list: {engineers[4].title()")
# other errors you might see and easily fix or avoid:
# NameError: name 'prit' is not defined. Did you mean 'print'?
# Syntax Error: f-string: expecting '}'
# Indentation Error: Unexpected Indent
print(f"sum of two numbers: {numbers[0] + numbers[-1]}")

# MODIFY THE LIST (UPDATE)
print("#3. MODIFY THE LIST (UPDATE)")
print(engineers)
engineers[0] = 'natalia'
print(engineers)

print("-- adding element to a list by appending...")
engineers.append("lasha") # adds to the end of the list
print(engineers)

print("-- adding element to a list by inserting...")
engineers.insert(2, "sabina")
print(engineers)

print("# 4. REMOVING ELEMENT FROM THE LIST.")
print("4.1 removing using del function, by index")
del engineers[1]
print(engineers)

print("4.2 removing using pop() function, last element or by index")
removed_engineer1=engineers.pop() # Remove and return item at index (default last).
print(engineers)
print("removing element on index 1, pop(1)")
removed_engineer2=engineers.pop(1)
print(engineers)
print(f"Removed engineers from the list: {removed_engineer1}, {removed_engineer2} ")

print("4.3 removing using remove function, by value")
print("add duplicate names to the list.")
engineers.append('yuling')
print(engineers)
engineers.remove("yuling") # removes first occurrence of value
print(engineers)

engineers.append('yuling')
print(engineers)
print('index of yuling:', engineers.index('yuling'))
engineers.insert(engineers.index('yuling')+1, "vazira")
print(engineers)

print('all indexes of yuling: ', engineers.index('yuling'))

# engineers.remove()

# HW 3-1, 3-2, 3-3
names = ['karen', 'joshua', 'angela', 'peter', 'andrew']