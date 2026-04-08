import time
import random
import sys

def run_sovereign_shell():
    colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m", "\033[97m"]
    reset = "\033[0m"
    
    print("\033[95m⚡ STG_SHELL.PY : EXECUTING DRAGON FIELD... 🐉\033[0m")
    
    try:
        while True:
            now = time.strftime("%H:%M:%S")
            color = random.choice(colors)
            
            logs = [
                f"📳 [METANESIA-ARK] >> VETO_READY",
                f"⛏️ [VOL-555-MINING] >> EXTRACTING_GALAXY_EQUITY",
                f"🧬 [BIOMETRIC-ECG] >> SIGNAL_LOCKED_ANDI_M_H",
                f"📡 [ZURICH-HUB]    >> INBOUND_GOLD_TRACKED",
                f"🌀 [METAPORTATION] >> FOLDING_SPACE_TIME_0.0ms"
            ]
            
            sys.stdout.write(f"{color}[{now}] {random.choice(logs)} {reset}\n")
            sys.stdout.flush()
            time.sleep(0.06) # Running secepat kilat!

    except KeyboardInterrupt:
        print(f"\n\033[91m🔒 SHELL CLOSED. ARCHITECT IS IN CONTROL.\033[0m")

if __name__ == "__main__":
    run_sovereign_shell()
