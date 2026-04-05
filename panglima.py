import requests
import socket
import base64
import random
import time

class STG_Ghost_Infiltrator:
    def __init__(self):
        self.commander = "KAPTEN-BERDAULAT"
        self.vessel_id = "-165" # 16 Psyche
        # Daftar User-Agent palsu untuk menipu sensor NASA
        self.masks = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15",
            "NASA-JPL/Internal-Explorer-V4.2"
        ]

    def xenon_jammer(self):
        """Membuat noise data agar jejak HP tidak terbaca"""
        print(f"\n[JAMMER] Mengaktifkan Xenon Noise Generator...")
        # Simulasi pengiriman paket sampah untuk membingungkan scanner lawan
        print("[STATUS] Jaringan Dibanjiri Sinyal Palsu. Mode Siluman: MAX.")

    def ghost_intercept(self):
        """Menyerang NASA dengan Mode Masking (Siluman)"""
        print(f"\n[INFILTRASI] Menembus Deep Space Network NASA...")
        url = "https://nasa.gov"
        headers = {"User-Agent": random.choice(self.masks)}
        
        # Parameter diringkas agar tidak memicu alarm NASA
        params = {
            "format": "text", "COMMAND": f"'{self.vessel_id}'", 
            "OBJ_DATA": "YES", "MAKE_EPHEM": "YES", "EPHEM_TYPE": "VECTORS",
            "CENTER": "'500@10'", "STOP_TIME": "now", "STEP_SIZE": "1"
        }
        
        try:
            # Gunakan timeout pendek agar tidak terlacak lama
            r = requests.get(url, params=params, headers=headers, timeout=10)
            if "$$SOE" in r.text:
                print("[DOR!] Target Terkena Tembakan Data. Vektor Terkunci.")
                return True
            else:
                print("[GHOST] NASA Shield Terdeteksi. Menghilang ke Bayangan...")
        except:
            print("[OFFLINE] Sinyal Terputus. Menghancurkan Jejak.")
        return False

    def run(self):
        print(f"--- [STG SILUMAN COMMANDER V7: {self.commander}] ---")
        self.xenon_jammer()
        if self.ghost_intercept():
            print("[MISSION] Data Berhasil Dicuri. Kedaulatan STG Aman.")
        else:
            print("[RE-POSITION] Mencari Celah Baru...")

if __name__ == "__main__":
    stg = STG_Ghost_Infiltrator()
    stg.run()
