from src.cli import greet_user, goodbye_user
from src.engine import run_game
from src.games.lcm import LCMGame
from src.games.progression import GeometricProgressionGame


def main():
    name = greet_user()
    while True:
        print("\nChoose a game:")
        print("1. Наименьшее общее кратное (НОК)")
        print("2. Геометрическая прогрессия")
        print("(Press enter to exit)")
        choice = input("Enter the number of the game you want to play: ")

        if choice == "":
            goodbye_user(name)
            break
        elif choice == "1":
            run_game(LCMGame, name)
        elif choice == "2":
            run_game(GeometricProgressionGame, name)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
