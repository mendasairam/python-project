questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
        "answer": 3  # Correct answer is the third option
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 2  # Correct answer is the second option
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": 3  # Correct answer is the third option
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"],
        "answer": 1  # Correct answer is the first option
    }
]

score = 0

for q in questions:
    print(q["question"])
    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")

    while True:
        try:
            user_choice = int(input("Your choice (1-4): "))
            if 1 <= user_choice <= 4:
                break
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    

    if user_choice == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['options'][q['answer'] - 1]}.")
    
    print()  # Print a blank line for better readability

print(f"Quiz Over! Your score is {score} out of {len(questions)}.")