from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from utils.encoding import encode_base64, decode_base64


# =====================
# Generate Key Pair
# =====================
def generate_keypair():
    try:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        public_key = private_key.public_key()

        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        return {
            "public_key": public_pem.decode(),
            "private_key": private_pem.decode()
        }

    except Exception as e:
        return {"error": str(e)}


# =====================
# Encrypt
# =====================
def encrypt(plaintext, public_key_pem):
    try:
        public_key = serialization.load_pem_public_key(
            public_key_pem.encode()
        )

        ciphertext = public_key.encrypt(
            plaintext.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return encode_base64(ciphertext)

    except Exception as e:
        return f"Error: {str(e)}"


# =====================
# Decrypt
# =====================
def decrypt(ciphertext_b64, private_key_pem):
    try:
        private_key = serialization.load_pem_private_key(
            private_key_pem.encode(),
            password=None
        )

        ciphertext = decode_base64(ciphertext_b64)

        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return plaintext.decode()

    except Exception as e:
        return f"Error: {str(e)}"