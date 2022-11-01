#texttriangle.py
#HMWK #2

usernumber = int(input("Enter a small positive integer: "))

print("")

for i in range(usernumber):
    print("#"*(i+1))

print("")

for i in range(usernumber):
    print("#"*(usernumber-i))
