

from utils.validators import is_non_empty

def get_text_input(label="Enter text"):
    while True:
        value = input(f"{label}: ").strip()
        if is_non_empty(value):
            return value
        print("Input cannot be empty. Please try again.")

def get_key_input():
    while True:
        key = input("Enter key: ").strip()
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

def get_text_input(label="Enter text"):
    return input(f"{label}: ").strip()

def get_key_input():
    return input("Enter key: ").strip()

def ask_generate_key():
    answer = input("Generate random key? (y/n): ").strip().lower()
    return answer == "y"