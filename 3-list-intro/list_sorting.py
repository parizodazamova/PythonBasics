# ordering the list
cars = ['tesla model x', 'byd', 'bmw i7', 'rivian r1t', 'lucid air']
# temporary : ascending, descending - creates the copy of the list
# permanently : ascending, descending - orders the original list
# reversing the list - reverses the original list

cars = ['tesla model x', 'byd', 'bmw i7', 'rivian r1t', 'lucid air']
print("# temporary: ascending, descending - creates the copy of the list")
print(f"Cars before sorting with sorted(): {cars}")

print("\n===============================================")
cars_sorted_asc = sorted(cars)
print(cars_sorted_asc) # SORTING TEMP IN ASCENDING
print(f"Cars after sorting with sorted(): {cars}")

print("\n===============================================")
cars_sorted_desc = sorted(cars, reverse=True)
print(cars_sorted_desc) # SORTING TEMP IN DESCENDING
print(f"Cars after sorting with sorted(): {cars}")

print("\n===============================================")
print("# permanently: ascending, descending - orders the originals list")
print(f"\nCars before sorting with sort():\n{cars}")
cars.sort()
print(f"\nCars after sorting with sort() ascending: \n{cars}")

print("\n===============================================")
print("# descending the order of cars")
cars.sort(reverse=True)
print(cars)

print("\n===============================================")
print("#Reversing the list - reverses the original list")
cars = ['tesla model x', 'byd', 'bmw i7', 'rivian r1t', 'lucid air']
print(cars)
print("\nReversing the list...")
cars.reverse()
print(cars)

print("\n===============================================")
# using default for sep, end, file, flush parameters
print("\n"'a', cars[2], cars[0])
# using default values for file, flush parameters
print("\n"'a', cars[2], cars[0], sep="|", end="\t\t\n")

print("\n==============================================")
print("#length of the list")
print(f"Length of the list with len():{len(cars)}")
print(f"Length of the phrase with len('Hello'):{len('Hello')}")

print("\nCompleted!!")

#takeaway!!!...................................
#temp sort: sorted(list), sorted(list, reverse=True)
#perm sort: list.sort(), list.sort(reverse=True)
#reverse the list: list.reverse()