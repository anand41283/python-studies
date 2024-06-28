"""
FILE HANDLING
-------------
In python ,files are treated in two modes.As text or binary.The file may be in the text or binary format,and each line of a file
is ended with the special character.
Hence,a file operation can be  done in the following order.

--> open a file
--> Read or write - performing operation
--> close the file

opening a file
--------------
python provides an open() function that accepts two arguments,file name and access mode in which the file is accessed.The function returns a file
object which can be used to perform various operations like reading,writing etc

syntax:
file_object=open(<file_name>,<access mode>)

Access mode
-----------
"r" - Read - Default value.Opens a file for reading,error if the file does not exist
"a" - Append - Opens a file for appending,creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file,returns an error if the file exists
"t" - Text - Default value.Text mode
"b" - Binary - Binary modde (eg. images)"""

#opens the file file.txt




"""
WRITING A CONTENT TO THE FILE
-----------------------------
To write some text to a file,wee need to open the file using the open method with one of the following access modes.
w: It will overwrite the file if any file exists.The file pointer is at the beginning of the file.
a: It will append the existing file.The file pointer is at the end """