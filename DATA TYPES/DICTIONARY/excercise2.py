#1.python program to create an empty dictionary
# d={}
# print(type(d))

#2.python prgrm to create a dictionary using dict() function
# di=dict({"name":"unni","age":24,"location":"Kunnamkulam"})
# print(di)
# print(type(di))

#3.python prgrm to create a dictionary with integer keys and print keys values and key value pair

# di={1:'anu',2:'vinu',3:'manu'}
# print(di.keys())
# print(di.values())
# print(di.items())

#4.python program to create a dictionary of 10 numbers and their squares
# seq=(1,2,3,4,5,6,7,8,9,10)
# di=dict.fromkeys(seq)
# for i in di:
#     di[i]=i**2
# print(di)
#method2
# di={}
# for i in range(1,11):
#     di[i]=i**2
# print(di)    


#5.python prgrm to create a dictionary and accessing each element using get() method
# seq=(1,2,3,4,5,6,7,8,9,10)
# di=dict.fromkeys(seq)
# for i in di:
#     di[i]=i**2
#     print(di.get(i))

#6.python prgrm to create a nested dictionary and accessing each element
# dict={1:{"name":"anjitha","age":24,"location":"kakkanad"},2:{"name":"appu","age":27,"location":"kasaragod"}}
# print(dict[1]["location"])
# print(dict[1]["name"])
# print(dict[1]["age"])
# print(dict[2]['name'])
# print(dict[2]['age'])
# print(dict[2]['location'])

#7.python prgrm to create a dictionary and add 5 items to the dictionary

# diction={"name:":"aabhi"}
# diction.update({"age":14,"location":"malappuram","course":"HSS","School":"GHSS MALAPPURAM","guardian":"muhammad"})
# print(diction)

#8.python program to create a dictionary with 7 items and remove 2 items using pop() and del
# diction={"name:":"aabhi"}
# diction.update({"age":14,"location":"malappuram","course":"HSS","School":"GHSS MALAPPURAM","guardian":"muhammad","score":98})
# diction.pop("guardian")
# del diction["course"]
# print(diction)

#9.python progrm to create a dictionary fruits with 3 items and change the fruit name apple to grapes
# fruits={1:"apple",2:"orange",3:"kiwi"}
# fruits[1]="grapes"
# print(fruits)

#10.python prgrm to create a dictionary with 10 items and copy the dict to another dict using dict() and find the length of new dict
# di={}
# for i in range(1,11):
#     di[i]=i**2
# new_dict=dict(di)
# print(new_dict)
# print(len(new_dict))

#11.python program to create a dictionary and print each keys in dictionary
# di=dict({"name":"unni","age":24,"location":"Kunnamkulam"})
# for i in di:
#     print(i)

#12.pyhon program to create a dictionary with integer value and key and print the sum of key value pair
# s={1:11,2:45,3:41,4:62} #o/p [13,47,44,66]
# sum=[]
# for i in s:
#     sum.append(i+s[i])
# print(sum)  

#13.write a prgrm to swap the position of dictionary item 
# mydict={1:"python",2:"php",3:"net",4:"c++"} #o/p mydict={1:"python",4:"c++",3:"net",2:"php"}
# list1=list(mydict.items())
# list1[1],list1[3]=list1[3],list1[1]
# mydict=dict(list1)
# print(mydict)

 