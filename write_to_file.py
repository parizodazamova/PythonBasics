from utilities import *


flavors_rel_path = "./data/flavors.txt"

def write_txt_file(file_path, lines):
    with open(file_path, 'a') as file_obj
        for line in lines:
            file_obj.write(line)
        return file_obj

# option 2: with loop
new_flavors = ["banana", "\npineapple", "\noreo"]

write_txt_file(flavors_rel_path, new_flavors)

students_rel_path = "./data/students.txt"
new_students = "Busra", "\nRustam", "\nNatalia"
write_txt_file(students_rel_path, new_students)