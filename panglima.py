import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Sovereign:
    def __init__(self):
        # API JPL NASA yang ASLI
        self.url = "https://nasa.gov"
        self.commander = "KAPTEN-BERDAULAT"
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def intercept(self):
        print(f"\n--- [STG LIVE TELEMETRY: {self.commander}] ---")
        params = {"sstr": "16", "orbit-physics": "true"}
        try:
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=20)
            if r.status_code == 200:
                data = r.json()
                print("[SUCCESS] Handshake NASA Berhasil.")
                orbit = data['orbit']['elements']
                print("\n[STG-REAL-TIME-ORBITAL-DATA]")
                for el in orbit:
                    print(f" > {el['label']}: {el['value']} {el.get('units', '')}")
                return True
            else:
                print(f"[REJECTED] Kode Error: {r.status_code}")
                return False
        except Exception as e:
            print(f"[CRITICAL] Gangguan Frekuensi: {e}")
            return False

if __name__ == "__main__":
    stg = STG_Sovereign()
    stg.intercept()

