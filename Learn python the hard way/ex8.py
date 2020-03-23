formatter = "{} {} {} {}"
#Instead of directly printing the values, We are calling arguments
# 4 values(1,2,3,4) are assigned to the 4 braces correspondingly
print(formatter.format("1", 2, 3, 4)) #Can/Can't use " "
#Here four strings are printed but same as above
print(formatter.format("one", "two", "threee", "four"))
#Here True or False condition is printed
print(formatter.format(True, "False", False, True)) #Can/Can't use " "

print( formatter.format(formatter, formatter, formatter, formatter, ))

print(formatter.format(
"Here I can write whatever I think,",
"it will be printed in a single line.",
"First reason is, it is being called by {} and .format functions.",
"i.e. Whatever inside the quotes willbe printed in the respective order"
))
