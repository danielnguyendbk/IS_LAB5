
from utils.validators import is_non_empty

def get_text_input(label="Enter text"):
    while True:
        value = input(f"{label}: ").strip()
        if is_non_empty(value):
            return value
        print("Input cannot be empty. Please try again.")


def get_key_input(label="Enter key"):
    while True:
        key = input(f"{label}: ").strip()
        if is_non_empty(key):
            return key
        print("Key cannot be empty. Please try again.")
def get_action():
    print("\n1. Encrypt")
    print("2. Decrypt")
    print("0. Back")
    while True:
        choice = input("Choose an action: ").strip()
        if choice in {"1", "2", "0"}:
            return choice
        print("Invalid choice. Please try again.")

def ask_generate_key():
    answer = input("Generate random key? (y/n): ").strip().lower()
    return answer == "y"


def ask_generate_key():
    while True:
        answer = input("Generate random key? (y/n): ").strip().lower()
        if answer in {"y", "n"}:
            return answer == "y"
        print("Invalid choice. Please enter y or n.")


def ask_try_again():
    while True:
        answer = input("Try again? (y/n): ").strip().lower()
        if answer in {"y", "n"}:
            return answer == "y"
        print("Invalid choice. Please enter y or n.")


def get_multiline_input(label="Enter text (end with empty line)"):
    print(label)
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    value = "\n".join(lines)
    if is_non_empty(value):
        return value
    print("Input cannot be empty. Please try again.")
    return get_multiline_input(label)