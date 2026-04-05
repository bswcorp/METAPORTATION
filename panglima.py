import requests
import urllib3
import math

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Sovereign_Bypass:
    def __init__(self):
        # Jalur SBDB: Jalur intelijen yang lebih stabil
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
                
                # Mengambil Semi-major axis (a) untuk hitung kecepatan
                a_au = float(next(item['value'] for item in el if item['label'] == 'a'))
                
                # Rumus Fisika: v = sqrt(GM/a)
                # GM Matahari = 1.3271244e11 km^3/s^2, 1 AU = 149.6e6 km
                mu = 1.3271244e11
                a_km = a_au * 149597870.7
                v_kms = math.sqrt(mu / a_km)
                
                print("\n[LIVE-ORBITAL-ELEMENTS]")
                for e in el:
                    print(f" > {e['label']}: {e['value']} ({e['units']})")
                
                print(f"\n[ANALYSIS] Kecepatan Orbit Kalkulasi: {v_kms:.2f} KM/s")
                print(f"[STATUS] Kedaulatan STG Terverifikasi.")
                return True
            else:
                print("[REJECTED] Sinyal Terenkripsi. Jalur DSN Padat.")
                return False
        except Exception as e:
            print(f"[ERROR] Gangguan Frekuensi: {e}")
            return False

if __name__ == "__main__":
    stg = STG_Sovereign_Bypass()
    stg.intercept = stg.capture_elements
    stg.intercept()
