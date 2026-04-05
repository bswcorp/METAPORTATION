import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Trajectory_Predictor:
    def __init__(self):
        self.url = "https://nasa.gov"
        self.commander = "KAPTEN-BERDAULAT"
        self.vessel_id = "'-165'" # ID Psyche Spacecraft
        self.headers = {"User-Agent": "STG-Alpha-Predictor/2.0"}

    def predict_mars_flyby(self):
        print(f"\n--- [STG TRAJECTORY PREDICTOR: {self.commander}] ---")
        print("[INFO] Melakukan Intersepsi Lintasan Mei 2026...")
        
        # Mengunci target pada fase Mars Flyby (Mei 2026)
        params = {
            "format": "text",
            "COMMAND": self.vessel_id,
            "OBJ_DATA": "NO",
            "MAKE_EPHEM": "YES",
            "EPHEM_TYPE": "VECTORS",
            "CENTER": "'500@10'",
            "START_TIME": "2026-05-15 00:00",
            "STOP_TIME": "2026-05-15 00:05",
            "STEP_SIZE": "1m"
        }
        
        try:
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=25)
            if "$$SOE" in r.text:
                print("[SUCCESS] Data Flyby Terkunci. Mengekstrak Vektor Masa Depan...")
                # Ambil data vektor XYZ dan kecepatan VX VY VZ
                future_data = r.text.split("$$SOE")[-1].split("$$EOE").strip()
                print(f"\n[MARS-FLYBY-VECTOR (MAY 2026)]\n{future_data}")
                return True
            else:
                print("[REJECTED] Sinyal Terenkripsi. NASA mengunci data masa depan.")
                return False
        except Exception as e:
            print(f"[ERROR] Gangguan Frekuensi: {e}")
            return False

if __name__ == "__main__":
    predictor = STG_Trajectory_Predictor()
    if predictor.predict_mars_flyby():
        print("\n[WEB4/5] Prediksi Kedaulatan Berhasil. Simpan ke GitHub.")
