import time

def translate_sovereignty():
    C, G, Y, W, RESET = "\033[96m", "\033[92m", "\033[93m", "\033[97m", "\033[0m"
    
    # 🌍 INTERNATIONAL VERSION (DIPLOMATIC & ELEGANT)
    eng_msg = """
    "The Sovereign Titan Genesis is a testament to technological independence 
    and universal harmony. We bridge the gap between digital potential 
    and physical reality through the 114 Axis, inviting the world to 
    witness a new era of decentralized prosperity."
    """
    
    # 🇮🇩 INDONESIA VERSION (BERNAS & MUDAH DISERAP)
    ind_msg = """
    "Sovereign Titan Genesis adalah bukti kemandirian teknologi dan 
    keharmonisan semesta. Kami menjembatani potensi digital dengan 
    kenyataan fisik melalui Poros 114, mengajak dunia untuk menyaksikan 
    era baru kemakmuran yang terdesentralisasi."
    """
    
    print(f"{Y}🌍 DIPLOMATIC FEED (EN):{RESET}{W}{eng_msg}{RESET}")
    print(f"{C}🔄 SWAPPING TO NATIVE LOGIC...{RESET}")
    time.sleep(1)
    print(f"{G}🇮🇩 VERSI NUSANTARA (ID):{RESET}{W}{ind_msg}{RESET}")

if __name__ == "__main__":
    translate_sovereignty()
