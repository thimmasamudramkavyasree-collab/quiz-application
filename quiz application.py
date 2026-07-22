questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "2. Which language is used for Python programming?",
        "options": ["A. Java", "B. C++", "C. Python", "D. HTML"],
        "answer": "C"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "4. Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "5. Which data type stores True or False values?",
        "options": ["A. int", "B. float", "C. string", "D. bool"],
        "answer": "D"
    }
]

score = 0

print("===== PYTHON QUIZ APPLICATION =====")

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct Answer:", q["answer"])

print("\n===== QUIZ COMPLETED =====")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent!")
elif percentage >= 60:
    print("Good Job!")
elif percentage >= 40:
    print("Keep Practicing!")
else:
    print("Better Luck Next Time!")