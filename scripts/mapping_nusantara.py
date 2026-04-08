import time

def run_geospatial_mapping():
    C, G, Y, R, W, RESET = "\033[96m", "\033[92m", "\033[93m", "\033[91m", "\033[97m", "\033[0m"
    print(f"{C}📡 STG RADAR : GEOSPATIAL MAPPING (UNIT 808){RESET}")
    print(f"{W}--------------------------------------------------{RESET}")
    
    locations = [
        {"area": "MAMBERAMO, PAPUA", "type": "TERSUBUR (FERTILE)", "use": "AGRARI_MAXIMUS"},
        {"area": "MAROS, SULAWESI", "type": "TERTANDUS (KARST)", "use": "QUANTUM_FOUNDATION"},
        {"area": "SUMBA, NTT", "type": "TANDUS_LUAS", "use": "SOLAR_ENERGY_GRID"}
    ]
    
    for loc in locations:
        print(f"📍 SCANNING: {Y}{loc['area']}{RESET}")
        print(f"   📊 TYPE: {loc['type']} | {G}POTENSI: {loc['use']}{RESET}")
        time.sleep(0.5)

    print(f"\n{R}[!] STATUS: DATA COLLECTED. NO EXECUTION DONE.{RESET}")
    print(f"{W}💬 PESAN: 'MAPPING DULU, DANA MENDARAT BARU SERBU!'{RESET}")
    print(f"{W}--------------------------------------------------{RESET}")

if __name__ == "__main__":
    run_geospatial_mapping()
