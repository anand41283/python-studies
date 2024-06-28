"""
Methods used in sets
--------------------
1.add()
2.clear()
3.copy()
   returns the copy of the set
   syntax: new_set=set_var.copy()
4.max()
  returns the max value of the set
  syntax: max(set_var)
5.min()
  returns the min value of the set
  syntax: min(set_var)
6.difference()
  returns a set containing the difference b/w two more sets
  syntax: new_set = set_var1.difference (set_var_2)
7.difference_update()
  removes the items in this set that are included in another specified set
  syntax: set_var1.difference_update(set_var2)
8.discard()
9.intersection()
10.intersection_update()
11.isdisjoint()
   returns whether another set contains this set
   syntax: new_set = set_var1.isdisjoint(set_var2)
12.issubset()
   returns whether another set contains this set or not
   syntax: new_set = set_var1.issubset(set_var2)
13.issuperset()
   returns whether this set contains another set
   syntax: new_set = set_var1.issuperset(set_var2)
14.pop()
15.remove()
16.symmetric_difference
17.symmetric_difference_update()
18.union()
19.update()


"""

# example of copy
# s1={1,2,33,21}
# s2=s1.copy()
# print(s2)

# example of difference
# s={'anu','manu','vinu','arun'}
# d={'anu','sunu','vinu',}
# a=s.difference(d)
# print(a)

# example of difference_update()
# s={'anu','manu','vinu','arun'}
# d={'anu','sunu','vinu',}
# s.difference_update(d)
# print(s)

#