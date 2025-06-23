# Mini Blockchain Python

## Giới thiệu
- Project nhỏ mô phỏng cách hoạt động của blockchain 1 cách cơ bản 
- Gồm các chức năng tạo block, kiểm tra tính hợp lệ, lưu trữ giao dịch và xuất dữ liệu ra file JSON. 

## Cấu trúc blockchain cơ bản

<!--
```bash
mini-blockchain/
├── blockchain/
│   ├── __init__.py
│   ├── block.py
│   ├── chain.py
│   └── utils.py
├── data/
│   ├── coins.json
│   └── users.json
├── test/
│   └── test_blockchain.py
├── bin/
│   └── main.exe
├── main.py
├── LICENSE
└── README.md

```
- mini-blockchain: folder chính
- blockchain: chứa source code chính
    + init: khởi tạo
    + block: class block
    + chain: class chain
    + utils: các hàm phụ 
- data: chứa dữ liệu block
    + users: tên người nhận và chuyển
    + block_history: lịch sử block
- tests: test file trước khi cho ra file main
- main: file chính
-->
```bash
mini-blockchain/                    # tên dự án 
├── blockchain/                     # mã nguồn chính
│   ├── __init__.py                 # khởi tạo module
│   ├── block.py                    # class Block
│   ├── chain.py                    # class Blockchain
│   └── utils.py                    # Các hàm phụ (còn lại)
├── data/                           # dữ liệu lưu trữ 
│   ├── block_history.json          # lưu block
│   └── users.json                  # Tên user (người chuyển -> người nhận)
├── test/                           # kiểm thử
│   └── test_blockchain.py          # Kiểm thử file main
├── bin/                            # file đã được build
│   └── main.exe                    # file main (.exe)
├── main.py                         # file main (source)
├── LICENSE                         # giấy phép nguồn mở
└── README.md                       # mô tả dự án 
```

## Cách chạy 

- Chuyển hướng đến 
```bash
cd bin/
python main.py
```
- Hoặc chạy file exe ở đường dẫn
```bash
/mini-blockchain/blockchain/bin/main.exe
```

## Screenshot

![image](https://github.com/user-attachments/assets/a956a10a-b583-42dc-a660-6f13bb09a8e9)

![image](https://github.com/user-attachments/assets/98af2971-6690-448d-b0bd-41fc1f0f533c)



