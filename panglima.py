import requests
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Sovereign:
    def __init__(self):
        # Endpoint API resmi NASA JPL
        self.url = "https://nasa.gov"
        self.commander = "KAPTEN-BERDAULAT"
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def capture_psyche_data(self):
        print(f"\n--- [STG DEEP-SPACE INTERCEPT: {self.commander}] ---")
        # Parameter Vektor Posisi dan Kecepatan
        params = {
            "format": "text",
            "COMMAND": "'-165'",
            "OBJ_DATA": "YES",
            "MAKE_EPHEM": "YES",
            "EPHEM_TYPE": "VECTORS",
            "CENTER": "'500@10'",
            "STOP_TIME": "now",
            "STEP_SIZE": "1"
        }
        try:
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=20)
            if "$$SOE" in r.text:
                print("[SUCCESS] Sinyal Terkunci pada Wahana Maxar 1300.")
                # Mengambil baris koordinat XYZ
                vector = r.text.split("$$SOE")[1].split("$$EOE")[0].strip()
                print(f"\n[VECTOR-STREAM]\n{vector}")
                return True
            else:
                print("[REJECTED] NASA Shield Aktif. Gunakan protokol alternatif.")
                return False
        except Exception as e:
            print(f"[ERROR] Gangguan Frekuensi: {e}")
            return False

if __name__ == "__main__":
    stg = STG_Sovereign()
    stg.capture_psyche_data()
