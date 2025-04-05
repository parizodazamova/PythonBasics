# 7-5

while True:
    age = input("Enter your age to see the ticket price: ")
    if age.lower() == 'quit':
        print(f"Breaking the loop and exiting ...")
        break
    elif not age.isdigit():
        print(f"Only numbers accepted. Try Again!")
        continue

    age = int(age)
    #age = int(input("Enter your age to see the ticket price: "))
    # if age == 0:
    #     print(f"Breaking the loop and exiting ...")
    #     break

    if 0 < age <= 3:
        print(f"Ticket is Free for you!")
    elif 3 < age <= 12:
        print(f"Ticket price is $10.")
    elif age > 12:
        print(f"Ticket price is $15")
    else:
        print(f"Please enter valid age.")

print(f"Completed the execution of {__file__}.")

# issue 1: TypeError: '<' not supported between instances of 'int' and 'str' : FIXED
# issue 2: ValueError: invalid literal for int() with base 10: 'a'
# issue 3: ValueError: invalid literal for int() with base 10: '12.5'