#find the max of 3 numbers with 3 parameters
def max_three(n1,n2,n3):
    return(n1 if (n1>n2) and (n1>n3) else n2 if (n2>n3) else n3)
print(max_three(5,62,311))
#print each vowels and consonents in the string
# def vow_cons(a):
#     li_v=[]
#     li_c=[]
#     for i in a:
#         if i.lower() in 'aeiou' and i.lower() not in li_v:
#             li_v.append(i) 
#         elif i.lower() not in 'aeiou' and i.lower() not in li_c:
#             li_c.append(i)
#     return("vowel",li_v,"consonent",li_c)             

# print(vow_cons(input("enter a string: ")))   

# def vow_cons(a):
#     li_v=[]
#     li_c=[]
#     for i in a:
#         if i.lower() in 'aeiou':
#             li_v.append(i) 
#         else:
#             li_c.append(i)
#     return(li_v,li_c)             

# x,y=(vow_cons(input("enter a string: "))) 
# print(x)
# print(y)  

# return(i)#Using a return inside of a loop will break it and exit the function even if the iteration is still not finished. 
# def vowel_cons(s): 
#     v=''
#     c=''
#     for i in s:
#         if i.lower() in 'aeiou':
#             v+=i
#         else:
#             c+=i
#     return("vowel",v,"consonent",c)     
# print(vowel_cons(input("enter a string: ")))   
#5*4*3*2*1
# def fact(n1):
#     fac=1
#     for i in range(n1,1,-1):#for i in range(1,n1):
#         fac*=i
#     return fac
# x=int(input("enter the number: "))
# print(fact(x))

# def fact(n1):
#     temp=n1
#     fac=1
#     while(temp>1):
#         fac*=temp
#         temp-=1
#     return(fac)
# x=int(input("enter the number: "))
# print(fact(x))



#prime or not
# def prime(x):
#     if x>1:
#         for i in range(2,x):
#             if x%i==0:
#                 print("not a prime number")
#                 break
#         else:
#             print("prime number")
#     else:
#         print("not a prime number")

# a=int(input("enter a number :"))
# prime(a)    
    

# def swap(a,b):
#     a,b=b,a
#     return(a,b)
# x=int(input('enter a number:'))
# y=int(input('enter a number:'))
# a,b=swap(x,y)
# print("after swapping")
# print(a)
# print(b)