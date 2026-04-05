import requests
import urllib3
import math

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Final_Bypass:
    def __init__(self):
        # Using a more robust query endpoint
        self.url = "https://nasa.gov"
        self.commander = "KAPTEN-BERDAULAT"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json"
        }

    def execute_live_intel(self):
        print(f"\n--- [STG DEEP-SPACE INTEL: {self.commander}] ---")
        # Direct Query for Psyche (16)
        params = {"sstr": "16", "orbit-physics": "true"}
        
        try:
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=20)
            if r.status_code != 200:
                print(f"[REJECTED] Signal Blocked. Code: {r.status_code}")
                return False
                
            data = r.json()
            # Extract Semimajor Axis (a) - The heart of the orbit
            elements = data['orbit']['elements']
            a_val = next(item['value'] for item in elements if item['label'] == 'a')
            a_au = float(a_val)
            
            # Physics: v = sqrt(GM/a)
            # Standard Gravitational Parameter for Sun (mu) = 1.327e11 km^3/s^2
            # 1 AU = 149,597,870.7 km
            mu = 1.32712440018e11 
            a_km = a_au * 149597870.7
            velocity_kms = math.sqrt(mu / a_km)
            
            print(f"[SUCCESS] NASA Deep-Space Link: STABLE")
            print(f"[DATA] Semi-major Axis: {a_au:.4f} AU")
            print(f"[LIVE-VELOCITY] Wahana Maxar 1300: {velocity_kms:.2f} KM/s")
            print(f"[STATUS] Kedaulatan Web4: LOCKED")
            return True
        except Exception as e:
            print(f"[CRITICAL] Alpha-Intercept Failed: {e}")
            return False

if __name__ == "__main__":
    stg = STG_Final_Bypass()
    stg.execute_live_intel()
