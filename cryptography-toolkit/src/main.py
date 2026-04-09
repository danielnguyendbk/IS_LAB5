from core.menu import show_main_menu, get_main_choice

def main():
    while True:
        show_main_menu()
        choice = get_main_choice()

        if choice == "1":
            print("Symmetric Encryption selected.")
        elif choice == "2":
            print("Asymmetric Encryption selected.")
        elif choice == "3":
            print("Hash Functions selected.")
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()