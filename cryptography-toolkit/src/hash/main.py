import hashlib

def calculate_hash(text, algorithm):
    """Gôm logic băm vào một chỗ, xử lý nhanh bằng mapping."""
    data_bytes = text.encode('utf-8')
    algo_map = {
        '1': hashlib.md5,
        '2': hashlib.sha256
    }
    
    func = algo_map.get(algorithm)
    return func(data_bytes).hexdigest() if func else None

def main_test():
    while True:
        print("\n--- MENU HASH ---")
        print("1. MD5")
        print("2. SHA-256")
        print("0. Thoat")
        
        choice = input("\nChon thuat toan (1/2/0): ").strip()
        
        if choice == '0':
            print("Dang thoat...")
            break
            
        if choice in ('1', '2'):
            plaintext = input("Nhap van ban: ")
            result = calculate_hash(plaintext, choice)
            
            algo_name = "MD5" if choice == '1' else "SHA-256"
            
            print(f"\nKET QUA {algo_name}:")
            print("-" * 40)
            print(result)
            print("-" * 40)
            print(f"Do dai: {len(result)} ky tu")
            
            input("\nNhan Enter de tiep tuc...")
        else:
            print("Lua chon khong hop le!")

if __name__ == "__main__":
    main_test()