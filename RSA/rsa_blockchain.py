"""
----------------------------------------------
  + Title: blockchain simulation program
  + Author: Truong Chinh
  + Github: https://github.com/trgchinhh
----------------------------------------------
"""

import hashlib, random, json, os, time
from datetime import datetime
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from tqdm import tqdm

names = [
        "Truong Chinh", "Truong An", "Duy Minh", "Duy Quang", "Ngoc Tu",
        "Thanh Phuc", "Manh Hung", "Nha Truc", "The An", "Thien An",
        "Gia Bao", "Khanh Dang", "Hai Dang", "Khanh Duy", "Bao Khanh",
        "Manh Cuong",
    ]

class Transaction:
    game = 1
    def __init__(self):
        self.data = {}
    
    def time_now(self):
        return datetime.now().strftime("%H:%M:%S %d/%m/%Y")

    def create_game(self):
        send_name = random.choice(names)
        receive_name = random.choice(names)
        while send_name == receive_name:
            receive_name = random.choice(names)
        amount = round(random.uniform(100000, 10000000), 3)
        fee = round(amount * ((0.5)/100), 6)
        time = self.time_now()
        code_data = send_name + receive_name + str(amount) + str(time)
        code = hashlib.md5(code_data.encode("utf-8")).hexdigest()
        self.data = {
            "Send name" : send_name,
            "Receive name" : receive_name,
            "Amount" : amount,
            "Fee" : fee,
            "Transaction code" : code,
            "Time" : time,
        }
        Transaction.game += 1
        return self.data

class Block:
    def __init__(self, index, data):
        self.index = index
        self.data = data
        self.prev_hash = ""
        self.now_hash = ""
        self.nonce = 0
        self.mine_time = 0.00
        self.signature = ""

    def hash(self):
        block_data = str(self.index) + json.dumps(self.data) + self.prev_hash + str(self.nonce)
        return hashlib.sha256(block_data.encode("utf-8")).hexdigest()

class BlockChain:
    def __init__(self, difficult):
        self.chain = []
        self.difficult = difficult
        self.path = "D:\\ThuGian_Python\\block.json"
        self.total_time = 0.00
        self.gen_keys()
        self.genesis_block()

    def gen_keys(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()
        with open("private.pem", "wb") as f:
            f.write(self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))
        with open("public.pem", "wb") as f:
            f.write(self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

    def sign_data(self, data_hash):
        return self.private_key.sign(data_hash.encode("utf-8"), padding.PKCS1v15(), hashes.SHA256()).hex()

    def verify_signature(self, data_hash, signature_hex):
        try:
            self.public_key.verify(
                bytes.fromhex(signature_hex),
                data_hash.encode("utf-8"),
                padding.PKCS1v15(),
                hashes.SHA256()
            )
            return True
        except:
            return False

    def genesis_block(self):
        genesis_data = {
            "Message" : "Genesis Block"
        }
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        block = Block(len(self.chain), genesis_data)
        block.index += 1
        block.now_hash = block.hash()
        block.signature = self.sign_data(block.now_hash)
        self.chain.append(block)
        self.print_block()

    def add_block(self, data):
        block = Block(len(self.chain), data)
        block.index += 1
        block.prev_hash = self.chain[-1].now_hash
        block.now_hash = block.hash()
        start_time = time.time()
        while not block.now_hash.startswith(self.difficult * "0"):
            block.nonce += 1
            block.now_hash = block.hash()
        end_time = time.time()
        block.mine_time = round(end_time - start_time, 2)
        self.total_time += block.mine_time
        block.signature = self.sign_data(block.now_hash)  
        self.chain.append(block)
        self.print_block()

    def print_block(self):
        last_block = self.chain[-1]
        content_block = {
            "Block": last_block.index,
            "Data": last_block.data,
            "Prev hash": last_block.prev_hash,
            "Hash": last_block.now_hash,
            "Nonce": last_block.nonce,
            "Mine time": str(last_block.mine_time) + "(s)",
            "Signature": last_block.signature[:16] 
        }
        #print(json.dumps(content_block, ensure_ascii=False, indent=4))
        self.save_block(content_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            now_block = self.chain[i]
            prev_block = self.chain[i-1]
            if now_block.prev_hash != prev_block.now_hash:
                return False
            if now_block.now_hash != now_block.hash():
                return False
            if not self.verify_signature(now_block.now_hash, now_block.signature):
                return False
        return True

    def save_block(self, content_block):
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as file:
                data = json.load(file)
        else:
            data = []
        data.append(content_block)
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

class Main:
    def __init__(self, number_blocks, difficult):
        self.blockchain = BlockChain(difficult)
        self.transaction = Transaction()
        self.number_blocks = number_blocks
        self.run()
     
    def run(self):
        print()
        for _ in tqdm(range(self.number_blocks), desc="Mining", unit="block"):
            self.blockchain.add_block(self.transaction.create_game())
        print("\nIs valid:", self.blockchain.is_valid())
        print("Total time:", round(self.blockchain.total_time, 2), "(s)")
        print(f"Completed adding {self.number_blocks} blocks to the chain with a difficulty of {self.blockchain.difficult} zeros")
        print(f"View block data at: {self.blockchain.path}")

if __name__ == "__main__":
    Main(10, 4)

# Main(a, b)
# a : number of blocks to add to the chain
# b : chain difficult (example "0000..." is difficult = 4)
