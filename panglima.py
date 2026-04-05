import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Shadow_Fetch:
    def __init__(self):
        # Jalur API Small-Body Database - Lebih Ringan & Stabil
        self.url = "https://nasa.gov"
        self.vessel = "16" # ID Asteroid/Wahana Psyche
        self.commander = "KAPTEN-BERDAULAT"
        self.headers = {"User-Agent": "Mozilla/5.0 (STG-Sovereign-Internal)"}

    def intercept(self):
        print(f"\n--- [STG SHADOW-FETCH: {self.commander}] ---")
        params = {"sstr": self.vessel, "orbit-physics": "true", "full-prec": "true"}
        
        try:
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=15)
            data = r.json()
            if 'orbit' in data:
                print("[SUCCESS] NASA Shield Ditembus. Sinyal Terkunci.")
                el = data['orbit']['elements']
                print("\n[STG-REAL-TIME-ORBITAL-DATA]")
                # Menampilkan Elemen Keplerian (DNA Orbit)
                for e in el:
                    print(f" > {e['label']}: {e['value']} ({e['units']})")
                return True
            else:
                print("[REJECTED] Sinyal Terenkripsi. Jalur DSN Padat.")
                return False
        except Exception as e:
            print(f"[ERROR] Gangguan Frekuensi: {e}")
            return False

if __name__ == "__main__":
    stg = STG_Shadow_Fetch()
    stg.intercept()
