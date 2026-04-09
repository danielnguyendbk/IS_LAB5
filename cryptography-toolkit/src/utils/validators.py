def is_non_empty(value: str) -> bool:
    return bool(value and value.strip())

def is_valid_menu_choice(choice: str, valid_choices: set) -> bool:
    return choice in valid_choices

def validate_key_length(key: str, valid_lengths: list[int]) -> bool:
    return len(key) in valid_lengths