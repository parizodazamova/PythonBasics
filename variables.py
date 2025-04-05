# comment line, not executable line
# Variables:

a = 20 # variable name is 'a', assigned 20 to a variable 'a', hence 20 is value of variable
b = 50

print("sum of variable and b is: ", a+b)
print("division :", a/b)
print("multiplication:", a*b)
print("subtraction:", a-b)

# NameError: name 'prnt' is not defined. Did you mean: 'print'?
# SyntaxError: '(' was never closed
# Indentation: IndentationError: unexpected indent - Using space in the beginning of the line.

#Naming convention of variable:
# meaningful and precise, must start with letters, must not start with numbers,
# if var.name consist of multiple words then use '_' (underscore), never use Space in the name
# preferable names will be all in lowercase
num1 = 45
num_2 = 56
user_name = 'johndoe'

#2/20/2025
num1 = 45
num_2 = 56
user_name = 'johndoe'
b=True #not 'b' was assigned booleon value
price = 45.66
print("*********************** String data types *************")
message = "Variables CAN hOLD much larger tEXT not just one number."
print(message)
print(message.upper())
print(message.lower())
print(message.title())

# f string - used without space
user_password = 'strong123'
msg = f"sum of the 'a' and 'b' variable is: {num1 + num_2 }"
# python sums the number, then converts the result to a text then
# concatenates with the rest of the text
# what ever in the curly braces executed as python code

print("sum of the 'num1' and 'num_2' variable is:".title())
print(msg.title())
print(msg.title())

# non-printable charachters \n (newline) , \t (tabs - 4 spaces)
print(f"My username is '{user_name}' \n\n\tand password is '{user_password}'. ")

print("--------------- Exercise -------------")
print(f"\t    *   \n\t   *** \n\t  ***** \n\t ******* \n\t   |||\n Happy New Year!!")

# name = 'mark'
name = input("Enter the name to greet:")
greeting = f"Hello {name.title()}, would you like to learn some Python today?"
print(greeting)

#H/W: 2-4, 2-5, 2-6, 2-7