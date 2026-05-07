from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from utils.encoding import encode_base64, decode_base64




def generate_keypair():
    try:
        key = RSA.generate(2048)

        private_pem = key.export_key(format="PEM").decode("utf-8")
        public_pem = key.publickey().export_key(format="PEM").decode("utf-8")

        return {
            "public_key": public_pem,
            "private_key": private_pem
        }

    except Exception as e:
        raise ValueError(f"RSA key generation failed: {str(e)}")


def encrypt(plaintext, public_key_pem):
    try:
        if not plaintext or not plaintext.strip():
            raise ValueError("Plaintext cannot be empty.")

        public_key = RSA.import_key(public_key_pem)

        if public_key.has_private():
            raise ValueError(
                "RSA encryption should use a public key. "
                "Using a private key belongs to digital signature, not normal encryption."
            )

        cipher = PKCS1_OAEP.new(public_key, hashAlgo=SHA256)
        ciphertext = cipher.encrypt(plaintext.encode("utf-8"))

        return encode_base64(ciphertext)

    except Exception as e:
        raise ValueError(f"RSA encryption failed: {str(e)}")


def decrypt(ciphertext_b64, private_key_pem):
    try:
        if not ciphertext_b64 or not ciphertext_b64.strip():
            raise ValueError("Ciphertext cannot be empty.")

        private_key = RSA.import_key(private_key_pem)

        if not private_key.has_private():
            raise ValueError("RSA decryption requires a private key.")

        ciphertext = decode_base64(ciphertext_b64)
        cipher = PKCS1_OAEP.new(private_key, hashAlgo=SHA256)

        plaintext = cipher.decrypt(ciphertext)
        return plaintext.decode("utf-8")

    except Exception as e:
        raise ValueError(f"RSA decryption failed: {str(e)}")