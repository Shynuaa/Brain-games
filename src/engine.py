def run_game(game_logic, name):
    print("\n"+game_logic.description)
    for i in range(3):
        question, correct_answer = game_logic.generate_game()
        user_answer = input(f"Question: {question}\nYour answer: ")
        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            answer = f"'{user_answer}' is wrong answer ;(. "
            correct_answer = f"Correct answer was '{correct_answer}'."
            print(answer + correct_answer)
            if i != 2:
                print(f"Let's try again, {name}!")
    print(f"Congratulations, {name}!")
