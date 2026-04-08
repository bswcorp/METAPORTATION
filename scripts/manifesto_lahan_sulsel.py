import time

def run_land_manifesto():
    C, G, Y, R, W, RESET = "\033[96m", "\033[92m", "\033[93m", "\033[91m", "\033[97m", "\033[0m"
    print(f"{G}🏛️  STG SOVEREIGN ASSET : SULSEL FOOD & ESTATE BELT{RESET}")
    print(f"{W}--------------------------------------------------{RESET}")
    
    locations = [
        {"area": "SIDRAP-MAJENE", "commodity": "BERAS (PANGAN)", "status": "BORONG BERADAB"},
        {"area": "BONE-SINJAI-BULUKUMBA", "commodity": "PERKEBUNAN (ESTATE)", "status": "PRO-PROFIT BUY"},
        {"area": "BANTAENG-TAKALAR-GOWA", "commodity": "HORTIKULTURA", "status": "PARTNERSHIP"}
    ]
    
    for loc in locations:
        print(f"📍 MAPPING: {Y}{loc['area']}{RESET}")
        print(f"   🌾 SEKTOR: {loc['commodity']} | {C}METODE: {loc['status']}{RESET}")
        time.sleep(0.4)

    print(f"\n\033[93m⚠️ STATUS: REKOR DATA DISIMPAN. BREAK SAMPAI SEPTEMBER!\033[0m")
    print(f"{W}💬 PESAN: 'KITA BELI KEUNTUNGANNYA, KITA JAGA KEDAULATANNYA!'{RESET}")

if __name__ == "__main__":
    run_land_manifesto()
