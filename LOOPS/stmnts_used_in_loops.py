""" statements used in loops
1. break
--->brings control out of loops
--->syntax
    break
2. continue
--->stop current iteration of the loop and continue with loop
--->syntax 
    continue
3. pass
--->for write empty loop  
--->not sure about what to execute inside the loop put pass for executing code without error  

"""

#example of break

# fruits =["orange","mango","kiwi","apple","banana"]
# for i in fruits:
#     print(i)  # till apple will be printing since print statement is before break
#     if (i=="apple"):
#         break


# fruits =["orange","mango","kiwi","apple","banana"]
# for i in fruits:
#     if (i=="apple"):
#         break
#     print(i) # apple won't print since print statement is after break

# example of continue

# fruits =["orange","mango","kiwi","apple","banana"]
# for x in fruits:
#     if (x=="kiwi"):
#         continue
#     print(x)

# example of pass

n=10
for i in range(n):
    pass
        

