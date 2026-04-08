import json
from web3 import Web3

def inspect_sovereign():
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    
    # Ambil alamat dari file status jika ada
    try:
        with open("last_deploy_status.json", "r") as f:
            status = json.load(f)
            address = status["address"]
    except:
        print("❌ Data deployment tidak ditemukan. Masukkan alamat manual!")
        return

    print(f"📡 Menginspeksi Kontrak di: {address}")
    
    # Cek apakah ada kode di alamat tersebut
    code = w3.eth.get_code(address)
    if code.hex() == '0x':
        print("❌ Alamat kosong! Kontrak mungkin belum benar-benar mendarat.")
    else:
        print("✅ KONTRAK AKTIF: Kode kedaulatan terdeteksi dan terkunci.")
        print(f"Biner Kontrak (Preview): {code.hex()[:64]}...")

if __name__ == "__main__":
    inspect_sovereign()
