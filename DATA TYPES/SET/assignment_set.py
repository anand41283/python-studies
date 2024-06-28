names={"ann","kevin","paru"}
# write a program to remove "ammu"
#names.remove("ammu")
#print(names)
#remove "appu" from the set names without error
names.discard("appu")
print(names)
#add 'kichu' to the set names
names.add("kichu")
print(names)
#add ["kevin","jeo","mithu"] to the set names
adds=["kevin","jeo","mithu"]
names.update(adds)
print(names)
#find the length of the set names
print(len(names))
#clear out the elements
names.clear()
print(names)
#find the length of the set names
print(len(names))
#delete the complete set
del names
