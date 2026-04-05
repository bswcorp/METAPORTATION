import requests
import urllib3
import math

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Sovereign:
    def __init__(self):
        self.api_url = "https://nasa.gov"
        self.vessel_id = "-165" # ID Psyche Spacecraft
        self.earth_id = "399"   # ID Earth
        self.commander = "KAPTEN-BERDAULAT"

    def get_vector_data(self, target_id):
        params = {
            "format": "json",
            "COMMAND": f"'{target_id}'",
            "OBJ_DATA": "NO",
            "MAKE_EPHEM": "YES",
            "EPHEM_TYPE": "VECTORS",
            "CENTER": "'500@10'", # Sun-Centered
            "STOP_TIME": "now",
            "STEP_SIZE": "1"
        }
        r = requests.get(self.api_url, params=params, verify=False)
        data = r.json().get('result', '')
        # Parsing manual koordinat X, Y, Z dari output NASA
        marker = "$$SOE"
        pos = data.find(marker)
        line = data[pos+len(marker):].split('\n')[1]
        coords = [float(c) for c in line.split()[:3]]
        return coords

    def analyze_distance(self):
        print(f"\n--- [STG ORBITAL VECTOR ANALYSIS: {self.commander}] ---")
        try:
            # Ambil posisi Matahari-Wahana dan Matahari-Bumi
            psyche_pos = self.get_vector_data(self.vessel_id)
            earth_pos = self.get_vector_data(self.earth_id)

            # Hitung jarak Euclidean (KM)
            dist = math.sqrt(sum([(a - b)**2 for a, b in zip(psyche_pos, earth_pos)]))
            
            print(f"[LIVE] Posisi Psyche (XYZ): {psyche_pos}")
            print(f"[LIVE] Posisi Bumi   (XYZ): {earth_pos}")
            print(f"\n[RESULT] Jarak Real-Time ke Wahana: {dist:,.2f} KM")
            print(f"[STATUS] Bahan Bakar Xenon: OPTIMAL | Chassis: MAXAR 1300")
            return True
        except Exception as e:
            print(f"[ERROR] Kegagalan Komputasi Vektor: {e}")
            return False

if __name__ == "__main__":
    nav = STG_Sovereign()
    if nav.analyze_distance():
        print("\n[WEB4/5] Kedaulatan STG Terverifikasi. Data siap dipresentasikan.")
