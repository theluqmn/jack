import random, time, sqlite3, os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_red(text):
    print(f"\033[31m{text}\033[0m")

def print_green(text):
    print(f"\033[32m{text}\033[0m")

def print_bold(text):
    print(f"\033[1m{text}\033[0m")

# generates questions according to parameters
def generate_questions(num_questions, num_length, num_range_min, num_range_max):
    questions = []

    for i in range(num_questions):
        question = { "numbers": [], "answer": 0, "time": 0, "correct": False }

        for i in range(num_length):
            number = random.randint(num_range_min, num_range_max)
            question["numbers"].append(number)
            question["answer"] += number
        
        questions.append(question)

    return questions

# handles prompting of questions
def prompt_question(number, question):
    print_bold(f"\nquestion {number}:")

    for i in range(len(question["numbers"])):
        if i < 0:
            print(f"-\t{question['numbers'][i]}")
        else:
            print(f"+\t{question['numbers'][i]}")

    time_start = time.time()
    answer = input("-----------\ntotal:\t")
    time_end = time.time()
    time_taken = (time_end - time_start).__round__(2)
    print(f"time:\t{time_taken}s")

    if answer == str(question["answer"]):
        print_green("correct!")
        question["correct"] = True
    else:
        print_red(f"incorrect\nanswer: {question['answer']}")

    return answer, time_taken

def test():
    questions = []
    default_presets = [
        { "name": "quick addition", "num_questions": 10, "num_length": 4, "num_range_min": 0, "num_range_max": 15 },
        { "name": "swift", "num_questions": 5, "num_length": 4, "num_range_min": -15, "num_range_max": 15 }
    ]

    # preset handling
    print_bold("jack")
    print("\nselect a preset:")
    for i in range(len(default_presets)):
        print(f"[{i+1}] {default_presets[i]['name']}")
    print("-----------\n[0] custom")
    preset = int(input("\npreset: "))

    if preset > len(default_presets): print_red("invalid preset")

    if preset == 0:
        num_questions = int(input("number of questions: "))
        num_length = int(input("number length: "))
        num_range_min = int(input("minimum number: "))
        num_range_max = int(input("maximum number: "))
        questions = generate_questions(1, 4, 0, 15)
    else:
        questions = generate_questions(default_presets[preset-1]["num_questions"], default_presets[preset-1]["num_length"], default_presets[preset-1]["num_range_min"], default_presets[preset-1]["num_range_max"])

    # prompt questions
    for i in range(len(questions)): 
        answer, time_taken = prompt_question(i+1, questions[i])
        questions[i]["answer"] = answer
        questions[i]["time"] = time_taken

    # results
    time_average = sum([question["time"] for question in questions]) / len(questions)
    percentage_correct = (sum([question["correct"] for question in questions]) / len(questions)) * 100

    print("\nResults:")
    print(f"Average time: {time_average}s")
    print(f"Percentage correct: {percentage_correct}% ({sum([question['correct'] for question in questions])}/{len(questions)})")

    return questions, preset

def load_profile(id):
    with sqlite3.connect("data/stats.db") as conn:
        with conn:
            conn.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, questions TEXT, preset INTEGER)")

            if id == 0:
                cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
                return [table[0] for table in cursor.fetchall()]
            else:
                conn.execute(f"SELECT * FROM {id}", (id,))
                return conn.fetchone()

def save_profile(id, questions, preset):
    with sqlite3.connect("data/stats.db") as conn:
        with conn:
            conn.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, questions TEXT, preset INTEGER)")
            conn.execute("INSERT INTO test (questions, preset) VALUES (?, ?)", (str(questions), preset))

# main function
if __name__ == "__main__":
    clear()
    print_bold("jack")
    print("A CLI-based mathematical game for you to train your basic arithmetic skills")
    print("-----------\n")

    # load a profile
    print_bold("select a profile to load:")
    profiles = load_profile(0)

    for i in range(len(profiles)):
        if profiles[i] == "sqlite_sequence": continue
        print(f"[{i+1}] {profiles[i]}")
    
    profile = int(input("\nprofile: "))
    if profile > len(profiles): print_red("invalid profile")

    # program loop
    while True:
        clear()
        print_bold(f"jack - {profiles[profile-1]}")
        print("-----------\n")
        print_bold("select an action:")
        print("[1] run test\n[2] view stats")

        action = int(input("\n-> "))

        clear()
        if action == 1:
            data = test()
            questions = data[0]
            preset = data[1]
            save_profile(profile, questions, preset)
        elif action == 2:
            print_bold(f"jack - {profiles[profiles-1]} stats")
            print("-----------\n")
            time.sleep(1)
        else:
            print_red("invalid action")
            time.sleep(1)