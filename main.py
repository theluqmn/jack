import random, time

def generate_question():
    total = 0
    for i in range(4):
        number = random.randint(0, 15)
        print(f"+\t{number}")
        total += number

    time_start = time.time()
    answer = input("----------\ntotal:\t")
    time_end = time.time()
    time_taken = (time_end - time_start).__round__(2)

    if answer == str(total):
        print("Correct!")
    else:
        print(f"Incorrect!\nAnswer: {total}")

    return answer, total, time_taken

stats = {
    "answer": [],
    "total": [],
    "time": []
}

for i in range(10):
    print(f"\nQuestion {i+1}:")
    answer, total, time_taken = generate_question()
    print(f"Time taken: {time_taken}s")
    stats["answer"].append(answer == str(total))
    stats["total"].append(total)
    stats["time"].append(time_taken)

print("\nResults:")
time_average = sum(stats["time"]) / len(stats["time"])
percentage_correct = (stats["answer"].count(True) / len(stats["answer"])) * 100
print(f"Average time: {time_average}s")
print(f"Percentage correct: {percentage_correct}%")