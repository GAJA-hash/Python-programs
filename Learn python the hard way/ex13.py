from sys import argv   #importing modules--> keeps programs small & documentation or other programmers
#read the WYSS section for how to run this
script,first,second, third, fourth = argv     #argument variable-->rather than holding all the arguments, it gets
                                            #assigned to four variables(script,first, second, third)"""

# “Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order.”
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


#study drill
print("Your previous name was", fourth)
fourth = input("What is your name?" )

print(f"Your current name is {fourth}")


"""Note: What’s the difference between argv and input()? The difference has
 to do with where the user is required to give input. If they give your
script inputs on the command line, then you use argv. If you want them to
input using the keyboard while the script is running, then use input()."""
