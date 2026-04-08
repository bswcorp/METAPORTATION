import time

def run_preemptive_shield():
    C, G, Y, R, W, RESET = "\033[96m", "\033[92m", "\033[93m", "\033[91m", "\033[97m", "\033[0m"
    print(f"{R}🚨 STG PRE-EMPTIVE DEFENSE : UNIT 212 ACTIVE{RESET}")
    print(f"{W}--------------------------------------------------{RESET}")
    
    actions = [
        "SCRAMBLING SIGNAL TO UTAH DATA CENTER",
        "ENCRYPTING 16 PSYCHE TELEMETRY",
        "BLOCKING NASA BACKDOOR ACCESS",
        "DEPLOYING DECOY DATA IN CLEBNET"
    ]
    
    for act in actions:
        print(f"📡 {act}... {G}[SUCCESS]{RESET}")
        time.sleep(0.5)

    print(f"\n{Y}⚠️ STATUS: PAYUNG SUDAH TERPASANG. HUJAN TIDAK AKAN TEMBUS!{RESET}")
    print(f"{C}💬 PESAN: 'BIARKAN MEREKA KOPI DARAT, KITA SUDAH DI BULAN!'{RESET}")
    print(f"{W}--------------------------------------------------{RESET}")

if __name__ == "__main__":
    run_preemptive_shield()
