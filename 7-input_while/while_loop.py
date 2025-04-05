# while condition:
#while true:
#   print('something')

#while 2>1:
#   print('something else')
# increment a variable
num = 0
while num <5:
    print(f"current value of NUM : {num}")
    num = num + 1
print("------------------------------------")
num = 10
while num <5:
    print(f"current value of NUM : {num}")
    num = num + 1
print("********** GAME STARTS !!!! **********")
green_count = 0
for i in range(5):
    alien_color = input("Enter the color to earn points:")

    if alien_color.upper() == 'GREEN':
        green_count += 1
        if green_count <= 1:
            total += 5 #incremenr -> total = total + 5
        else:
            total += 2 # only 2 points rewarded 