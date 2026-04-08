import json
from web3 import Web3

# 1. Koneksi ke Jaringan (Ganti dengan URL Alchemy/Infura Anda)
w3 = Web3(Web3.HTTPProvider('URL_ALCHEMY_ANDA'))

# 2. Detail Kontrak (Gunakan ABI yang Anda berikan tadi)
contract_address = 'ALAMAT_KONTRAK_YANG_SUDAH_DEPLOY'
abi = json.loads('[...PASTE_ABI_YANG_ANDA_KIRIM_TADI_DI_SINI...]')

contract = w3.eth.contract(address=contract_address, abi=abi)

def laksanakan_misi(service_type, blueprint_hex, destination):
    private_key = 'PRIVATE_KEY_ANDA'
    account = w3.eth.account.from_key(private_key)
    
    # Konversi blueprint ke bytes32
    blueprint_bytes = w3.to_bytes(hexstr=blueprint_hex)
    
    print(f"[STG] Mengirim Sinyal Metaportasi ke {destination}...")
    
    # Build Transaksi
    tx = contract.functions.requestService(
        service_type, 
        blueprint_bytes, 
        destination
    ).build_transaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gas': 200000,
        'gasPrice': w3.to_wei('50', 'gwei')
    })
    
    # Sign & Kirim
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    print(f"[SUCCESS] Misi Terkunci di Blockchain! Hash: {tx_hash.hex()}")

# Contoh Eksekusi: Tipe 1, Blueprint dari hash panglima.py, Tujuan Gerbang Lenovo
# laksanakan_misi(1, "0xd819bedaa96fa73cd26e0770db2f33b8c5e71c7d5b6f36711027652c41f4478b", "LENOVO_SECTOR_7")
