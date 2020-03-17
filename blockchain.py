import hashlib
import time
# blockchain implementation

class Blockchain():
    """ Blockchain constructor """
    def __init__(self, previous_hash, block_data, timestamp):
        """ this are the blockchain properties """
        self.previous_hash = previous_hash
        self.block_data = block_data
        self.timestamp = timestamp

    def  create_genesis_block(self):
        """ this one will create the genesis block """
        block_result = str(self.previous_hash) + str(self.block_data) + str(self.timestamp)
        block_result = hashlib.sha256(block_result.encode(encoding="UTF-8"))
        block_result = block_result.hexdigest()
        return block_result

    


#  dummy data to begin the genesis block
the_previous_hash = "00801056d95838f7bccb6f9d5bc312b9c6f001d723689820310538c02ea4f327"
the_block_data = "0"
the_timestamp =  round(time.time())

new_blockchain = Blockchain(the_previous_hash, the_block_data, the_timestamp)

print(new_blockchain.create_genesis_block())