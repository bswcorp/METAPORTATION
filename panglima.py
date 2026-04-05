import requests
import urllib3
from datetime import datetime, timedelta

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Sovereign_Vektor:
    def __init__(self):
        self.url = "https://nasa.gov"
        self.commander = "KAPTEN-BERDAULAT"
        self.headers = {"User-Agent": "STG-Command-Center/1.0"}

    def capture_vectors(self):
        print(f"\n--- [STG VECTOR INTERCEPT: {self.commander}] ---")
        
        # Mengatur jendela waktu 10 menit yang lalu agar bypass filter 'now'
        past_time = (datetime.utcnow() - timedelta(minutes=10)).strftime('%Y-%m-%d %H:%M')
        end_time = (datetime.utcnow() - timedelta(minutes=9)).strftime('%Y-%m-%d %H:%M')
        
        params = {
            "format": "text",
            "COMMAND": "'-165'",  # ID Pesawat Psyche
            "OBJ_DATA": "NO",
            "MAKE_EPHEM": "YES",
            "EPHEM_TYPE": "VECTORS",
            "CENTER": "'500@10'", # Pusat Matahari
            "START_TIME": past_time,
            "STOP_TIME": end_time,
            "STEP_SIZE": "1m"
        }
        
        try:
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=25)
            if "$$SOE" in r.text:
                print("[SUCCESS] Handshake Berhasil. Sinyal Vektor Terkunci!")
                # Ambil data koordinat XYZ di antara marker SOE dan EOE
                vector_data = r.text.split("$$SOE")[-1].split("$$EOE").strip()
                print(f"\n[LIVE-VECTOR-STREAM]\n{vector_data}")
                return True
            else:
                print("[REJECTED] NASA Shield Masih Aktif. Gunakan Cadangan SBDB.")
                return False
        except Exception as e:
            print(f"[ERROR] Gangguan Frekuensi: {e}")
            return False

if __name__ == "__main__":
    nav = STG_Sovereign_Vektor()
    nav.capture_vectors()
