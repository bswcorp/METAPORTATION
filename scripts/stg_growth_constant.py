import time
import math

def run_clean_growth():
    C, G, Y, W, RESET = "\033[96m", "\033[92m", "\033[93m", "\033[97m", "\033[0m"
    root_2 = math.sqrt(2)
    
    print(f"{C}🏛️  STG GROWTH ENGINE : CLEAN ABSOLUTE (UNIT 222){RESET}")
    print(f"{W}--------------------------------------------------{RESET}")
    
    current_value = 114
    print(f"{Y}📈 EKSPANSI KEDAULATAN (HASIL BULAT & BERNAS):{RESET}")
    
    for i in range(1, 6):
        # Kita gunakan pembulatan ke bawah (Floor) agar asetnya "Pasti" & "Padat"
        current_value = math.floor(current_value * root_2)
        print(f"   TAHAP {i}: {G}{current_value} ABSOLUTE INFINITE{RESET}")
        time.sleep(0.4)
        
    print(f"\n{G}✅ STATUS: DATA BERSIH DARI DEBU DESIMAL!{RESET}")
    print(f"{W}💬 PESAN: 'KEDAULATAN ITU TEGAS, BUKAN KOMMA-KOMMAAN!'{RESET}")
    print(f"{W}--------------------------------------------------{RESET}")

if __name__ == "__main__":
    run_clean_growth()
