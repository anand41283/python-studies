#Append---> will write the content without removing the existing content of the file.If file does not exist then will create a new file
f=open("C:\\Users\\anjit\\OneDrive\\Desktop\\Python\\File_handling\\data.txt",'a')
f.write("\nI have a dog\nHer name is Jennie\nShe is so cute.")
f.close()