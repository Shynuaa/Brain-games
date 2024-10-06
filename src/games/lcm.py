import math
import random


class LCMGame:
    description = "Find the smallest common multiple of given numbers."

    @staticmethod
    def generate_game():
        numbers = [random.randint(1, 100) for _ in range(3)]
        lcm = numbers[0]
        for num in numbers[1:]:
            lcm = lcm * num // math.gcd(lcm, num)
        question = " ".join(map(str, numbers))
        return question, lcm
