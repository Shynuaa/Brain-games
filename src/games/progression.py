import random


class GeometricProgressionGame:

    description = "What number is missing in the progression?"

    @staticmethod
    def generate_game():
        length = random.randint(5, 10)
        start = random.randint(1, 10)
        ratio = random.randint(2, 5)
        progression = [start * (ratio ** i) for i in range(length)]
        missing_index = random.randint(0, length - 1)
        correct_answer = progression[missing_index]
        progression[missing_index] = ".."
        question = " ".join(map(str, progression))
        return question, correct_answer
