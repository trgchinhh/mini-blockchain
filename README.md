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
mini-blockchain/                    # Tên dự án 
├── blockchain/                     # Mã nguồn chính
│   ├── __init__.py                 # Khởi tạo module
│   ├── block.py                    # Class Block
│   ├── chain.py                    # Class Blockchain
│   └── utils.py                    # Các hàm phụ (còn lại)
├── data/                           # Dữ liệu lưu trữ 
│   ├── block_history.json          # Lưu block
│   └── users.json                  # Tên user (người chuyển -> người nhận)
├── test/                           # Kiểm thử
│   └── test_blockchain.py          # Kiểm thử file main
├── bin/                            # File đã được build
│   └── main.exe                    # File main (.exe)
├── main.py                         # File main (source)
├── LICENSE                         # Giấy phép nguồn mở
└── README.md                       # Mô tả dự án 

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

- Folder RSA (demo mã hóa bất đối xúng trong blockchain)

<!--
## Screenshot
<p align="center">
    <img src="https://github.com/user-attachments/assets/b611af0a-2828-4c07-af76-726d2748e8f5" width="45%"/>
    <img src="https://github.com/user-attachments/assets/f2162ee0-11f2-4dc5-882f-4a975a041c49" width="45%"/>
</p>
-->




