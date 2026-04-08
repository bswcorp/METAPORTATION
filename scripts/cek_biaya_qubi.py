import json
from web3 import Web3

def check_registry():
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    metaport_address = "0x37ED4AD7fC17cc0F1960Ee077D280FF14fe5AeeD"
    
    abi = json.loads('[{"inputs":[{"internalType":"enum MetaportationProtocol.ServiceType","name":"","type":"uint8"}],"name":"registry","outputs":[{"internalType":"uint256","name":"priority","type":"uint256"},{"internalType":"uint256","name":"cost","type":"uint256"},{"internalType":"bool","name":"isQuantumSafe","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"qubicoinBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')
    
    contract = w3.eth.contract(address=metaport_address, abi=abi)
    admin = w3.eth.accounts[0]
    
    # 1. Cek Saldo Qubicoin Anda
    balance = contract.functions.qubicoinBalance(admin).call()
    # 2. Cek Biaya Layanan (ServiceType 0)
    priority, cost, safety = contract.functions.registry(0).call()
    
    print(f"🏛️  [STG-INTEL] STATUS PROTOKOL:")
    print(f"👑 Saldo Qubicoin Panglima: {balance}")
    print(f"💸 Biaya Layanan (Type 0): {cost}")
    print(f"🛡️  Quantum Safe: {safety}")
    
    if balance < cost:
        print("\n❌ KONFIRMASI: Saldo Qubicoin Kurang! Sistem Menolak Injeksi.")
    else:
        print("\n✅ Saldo cukup, kemungkinan error lain pada logika 'blueprint'.")

if __name__ == "__main__":
    check_registry()
