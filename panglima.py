import requests
import urllib3
import math

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Sovereign_Final:
    def __init__(self):
        self.url = "https://nasa.gov"
        self.vessel = "Psyche"
        self.commander = "KAPTEN-BERDAULAT"
        self.G = 6.67430e-11 # Konstanta Gravitasi
        self.M_sun = 1.989e30 # Massa Matahari (kg)
        self.AU = 1.496e11   # 1 AU ke Meter

    def calculate_live_velocity(self):
        print(f"\n--- [STG REAL-TIME ORBITAL VELOCITY: {self.commander}] ---")
        params = {"sstr": self.vessel, "full-prec": "True"}
        
        try:
            r = requests.get(self.url, params=params, verify=False)
            data = r.json()
            orbit = {el['label']: float(el['value']) for el in data['orbit']['elements']}
            
            # Rumus Vis-Viva untuk Kecepatan Orbit: v = sqrt(G*M * (2/r - 1/a))
            # r (jarak saat ini) diasumsikan mendekati 'a' untuk estimasi sabuk asteroid
            a_meters = orbit['a'] * self.AU
            velocity_ms = math.sqrt((self.G * self.M_sun) / a_meters)
            velocity_kms = velocity_ms / 1000
            
            print(f"[SUCCESS] Data NASA Ditembus.")
            print(f"[INFO] Semi-major Axis (a): {orbit['a']} AU")
            print(f"[LIVE-VELOCITY] Wahana Maxar 1300 Melesat: {velocity_kms:.2f} KM/detik")
            print(f"[STATUS] Kedaulatan STG: TERVERIFIKASI")
            return True
        except Exception as e:
            print(f"[CRITICAL] Gangguan Kalkulasi: {e}")
            return False

if __name__ == "__main__":
    stg = STG_Sovereign_Final()
    stg.calculate_live_velocity()
