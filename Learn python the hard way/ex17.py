
from sys import argv
from os.path import exists #a new command 'exists' imported.

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#We could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()

indata = (open(from_file).read())  #Doing the above two lines in one line. No need to put "indata.close()"


print(f"THe input file is {len(indata)} bytes long")

#'exists' returns True if a file exists, based on its mame in a string as an argument. It returns False if not.
print(f"Does the output file exist? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, CTRL-C to abort.")
input()#in_file.close()

out_file = open(to_file, 'w') # truncate the file first and enable write to file.
out_file.write(indata)


#out_file = open(to_file)
#print(out_file.read()) # If you want to read the copied text you can enable the above 2 linese.
print("Alright, all done.")
#in_file.close()

out_file.close()
#in_file.close()

#study drill
#Short version of the above program in one line.
'''
from sys import argv;from os.path import exists;script, from_file, to_file = argv; indata = (open(from_file).read()); open(to_file,'w').write(indata)
'''
