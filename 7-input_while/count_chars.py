#1. given a phrase "Happy women's day", count how many times each letter was used.  Use dictionary, for loop,
# if condition, setdefault()
# phrase = "Happy women's day"
phrase = input("Enter a phrase: ")

letter_count = {}
for char in phrase.lower():
    # Convert to lowercase so 'H' and 'h' are treated the same
    # option1

    # if char in letter_count.keys():
    #     # increment existing value
    #     letter_count[char] += 1
    # else:
    #     # add key to dictionary with value 1
    #     letter_count[char] = 1

    # option2:
    # if char.isalpha(): # count only letters
    if char.isdigit():
        # If letter is not in dictionary, set it to 0
        letter_count.setdefault(char, 0)
        # Increase the count of that letter
        letter_count[char] += 1

print(letter_count)
print("************** GAME STARTS !!!! *****************")
total = 0
green_count = 0
alien_color = ""
while alien_color.lower() != 'quit' and alien_color.lower() != 'q':
    alien_color = input("Enter the color to earn points: ")

    if alien_color.upper() == 'GREEN':
        green_count += 1
        if green_count <= 1:
            total += 5  # increment -> total = total + 5
        else:
            total += 2  # only 2 points rewarded with after first green

        print(f"You have just earned 5 points!\nTotal points: {total}")

    elif alien_color.lower() == 'red':
        if total >= 1:
            total -= 1
            print(f"1 point was deducted.\nTotal points: {total}")
        else:
            print(f"Total points: {total}")
    else:
        print(f"No points earned. Try Again!\nTotal points: {total}")
        
phrase = ""
while phrase != 'q':
    phrase = input("Enter a phrase: ")

    letter_count = {}
    for char in phrase.lower():
        # Convert to lowercase so 'H' and 'h' are treated the same
        # option1

        # if char in letter_count.keys():
        #     # increment existing value
        #     letter_count[char] += 1
        # else:
        #     # add key to dictionary with value 1
        #     letter_count[char] = 1

        # option2:
        # if char.isalpha(): # count only letters
        if char.isdigit():
            # If letter is not in dictionary, set it to 0
            letter_count.setdefault(char, 0)
            # Increase the count of that letter
            letter_count[char] += 1

    print(letter_count)