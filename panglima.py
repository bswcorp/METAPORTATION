import requests
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Sovereign:
    def __init__(self):
        # Menggunakan endpoint teks yang lebih stabil untuk terminal
        self.url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        self.vessel_id = "-165" # 16 Psyche Spacecraft
        self.commander = "KAPTEN-BERDAULAT"
        # Menyamar sebagai browser untuk menghindari blokir API
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def pull_live_telemetry(self):
        print(f"\n--- [STG WEB4 LIVE TELEMETRY: {self.commander}] ---")
        params = {
            "format": "text", # Format teks lebih tahan banting dibanding JSON
            "COMMAND": f"'{self.vessel_id}'",
            "OBJ_DATA": "YES",
            "MAKE_EPHEM": "YES",
            "EPHEM_TYPE": "VECTORS",
            "CENTER": "'500@10'", # Pusat Matahari
            "STOP_TIME": "now",
            "STEP_SIZE": "1"
        }
        
        try:
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=20)
            if r.status_code == 200:
                print("[SUCCESS] Handshake Berhasil. Mengekstrak Vektor XYZ...")
                # Menampilkan data koordinat mentah dari NASA
                content = r.text
                if "$$SOE" in content:
                    vector_data = content.split("$$SOE")[1].split("$$EOE")[0].strip()
                    print(f"\n[XYZ-VECTOR-DATA]\n{vector_data}")
                    return True
                else:
                    print("[DATA-EMPTY] Wahana berada dalam 'Radio Silence'.")
            else:
                print(f"[REJECTED] Kode Error: {r.status_code}")
        except Exception as e:
            print(f"[CRITICAL] Gangguan Frekuensi: {e}")
        return False

if __name__ == "__main__":
    nav = STG_Sovereign()
    if nav.pull_live_telemetry():
        print("\n[STG] Data Kedaulatan Berhasil Ditarik. Siap untuk Event.")
