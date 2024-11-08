# Simple Quiz Game

def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Paris", "C) Madrid", "D) Rome"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Venus"],
            "answer": "C"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["A) Elephant", "B) Blue Whale", "C) Great White Shark", "D) Giraffe"],
            "answer": "B"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'To be, or not to be'?",
            "options": ["A) Charles Dickens", "B) Jane Austen", "C) William Shakespeare", "D) Mark Twain"],
            "answer": "C"
        }
    ]

    score = 0

    print("Welcome to the Quiz Game!")
    print("Type the letter of the correct answer for each question.\n")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        
        answer = input("Your answer: ").strip().upper()
        
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}\n")

    print(f"You've completed the quiz! Your score: {score} out of {len(questions)}")

# Run the quiz game
quiz_game()
