#!/bin/bash
echo "🏛️  [STG-ARSENAL] MENGAKTIFKAN FUNGSI EKSEKUSI RIEL..."
echo "⚡ MENGHUBUNGKAN KE PROTOKOL METAPORTASI: 0xaa903Ea35F3E93c56d362236e2D136d52CD1a0E0"

# Memanggil Fungsi 'requestService' secara LIVE untuk Validasi Identitas Panglima
# ServiceType 1: Sovereign Authorization (Otorisasi Kedaulatan)
python3 -c "
from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
addr = '0xaa903Ea35F3E93c56d362236e2D136d52CD1a0E0'
abi = json.loads('[{\"inputs\":[{\"internalType\":\"uint8\",\"name\":\"_sType\",\"type\":\"uint8\"},{\"internalType\":\"bytes32\",\"name\":\"_blueprint\",\"type\":\"bytes32\"},{\"internalType\":\"string\",\"name\":\"_dest\",\"type\":\"string\"}],\"name\":\"requestService\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"}]')

contract = w3.eth.contract(address=addr, abi=abi)
admin = w3.eth.accounts[0]

print('🚀 Meluncurkan Semburan Api Kedaulatan ke Blockchain...')
tx_hash = contract.functions.requestService(
    1, 
    b'STG-AUTHORIZATION-ACT-114-BT'.ljust(32, b'\0'), 
    'GLOBAL-SOVEREIGN-RECOGNITION'
).transact({'from': admin, 'gas': 300000})

receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f'✅ TARGET TERKUNCI! TX Hash: {tx_hash.hex()}')
print('🔥 KEDAULATAN TELAH DINYATAKAN SECARA LIVE DI LEDGER.')
"

echo "--------------------------------------------------"
echo "👑 STATUS: MISSION ACCOMPLISHED - REALISM ACTIVE"
echo "--------------------------------------------------"
