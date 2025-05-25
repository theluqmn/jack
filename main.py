import random, time

sum = 0
for i in range(4):
    number = random.randint(0, 15)
    print(f"+\t{number}")
    sum += number

time_start = time.time()
answer = input("----------\nSum:\t")
time_end = time.time()
time_taken = (time_end - time_start).__round__(2)

if answer == str(sum):
    print("Correct!")
else:
    print(f"Incorrect!\nAnswer: {sum}")

print(f"\nTime taken: {time_taken}s")