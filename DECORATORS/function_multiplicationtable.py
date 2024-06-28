#  Write a function that inputs a number and prints the multiplication table of that number

def multiplication(x):
    for i in range(1,11):
        print(f"{i} * {x} = {i*x}")

a=int(input("enetr a number:"))
multiplication(a)