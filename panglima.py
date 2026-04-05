import requests
import urllib3
import socket
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Sovereign_Auto:
    def __init__(self):
        self.commander = "KAPTEN-BERDAULAT"
        self.target_port = 80
        self.vessel_id = "-165"

    def auto_discover_bridge(self):
        """Memindai Jaringan Lokal secara Mandiri"""
        print(f"\n[SCANNING] STG Auto-Discovery Memindai Node H2K...")
        # Mendapatkan IP lokal HP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        
        prefix = ".".join(local_ip.split(".")[:-1]) + "."
        print(f"[STATUS] Basis IP Terdeteksi: {prefix}0/24")

        # Mencoba 5 IP terakhir yang sering digunakan laptop (Bisa di-expand)
        for i in range(1, 255):
            target = f"{prefix}{i}"
            try:
                # Handshake kilat
                r = requests.get(f"http://{target}/pulse", timeout=0.1)
                if r.status_code == 200:
                    print(f"[SUCCESS] Node Lenovo Terdeteksi di: {target}")
                    return target
            except:
                continue
        return None

    def intercept_nasa(self):
        print(f"\n--- [STG DEEP-SPACE INTERCEPT: {self.commander}] ---")
        url = "https://nasa.gov"
        # Kita tarik data elemen orbit (SBDB) karena lebih ringan & jarang diblokir
        params = {
            "format": "text", "COMMAND": "'-165'", "OBJ_DATA": "YES",
            "MAKE_EPHEM": "YES", "EPHEM_TYPE": "ELEMENTS", "CENTER": "'500@10'",
            "STOP_TIME": "now", "STEP_SIZE": "1"
        }
        try:
            r = requests.get(url, params=params, verify=False, timeout=15)
            if "$$SOE" in r.text:
                print("[SUCCESS] Handshake NASA Berhasil. Data Elemen Terkunci.")
                return True
        except:
            print("[ERROR] Jalur DSN Padat. Menggunakan Data Cache Web5.")
        return False

    def run(self):
        # 1. Tarik Data NASA
        nasa_ok = self.intercept_nasa()
        
        # 2. Cari Hardware Secara Otomatis
        bridge_ip = self.auto_discover_bridge()
        
        if nasa_ok and bridge_ip:
            print(f"\n[ACTION] Sinkronisasi Metaportasi ke {bridge_ip}...")
            requests.get(f"http://{bridge_ip}/pulse")
            print("[STATUS] Xenon Pulse Aktif di Lenovo!")
        else:
            print("\n[FALLBACK] Mode Berdaulat Mandiri Aktif (Hardware Offline).")

if __name__ == "__main__":
    stg = STG_Sovereign_Auto()
    stg.run()
