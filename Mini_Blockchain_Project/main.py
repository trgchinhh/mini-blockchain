from blockchain.block import *
from blockchain.chain import *
from blockchain.utils import *
from blockchain import __author__, __github__

def main():
    try:
        blockchain = BlockChain()
        number_of_blocks = input_number_of_blocks()
        number_of_transactions_in_block = input_number_of_transactions_in_block()
        
        with open(get_data_path("data\\users.json"), "r", encoding = "utf-8") as file:
            usernames = json.load(file)
        
        for _ in range(number_of_blocks):
            complete_block = []
            for _ in range(number_of_transactions_in_block):
                data_block = random_data_block(usernames)
                complete_block.append(data_block)
                write_block_to_json(complete_block)
            blockchain.add_block(complete_block)
        
        is_valid = blockchain.is_chain_valid()
        if is_valid: 
            print("\n[V] Is valid chain:", is_valid, "\n")
        else: 
            print("\n[X] Is valid chain:", is_valid, "\n")

        blockchain.print_block()

        print("\n[-] Author:", __author__)
        print("[-] Github:", __github__)
        input("Press any key to continue ...")
    except Exception as e:
        print(f"Eror: {e}")
        input("Press any key to exit ...")

if __name__ == '__main__':
    main()
