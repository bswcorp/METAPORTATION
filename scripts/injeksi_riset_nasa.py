import json
from web3 import Web3
import hashlib

def inject_nasa_data():
    print("📡 [STG-WEB5] MEMULAI INJEKSI DATA RISET NASA KE PROTOKOL...")
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    
    # 1. Alamat Kontrak Metaport yang baru dideploy
    metaport_address = "0x37ED4AD7fC17cc0F1960Ee077D280FF14fe5AeeD"
    
    # 2. Ambil Data Riset NASA dari modul-psyche
    with open("modul-psyche/status.json", "r") as f:
        nasa_data = f.read()
    
    # Buat Blueprint (Hash SHA256 dari data NASA)
    blueprint = w3.keccak(text=nasa_data)
    print(f"🧬 Blueprint Data (Hash): {blueprint.hex()}")

    # 3. Setup Kontrak (Gunakan ABI dari intelijen sebelumnya)
    abi = json.loads('[{"inputs":[{"internalType":"enum MetaportationProtocol.ServiceType","name":"_sType","type":"uint8"},{"internalType":"bytes32","name":"_blueprint","type":"bytes32"},{"internalType":"string","name":"_dest","type":"string"}],"name":"requestService","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
    
    contract = w3.eth.contract(address=metaport_address, abi=abi)
    admin = w3.eth.accounts[0]

    # 4. Kirim Injeksi Data (ServiceType 0 = Deep Space Research)
    print("⚡ Mentransmisikan data ke Blockchain...")
    tx_hash = contract.functions.requestService(
        0,              # ServiceType
        blueprint,      # Blueprint (Data NASA)
        "114-BT-VAULT"  # Destination
    ).transact({'from': admin})

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    print("==================================================")
    print(f"✅ [INJEKSI SUKSES] DATA NASA TERPATRI!")
    print(f"Transaction Hash: {tx_hash.hex()}")
    print(f"Status: IMMUTABLE DATA LOCKED")
    print("==================================================")

if __name__ == "__main__":
    inject_nasa_data()
