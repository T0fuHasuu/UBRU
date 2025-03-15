import json

def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def ask_questions(questions):
    score = 0
    for question_data in questions:
        print(question_data["question"])
        for option in question_data["options"]:
            print(option)
        answer = input("Your answer: ").lower()
        if answer == question_data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is {question_data['answer']}.\n")
    print(f"You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    questions = load_questions("quiz_questions.json")
    ask_questions(questions)
