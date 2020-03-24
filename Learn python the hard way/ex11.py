print("How old are you?", end = '')
#Already we have seen assigning variables to keywords. Here we are assigning input variables.
age = input()
print("How tall are you?", end ='')
height = input()
print("How much do you weigh?", end ='')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#Study Drills
print("What is your name?", end = '')
name = input()
print(f"My name is {name}")

#Other way to get input and print.
name = input("What is your name? ")
print("My name is "  + name )


#Another program
print("""
Accept input from keyboard
""")
First_Name = input("Enter your first name:")
Last_Name = input("Enter your last name:")
City  = input("Enter your city of resident:")
State = input("Enter your state of resident:")

print("Your name is "+ First_Name + "," +Last_Name)
print("You live in " +City+ "," +State)


#Let's do some math
print("""\n\nLet's do some math""")
number1 = input("Enter the first number:")
number2 = input("Enter the second number:")
addition = number1 + number2
print ("The addition of two numbers is",addition)

#The above coding doesn't work, so try the code as like below
print("""\n\nLet's do some math""")
number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
addition = number1 + number2
#(the below line not working bcoz it must be 'string' not 'integer')
#print ("The addition of two numbers" +number1+ "and" +number2+ "is" +addition)
print (f"The addition of two numbers {number1} and {number2} is {addition}")
