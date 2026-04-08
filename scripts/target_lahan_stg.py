import time

def lock_sovereign_land():
    C, G, Y, R, W, RESET = "\033[96m", "\033[92m", "\033[93m", "\033[91m", "\033[97m", "\033[0m"
    print(f"{C}🏛️  STG LAND ACQUISITION : TRIANGLE OF POWER (MAROS-PANGKEP-BARRU){RESET}")
    print(f"{W}--------------------------------------------------{RESET}")
    
    targets = [
        {"kab": "MAROS", "spec": "GRANITIC FOUNDATION", "unit": "DATA_CENTER_CORE"},
        {"kab": "PANGKEP", "spec": "KARST STABILITY", "unit": "SPACE_DRONE_BASE"},
        {"kab": "BARRU", "spec": "DEEP SEA PORT ACCESS", "unit": "LOGISTIC_GATEWAY"}
    ]
    
    for t in targets:
        print(f"📍 TARGETING: {Y}{t['kab']}{RESET}")
        print(f"   🏗️  SPEC: {t['spec']} | {G}FUTURE: {t['unit']}{RESET}")
        time.sleep(0.5)

    print(f"\n{R}[!] STATUS: COORDINATES SAVED IN BANK STG (008).{RESET}")
    print(f"{W}💬 PESAN: 'MOBILITAS KERETA SIAP, DANA TINGGAL INJECT!'{RESET}")
    print(f"{W}--------------------------------------------------{RESET}")

if __name__ == "__main__":
    lock_sovereign_land()
