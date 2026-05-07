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


#Đình Thạch
def validate_aes_key(key: str) -> bytes:
    """
    Validate AES key.
    Hỗ trợ cả chuỗi ký tự thường (16, 24, 32 chars) và chuỗi Hex (32, 48, 64 chars).
    """
    validate_non_empty(key, "AES key")

    if len(key) in [32, 48, 64]:
        try:
            return bytes.fromhex(key)
        except ValueError:
            pass

    if validate_key_length(key, [16, 24, 32]):
        return key.encode("utf-8")

    raise ValueError("AES key must be 16, 24, or 32 bytes (or 32, 48, 64 hex characters).")


def validate_rsa_public_key(public_key_pem: str) -> str:
    validate_non_empty(public_key_pem, "RSA public key")

    if "-----BEGIN PUBLIC KEY-----" not in public_key_pem:
        raise ValueError("RSA public key must start with -----BEGIN PUBLIC KEY-----")

    if "-----END PUBLIC KEY-----" not in public_key_pem:
        raise ValueError("RSA public key must end with -----END PUBLIC KEY-----")

    return public_key_pem.strip()


def validate_rsa_private_key(private_key_pem: str) -> str:
    validate_non_empty(private_key_pem, "RSA private key")

    if "-----BEGIN PRIVATE KEY-----" not in private_key_pem:
        raise ValueError("RSA private key must start with -----BEGIN PRIVATE KEY-----")

    if "-----END PRIVATE KEY-----" not in private_key_pem:
        raise ValueError("RSA private key must end with -----END PRIVATE KEY-----")

    return private_key_pem.strip()