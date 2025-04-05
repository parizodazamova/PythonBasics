# 5-3

# alien_color = 'green'
# alien_color = 'red'
# alien_color = 5
# alien_color = 'Green' # FAIL -> fix -> pass

total = 0
green_count = 0
for i in range(3):
    alien_color = input("Enter the color to earn points: ")

    if alien_color.upper() == 'GREEN':
        print(f"You have just earned 5 points!\nTotal points: {total} ")
        green_count += 1
        if green_count <= 1:
            total += 5  # increment total = total + 5

    elif alien_color.lower() == 'red':
        total -= 1
        print(f"1 point was deducted.\nTotal points: {total}")
    else:
        print(f"No points earned. Try Again!\nTotal points: {total}")

print("---------------------------------------------")

# '''
#
# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
#
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#
# • Write an if statement to test whether the alien’s color is green. If it is, print
#
# a message that the player just earned 5 points.
#
# • Write one version of this program that passes the if test and another that
#
# fails. (The version that fails will have no output.)
#
# '''

# alien_color = 'green'

# alien_color = 'red'

# alien_color = 5

# alien_color = 'Green' # FAIL -> fix -> pass



