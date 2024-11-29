import os


def greet(name):
    """Greet the user by name."""
    print(f"Hello, {name}!")


def main():
    """Main function to run the program."""
    user_name = input("Enter your name: ")
    greet(user_name)


if __name__ == "__main__":
    main()
