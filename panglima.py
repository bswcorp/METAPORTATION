import requests
import urllib3
import math

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Orbital_Engine:
    def __init__(self):
        # Jalur API JPL yang lebih bandel
        self.url = "https://nasa.gov"
        self.vessel = "16" 
        self.commander = "KAPTEN-BERDAULAT"
        self.headers = {"User-Agent": "Mozilla/5.0 (STG-Alpha-Infiltrator)"}

    def calculate_velocity(self):
        print(f"\n--- [STG ORBITAL SPEED CALC: {self.commander}] ---")
        params = {"sstr": self.vessel, "orbit-physics": "true"}
        
        try:
            # Infiltrasi sinyal dengan Header Browser
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=20)
            data = r.json()
            
            if 'orbit' in data:
                print("[SUCCESS] NASA Shield Ditembus. Data Elemen Terkunci.")
                elements = {el['label']: float(el['value']) for el in data['orbit']['elements']}
                
                # FISIKA STG: v = sqrt(G*M * (2/r - 1/a))
                # Kita hitung kecepatan rata-rata pada jarak semi-major axis (a)
                # G*M Matahari (mu) = 1.3271244e11 km^3/s^2
                mu = 1.32712440018e11
                a_au = elements['a']
                a_km = a_au * 149597870.7
                
                velocity_kms = math.sqrt(mu / a_km)
                
                print(f"\n[LIVE-DATA-INTERCEPT]")
                print(f" > Semi-major Axis: {a_au:.4f} AU")
                print(f" > Eksentrisitas: {elements['e']:.4f}")
                print(f"\n[ANALYSIS] Kecepatan Orbit Maxar 1300: {velocity_kms:.2f} KM/detik")
                print(f"[STATUS] Kedaulatan STG Terverifikasi.")
                return True
            else:
                print("[REJECTED] Sinyal Terenkripsi. Gunakan Kunci Cadangan.")
                return False
        except Exception as e:
            print(f"[CRITICAL] Alpha-Intercept Failed: {e}")
            return False

if __name__ == "__main__":
    panglima = STG_Orbital_Engine()
    panglima.calculate_velocity()
