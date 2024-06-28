# Functions used in python


"""
1.append()
2.insert()
3.extend()
4.remove()
5.del
6.index()
7.pop()
8.clear()
9.max()
10.min()
11.reverse
12.sort
13.count

"""
#append() ----> adding new item to the list (values added in the last)
#syntax ----> list_name.append(new_element)

# l1=[1,2,3,4,5]
# print(l1)
# l1.append(6)
# print(l1)

#insert() ----> adding a element to the list at specified index
#syntax ----> list_name.insert(index,new_element)

# l1=[9,25,11,41,53]
# l1.insert(2,8)
# print(l1)

#extend() ----> append elements from another list to current list (adding two lists)
#syntax ----> current_list.extend(another_list)

# l2=['kiwi','apple','orange']
# l3=[1,2,3,4]
# print(l2)
# print(l3)
# l2.extend(l3)
# print(l2)

#remove() ----> remove specified item/element from the list
#syntax ----> list_name.remove(item)

# l2=['kiwi','apple','orange']
# l2.remove('orange')
# print(l2)

#pop() ----> remove the specified index value
     # ----> if do not specified index value removes last item
#syntax ----> list_name.pop(index)

# l1=[9,25,11,41,53]
# print(l1)
# l1.pop(3)
# print(l1)
# l1.pop()
# print(l1)

#del ----> remove the specified index value
    #----> if do not specified index value delete the list
#syntax ----> del.list_name[index]

# fruits=['apple','kiwi','mango','orange','pineapple'] 
# del fruits[2]
# print(fruits)
# del fruits
# print(fruits)#will throw name error--->previous line of code delets list fruits   

#clear() ----> empties the list (list still remains but not the content )
#syntax ----> list_name.clear()

# l1=['bus','blue','car',52,23.1,8]
# l1.clear()
# print(l1)

#index() ----> find the index value
#syntax ----> list_name.index(item)

# l1=['bus','blue','car',52,23.1,'car']
# print(l1)
# print(l1.index('car')) # if duplicates are available in the list  will return the index of  first availabe element
# print(l1.index(23.1))

#max() ----> return max element in the list
#syntax ----> max(list_name)

# l1=['bus','blue','car','car']
# l2=[1,11,21,31,41,82,15]
# print(max(l2))
# print(max(l1))

#min() ----> return min element in the list
#syntax ----> min(list_name)

# l1=['bus','blue','car','car']
# l2=[1,11,21,31,41,82,15]
# print(min(l1))
# print(min(l2))

#reverse() ----> reverse the list
#syntax ----> list_name.reverse()

# l1=['bus','blue','car','car']
# l1.reverse()
# print(l1)

#sort() ----> sort the elements in the list
       #----> by default ascending order
       #---->parameter reverse---> reverse=True will sort decsending order

# l1=[1,2,3,4,23,17,56]
# # l1.sort()       
# # print(l1)
# l1.sort(reverse=True)
# print(l1)

#count() ----> count the specified object
# # syntax ----> list_name.count(item)

# l1=['bus','blue','car','car']
# print(l1.count('car'))
# print(l1.count('blue'))





