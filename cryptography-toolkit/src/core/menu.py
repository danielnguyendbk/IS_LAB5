def show_main_menu():
    print("\n=== CRYPTOGRAPHY TOOLKIT ===")
    print("1. Symmetric Encryption")
    print("2. Asymmetric Encryption")
    print("3. Hash Functions")
    print("0. Exit")


def get_main_choice():
    return input("Choose an option: ").strip()