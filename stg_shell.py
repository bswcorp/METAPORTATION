import time
import os
import subprocess

def clear(): os.system('clear')

def header():
    print("\033[1;36m" + "="*60)
    print("   🌌 STG-OS: GALAXY COMMANDER SHELL v1.0 (MIL-SPEC)")
    print("   [Sector: LENOVO GATE] | [Status: SOVEREIGN-ACTIVE]")
    print("="*60 + "\033[0m")

def run_ultimatum():
    print("\n\033[1;32m[SYSTEM] Memulai Protokol NIGHTWATCH via ultimatum.py...\033[0m")
    time.sleep(1)
    try:
        # Menjalankan ultimatum.py sebagai proses terpisah
        subprocess.run(["python3", "ultimatum.py"])
    except Exception as e:
        print(f"\033[1;31m[ERROR] Gagal memanggil ultimatum.py: {e}\033[0m")
        time.sleep(2)

def main_ui():
    while True:
        clear()
        header()
        print("\033[1;32m [1] ACTIVATE NIGHTWATCH\033[0m    (Run ultimatum.py)")
        print("\033[1;33m [2] QS-GUARDIAN SEARCH\033[0m     (Intel Search)")
        print("\033[1;34m [3] CHECK $STATE BALANCE\033[0m   (Blockchain Ledger)")
        print("\033[1;35m [4] ACT-ARK RADAR\033[0m          (Solar Event)")
        print("\033[1;37m [0] EXIT STEALTH MODE\033[0m")
        print("-" * 60)
        
        choice = input("\033[1;36mSTG-COMMANDER> \033[0m")

        if choice == "1":
            run_ultimatum()
        elif choice == "2":
            query = input("\033[1;33mQS-SEARCH QUERY: \033[0m")
            print(f"\033[0;33m[SEARCHING] Accessing Guardian Nodes for '{query}'...\033[0m")
            time.sleep(2)
        elif choice == "3":
            print("\033[1;34m[LEDGER] Verified Balance: 1.000.000.000 $STATE\033[0m")
            time.sleep(2)
        elif choice == "0":
            print("Going dark...")
            break
        else:
            print("Invalid Protocol.")
            time.sleep(1)

if __name__ == "__main__":
    main_ui()

