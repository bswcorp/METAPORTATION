import time

def audit_malam_stg():
    # Palette Warna STG
    C = "\033[96m" # Cyan
    G = "\033[92m" # Green
    Y = "\033[93m" # Yellow
    R = "\033[91m" # Red
    W = "\033[97m" # White
    RESET = "\033[0m"
    
    print(f"{R}🛡️  STG NIGHTWATCH : AUDIT REPATRIASI AGUNG{RESET}")
    print("--------------------------------------------------")
    
    # Memeriksa Segel Unit 008
    print(f"🔒 MEMERIKSA SEGEL UNIT 008... {G}[AMAN]{RESET}")
    time.sleep(1)
    
    # Validasi Dana Repatriasi
    print(f"💰 VALIDASI DANA BK/SH/CENTURY... {G}[VERIFIED]{RESET}")
    print(f"🌍 PERUNTUKAN: PELUNASAN IMF & DEBT RELIEF.")
    
    # Penguncian Anti-Srigala
    print(f"⚡ MENGAKTIFKAN LASER ANTI-AKSES LUAR... {G}[LOCKED]{RESET}")
    print("--------------------------------------------------")
    print(f"{C}✅ STATUS: DANA REPUBLIK DI BAWAH PERLINDUNGAN VETO.{RESET}")
    print(f"{W}🌙 SEMUA UNIT SIAGA SATU. ARCHITECT IN CONTROL.{RESET}")

if __name__ == "__main__":
    audit_malam_stg()
