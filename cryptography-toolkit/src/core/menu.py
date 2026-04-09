def show_main_menu():
    print("\n=== CRYPTOGRAPHY TOOLKIT ===")
    print("1. Symmetric Encryption")
    print("2. Asymmetric Encryption")
    print("3. Hash Functions")
    print("0. Exit")


def get_main_choice():
    return input("Choose an option: ").strip()

def show_symmetric_menu():
    print("\n--- Symmetric Encryption ---")
    print("1. AES")
    print("2. DES")
    print("3. 3DES")
    print("0. Back")

def show_asymmetric_menu():
    print("\n--- Asymmetric Encryption ---")
    print("1. RSA")
    print("0. Back")

def show_hash_menu():
    print("\n--- Hash Functions ---")
    print("1. MD5")
    print("2. SHA-256")
    print("0. Back")

def get_sub_choice():
    return input("Choose an algorithm: ").strip()