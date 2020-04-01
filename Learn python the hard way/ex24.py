print("Let's pracitice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n new lines and \t tabs.')

poem= """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""

print("-------------")
print(poem)
print("-------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)#values returned from line 25 in the same order(not in the name values.)
#print(beans, jars, crates)

#remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
#It'sjust like with an f"" cooked_string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
print("With a starting point of: {}".format(start_point))
#this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars and {} crates.".format(*formula)) '''*formula assigns
returned values from jelly_beans, jars, crates to the respective {}'s. We can't
do this trick in "f"({jelly_beans}, {jars}, {crates} )'''
