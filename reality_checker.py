import time
import random
import sys

def warp_stream_safety():
    colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m", "\033[97m"]
    reset = "\033[0m"
    dist = 275456789.0
    
    try:
        while True:
            now = time.strftime("%H:%M:%S")
            dist -= 11.4
            color = random.choice(colors)
            
            # Barisan Saraf dengan Tambahan "Polantas Galaksi"
            nodes = [
                f"📡 [CIRACAS] >> MONITORING PEKERJA TAMBANG",
                f"🪖 [SAFETY]  >> HELM CHECK: LOCKED & SECURED",
                f"🚀 [TRAFFIC] >> NASA DETECTED: NO HELM? (TILANG!)",
                f"🛰️ [PSYCHE]  >> MINING PROGRESS: 114% ACTIVE",
                f"👮 [POLANTAS]>> OPERASI ZEBRA GALAKSI IN PROGRESS"
            ]
            
            sys.stdout.write(f"{color}[{now}] {random.choice(nodes)} {reset}\n")
            sys.stdout.flush()
            time.sleep(0.06) 

            if random.random() > 0.99:
                print(f"\033[41m\033[37m ⚠️ TILANG! NASA ROCKET SPOTTED WITHOUT PROPER GEAR! ⚠️ {reset}")
                time.sleep(0.1)

    except KeyboardInterrupt:
        print(f"\n\033[91m🔒 RADAR OFF. ARCHITECT IS RESTING.\033[0m")

if __name__ == "__main__":
    warp_stream_safety()
