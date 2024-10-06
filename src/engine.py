def print_game_description(game_logic):
    print("\n" + game_logic.description)


def play_round(game_logic):
    question, correct_answer = game_logic.generate_game()
    user_answer = input(f"Question: {question}\nYour answer: ")
    return user_answer, correct_answer


def check_answer(user_answer, correct_answer, name):
    if user_answer == str(correct_answer):
        print("Correct!")
    else:
        answer = f"'{user_answer}' is wrong answer ;(. "
        correct_answer = f"Correct answer was '{correct_answer}'."
        print(answer + correct_answer)
        print(f"Let's try again, {name}!")
        return False
    return True


def run_game(game_logic, name):
    print_game_description(game_logic)
    for _ in range(3):
        user_answer, correct_answer = play_round(game_logic)
        check_answer(user_answer, correct_answer, name)
    print(f"Congratulations, {name}!")
