from sys import argv

script, filename = argv #Assigns 'script, filename' to what script and filename we give in the respective order.

txt = open(filename) # Assigns a variable named 'txt' to the contents of the given file.
print(f"Your script name is {script}:")
print(f"Here's your file {filename}:")
print(txt.read()) #reads(prints) the contents of the given file.
txt.close() #Closing the file.

print("Type the filename again:")
file_again = input('>')   # Gets a new file from user and assign a new name called "file_again"

txt_again = open(file_again)# Assigns a variable named 'txt_again' to the contents of the given file (file_again)

print(txt_again.read())  #reads(prints) the contents of the given file(file_again).
txt_again.close() #Closing the file

#Study drill
"""Simply saying first we need to "open" the file and "read" the file"""
moviename = input("Enter the movie you like:")
type = open(moviename) #Opening the file and assigning a variable name
print(type.read())#Reading the file
type.close()#Closing the file
