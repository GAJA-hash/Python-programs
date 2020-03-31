from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)# Each time you do f.seek(0) you’re moving
            #to the start of the file. Each time you do f.readline()
            #you’re reading a line from the file and moving the read
            #head to right after the \n that ends that line. .

def print_a_line(line_count, f):
    print(line_count, f.readline())
    """How does readline() know where each line is?
        Inside readline() is code that scans each byte of the file until
        it finds a \n character, then stops reading the file to return
        what it found so far. The file f is responsible for maintaining
        the current position in the file after each readline() call,
        so that it will keep reading each line.
    """

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

#Gonna use this: x = x + y is the same as x += y.
current_line  += 1 #Don't use '=+'. It will go to inifinite loop.
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
