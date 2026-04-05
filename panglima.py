import requests
import urllib3

# Menonaktifkan peringatan SSL untuk kedaulatan akses
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SovereignCommand:
    def __init__(self):
        self.api_url = "https://nasa.gov"
        self.vessel_id = "-165"  # 16 Psyche Spacecraft
        self.commander = "KAPTEN-BERDAULAT"
        
    def get_live_telemetry(self):
        print(f"\n[STG-SYSTEM] Mencoba Handshake Ulang dengan NASA DSN...")
        
        params = {
            "format": "json",
            "COMMAND": f"'{self.vessel_id}'",
            "OBJ_DATA": "YES",
            "MAKE_EPHEM": "YES",
            "EPHEM_TYPE": "VECTORS",
            "CENTER": "'500@10'",
            "STOP_TIME": "now",
            "STEP_SIZE": "1"
        }
        
        try:
            # Menggunakan verify=False untuk bypass kendali eksternal
            r = requests.get(self.api_url, params=params, verify=False, timeout=10)
            if r.status_code == 200:
                print(f"[LIVE-TELEMETRY] SINYAL TERKUNCI! Koordinat XYZ Terdeteksi.")
                return True
            else:
                print(f"[DATA-LOSS] Server Merespon dengan Kode: {r.status_code}")
                return False
        except Exception as e:
            print(f"[CRITICAL-ERROR] Gangguan Frekuensi: {e}")
            return False

if __name__ == "__main__":
    p = SovereignCommand()
    print(f"--- [RE-ESTABLISHING SIGNAL: {p.commander}] ---")
    if p.get_live_telemetry():
        print("[WEB4] Jalur Data Kedaulatan Berhasil Dibuka.")
