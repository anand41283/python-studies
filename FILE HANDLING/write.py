#write the content to a text file---> will create a new txt file data.txt and write content to that
f=open("C:\\Users\\anjit\\OneDrive\\Desktop\\Python\\File_handling\\data.txt",'w')
f.write("My name is anjitha\nIam 24 years old\nIam from kasaragod")
f.close()

#write the content to an existing file----> will erase all the content in the existing file and write the given content to the file
f=open("C:\\Users\\anjit\\OneDrive\\Desktop\\Python\\File_handling\\data.txt",'w')
f.write("I have a dog\nHer name is Jennie\nShe is so cute.")
f.close()

#writelines()
f=open("C:\\Users\\anjit\\OneDrive\\Desktop\\Python\\File_handling\\data.txt",'w')
f.writelines(['My name is anjitha\nIam 24 years old\nIam from kasaragod'])
f.close()