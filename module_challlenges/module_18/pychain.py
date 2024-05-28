# PyChain Ledger
################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib

# Step 1: Create a Record Data Class
# * Create a new data class named `Record`. This class will serve as the blueprint for the financial transaction records that the blocks of the ledger will store.

# @TODO
# Create a Record Data Class that consists of the `sender`, `receiver`, and `amount` attributes
# Comment: Each block has data that is sender, receiver, amount for each block in a dataclass called Record

@dataclass
class Record:
    sender: str
    receiver: str
    amount: float


# Step 2: Modify the Existing Block Data Class to Store Record Data
# * Change the existing `Block` data class by replacing the generic `data` attribute with a `record` attribute that’s of type `Record`.
@dataclass
class Block:

    # @TODO
    # Rename the `data` attribute to `record`, and set the data type to `Record`
    # Comment: This class is our block that contains information like Record, creator, previous hash, and timestamp
    # Comment: This class contains a hashing algo (sha), uses nonce to validate the hash, and returns a new hash in hexdigest form (letters and numbers)
    
    record: Record

    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: int = 0

    def hash_block(self):
        sha = hashlib.sha256()

        record = str(self.record).encode()
        sha.update(record)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()


@dataclass
class PyChain:
    chain: List[Block]
    difficulty: int = 4

    def proof_of_work(self, block):

        calculated_hash = block.hash_block()

        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):

            block.nonce += 1

            calculated_hash = block.hash_block()

        print("Wining Hash", calculated_hash)
        return block

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block) # comment: proved last block
        self.chain += [block] # comment: now will add this new block

    def is_valid(self):
        block_hash = self.chain[0].hash_block()

        for block in self.chain[1:]:
            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False

            block_hash = block.hash_block()

        print("Blockchain is Valid")
        return True

################################################################################
# Streamlit Code

# Adds the cache decorator for Streamlit


@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block("Genesis", 0)])


st.markdown("# PyChain")
st.markdown("## Store a Transaction Record in the PyChain")

pychain = setup()

################################################################################
# Step 3: Add Relevant User Inputs to the Streamlit Interface
# * Create additional user input areas in the Streamlit application. These input areas should collect the relevant information for each financial record that you’ll store in the `PyChain` ledger.

# @TODO:
# Delete the `input_data` variable from the Streamlit interface.
input_data = st.text_input("Block Data")

# @TODO:
# Add an input area where you can get a value for `sender` from the user.
sender_data = st.text_input("sender")

# @TODO:
# Add an input area where you can get a value for `receiver` from the user.
receiver_data = st.text_input("receiver")

# @TODO:
# Add an input area where you can get a value for `amount` from the user.
amount_data = st.number_input("amount")

if st.button("Add Block"):
    prev_block = pychain.chain[-1] # cc - gets previous block information
    prev_block_hash = prev_block.hash_block() # cc - gets hash of previous block

    # @TODO
    # Update `new_block` so that `Block` consists of an attribute named `record`
    # which is set equal to a `Record` that contains the `sender`, `receiver`, and `amount` values
    
    # Comment: each new block will have have sender, receiver, and amount info inputed, plus creater_id
    # Comment: each new block will will store or have the hash of the previous block as prev_hash 
    
    new_block = Block(
        record=Record(sender=sender_data,receiver=receiver_data,amount=amount_data),
        creator_id=42,
        prev_hash=prev_block_hash
    )

    pychain.add_block(new_block)
    st.balloons()

################################################################################
# Streamlit Code (continues)

st.markdown("## The PyChain Ledger")

pychain_df = pd.DataFrame(pychain.chain).astype(str)
st.write(pychain_df)

difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 2)
pychain.difficulty = difficulty

st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", pychain.chain
)

st.sidebar.write(selected_block)

if st.button("Validate Chain"):
    st.write(pychain.is_valid())

################################################################################
# Step 4: Test the PyChain Ledger by Storing Records
# * Test your complete `PyChain` ledger.
# Comment: See README.md for screenshots


