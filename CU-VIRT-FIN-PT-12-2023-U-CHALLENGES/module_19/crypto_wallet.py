# Cryptocurrency Wallet
################################################################################

# This file contains the Ethereum transaction functions that you have created throughout this module’s lessons.
# By using import statements, you will integrate this `crypto_wallet.py` Python script
# into the KryptoJobs2Go interface program that is found in the `krypto_jobs.py` file.

################################################################################
# Imports
import os
import requests
from dotenv import load_dotenv

load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy

from web3 import Web3 # New
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545')) # New
################################################################################
# Wallet functionality

#This generate_account for etherum using web3 and gets 30eth as intial balance
def generate_account(w3):
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Fetch mnemonic from environment variable.
    mnemonic = os.getenv("MNEMONIC")

    Account = w3.eth.account.create() # New
    # Create Wallet Object
    wallet = Wallet(mnemonic)

    # Derive Ethereum Private Key
    private, public = wallet.derive_account("eth")
    # Comment: Gets 30 Ether from some other account as intial balcne 
    get_funds(Account.address)

    # Convert private key into an Ethereum account
    # account = Account.privateKeyToAccount(private) # NEW: Not Using

    return Account # Comment: returning new Account


def get_balance(w3, address):
    """Using an Ethereum account address access the balance of Ether"""
    # Get balance of address in Wei
    wei_balance = w3.eth.get_balance(address)

    # Convert Wei value to ether
    ether = w3.from_wei(wei_balance, "ether")

    # Return the value in ether
    return ether


def send_transaction(w3, account, to, wage):
    """Send an authorized transaction to the Ganache blockchain."""
    # Set gas price strategy

    # Convert eth amount to Wei
    value = w3.to_wei(wage, "ether")

    # Calculate gas estimate
 

    # Construct a raw transaction
    raw_tx = {
        "to": to,
        "from": account.address,
        "value": value,
        "gas": 6721975,
        "gasPrice": w3.to_wei('50','gwei'),
        "nonce": w3.eth.get_transaction_count(account.address),
    }

    # Sign the raw transaction with ethereum account
    signed_tx = account.sign_transaction(raw_tx)

    # Send the signed transactions
    return w3.eth.send_raw_transaction(signed_tx.rawTransaction)


# Comment: New function that transfered 30 ETHER from Ganache 
def get_funds(address):
    
    key = '0xcdba7f1f023d552ab4ab4243277849930583f350ff3f22a1cff0928fffa2bcaf'
    deafault_account=w3.eth.accounts[0]
    tx={
            'nonce':w3.eth.get_transaction_count(deafault_account),
            'to':address,
            'value': w3.to_wei('30','ether'),
            'gas': 6721975,
            'gasPrice': w3.to_wei('50','gwei'),
        }
    signed_tx=w3.eth.account.sign_transaction(tx,key)
    tx_hash=w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(tx_hash)