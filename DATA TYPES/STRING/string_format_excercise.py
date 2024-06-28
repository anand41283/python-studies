"""
1."I want 3 pieces of item 567 for 45 dollars" using f string and format()
quantity=3
item=567
price=45

2."hello,Heric you are 45"
name='Heric'
age=45

3."There are total of 36 apples"
bags=36
fruits="apples"

4."Sachin is a batsman"
name="sachin"
dept="batsman"

"""
quantity=3
item=567
price=45
print(f'I want {quantity} pieces of item {item} for {price} dollars')
st="I want {1} pieces of item {0} for {2} dollars"
print(st.format(item,quantity,price))

# name='Heric'
# age=45
# print(f"hello,{name} you are {age}")
# txt="hello,{1} you are {0}"
# print(txt.format(age,name))

# bags=36
# fruits="apples"
# print(f'There are total of {bags} {fruits}')
# s="There are total of {} {}"
# print(s.format(bags,fruits))



# name="Sachin"
# dept="batsman"
# print(f'{name} is a {dept}')
# txt1='{} is a {}'
# print(txt1.format(name,dept))