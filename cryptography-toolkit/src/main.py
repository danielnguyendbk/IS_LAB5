from core.menu import (
    show_main_menu, get_main_choice,
    show_symmetric_menu, show_asymmetric_menu, show_hash_menu,
    get_sub_choice
)
from core.input_handler import get_action, get_text_input, get_key_input, ask_generate_key, get_text_input
from utils.validators import is_valid_menu_choice, validate_key_length

from symmetric.des import DESTool
from symmetric.tripledes import TripleDESTool
from utils.keygen import generate_des_key, generate_3des_key
from asymmetric.rsa_tool import generate_keypair, encrypt, decrypt
from core.output_formatter import print_result, print_error


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

                if algo_choice == "2":  # DES
                    if use_auto_key:
                        key = generate_des_key()
                    else:
                        key = get_key_input("Enter DES key (8 chars)")

                    ciphertext = DESTool.encrypt(plaintext, key)

                    print_result(
                        title="Execution Result",
                        algorithm="DES",
                        action="Encrypt",
                        input_data=plaintext,
                        key=key,
                        output_data=ciphertext
                    )

                elif algo_choice == "3":  # 3DES
                    if use_auto_key:
                        key_size = input("Choose 3DES key size (16 or 24): ").strip()
                        if key_size not in {"16", "24"}:
                            print_error("3DES key size must be 16 or 24.")
                            continue
                        key = generate_3des_key(int(key_size))
                    else:
                        key = get_key_input("Enter 3DES key (16 or 24 chars)")

                    ciphertext = TripleDESTool.encrypt(plaintext, key)

                    print_result(
                        title="Execution Result",
                        algorithm="3DES",
                        action="Encrypt",
                        input_data=plaintext,
                        key=key,
                        output_data=ciphertext
                    )

                else:
                    print_error("AES module is not completed yet.")
                    continue

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

                if algo_choice == "2":  # DES
                    if not validate_key_length(key, [8]):
                        print_error("DES key must be 8 characters long.")
                        continue

                    plaintext = DESTool.decrypt(ciphertext, key)

                    print_result(
                        title="Execution Result",
                        algorithm="DES",
                        action="Decrypt",
                        input_data=ciphertext,
                        key=key,
                        output_data=plaintext
                    )

                elif algo_choice == "3":  # 3DES
                    if not validate_key_length(key, [16, 24]):
                        print_error("3DES key must be 16 or 24 characters long.")
                        continue

                    plaintext = TripleDESTool.decrypt(ciphertext, key)

                    print_result(
                        title="Execution Result",
                        algorithm="3DES",
                        action="Decrypt",
                        input_data=ciphertext,
                        key=key,
                        output_data=plaintext
                    )

                else:
                    print_error("AES module is not completed yet.")
                    continue

                decision = handle_post_action()
                if decision == "retry":
                    continue
                elif decision == "back":
                    break
                elif decision == "exit":
                    raise SystemExit
            else:
                print("Invalid action. Please try again.")


def get_rsa_action():
    print("\n1. Generate Key Pair")
    print("2. Encrypt")
    print("3. Decrypt")
    print("0. Back")
    return input("Choose an action: ").strip()


def handle_asymmetric():
    while True:
        show_asymmetric_menu()
        algo_choice = get_sub_choice()

        if algo_choice == "0":
            break
        elif algo_choice != "1":
            print_error("Invalid asymmetric algorithm choice.")
            continue

        while True:
            action = get_rsa_action()

            if action == "0":
                break

            elif action == "1":
                keys = generate_keypair()

                if "error" in keys:
                    print_error(keys["error"])
                    continue

                public_key = keys["public_key"]
                private_key = keys["private_key"]

                print_result(
                    title="RSA Key Generation Result",
                    algorithm="RSA",
                    action="Generate Key Pair",
                    input_data="N/A",
                    key=f"Public Key:\n{public_key}\nPrivate Key:\n{private_key}",
                    output_data="Key pair generated successfully"
                )

            elif action == "2":
                plaintext = get_text_input("Enter plaintext")
                public_key = get_text_input("Enter public key")

                try:
                    ciphertext = encrypt(plaintext, public_key)

                    print_result(
                        title="RSA Encryption Result",
                        algorithm="RSA",
                        action="Encrypt",
                        input_data=plaintext,
                        key=public_key,
                        output_data=ciphertext
                    )

                except Exception as e:
                    print_error(str(e))
                    continue

                print_result(
                    title="Execution Result",
                    algorithm="RSA",
                    action="Encrypt",
                    input_data=plaintext,
                    key=public_key,
                    output_data=ciphertext
                )

            elif action == "3":
                ciphertext = get_text_input("Enter ciphertext")
                private_key = get_text_input("Enter private key")

                try:
                    plaintext = decrypt(ciphertext, private_key)

                    print_result(
                        title="RSA Decryption Result",
                        algorithm="RSA",
                        action="Decrypt",
                        input_data=ciphertext,
                        key=private_key,
                        output_data=plaintext
                    )

                except Exception as e:
                    print_error(str(e))
                    continue

                print_result(
                    title="Execution Result",
                    algorithm="RSA",
                    action="Decrypt",
                    input_data=ciphertext,
                    key=private_key,
                    output_data=plaintext
                )

            else:
                print_error("Invalid RSA action.")
                continue

            decision = handle_post_action()
            if decision == "retry":
                continue
            elif decision == "back":
                break
            elif decision == "exit":
                raise SystemExit


def handle_hash():
    while True:
        show_hash_menu()
        algo_choice = get_sub_choice()

        if algo_choice == "0":
            break
        elif algo_choice not in {"1", "2"}:
            print_error("Invalid hash algorithm choice.")
            continue

        text = get_text_input("Enter text")

        if algo_choice == "1":
            algorithm_name = "MD5"
            digest = "<<md5 placeholder>>"
        else:
            algorithm_name = "SHA-256"
            digest = "<<sha256 placeholder>>"

        print_result(
            title="Execution Result",
            algorithm=algorithm_name,
            action="Hash",
            input_data=text,
            key=None,
            output_data=digest
        )

        decision = handle_post_action()
        if decision == "retry":
            continue
        elif decision == "back":
            break
        elif decision == "exit":
            raise SystemExit

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
            if not is_valid_menu_choice(choice, {"1", "2", "3", "0"}):
                print_error("Invalid main menu choice.")
                continue

if __name__ == "__main__":
    main()