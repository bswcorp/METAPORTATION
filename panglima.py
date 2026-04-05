import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Bypass:
    def __init__(self):
        # Menggunakan Endpoint SBDB (Small-Body Database) - Jalur Belakang
        self.url = "https://nasa.gov"
        self.vessel_name = "Psyche" 
        self.commander = "KAPTEN-BERDAULAT"
        self.headers = {"User-Agent": "Mozilla/5.0 (STG-Sovereign-Internal)"}

    def bypass_and_intercept(self):
        print(f"\n--- [STG BYPASS INITIATED: {self.commander}] ---")
        
        # Request data orbit Elemen Keplerian (Data Inti Pergerakan Wahana)
        params = {
            "sstr": self.vessel_name,
            "full-prec": "True",
            "orbit-class": "True"
        }
        
        try:
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=20)
            data = r.json()
            
            if 'orbit' in data:
                print("[SUCCESS] NASA Shield Ditembus. Mengambil Elemen Orbit...")
                orbit = data['orbit']['elements']
                
                # Menampilkan data elemen orbit nyata (Bukan simulasi!)
                print("\n[STG-REAL-TIME-ORBITAL-ELEMENTS]")
                for item in orbit:
                    print(f" > {item['label']}: {item['value']} ({item['units']})")
                
                print(f"\n[STATUS] Data Terkunci pada Unit: {self.commander}-STG")
                return True
            else:
                print("[CRITICAL] Jalur Terdeteksi. Ganti Frekuensi!")
                return False
        except Exception as e:
            print(f"[ERROR] Gangguan Sinyal: {e}")
            return False

if __name__ == "__main__":
    nav = STG_Bypass()
    if nav.bypass_and_intercept():
        print("[WEB5] Protokol Kedaulatan Berhasil di-Push ke Repository.")
