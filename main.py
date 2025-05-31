import random, time

def generate_questions(num_questions, num_length, num_range_min, num_range_max):
    questions = []

    for i in range(num_questions):
        question = { "numbers": [], "answer": 0, "time": 0, "correct": False }

        for i in range(num_length):
            number = random.randint(num_range_min, num_range_max)
            question["numbers"].append(number)
            answer += number

    return questions

def prompt_question(number, question):
    print(f"\nquestion {number}:")

    for i in range(len(question["numbers"])):
        if i < 0:
            print(f"-\t{question['numbers'][i]}")
        else:
            print(f"+\t{question['numbers'][i]}")
    time_start = time.time()
    answer = input("----------\ntotal:\t")
    time_end = time.time()
    time_taken = (time_end - time_start).__round__(2)
    print(f"Time taken: {time_taken}s")

    if answer == str(question["answer"]):
        print("correct!")
        question["correct"] = True
    else:
        print(f"incorrect!\nanswer: {question['answer']}")

    return answer, time_taken

if __name__ == "__main__":
    questions = generate_questions(10, 4, 0, 15)
    for i in range(len(questions)):
        answer, time_taken = prompt_question(i+1, questions[i])
        questions[i]["answer"] = answer
        questions[i]["time"] = time_taken

    time_average = sum([question["time"] for question in questions]) / len(questions)
    percentage_correct = (sum([question["correct"] for question in questions]) / len(questions)) * 100

    print("\nResults:")
    print(f"Average time: {time_average}s")
    print(f"Percentage correct: {percentage_correct}% ({sum([question['correct'] for question in questions])}/{len(questions)})")