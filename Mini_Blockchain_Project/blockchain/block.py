class Block:
    def __init__(self, data):
        self.data = data
        self.prev_hash = ""
        self.hash = ""
        self.nonce = 0
        self.time = 0.00
        self.valid = ""

        