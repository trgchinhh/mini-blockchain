import hashlib, json, time, random, os, sys

COIN_NAME = "NTC"

def hash(block):
    block_data = json.dumps(block.data) + block.prev_hash + str(block.nonce)
    block_data = block_data.encode("utf-8")
    return hashlib.sha256(block_data).hexdigest()

def write_block_to_json(block_data, filename="block_history.json"):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    data.append(block_data)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_data_path(filename):
    try:
        base_path = sys._MEIPASS 
    except AttributeError:
        base_path = os.path.abspath(".")  
    return os.path.join(base_path, filename)

def random_data_block(usernames):
    username_send = random.choice(usernames)
    username_receive = random.choice(usernames)
    amount = random.uniform(0.2, 100.0)
    while username_send == username_receive:
        username_receive = random.choice(usernames)
    return {
        f"from": f"{username_send}",
        f"to": f"{username_receive}",
        f"amout": f"{amount:.2f}",
        f"coin": f"{COIN_NAME}"
    }    

def input_number_of_blocks():
    number_of_blocks = int(input("Number of blocks: "))
    if not isinstance(number_of_blocks, int):
        print("Input must integer")
        input_number_of_blocks()
    return number_of_blocks    

def input_number_of_transactions_in_block():
    number_of_transactions_in_block = int(input("number_of_transactions_in_block: "))
    if not isinstance(number_of_transactions_in_block, int):
        print("Input must integer")
        input_nnumber_of_transactions_in_block()
    return number_of_transactions_in_block

