import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Bypass:
    def __init__(self):
        # Jalur Belakang: Small-Body Database API
        self.url = "https://nasa.gov"
        self.vessel = "16" # ID Asteroid/Wahana Psyche
        self.commander = "KAPTEN-BERDAULAT"

    def intercept(self):
        print(f"\n--- [STG SHADOW-FETCH: {self.commander}] ---")
        params = {"sstr": self.vessel, "orbit-physics": "true", "full-prec": "true"}
        
        try:
            r = requests.get(self.url, params=params, verify=False, timeout=15)
            data = r.json()
            if 'orbit' in data:
                print("[SUCCESS] NASA Shield Ditembus. Mengambil Data Vektor...")
                el = data['orbit']['elements']
                # Tampilkan data orbit inti sebagai bukti kedaulatan
                print(f"\n[LIVE-ORBITAL-ELEMENTS]")
                for e in el:
                    print(f" > {e['label']}: {e['value']} ({e['units']})")
                return True
            else:
                print("[REJECTED] Sinyal Terenkripsi. Gunakan Kunci STG-Alpha.")
                return False
        except Exception as e:
            print(f"[ERROR] Gangguan Frekuensi: {e}")
            return False

if __name__ == "__main__":
    stg = STG_Bypass()
    stg.intercept()
