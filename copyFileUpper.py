#fileUpper.py
#HMWK #2

#find user input
x = input("Choose a file to open and read in uppercase (please enter sample2): ")
filename = x + ".txt"

#read file and uppercase text   
inFile = open(filename, 'r')
contents = inFile.read()
newcontents = contents.upper()
inFile.close

#name new file
newname = "UPPER" + filename

#write new file
outFile = open(newname, 'w')
outFile.write(newcontents)
outFile.close()
