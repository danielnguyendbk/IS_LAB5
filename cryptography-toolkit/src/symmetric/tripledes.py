from __future__ import annotations

import base64
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

from utils.validators import validate_3des_key, validate_non_empty

BLOCK_SIZE = 8


class TripleDESTool:
    @staticmethod
    def _normalize_key(key: str) -> bytes:
        raw_key = validate_3des_key(key)
        try:
            return DES3.adjust_key_parity(raw_key)
        except ValueError as exc:
            raise ValueError(
                "Invalid 3DES key. Please use a different 16-byte or 24-byte key."
            ) from exc

    @staticmethod
    def encrypt(plaintext: str, key: str) -> str:
        validate_non_empty(plaintext, "Plaintext")
        key_bytes = TripleDESTool._normalize_key(key)

        cipher = DES3.new(key_bytes, DES3.MODE_ECB)
        padded_data = pad(plaintext.encode("utf-8"), BLOCK_SIZE)
        ciphertext = cipher.encrypt(padded_data)
        return base64.b64encode(ciphertext).decode("utf-8")

    @staticmethod
    def decrypt(ciphertext_b64: str, key: str) -> str:
        validate_non_empty(ciphertext_b64, "Ciphertext")
        key_bytes = TripleDESTool._normalize_key(key)

        try:
            ciphertext = base64.b64decode(ciphertext_b64.encode("utf-8"))
        except Exception as exc:
            raise ValueError("Ciphertext must be valid Base64.") from exc

        try:
            cipher = DES3.new(key_bytes, DES3.MODE_ECB)
            decrypted = cipher.decrypt(ciphertext)
            plaintext = unpad(decrypted, BLOCK_SIZE)
            return plaintext.decode("utf-8")
        except Exception as exc:
            raise ValueError(
                "Decryption failed. Check if the key/ciphertext is correct."
            ) from exc