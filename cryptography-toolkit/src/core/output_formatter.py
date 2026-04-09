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