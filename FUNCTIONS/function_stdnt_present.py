#define a function that accept roll number and returns whether the student is present or not
#[20,45,78,65,2,3,4,5]#present values
# def roll(num):
#     p=[20,45,78,65,2,3,4,5]
#     return("present" if num in p else "not present")
# x=int(input("enter roll number: "))
# print(roll(x))

#swap two numbers using function
#define a function that accept uppercase string and return lower case string

# def lower_case(s):
#     for i in s:
#         if i.isupper()==False:
#             print("enter your string in uppercase")
#             break
#     else:    
#         print(s.lower())#return(s.lower())
# x=input("enter your string in uppercase: ")
# lower_case(x)
#print(lower_case(x))
#define a function that accepts radius and find area of circle

# def area_circle(r):
#     return(3.14*r**2)
# radius=eval(input("enter radius: "))
# print(area_circle(radius))

# check given number is palindrome or not
# def palindrome(num):
#     temp=num
#     rev=0
#     while(num!=0):
#         dig=num%10
#         rev=rev*10+dig
#         num//=10
#     return("palindrome" if temp==rev else "not palindrome")
# x=int(input("enter the number: "))
# print(palindrome(x))


def palindrome(a):
    rev=0
    temp=a
    while(temp!=0):
        dig=temp%10
        rev=rev*10+dig
        temp//=10
    return 'is palindrome' if rev==a else 'not palindrome'
x=int(input("enter the number: "))   
print(palindrome(x))