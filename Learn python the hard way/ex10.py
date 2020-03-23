tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split \n on a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
a=tabby_cat
print("{}".format(a)) #not working-->print("{}.format(a)") & print({}.format(a))
print(persian_cat)
print(backslash_cat)
print(fat_cat)



print("\a \b \v \f AT==BOY\b")
print("\r Small boy")
print("feae")
print("\uafed") #Character with 16-bit hex value xxxx. print("\ufea") not working.
