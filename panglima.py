import requests
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Alpha_Infiltrator:
    def __init__(self):
        # Jalur Text-Based JPL (Paling Bandel)
        self.url = "https://nasa.gov"
        self.commander = "KAPTEN-BERDAULAT"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    def intercept(self):
        print(f"\n--- [STG ALPHA INFILTRATION: {self.commander}] ---")
        params = {
            "format": "text", # Kita minta format teks, bukan JSON
            "COMMAND": "'-165'", # ID Wahana Psyche
            "OBJ_DATA": "YES",
            "MAKE_EPHEM": "YES",
            "EPHEM_TYPE": "VECTORS",
            "CENTER": "'500@10'",
            "STOP_TIME": "now",
            "STEP_SIZE": "1"
        }
        
        try:
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=20)
            content = r.text
            
            if "$$SOE" in content:
                print("[SUCCESS] NASA Radio Shield Ditembus. Sinyal Terkunci.")
                # Mengambil data Vektor XYZ
                data_stream = content.split("$$SOE")[-1].split("$$EOE")[0].strip()
                print("\n[STG-LIVE-VECTOR-STREAM]")
                print(data_stream)
                print("\n[STATUS] Data Kedaulatan Berhasil Ditarik.")
                return True
            else:
                print("[REJECTED] Sinyal Terenkripsi. Gunakan Jalur Darurat.")
                return False
        except Exception as e:
            print(f"[CRITICAL] Handshake Gagal: {e}")
            return False

if __name__ == "__main__":
    stg = STG_Alpha_Infiltrator()
    stg.intercept()
