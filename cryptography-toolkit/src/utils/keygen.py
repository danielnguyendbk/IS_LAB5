from __future__ import annotations

from Crypto.Random import get_random_bytes
import base64
def generate_des_key() -> str:
    return get_random_bytes(8).decode("latin-1")
def generate_3des_key(key_size: int = 24) -> str:
    if key_size not in (16, 24):
        raise ValueError("3DES key size must be 16 or 24 bytes.")
    return get_random_bytes(key_size).decode("latin-1")
def to_base64(data: bytes) -> str:
    return base64.b64encode(data).decode("utf-8")
def from_base64(data: str) -> bytes:
    return base64.b64decode(data.encode("utf-8"))


def generate_aes_key(key_size_bits=256) -> bytes:
    """Generate a random AES key (default 256-bit)."""
    if key_size_bits not in [128, 192, 256]:
        raise ValueError("AES key size must be 128, 192, or 256 bits.")
    return get_random_bytes(key_size_bits // 8)
