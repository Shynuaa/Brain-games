def greet_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name?\n")
    print(f"Hello, {name}!")
    return name


def goodbye_user(name):
    print(f"Goodbye, {name}!\n")
