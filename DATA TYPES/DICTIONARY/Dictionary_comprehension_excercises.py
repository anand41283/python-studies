# 1.Create a dictionary from the list with same key:value pairs, such as: {"key": "key"}.

# lst=["NY", "FL", "CA", "VT"]
# x={y:y for y in lst}
# print(x)


# 2.First, create a range from 100 to 160 with steps of 10.
#Second, using dict comprehension, create a dictionary where each number in the range is the key and each item divided by 100 is the value.

# d={key:key/100 for key in range(100,161,10)}
# print(d)

# 3.Using dict comprehension and a conditional argument create a dictionary from the current dictionary where only the key:value pairs with value above 2000 are taken to the new dictionary.

# dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
# dict2={x:dict1[x] for x in dict1 if dict1[x]>2000}
# print(dict2)


#4.
# normal
# square_dict = dict()
# for num in range(1, 11):
#     square_dict[num] = num*num
# print(square_dict)


# dictionary comprehension

# square_dict={num:num*num for num in range(1,11)}
# print(square_dict)


#5.

#item price in dollars
# old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

# dollar_to_pound = 0.76
# new_price={key:old_price[key]*dollar_to_pound for key in old_price}
# # new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
# print(new_price)
#6. only items with even value should be added to the new dictionary
# original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

# new_dict={k:original_dict[k] for k in original_dict if original_dict[k]%2==0}

# print(new_dict)

# even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
# print(even_dict)

# 7.only the items with an odd value of less than 40 should be added to the new dictionary
# original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
# new_dict={k:v for (k,v) in original_dict.items() if (v%2!=0 and v<40)}
# print(new_dict)

#The items with a value of 40 or more have the value of 'old' while others have the value of 'young'.
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
# new_dict={k:("old" if v>=40 else "young")for (k,v) in original_dict.items()}
new_dict={k:("old" if original_dict[k]>=40 else "young")for k in original_dict}
print(new_dict)


# 8.a multiplication table in a nested dictionary, for numbers from 2 to 4.


# normal
dictionary = dict()
for k1 in range(11, 16):
    dictionary[k1] = dict()
    for k2 in range(1, 6):
        dictionary[k1][k2] = k1*k2
print(dictionary)