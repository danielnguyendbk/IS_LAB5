from core.menu import (
    show_main_menu, get_main_choice,
    show_symmetric_menu, show_asymmetric_menu, show_hash_menu,
    get_sub_choice
)
from core.input_handler import get_action, get_text_input, get_key_input, ask_generate_key
from hash.digest_tool import hash_processor
from utils.validators import is_valid_menu_choice, validate_key_length, validate_aes_key
from core.input_handler import get_action, get_text_input, get_key_input, ask_generate_key, get_multiline_input
from utils.validators import is_valid_menu_choice, validate_key_length

from symmetric.aes import encrypt_aes, decrypt_aes
from symmetric.des import DESTool
from symmetric.tripledes import TripleDESTool
from utils.keygen import generate_des_key, generate_3des_key, generate_aes_key

from utils.keygen import generate_des_key, generate_3des_key
from asymmetric.rsa_tool import generate_keypair, encrypt, decrypt
from core.output_formatter import print_result, print_error


def show_aes_encrypt_sample():
    print("\n--- Quick Test Sample: AES Encrypt ---")
    print("Plaintext: hello from ptit")
    print("Key      : 1234567890abcdef")
    print("Note     : AES key must be 16, 24, or 32 characters.")
    print("--------------------------------------\n")


def show_aes_decrypt_sample():
    print("\n--- Quick Test Sample: AES Decrypt ---")
    print("Ciphertext: Paste ciphertext from AES encrypt result")
    print("Key       : 1234567890abcdef")
    print("--------------------------------------\n")


def show_des_encrypt_sample():
    print("\n--- Quick Test Sample: DES Encrypt ---")
    print("Plaintext: hello from ptit")
    print("Key      : 12345678")
    print("Note     : DES key must be exactly 8 characters.")
    print("--------------------------------------\n")


def show_des_decrypt_sample():
    print("\n--- Quick Test Sample: DES Decrypt ---")
    print("Ciphertext: Paste ciphertext from DES encrypt result")
    print("Key       : 12345678")
    print("--------------------------------------\n")


def show_3des_encrypt_sample():
    print("\n--- Quick Test Sample: 3DES Encrypt ---")
    print("Plaintext: hello from ptit")
    print("Key      : 1234567890abcdef")
    print("Note     : 3DES key must be 16 or 24 characters.")
    print("--------------------------------------\n")


def show_3des_decrypt_sample():
    print("\n--- Quick Test Sample: 3DES Decrypt ---")
    print("Ciphertext: Paste ciphertext from 3DES encrypt result")
    print("Key       : 1234567890abcdef")
    print("--------------------------------------\n")


def show_rsa_generate_sample():
    print("\n--- Quick Test Sample: RSA Key Pair ---")
    print("Choose this option to generate public/private key pair.")
    print("Copy public key for encryption.")
    print("Copy private key for decryption.")
    print("--------------------------------------\n")


def show_rsa_encrypt_sample():
    print("\n--- Quick Test Sample: RSA Encrypt ---")
    print("Plaintext : hello from ptit")
    print("Public Key: Paste public key generated from option 1")
    print("--------------------------------------\n")


def show_rsa_decrypt_sample():
    print("\n--- Quick Test Sample: RSA Decrypt ---")
    print("Ciphertext : Paste ciphertext from RSA encrypt result")
    print("Private Key: Paste private key generated from option 1")
    print("--------------------------------------\n")


def show_hash_sample():
    print("\n--- Quick Test Sample: Hash ---")
    print("Text: hello from ptit")
    print("--------------------------------------\n")


def handle_post_action():
    next_choice = ask_next_step()
    if next_choice == "1":
        return "retry"
    elif next_choice == "2":
        return "back"
    elif next_choice == "0":
        return "exit"
    return "retry"

def get_valid_algorithm_choice(valid_choices: set[str], menu_name: str = "algorithm") -> str:
    while True:
        choice = get_sub_choice().strip()

        if choice in valid_choices:
            return choice

        print_error(
            f"Invalid {menu_name} choice. "
            f"Please choose one of: {', '.join(sorted(valid_choices))}."
        )

def handle_symmetric():
    while True:
        show_symmetric_menu()
        algo_choice = get_valid_algorithm_choice({"0", "1", "2", "3"}, "algorithm")

        if algo_choice == "0":
            break
        

        while True:
            action = get_action()

            if action == "0":
                break

            elif action == "1":  # Encrypt
                if algo_choice == "1":
                    show_aes_encrypt_sample()
                elif algo_choice == "2":
                    show_des_encrypt_sample()
                elif algo_choice == "3":
                    show_3des_encrypt_sample()

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

                elif algo_choice == "1":  # AES
                    if use_auto_key:
                        key = generate_aes_key(256)
                    else:
                        key_input = get_key_input("Enter AES key (16, 24, or 32 chars)")
                        try:
                            key = validate_aes_key(key_input)
                        except ValueError as e:
                            print_error(str(e))
                            continue

                    ciphertext = encrypt_aes(plaintext, key, mode='CBC')

                    print_result(
                        title="Execution Result",
                        algorithm="AES",
                        action="Encrypt",
                        input_data=plaintext,
                        key=key.hex() if isinstance(key, bytes) else key,
                        output_data=ciphertext
                    )

                else:
                    print_error("Algorithm module is not completed yet.")
                    continue

                decision = handle_post_action()
                if decision == "retry":
                    continue
                elif decision == "back":
                    break
                elif decision == "exit":
                    raise SystemExit
            elif action == "2":  # Decrypt
                if algo_choice == "1":
                    show_aes_decrypt_sample()
                elif algo_choice == "2":
                    show_des_decrypt_sample()
                elif algo_choice == "3":
                    show_3des_decrypt_sample()

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

                elif algo_choice == "1":  # AES
                    try:
                        key_bytes = validate_aes_key(key)
                        plaintext = decrypt_aes(ciphertext, key_bytes, mode='CBC')

                        print_result(
                            title="Execution Result",
                            algorithm="AES",
                            action="Decrypt",
                            input_data=ciphertext,
                            key=key,
                            output_data=plaintext
                        )
                    except Exception as e:
                        print_error(str(e))
                        continue

                else:
                    print_error("Algorithm module is not completed yet.")
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


def ask_use_saved_key(key_type):
    while True:
        answer = input(f"Use last generated {key_type}? (y/n): ").strip().lower()
        if answer in {"y", "n"}:
            return answer == "y"
        print_error("Invalid choice. Please enter y or n.")
    
def get_rsa_action():
    print("\n1. Generate Key Pair")
    print("2. Encrypt")
    print("3. Decrypt")
    print("0. Back")

    while True:
        choice = input("Choose an action: ").strip()

        if choice in {"1", "2", "3", "0"}:
            return choice

        print_error("Invalid RSA action. Please choose 1, 2, 3, or 0.")


def handle_asymmetric():
    last_public_key = None
    last_private_key = None
    last_ciphertext = None

    while True:
        show_asymmetric_menu()
        algo_choice = get_valid_algorithm_choice({"1", "0"}, "asymmetric algorithm")

        if algo_choice == "0":
            break
    

        while True:
            action = get_rsa_action()

            if action == "0":
                break

            elif action == "1":
                show_rsa_generate_sample()

                try:
                    keys = generate_keypair()

                    last_public_key = keys["public_key"]
                    last_private_key = keys["private_key"]

                    print_result(
                        title="RSA Key Generation Result",
                        algorithm="RSA",
                        action="Generate Key Pair",
                        input_data="N/A",
                        key=f"Public Key:\n{last_public_key}\nPrivate Key:\n{last_private_key}",
                        output_data="Key pair generated successfully. You can now use this key pair for encryption/decryption."
                    )

                except Exception as e:
                    print_error(str(e))
                    continue

            elif action == "2":
                show_rsa_encrypt_sample()
                plaintext = get_text_input("Enter plaintext")

                if last_public_key is not None and ask_use_saved_key("public key"):
                    public_key = last_public_key
                else:
                    public_key = get_multiline_input("Enter public key (PEM, end with empty line):")

                try:
                    ciphertext = encrypt(plaintext, public_key)
                    last_ciphertext = ciphertext

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

            elif action == "3":
                show_rsa_decrypt_sample()

                if last_ciphertext is not None and ask_use_saved_key("ciphertext"):
                    ciphertext = last_ciphertext
                else:
                    ciphertext = get_text_input("Enter ciphertext")

                if last_private_key is not None and ask_use_saved_key("private key"):
                    private_key = last_private_key
                else:
                    private_key = get_multiline_input("Enter private key (PEM, end with empty line):")

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
        algo_choice = get_valid_algorithm_choice({"1", "2", "0"}, "hash algorithm")

        if algo_choice == "0":
            break
        
        show_hash_sample()
        text = get_text_input("Enter text")

        if algo_choice == "1":
            algorithm_name = "MD5"
            digest = hash_processor(text, "MD5")
        else:
            algorithm_name = "SHA-256"
            digest = hash_processor(text, "SHA-256")

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
    print("\n1. Continue")
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