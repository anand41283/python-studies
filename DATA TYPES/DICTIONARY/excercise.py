"""
1.create a empty dictionary
2.create a dictionary course with key:course_name,pass_out,college
3.change the value of pass_out year 2018 to 2019
4.add a new item loaction to the dict course using update()
5.print each keys in the dict course
6.print each values in the dict course
7.print each item in the dict course
8.remove the item college
9.find the length of the dictionary
10.clear out the dictionary
11.delete the dictionary completely """

# #1.
# empty={}
# #2.
# course={"course_name":"MSc CS","pass_out":2018,"college":"CUSAT"}
# print(course)
# #3.
# course["pass_out"]=2019
# print(course)
# #4.
# course.update({"location":"kochi"})
# print(course)
# #5.
# print(course.keys())
# #6.
# print(course.values())
# #7.
# print(course.items())
# #8.
# del course['college']#course.pop('college')
# print(course)
# #9.
# print(len(course))
# #10.
# course.clear()
# print(course)
# #11.
# del course
# print(course)

# course={"name":['anu','vinu','manu','sunu'],"age":[23,24,22,21],"company":['abc','sas','mod']}
# print(course)
# print(course.values())
#print(course['company'])
