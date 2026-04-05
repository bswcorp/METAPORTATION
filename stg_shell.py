import time
import os
import subprocess

def clear(): os.system('clear')

def header():
    print("\033[1;32m") 
    print(r"""
    ███████╗████████╗ ██████╗ 
    ██╔════╝╚══██╔══╝██╔════╝ 
    ███████╗   ██║   ██║  ███╗
    ╚════██║   ██║   ██║   ██║
    ███████║   ██║   ╚██████╔╝
    ╚══════╝   ╚═╝    ╚═════╝ 
    SOVEREIGN TITAN GENESIS v1.0
    [MILITARY-GRADE-GALAXY]
    """)
    print("\033[1;36m" + "="*60)
    print("   [Sector: LENOVO GATE] | [Status: SOVEREIGN-ACTIVE]")
    print("="*60 + "\033[0m")

def main_ui():
    while True:
        clear()
        header()
        print("\033[1;32m [1] ACTIVATE NIGHTWATCH\033[0m    (New: ultimatum.py)")
        print("\033[1;33m [2] PANGLIMA PROTOCOL\033[0m     (Legacy: panglima.py)")
        print("\033[1;34m [3] CORE NIGHTWATCH SH\033[0m    (Legacy: .sh Script)")
        print("\033[1;35m [4] QS-GUARDIAN SEARCH\033[0m     (Intel Search)")
        print("\033[1;31m [5] CHECK $STATE BALANCE\033[0m   (Blockchain)")
        print("\033[1;37m [0] EXIT STEALTH MODE\033[0m")
        print("-" * 60)
        
        try:
            choice = input("\033[1;36mSTG-COMMANDER> \033[0m")
            if choice == "1":
                subprocess.run(["python3", "ultimatum.py"])
            elif choice == "2":
                print("\033[1;33m[SYSTEM] Memanggil Protokol PANGLIMA...\033[0m")
                time.sleep(1)
                subprocess.run(["python3", "panglima.py"])
            elif choice == "3":
                print("\033[1;34m[SYSTEM] Menjalankan Shell Nightwatch...\033[0m")
                time.sleep(1)
                subprocess.run(["bash", "STG-CORE-NIGHTWATCH.sh"])
            elif choice == "4":
                query = input("\033[1;33mQS-SEARCH QUERY: \033[0m")
                print(f"\033[0;33m[SEARCHING] Connecting to Guardian Nodes for '{query}'...\033[0m")
                time.sleep(2)
            elif choice == "5":
                print("\033[1;31m[LEDGER] Verified Balance: 1.000.000.000 $STATE\033[0m")
                time.sleep(2)
            elif choice == "0":
                print("Going dark...")
                break
        except KeyboardInterrupt:
            print("\nReturning to Base...")
            break

if __name__ == "__main__":
    main_ui()

