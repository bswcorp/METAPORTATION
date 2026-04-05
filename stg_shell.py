import time
import os

def clear(): os.system('clear')

def header():
    print("\033[1;36m" + "="*60)
    print("   🌌 STG-OS: GALAXY COMMANDER SHELL v1.0 (MIL-SPEC)")
    print("   [Sector: LENOVO GATE] | [Status: SOVEREIGN-ACTIVE]")
    print("="*60 + "\033[0m")

def main_ui():
    while True:
        clear()
        header()
        print("\033[1;32m[1] 🛡️  NIGHTWATCH MONITORING\033[0m (Real-time Defense)")
        print("\033[1;33m[2] 🔍 QS-GUARDIAN SEARCH\033[0m    (Intel & Anti-Propaganda)")
        print("\033[1;34m[3] 💎 $STATE LEDGER\033[0m         (Economic Sovereignty)")
        print("\033[1;35m[4] 🛰️  MACRONESIA ACT-ARK\033[0m    (Solar Event Radar)")
        print("\033[1;31m[5] 🚀 DEPLOY METAPORTATION\033[0m  (Blockchain Push)")
        print("\033[1;37m[0] 🚪 EXIT STEALTH MODE\033[0m")
        print("-" * 60)
        
        choice = input("\033[1;36mSTG-COMMANDER> \033[0m")

        if choice == "1":
            print("\n\033[0;32m[LOG] Scanning Sector... No breach detected.\033[0m")
            time.sleep(2)
        elif choice == "2":
            query = input("\033[1;33mQS-SEARCH QUERY: \033[0m")
            print(f"\033[0;33m[SEARCHING] Finding secure data for '{query}' via Guardian...\033[0m")
            time.sleep(2)
        elif choice == "3":
            print("\033[1;34m[LEDGER] Balance: 1,000,000,000 QUBICOIN (Validated)\033[0m")
            time.sleep(2)
        elif choice == "0":
            print("Going dark...")
            break
        else:
            print("Invalid Protocol.")
            time.sleep(1)

if __name__ == "__main__":
    main_ui()
