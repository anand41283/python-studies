# Assign a different name to function and call it through the new name
#Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
# Assign a different name to function using the assignment (=) operator.
#fun_name = new_name

def display_student(name, age):
    print(name, age)

show_student=display_student
show_student("Emma", 26)

