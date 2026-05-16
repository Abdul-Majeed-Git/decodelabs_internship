score = 0

def ask_question(question, correct_answer, q_number):
    global score
    
    user_input = input(f"Q{q_number}: {question}\nAns: ")
    
    choice = user_input.strip().lower()
    if choice == correct_answer.lower():
        print("Correct answer!")
        score = score + 1
    else:
        print(f"Wrong answer! The correct answer is {correct_answer}.")

if __name__ == "__main__":
    print("==== WELCOME TO THE GENERAL KNOWLEDGE QUIZ ====")
    
    # Question 1
    ask_question("What is the capital of France?", "Paris", 1)
    
    # Question 2
    ask_question("In which year did Pakistan get independence?", "1947", 2)
    
    # Question 3
    ask_question("What is the capital of Pakistan?", "Islamabad", 3)
    
    # Final Results
    print("====================================")
    print("             GAME OVER              ")
    print("====================================")
    print(f"Your Final Score is: {score:>2}/3")
    print("====================================")