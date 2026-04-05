import requests
import urllib3
from datetime import datetime, timedelta

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Sovereign_Alpha:
    def __init__(self):
        self.url = "https://nasa.gov"
        self.vessel_id = "-165" # 16 Psyche
        self.commander = "KAPTEN-BERDAULAT"
        self.headers = {"User-Agent": "STG-Command-Center/1.0"}

    def intercept_telemetry(self):
        print(f"\n--- [STG ALPHA INTERCEPT: {self.commander}] ---")
        
        # Set rentang waktu 5 menit yang lalu agar data pasti ada di database NASA
        start_time = (datetime.utcnow() - timedelta(minutes=10)).strftime('%Y-%m-%d %H:%M')
        stop_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M')
        
        params = {
            "format": "text",
            "COMMAND": f"'{self.vessel_id}'",
            "OBJ_DATA": "NO",
            "MAKE_EPHEM": "YES",
            "EPHEM_TYPE": "VECTORS",
            "CENTER": "'500@0'", # Pusat Massa Tata Surya (SSB) - Paling Akurat
            "START_TIME": start_time,
            "STOP_TIME": stop_time,
            "STEP_SIZE": "1m"
        }
        
        try:
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=30)
            content = r.text
            
            if "$$SOE" in content:
                print("[LIVE] SINYAL TERBONGKAR. Mengekstrak Vektor Inti...")
                # Ambil data di antara marker SOE dan EOE
                data_block = content.split("$$SOE")[1].split("$$EOE")[0].strip()
                print("\n[VECTOR-STREAM-XYZ]")
                print(data_block)
                print("\n[STATUS] Data Vektor Berdaulat Berhasil Terintegrasi.")
                return True
            else:
                print("[ERROR] NASA Shield Active. Jalankan protokol Bypass.")
                return False
        except Exception as e:
            print(f"[CRITICAL] Jalur Komunikasi Putus: {e}")
            return False

if __name__ == "__main__":
    stg = STG_Sovereign_Alpha()
    if stg.intercept_telemetry():
        print(f"[WEB5] Transmisi Terkunci. Simpan ke Repo Metaportasi.")
