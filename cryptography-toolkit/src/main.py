from core.menu import (
    show_main_menu, get_main_choice,
    show_symmetric_menu, show_asymmetric_menu, show_hash_menu,
    get_sub_choice
)

def handle_symmetric():
    while True:
        show_symmetric_menu()
        choice = get_sub_choice()
        if choice == "1":
            print("AES selected.")
        elif choice == "2":
            print("DES selected.")
        elif choice == "3":
            print("3DES selected.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def handle_asymmetric():
    while True:
        show_asymmetric_menu()
        choice = get_sub_choice()
        if choice == "1":
            print("RSA selected.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def handle_hash():
    while True:
        show_hash_menu()
        choice = get_sub_choice()
        if choice == "1":
            print("MD5 selected.")
        elif choice == "2":
            print("SHA-256 selected.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        show_main_menu()
        choice = get_main_choice()

        if choice == "1":
            handle_symmetric()
        elif choice == "2":
            handle_asymmetric()
        elif choice == "3":
            handle_hash()
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()