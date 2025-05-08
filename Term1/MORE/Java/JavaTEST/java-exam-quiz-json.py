import json
import random

def load_questions(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['questions']

def run_quiz(questions, num_questions=10):
    score = 0
    selected_questions = random.sample(questions, min(num_questions, len(questions)))
    
    for i, q in enumerate(selected_questions, 1):
        print(f"\nQuestion {i}:")
        print(q["question"])
        
        choices = q["choices"]
        random.shuffle(choices)
        
        for j, choice in enumerate(choices, 1):
            print(f"{j}. {choice}")
        
        while True:
            try:
                answer = int(input("Enter your answer (1-4): "))
                if 1 <= answer <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        
        if choices[answer - 1] == q["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {q['correct_answer']}")
    
    print(f"\nQuiz completed! Your score: {score}/{num_questions}")
    print(f"Percentage: {(score/num_questions)*100:.2f}%")

if __name__ == "__main__":
    print("Welcome to the Java Exam Quiz!")
    questions = load_questions('java_exam_questions.json')
    run_quiz(questions)
