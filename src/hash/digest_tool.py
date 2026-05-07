import hashlib

def hash_processor(input_string, algorithm='SHA-256'):
    """
    Xử lý băm văn bản dựa trên thuật toán được chọn.
    """
    if not input_string:
        return "Error: Input cannot be empty."

    
    data_bytes = input_string.encode('utf-8')

    if algorithm.upper() == 'MD5':
        # MD5: 128-bit, 32 ký tự hex
        return hashlib.md5(data_bytes).hexdigest()
    
    elif algorithm.upper() == 'SHA-256':
        # SHA-256: 256-bit, 64 ký tự hex
        return hashlib.sha256(data_bytes).hexdigest()
    
    else:
        return "Error: Unsupported algorithm."  