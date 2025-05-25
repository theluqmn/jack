import random

sum = 0
for i in range(4):
    number = random.randint(0, 15)
    print(f"+\t{number}")
    sum += number

answer = input("Enter the sum: ")
if answer == str(sum):
    print("Correct!")
else:
    print("Incorrect!")