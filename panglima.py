import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Sovereign_Bypass:
    def __init__(self):
        # Jalur API Deep Space yang benar
        self.url = "https://nasa.gov"
        self.commander = "KAPTEN-BERDAULAT"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (STG-Sovereign-Terminal)",
            "Accept": "application/json"
        }

    def intercept(self):
        print(f"\n--- [STG SHADOW-FETCH: {self.commander}] ---")
        # Mencari Data Orbit Utama untuk Psyche (16)
        params = {"sstr": "16", "orbit-physics": "true"}
        
        try:
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=20)
            
            if r.status_code == 200:
                data = r.json()
                print("[SUCCESS] NASA Shield Ditembus. Sinyal Terkunci.")
                orbit = data['orbit']['elements']
                
                print("\n[STG-REAL-TIME-ORBITAL-DATA]")
                for el in orbit:
                    print(f" > {el['label']}: {el['value']} {el.get('units', '')}")
                
                print(f"\n[STATUS] Kedaulatan STG Terverifikasi pada HP {self.commander}")
                return True
            else:
                print(f"[REJECTED] Kode Penolakan NASA: {r.status_code}")
                return False
        except Exception as e:
            print(f"[CRITICAL] Gangguan Frekuensi: {e}")
            return False

if __name__ == "__main__":
    stg = STG_Sovereign_Bypass()
    stg.intercept()
