numbers=[4, 55, 22, 1, -9, 0, 23]

# how do you find biggest and smallest number in the list?
# numbers list
# lets sort in ascending,
# first number is smallest (min), last number is the biggest (max)
# code - implementation
print("\nSorting the list in ascending order...")
numbers.sort()
print(f"min number:{numbers[0]}, max number:{numbers[-1]}")

# HW.3-8, 3-9, 3-10
# 3-8
locations = ['hawaii', 'canada', 'japan', 'mexico', 'australia']
print(f"Locations before sorting with sorted():{locations}")
locations_sorted_asc = sorted(locations)
print(locations_sorted_asc)
print(f"Locations after sorting with sorted():{locations}")


