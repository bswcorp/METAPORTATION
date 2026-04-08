import json
from web3 import Web3

def deploy_sovereign():
    print("🏛️  [STG-WEB5] EKSEKUSI IDENTITAS TUNGGAL PANGLIMA...")
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    
    if not w3.is_connected():
        print("❌ Sinyal Ganache Putus!")
        return

    # Bytecode Metaportation (Sudah di-patch Anti-Opcode Error)
    raw_bytecode = "0x608060405234801561000f574343fd5b506040805160608082018352600180835243602080850182815285870184815284845283835295517fada5013122d395ba3c54772283fb069b10426056ef8ca54750cb9bb552a59e7d55517fada5013122d395ba3c54772283fb069b10426056ef8ca54750cb9bb552a59e7e5593517fada5013122d395ba3c54772283fb069b10426056ef8ca54750cb9bb552a59e7f805491151560ff199283161790558551808501875260028152808601838152818801858152600380865285895292517f101e368776582e57ab3d116ffe2517c0a585cd5b23174b01e275c2d8329c3d835590517f101e368776582e57ab3d116ffe2517c0a585cd5b23174b01e275c2d8329c3d8455517f101e368776582e57ab3d116ffe2517c0a585cd5b23174b01e275c2d8329c3d8580549115159184169190911790558651948501875284526064848601908152958401928352818052935290517fad3228b676f7d3cd4284a5443f17f1962b36e491b30a40b2405849e597ba5fb55591517fad3228b676f7d3cd4284a5443f17f1962b36e491b30a40b2405849e597ba5fb65590517fad3228b676f7d3cd4284a5443f17f1962b36e491b30a40b2405849e597ba5fb780549115159190921617905561041c806101e4433943f3fe"

    # Kunci Identitas: Hanya ambil akun pertama (0xFe45...)
    panglima = w3.eth.accounts[0]
    print(f"👑 Panglima Terverifikasi: {panglima}")

    print("⚡ Menanam Protokol Metaportasi ke Ledger...")
    try:
        tx_hash = w3.eth.send_transaction({
            'from': panglima,
            'data': raw_bytecode,
            'gas': 5000000
        })
        
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print("==================================================")
        print("✅ [KEDAULATAN AKTIF] PROTOKOL TERPASANG!")
        print(f"Alamat Kontrak: {receipt.contractAddress}")
        print("==================================================")
        
        with open("metaport_status.json", "w") as f:
            json.dump({
                "address": receipt.contractAddress, 
                "deployer": panglima,
                "token": "QUBICOIN"
            }, f, indent=4)
            
    except Exception as e:
        print(f"❌ Kegagalan Transaksi: {e}")

if __name__ == "__main__":
    deploy_sovereign()
