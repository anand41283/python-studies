# Write a program to create a function show_employee() using the following conditions.

# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary


def showEmployee(name,salary=9000):
    print("Name:",name)
    print("Salary:",salary)

showEmployee("Ben", 12000)
showEmployee("Jessa")