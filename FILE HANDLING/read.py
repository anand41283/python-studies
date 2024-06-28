#Read the content of the file
#open(<file_name>,<access mode>)
f=open("C:\\Users\\anjit\\OneDrive\\Desktop\\Python\\File_handling\\read.txt","r")
# a=f.read(5)
# b=f.read(4) #we can give parameter inside read method...that much characters will be read.After that start reading from that particular position
# print(a)
# print(b)
c=f.readline()#used to read single line in the txt file.
print(c)
f.close()