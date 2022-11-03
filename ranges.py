import random, time


print("This is the first part, 'First use the range function and a for-loop to produce the sequence 1, 2, 3, 4, and then print the numbers, one number per line.'")
for i in range(4):
    print(i+1)

time.sleep(2)
    
print("This is the second part, 'Prompt the user to input an integer n and print the sequence 1, 2, 3, ... , n - including n, using a for-loop.'")


n = int(input("Enter a number"))

for i in range(n):
    print(i+1)

time.sleep(2)

print("This is the third part, 'Use a Simple Repeat Loop to find and print five randomly chosen numbers from the range 1, 2, 3, ... , n.'")


n = int(input("Enter a number"))

for i in range(5):
    print(random.randrange(n))
