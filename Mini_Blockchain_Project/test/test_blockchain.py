import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from blockchain.__init__ import *
from blockchain.__init__ import __author__, __github__

def get_data_path(filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "data", filename)

def test_main():
    try:
        blockchain = BlockChain()
        number_of_blocks = input_number_of_blocks()
        number_of_transactions_in_block = input_number_of_transactions_in_block()
        
        with open(get_data_path("users.json"), "r", encoding = "utf-8") as file:
            usernames = json.load(file)
        
        for _ in range(number_of_blocks):
            complete_block = []
            for _ in range(number_of_transactions_in_block):
                data_block = random_data_block(usernames)
                complete_block.append(data_block)
                write_block_to_json(complete_block)
            blockchain.add_block(complete_block)
        
        is_valid = blockchain.is_chain_valid()
        print("\n[V] Is valid chain:", is_valid, "\n")
        
        blockchain.print_block()
        print("Author:", __author__)
        input("Press Enter to exit ...")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    test_main()
