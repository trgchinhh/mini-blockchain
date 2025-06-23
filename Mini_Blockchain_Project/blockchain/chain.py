from blockchain.utils import *
from blockchain.block import *

class BlockChain:
    def __init__(self):
        self.chain = []
        self.total_time = 0.00
        block = Block("Genesis Block")
        block.hash = hash(block)
        self.chain.append(block)

    def add_block(self, data):
        block = Block(data)
        block.prev_hash = self.chain[-1].hash
        block.hash = hash(block)
        start = time.time()
        while block.hash.startswith(block.prev_hash[60:]) == False:
            block.nonce += 1
            block.hash = hash(block)
        end = time.time()
        block.time = end - start
        self.total_time += block.time
        self.chain.append(block)
    
    def is_block_valid(self, current_block, previous_block):
        if current_block.prev_hash != previous_block.hash:
            return False
        if current_block.hash != hash(current_block):
            return False
        return True

    def print_block(self):
        for i, block in enumerate(self.chain):
            print(f" ┌• Block {i}")
            for transaction in block.data:
                if(not isinstance(transaction, dict)):
                    print(f" ├─• Data: {block.data}")
                    break
                else:
                    print(f" ├─┬• Data: ")
                    order = 1
                    for transaction in block.data:
                        print(f" │ ├  + ({order}) -> {json.dumps(transaction, ensure_ascii=False)}")
                        order += 1
                    break
            print(f" ├─┬• Hash: ") 
            print(f" │ ├  + Prev hash: {block.prev_hash}")
            print(f" │ ├  + Now Hash: {block.hash}")
            print(f" ├• Nonce: {block.nonce}")
            if(i > 0):
                valid = self.is_block_valid(block, self.chain[i-1])
                print(f" ├• Time: {block.time:.4f}(s)")
                print(f" └• Valid: {valid}")
            else: 
                print(f" └• Time: {block.time:.4f}(s)")  
            print()   
        print(f"[+] Total time: {self.total_time:.4f}(s)")           

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previos_block = self.chain[i-1]
            if current_block.prev_hash != previos_block.hash:
                return False
            if current_block.hash != hash(current_block):
                return False
        return True
 
