def get_action():
    print("\n1. Encrypt")
    print("2. Decrypt")
    print("0. Back")
    return input("Choose an action: ").strip()

def get_text_input(label="Enter text"):
    return input(f"{label}: ").strip()

def get_key_input():
    return input("Enter key: ").strip()

def ask_generate_key():
    answer = input("Generate random key? (y/n): ").strip().lower()
    return answer == "y"