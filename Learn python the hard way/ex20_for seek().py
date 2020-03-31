
# 1. Python program to demonstrate
# seek() method


# Opening "GfG.txt" text file
f = open("ex20_for seek().txt",'r')

# Second parameter is by default 0
# sets Reference point to twentieth
# index position from the beginning
f.seek(20)

# prints current postion
print(f.tell())

print(f.readline())
print(f.readline())

f.close()




#2. Playing with seek and def
def test_seek(print_line):
    print(print_line.readline())

f = open("ex20_for seek()1.txt", 'r')
test_seek(f)
f.seek(0)
test_seek(f)
f.seek(1)#%%%%%%%Move "cursor" 6 times from starting("byte" values not "line")%%%%%%#
test_seek(f)
f.seek(2)
test_seek(f)
#f.seek(3)
test_seek(f)
#f.seek(4)
test_seek(f)
#f.seek(5)
test_seek(f)
#f.seek(6)
test_seek(f)
#f.seek(7)
test_seek(f)
#f.seek(8)
test_seek(f)

f.close()



#3. Seek using for loopls


def test_seek(print_line):
    print(print_line.readline())

f = open("ex20_for seek()1.txt", 'r')

#Going to use for loop
for numbers in range(0,4):
    test_seek(f)
    f.seek(numbers)
f.close()


#4. Seek using while loop
def test_seek(print_line):
    print(print_line.readline())

f = open("ex20_for seek()1.txt", 'r')

#Going to use while loop
number = 0
while number < 4:
    test_seek(f)
    f.seek(number)
    #Gonna use this: x = x + y is the same as x += y.
    number += 1 #Don't use '=+'. It will go to inifinite loop.
f.close()
