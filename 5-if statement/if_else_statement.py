# Unit Testing:
# age = 10 -> pass
# age = 17 # -> pass
# age = 'abc' -> fail TypeError
# age = None -> fail TypeError
# age = -10 # -> fail -> fixed -> pass
# age = 0 # -> pass
age = 76 # -> pass

if 0 <= age < 17:
    print("You are NOT eligible to apply for Driver's permit.")
    print(f"You can apply after {17-age} years.")
    # disable the continue button

elif 17<= age <=75:
    print("You are eligible to apply for Driver's permit.")
    #enable to continue button
elif age > 75:
    print("Ohh. Drive Carefully or just get an uber/lift.")
    print("Make sure you renew the DL and drive carefully.")
else:
    print("Please check the age entry, it is not valid.")
    # disable the continue button
print("----------------------------------------------------")

