import json
from web3 import Web3
import solcx
import os

def run_mission():
    print("🏛️  [STG-WEB5] MEMULAI RE-ASSEMBLY KEDAULATAN...")
    
    # Pasang compiler 0.8.19 (Anti-PUSH0) secara otomatis
    print("⏳ Mendownload Native Compiler ARM64...")
    solcx.install_solc('0.8.19')
    solcx.set_solc_version('0.8.19')

    # Recompile Kontrak ke Standar Paris (Tanpa Pincang Biner)
    print("⚡ Merakit Kode TITAN-PSYCHE-MONO (EVM Paris)...")
    compiled_sol = solcx.compile_files(
        ['TITAN-PSYCHE-MONO.sol'],
        evm_version='paris',
        optimize=True
    )
    
    # Ambil biner dan abi hasil rakitan baru
    contract_id = 'TITAN-PSYCHE-MONO.sol:STGSovereignVault'
    if contract_id not in compiled_sol:
        # Cek nama kontrak jika berbeda
        contract_id = list(compiled_sol.keys())[0]
        
    abi = compiled_sol[contract_id]['abi']
    bytecode = compiled_sol[contract_id]['bin']

    # Hubungkan ke Markas Internal (Ganache)
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    if not w3.is_connected():
        print("❌ Ganache Belum Aktif!")
        return

    admin = w3.eth.accounts[0]
    print(f"👑 Akun Panglima: {admin}")

    # Tanam ke Ledger
    print("🚀 Meluncurkan Kedaulatan ke Blockchain...")
    SovereignContract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = SovereignContract.constructor().transact({'from': admin, 'gas': 6000000})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print("==================================================")
    print("✅ [MISSION ACCOMPLISHED] ASSET MERDEKA!")
    print(f"Alamat Kontrak: {tx_receipt.contractAddress}")
    print("==================================================")

    # Update Status
    with open("last_deploy_status.json", "w") as f:
        json.dump({"address": tx_receipt.contractAddress, "status": "IMMUTABLE"}, f, indent=4)

if __name__ == "__main__":
    run_mission()
