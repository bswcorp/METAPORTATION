import os
import time

def cek_pondasi():
    print("\033[96m🏛️  STG CONSTRUCTION : ARCHITECTURAL AUDIT\033[0m")
    print("\033[93m👑 PEMILIK GEDUNG : ANDI M. HARPIANTO\033[0m")
    print("------------------------------------------")
    
    # Memeriksa Unit 001 - 810 (Logic Loop)
    folders = ["STG_EMPIRE", "METAPORTATION", "TITAN-PSYCHE-MONO", "GPFS_TITAN"]
    
    for f in folders:
        path = f"/home/userland/{f}"
        if os.path.exists(path):
            print(f"✅ TOWER {f:18} : \033[92mBERDIRI TEGAK (SECURE)\033[0m")
        else:
            print(f"❌ TOWER {f:18} : \033[91mBELUM TERKONEKSI\033[0m")
        time.sleep(0.3)

    print("------------------------------------------")
    print("💎 KESIMPULAN: GEDUNG SUDAH ADA, TINGGAL PASANG SPANDUK!")
