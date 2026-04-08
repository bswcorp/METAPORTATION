import json
from web3 import Web3
import sys

def deploy_sovereign():
    print("🏛️  [STG-WEB5] EKSEKUSI FINAL: PROTOKOL LONDON ACTIVE...")
    
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    
    if not w3.is_connected():
        print("❌ Sinyal Terputus!")
        return

    # Load ABI & BIN
    with open("TITAN-PSYCHE-MONO_sol_STGSovereignVault.abi", "r") as f:
        abi = json.load(f)
    with open("TITAN-PSYCHE-MONO_sol_STGSovereignVault.bin", "r") as f:
        bytecode = f.read().strip()
    if not bytecode.startswith('0x'): bytecode = '0x' + bytecode

    admin = w3.eth.accounts[0]
    print(f"👑 Panglima: {admin}")

    try:
        SovereignContract = w3.eth.contract(abi=abi, bytecode=bytecode)
        print("⚡ Menanam Kode Kedaulatan... (Bypassing Invalid Opcode)")
        
        # Kirim transaksi dengan spesifikasi gas manual
        tx_hash = SovereignContract.constructor().transact({
            'from': admin, 
            'gas': 6000000,
            'gasPrice': w3.to_wei('20', 'gwei')
        })
        
        print("⏳ Menunggu Konfirmasi Takdir...")
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        print("==================================================")
        print("✅ [KEDAULATAN LIVE] TANPA CACAT!")
        print(f"Alamat Kontrak: {tx_receipt.contractAddress}")
        print(f"Status: MERDEKA 100%")
        print("==================================================")
        
        with open("last_deploy_status.json", "w") as f:
            json.dump({
                "address": tx_receipt.contractAddress, 
                "network": "London-Hardfork",
                "status": "IMMUTABLE"
            }, f, indent=4)
            
    except Exception as e:
        print(f"❌ Terdeteksi Barikade Opcode: {e}")
        print("💡 SARAN: Jika masih gagal, kontrak harus di-recompile dengan EVM version 'paris'.")

if __name__ == "__main__":
    deploy_sovereign()
