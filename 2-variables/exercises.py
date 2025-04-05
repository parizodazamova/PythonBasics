# 2-5
print('Albert Einstein once said, "A person who never made a')
print('mistake never tried anything new."')

# 2-6
famous_person = "Albert Einstein"
message = "'A person who never made a mistake never tried anything new.'"
print("{0} once said, {1}". format(famous_person, message))
message = "A person who never made a mistake never tried anything new."
print(f"\n\n {message} \n\t-{famous_person}")

# 2-7
name = " \tJames Bond\n "
print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())
print(name.rstrip())
print(name.strip())
