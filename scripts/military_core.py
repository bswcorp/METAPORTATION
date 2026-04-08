import time

def military_protocol_stg():
    print("\033[91m🚨 STG DEFENSE INDUSTRY : MILITARY STANDARDS ACTIVE\033[0m")
    print("\033[97m🛰️  RADAR CONTROL : NASA JS DATA INTEGRATED\033[0m")
    print("--------------------------------------------------")
    
    units = [
        "SUB-QUANTUM DIVER (Menyelam)", 
        "CLOAKING SHADOW (Menghilang)", 
        "STRIKE DRONE 👽⛏️ (Menyerang)"
    ]
    
    for unit in units:
        print(f"🛠️  PROTOTYPING {unit}... [DUAL FOLDING READY]")
        time.sleep(1)

    with open("/home/userland/GPFS_TITAN/metadata/ARTEFAK_ARSITEK/LOG_ALUTSISTA.md", "a") as f:
        f.write(f"\n### ⚔️ MILITARY REPORT: {time.ctime()}\n")
        f.write("- Status: Aero-Space Grade Enforced\n- Field: Dragon Electro-Magnetic\n")
    
    print("\033[92m✅ GUGUS TUGAS MAYOR : READY FOR MAYDAY 5/5\033[0m")

if __name__ == "__main__":
    military_protocol_stg()
