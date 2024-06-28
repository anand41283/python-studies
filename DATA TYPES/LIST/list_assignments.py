# create a new list and add the fruits
fruits=[]
limit=int(input("enter no of elements in the list:"))
for i in range(0,limit):
    fruits.append(input("enter the name of fruit:"))
print(fruits)    


#print the first and last element

print(f"first element is{fruits[0]}")
print(f"last element is {fruits[-1]}")


#change the value of apple to kiwi
fruits=['apple','orange','mango']
fruits[0]='kiwi'
print(fruits)

#remove the last element
l1=['apple','kiwi','orange','potato']
#l1.pop(-1)
l1.pop()

print(l1)

#add a new element
fruits.append('potato')
fruits.insert(1,'jack fruit')
print(fruits)

#add a new element to index 4

fruits.insert(4,'lichi')
print(fruits)

#pop out the element (index=3)
fruits.pop(3)
print(fruits)

#find max value
print(max(fruits))

#find the min value
print(min(fruits))

#print the list in reverse order
fruits.reverse()
print(fruits)

# sort the list in descending order
l2=[32,45,10,89,1,3,21,13,100]
l2.sort(reverse=True)
print(l2)

#print the cubes of numbers in list using L.C
l1=[2,4,5,6,3,8,9]
print([x**3 for x in l1 ])

#L.C for square of even numbers
print([i**2 for i in range(0,10) if i%2==0])



