from __future__ import annotations
def is_non_empty(value: str) -> bool:
    return bool(value and value.strip())

def is_valid_menu_choice(choice: str, valid_choices: set) -> bool:
    return choice in valid_choices

def validate_key_length(key: str, valid_lengths: list[int]) -> bool:
    return len(key) in valid_lengths

# Minh Thành
def validate_non_empty(value: str, field_name: str = "Input") -> str:
    if not is_non_empty(value):
        raise ValueError(f"{field_name} cannot be empty.")
    return value


def validate_des_key(key: str) -> bytes:
    validate_non_empty(key, "DES key")
    if not validate_key_length(key, [8]):
        raise ValueError("DES key must be exactly 8 characters.")
    return key.encode("utf-8")


def validate_3des_key(key: str) -> bytes:
    validate_non_empty(key, "3DES key")
    if not validate_key_length(key, [16, 24]):
        raise ValueError("3DES key must be either 16 or 24 characters.")
    return key.encode("utf-8")