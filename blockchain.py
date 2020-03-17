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
