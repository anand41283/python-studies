"""
COPY A DICTIONARY
-----------------
1.using copy()

"""
student={"name":"Anitha",
         "age":45,
         "course":"MA English"
         }
print(student)
std=student.copy()
print(std)

#2.Using dict()
std1=dict(student)
print(std1)


#Nested dictionary
#-----------------

#A dictionary contain dictionaries,this is called nested dictionaries
#dict_var={dicta:{key1:value1},dictb:{key2:vallue2}}

people={1:{"name":"john","age":24},2:{"name":"anu","age":29}}
print(people)

#access the elements

print(people[1]["name"]) #o/p john
print(people[2]["age"]) #o/p 29