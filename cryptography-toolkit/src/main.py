from core.menu import (
    show_main_menu, get_main_choice,
    show_symmetric_menu, show_asymmetric_menu, show_hash_menu,
    get_sub_choice
)
from core.input_handler import get_action, get_text_input, get_key_input, ask_generate_key

def handle_post_action():
    next_choice = ask_next_step()
    if next_choice == "1":
        return "retry"
    elif next_choice == "2":
        return "back"
    elif next_choice == "0":
        return "exit"
    return "retry"

def handle_symmetric():
    while True:
        show_symmetric_menu()
        algo_choice = get_sub_choice()

        if algo_choice == "0":
            break
        elif algo_choice not in {"1", "2", "3"}:
            print("Invalid choice. Please try again.")
            continue

        while True:
            action = get_action()

            if action == "0":
                break

            elif action == "1":  # Encrypt
                plaintext = get_text_input("Enter plaintext")
                use_auto_key = ask_generate_key()

                if use_auto_key:
                    key = "AUTO_GENERATED"
                else:
                    key = get_key_input()

                # Chỗ này sau này thay bằng hàm AES/DES/3DES thật
                ciphertext = "<<ciphertext placeholder>>"

                print_result(
                    title="Execution Result",
                    algorithm="AES",
                    action="Encrypt",
                    input_data=plaintext,
                    key=key,
                    output_data=ciphertext
                )

                decision = handle_post_action()
                if decision == "retry":
                    continue
                elif decision == "back":
                    break
                elif decision == "exit":
                    raise SystemExit

            elif action == "2":  # Decrypt
                ciphertext = get_text_input("Enter ciphertext")
                key = get_key_input()

                plaintext = "<<plaintext placeholder>>"

                print_result(
                    title="Execution Result",
                    algorithm="AES",
                    action="Decrypt",
                    input_data=ciphertext,
                    key=key,
                    output_data=plaintext
                )

                decision = handle_post_action()
                if decision == "retry":
                    continue
                elif decision == "back":
                    break
                elif decision == "exit":
                    raise SystemExit

            else:
                print("Invalid action. Please try again.")



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

def print_result(title, algorithm, action, input_data, key=None, output_data=None):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)
    print(f"Algorithm : {algorithm}")
    print(f"Action    : {action}")
    print(f"Input     : {input_data}")
    if key is not None:
        print(f"Key       : {key}")
    print(f"Output    : {output_data}")
    print("=" * 40)

def print_error(message):
    print(f"[ERROR] {message}")

def ask_next_step():
    print("\n1. Try Again")
    print("2. Back to Menu")
    print("0. Exit")
    return input("Choose next step: ").strip()

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