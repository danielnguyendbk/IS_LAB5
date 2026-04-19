from __future__ import annotations

import base64
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

from utils.validators import validate_des_key, validate_non_empty

BLOCK_SIZE = 8


class DESTool:
    @staticmethod
    def encrypt(plaintext: str, key: str) -> str:
        validate_non_empty(plaintext, "Plaintext")
        key_bytes = validate_des_key(key)

        cipher = DES.new(key_bytes, DES.MODE_ECB)
        padded_data = pad(plaintext.encode("utf-8"), BLOCK_SIZE)
        ciphertext = cipher.encrypt(padded_data)
        return base64.b64encode(ciphertext).decode("utf-8")

    @staticmethod
    def decrypt(ciphertext_b64: str, key: str) -> str:
        validate_non_empty(ciphertext_b64, "Ciphertext")
        key_bytes = validate_des_key(key)

        try:
            ciphertext = base64.b64decode(ciphertext_b64.encode("utf-8"))
        except Exception as exc:
            raise ValueError("Ciphertext must be valid Base64.") from exc

        try:
            cipher = DES.new(key_bytes, DES.MODE_ECB)
            decrypted = cipher.decrypt(ciphertext)
            plaintext = unpad(decrypted, BLOCK_SIZE)
            return plaintext.decode("utf-8")
        except Exception as exc:
            raise ValueError(
                "Decryption failed. Check if the key/ciphertext is correct."
            ) from exc