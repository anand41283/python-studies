# Reduce
from functools import reduce
# product = 1
# list1 = [1, 5, 4, 6]
# for num in list1:
#     product *= num

# print(product)

# using reduce
# list1 = [1, 5, 4, 6]
# product = reduce((lambda x, y: x*y), list1)
# print(product)


# to find the sum of numbers 1-10


sum=reduce(lambda x,y:x+y,(i for i in range(1,11)))
print(sum)