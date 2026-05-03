# Cryptography Toolkit

Bộ công cụ CLI cho mã hóa đối xứng (AES, DES, 3DES), mã hóa bất đối xứng (RSA) và hàm băm (MD5, SHA-256).

## Tính năng
- Đối xứng: AES (CBC), DES, 3DES mã hóa/giải mã
- Bất đối xứng: RSA tạo khóa, mã hóa/giải mã
- Hàm băm: MD5, SHA-256
- Menu CLI và quick test sample trước khi nhập

## Video demo
- https://drive.google.com/file/d/1_mMF9xlL7kAhXGGizBZI40obHH7gComJ/view?usp=sharing

## Yêu cầu
- Python 3.8+
- pycryptodome

Cài đặt phụ thuộc (từ thư mục repo cha):
```
py -m pip install -r requirements.txt
```

## Cách chạy
Từ thư mục repo cha:
```
py src\main.py
```

## Cấu trúc thư mục
```
cryptography-toolkit/
  requirements.txt
  src/
    main.py
    asymmetric/
      rsa_tool.py
    core/
      input_handler.py
      menu.py
      output_formatter.py
    hash/
      digest_tool.py
      main.py
    symmetric/
      aes.py
      des.py
      tripledes.py
    utils/
      encoding.py
      keygen.py
      validators.py
```

## Lưu ý
- Khóa AES phải dài 16, 24 hoặc 32 ký tự.
- Khóa DES phải đúng 8 ký tự.
- Khóa 3DES phải dài 16 hoặc 24 ký tự.
