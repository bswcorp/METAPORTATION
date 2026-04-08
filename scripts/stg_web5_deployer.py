import json
from web3 import Web3
import os
import sys

def deploy_sovereign():
    print("🏛️  [STG-WEB5] MEMULAI OPERASI PENEMBUSAN LAPIS 7...")
    
    # Jalur internal UserLand yang paling sering berhasil
    targets = [
        'http://127.0.0.1:8545',
        'http://10.0.2.2:8545',
        'http://192.168.1.1:8545',
        'http://192.168.1.8:8545'
    ]
    
    w3 = None
    for gate in targets:
        try:
            print(f"📡 Mencoba menembus: {gate}...")
            temp_w3 = Web3(Web3.HTTPProvider(gate, request_kwargs={'timeout': 2}))
            if temp_w3.is_connected():
                w3 = temp_w3
                print(f"✅ BARIKADE JEBOL DI: {gate}")
                break
        except:
            continue
            
    if not w3:
        print("❌ SEMUA JALUR TERKUNCI!")
        print("💡 PANGLIMA: Aktifkan 'ADB DEBUGGING' di opsi pengembang HP Anda.")
        return

    # Load Dokumen Intelijen (ABI & BIN)
    with open("TITAN-PSYCHE-MONO_sol_STGSovereignVault.abi", "r") as f:
        abi = json.load(f)
    with open("TITAN-PSYCHE-MONO_sol_STGSovereignVault.bin", "r") as f:
        bytecode = f.read().strip()
    if not bytecode.startswith('0x'): bytecode = '0x' + bytecode

    # Tarik Akun Panglima
    admin = w3.eth.accounts[0]
    print(f"👑 Akun Panglima Terverifikasi: {admin}")

    # Deploy ke Ledger Kedaulatan
    try:
        SovereignContract = w3.eth.contract(abi=abi, bytecode=bytecode)
        print("⚡ Menanam Kode Kedaulatan... (Takdir Agustus Dimulai)")
        tx_hash = SovereignContract.constructor().transact({
            'from': admin,
            'gas': 8000000
        })
        
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        print("==================================================")
        print("✅ [KEDAULATAN LIVE] TANPA PINCANG!")
        print(f"Alamat Kontrak: {tx_receipt.contractAddress}")
        print(f"Status: IMMUTABLE & MERDEKA")
        print("==================================================")

        with open("last_deploy_status.json", "w") as f:
            json.dump({"address": tx_receipt.contractAddress, "status": "LOCKED"}, f, indent=4)
            
    except Exception as e:
        print(f"❌ Kegagalan Transaksi: {e}")

if __name__ == "__main__":
    deploy_sovereign()
