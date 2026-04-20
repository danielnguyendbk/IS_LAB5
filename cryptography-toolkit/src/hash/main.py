import hashlib
import os

def calculate_hash(text, algorithm):
    data_bytes = text.encode('utf-8')
    
    if algorithm == '1':
        return hashlib.md5(data_bytes).hexdigest()
    elif algorithm == '2':
        # Thuật toán SHA-256
        return hashlib.sha256(data_bytes).hexdigest()
    return None

def main_test():
    while True:
        
      
        print("HASH")
        print("1. Chạy thuật toán MD5")
        print("2. Chạy thuật toán SHA-256")
        print("0. Thoát chương trình")
        
        choice = input("\nChọn thuật toán muốn test (1/2/0): ")
        
        if choice == '0':
            print("Đang thoát...")
            break
            
        if choice in ['1', '2']:
            plaintext = input(" Nhập văn bản cần băm: ")
            
            # Thực hiện băm
            result = calculate_hash(plaintext, choice)
            
            algo_name = "MD5" if choice == '1' else "SHA-256"
            
            print(f"\n KẾT QUẢ {algo_name}:")
            print(f"------------------------------------------")
            print(f"{result}")
            print(f"------------------------------------------")
            print(f"Độ dài chuỗi: {len(result)} ký tự")
            
            input("\nNhấn Enter để tiếp tục test...")
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main_test()