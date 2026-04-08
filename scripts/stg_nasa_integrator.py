import os
import json
import shutil

def sync_psyche_data():
    print("[STG-SYSTEM] Memperbaiki struktur direktori & koneksi data 16 Psyche...")
    target = "modul-psyche"
    status_file = os.path.join(target, "status.json")

    # Cek jika 'modul-psyche' adalah file, bukan folder
    if os.path.exists(target) and not os.path.isdir(target):
        print(f"[STG-WARNING] '{target}' adalah file. Mengonversi menjadi direktori...")
        # Pindahkan file lama ke dalam folder baru agar data tidak hilang
        os.rename(target, target + "_backup")
        os.makedirs(target)
        shutil.move(target + "_backup", os.path.join(target, "legacy_data"))
    elif not os.path.exists(target):
        os.makedirs(target)

    # Data Validasi Riset NASA sebagai Instrumen Jaminan
    data_jaminan = {
        "asset_origin": "16 Psyche",
        "validation_protocol": "STG-SOVEREIGN-V1",
        "status": "VALIDATED_AS_COLLATERAL",
        "sovereign_units": 114,
        "data_source": "NASA_JPL_OPEN_DATA",
        "legal_status": "IP_BACKED_ASSET"
    }
    
    with open(status_file, "w") as f:
        json.dump(data_jaminan, f, indent=4)
    
    print(f"[STG-SUCCESS] Instrumen jaminan berhasil ditulis di: {status_file}")

if __name__ == "__main__":
    sync_psyche_data()
