import json
from web3 import Web3

def final_injection():
    print("📡 [STG-WEB5] MENGINJEKSI DATA NASA KE PROTOKOL ASLI...")
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    
    # Alamat Kontrak Baru Anda
    metaport_address = "0xaa903Ea35F3E93c56d362236e2D136d52CD1a0E0"
    
    with open("modul-psyche/status.json", "r") as f:
        nasa_data = f.read()
    
    blueprint = w3.keccak(text=nasa_data)
    abi = json.loads('[{"inputs":[{"internalType":"uint8","name":"_sType","type":"uint8"},{"internalType":"bytes32","name":"_blueprint","type":"bytes32"},{"internalType":"string","name":"_dest","type":"string"}],"name":"requestService","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
    
    contract = w3.eth.contract(address=metaport_address, abi=abi)
    panglima = w3.eth.accounts[0]

    print(f"⚡ Mentransmisikan Blueprint: {blueprint.hex()}")
    tx_hash = contract.functions.requestService(
        0, 
        blueprint, 
        "114-BT-SOVEREIGN-VAULT"
    ).transact({'from': panglima})

    w3.eth.wait_for_transaction_receipt(tx_hash)
    print("==================================================")
    print("✅ [MISSION COMPLETE] DATA NASA TERKUNCI DI LEDGER!")
    print(f"TX: {tx_hash.hex()}")
    print("==================================================")

if __name__ == "__main__":
    final_injection()
