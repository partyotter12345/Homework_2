#fileUpper.py
#HMWK #2

x = input("Choose a file to open and read in uppercase (please enter sample2): ")
filename = x + ".txt"
      
inFile = open(filename, 'r')
contents = inFile.read()
print(contents.upper())
