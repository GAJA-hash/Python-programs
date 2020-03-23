#To call a variable we can use the below shown examples.
#f"some stuff here {avariable}"
#f"some other stuff {anothervar}"

types_of_people = 10
x = f"There are {types_of_people} types of people." #string 1

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." #string 2

print (x)
print (y)

print(f"I said: {x}")  #string 3
print(f"I also said: '{y}'")  #string 4

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"   #string 5
#The {}in the above coding uses to call the variable
#which is assigned in below coding within .format()
print(joke_evaluation.format (hilarious))

#Repeated the above 3(5) lines using another coding
print("\n\n\n")
print("another method")
hilarious = "False"
joke_evaluation = "Isn't that joke so funny?! "

print(joke_evaluation + hilarious)



w = "This is the left side of....."
e = "a string with a right side."

print (w + e)

#study drill
print("\n\n\n")
print("study drill \n\n")
testing = True
a = "{}"                #not working --->1 = "{}"
print(a.format(testing))#not working------>print(1.format(testing)

print('\n\n or \n\n')

#Assigning values in the respective order

print('\n\n e.g. \n\n')
print("We {} this way {}." .format('can do', 'too'))

#more values called using { } and .format
print("\n\nTo print True, True, False")
print("{} {} {} " .format(True, True, "False"))#Since True/False is a keyword we can either or not use ""
