import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_aes(plaintext: str, key: bytes, mode: str = 'CBC') -> str:
    """
    Mã hóa văn bản bằng thuật toán AES.
    Hỗ trợ chế độ CBC và ECB. Trả về chuỗi định dạng Base64.
    """
    mode = mode.upper()
    try:
        padded_data = pad(plaintext.encode('utf-8'), AES.block_size)
        
        if mode == 'CBC':
            cipher = AES.new(key, AES.MODE_CBC)
            ct_bytes = cipher.encrypt(padded_data)
            result = cipher.iv + ct_bytes
        elif mode == 'ECB':
            cipher = AES.new(key, AES.MODE_ECB)
            result = cipher.encrypt(padded_data)
        else:
            raise ValueError("Chế độ không hỗ trợ. Vui lòng chọn 'CBC' hoặc 'ECB'.")
        
        return base64.b64encode(result).decode('utf-8')
    except Exception as e:
        raise Exception(f"Lỗi mã hóa AES: {str(e)}")

def decrypt_aes(ciphertext_b64: str, key: bytes, mode: str = 'CBC') -> str:
    """
    Giải mã chuỗi Base64 AES về văn bản gốc.
    """
    mode = mode.upper()
    try:
        raw_data = base64.b64decode(ciphertext_b64)
        
        if mode == 'CBC':
            ct = raw_data[AES.block_size:]
            cipher = AES.new(key, AES.MODE_CBC, iv)
            pt_padded = cipher.decrypt(ct)
        elif mode == 'ECB':
            cipher = AES.new(key, AES.MODE_ECB)
            pt_padded = cipher.decrypt(raw_data)
        else:
            raise ValueError("Chế độ không hỗ trợ. Vui lòng chọn 'CBC' hoặc 'ECB'.")
        
        pt_bytes = unpad(pt_padded, AES.block_size)
        return pt_bytes.decode('utf-8')
    except ValueError:
        raise Exception("Giải mã thất bại: Có thể do sai khóa, sai chế độ (Mode), hoặc dữ liệu bị hỏng.")
    except Exception as e:
        raise Exception(f"Lỗi giải mã AES: {str(e)}")