import hashlib
import json

from time import time
from uuid import uuid4

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """ Validates the proof """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256.(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def new_block(self, proof, previous_hash=None):
        # Creates a new Block and adds it to the chain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transaction = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount):
        # Adds a new transaction to the list of transactions
        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]

    @staticmethod
    def hash(block):
        # Creates a SHA-256 has of Block
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
