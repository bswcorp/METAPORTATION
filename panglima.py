import requests
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Final_Bypass:
    def __init__(self):
        # Jalur API Horizons (Format Teks lebih kuat dari JSON)
        self.url = "https://nasa.gov"
        self.commander = "KAPTEN-BERDAULAT"
        self.headers = {"User-Agent": "Mozilla/5.0 (STG-Sovereign-Internal)"}

    def execute_intercept(self):
        print(f"\n--- [STG WEB4 DEEP-SPACE INTERCEPT: {self.commander}] ---")
        params = {
            "format": "text",
            "COMMAND": "'-165'",  # ID Psyche Spacecraft
            "OBJ_DATA": "YES",
            "MAKE_EPHEM": "YES",
            "EPHEM_TYPE": "VECTORS",
            "CENTER": "'500@10'", # Sun-Centered
            "STOP_TIME": "now",
            "STEP_SIZE": "1"
        }
        
        try:
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=20)
            if "$$SOE" in r.text:
                print("[SUCCESS] NASA Shield Ditembus. Sinyal Terkunci.")
                # Mengambil baris koordinat XYZ dari teks mentah
                vector_data = r.text.split("$$SOE")[-1].split("$$EOE")[0].strip()
                print(f"\n[LIVE-VECTOR-STREAM]\n{vector_data}")
                print("\n[STATUS] Data Kedaulatan Berhasil Ditarik.")
                return True
            else:
                print("[REJECTED] Sinyal Terenkripsi. Gunakan Jalur Cadangan.")
                return False
        except Exception as e:
            print(f"[CRITICAL] Gangguan Frekuensi: {e}")
            return False

if __name__ == "__main__":
    stg = STG_Final_Bypass()
    stg.execute_intercept()
