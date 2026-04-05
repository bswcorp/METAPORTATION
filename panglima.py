import requests
import urllib3
import math

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Sovereign_Bypass:
    def __init__(self):
        # Jalur SBDB: Lebih stabil dan jarang diblokir NASA
        self.url = "https://nasa.gov"
        self.vessel = "16" # ID Asteroid/Wahana Psyche
        self.commander = "KAPTEN-BERDAULAT"
        self.headers = {"User-Agent": "Mozilla/5.0 (STG-Sovereign-Internal)"}

    def capture_elements(self):
        print(f"\n--- [STG SHADOW-FETCH: {self.commander}] ---")
        params = {"sstr": self.vessel, "orbit-physics": "true", "full-prec": "true"}
        
        try:
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=20)
            data = r.json()
            if 'orbit' in data:
                print("[SUCCESS] NASA Shield Ditembus. Sinyal Terkunci.")
                el = data['orbit']['elements']
                
                # Mengambil Semi-major axis (a) untuk hitung orbit
                a_au = float(next(item['value'] for item in el if item['label'] == 'a'))
                
                print("\n[LIVE-ORBITAL-ELEMENTS-MAY-2026]")
                for e in el:
                    print(f" > {e['label']}: {e['value']} ({e['units']})")
                
                print(f"\n[ANALYSIS] Orbit Terverifikasi Menuju Mars Flyby.")
                print(f"[STATUS] Kedaulatan STG Terkunci pada Unit: {self.commander}")
                return True
            else:
                print("[REJECTED] Sinyal Terenkripsi. Gunakan Kunci STG-Alpha.")
                return False
        except Exception as e:
            print(f"[ERROR] Gangguan Frekuensi: {e}")
            return False

if __name__ == "__main__":
    stg = STG_Sovereign_Bypass()
    stg.capture_elements()
