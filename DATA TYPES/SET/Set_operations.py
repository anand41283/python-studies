"""
JOIN TWO SETS
-------------
1.Union()
  It returns a new set containing all items from both sets
2.Update()
  Insert all items from one set to another
3.Intersection()
  Return a new set that only contains the item that are present in both sets
4.Intersection_update()
  Keep only the items that are present in both sets
5.Symmetric_difference_update()
  Keep only the items that are not present in both sets
6.Symmetric_difference()
  Return a new set that only contains the item that are not present in both sets.
  
"""

set1={1,2,3,4}
set2={1,2,5,6,7}
#union example
set3=set1.union(set2)
print(set3)

#update example
set1.update(set2)
print(set1)

#union and update will exclude any duplicates
s1={'a','b','c'}
s2={'b','c','d'}

#intersection

s3=s1.intersection(s2)
print(s3)

#intersecton_update
s1.intersection_update(s2)
print(s1)

s1={'a','b','c'}
s2={'b','c','d'}
#symmetric_difference_update
s1.symmetric_difference_update(s2)
print(s1)

#symmetric_difference
s3=s1.symmetric_difference(s2)
print(s3)

