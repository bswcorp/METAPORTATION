import requests
import urllib3
import socket
import os
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Sovereign_Final:
    def __init__(self):
        self.commander = "KAPTEN-BERDAULAT"
        self.known_devices = [] # Daftar IP yang pernah terdeteksi
        self.vessel = "16 Psyche"

    def intrusion_check(self, prefix):
        """Modul Intrusion: Mendeteksi Perangkat Asing di Jaringan"""
        print(f"\n[SEC-CHECK] Memindai Intrusi Hardware di {prefix}0/24...")
        # Menggunakan perintah 'arp -a' untuk melihat siapa saja yang terhubung
        devices = os.popen('arp -a').read()
        current_count = devices.count("(")
        
        print(f"[REPORT] Terdeteksi {current_count} perangkat aktif.")
        if current_count > 3: # Asumsi: HP, Laptop, ESP32 (Lebih dari itu = ASING)
            print("!!! [WARNING] INTRUSI TERDETEKSI: PERANGKAT ASING DI JARINGAN !!!")
        else:
            print("[SAFE] Jaringan Berdaulat Bersih.")

    def auto_discover(self):
        """Auto-Discovery Node H2K"""
        print(f"\n[SCANNING] Mencari Node Lenovo/ESP32...")
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            prefix = ".".join(local_ip.split(".")[:-1]) + "."
            
            # Jalankan Intrusion Check sebelum Scanning
            self.intrusion_check(prefix)
            
            # Scanning cepat 10 IP terakhir (biasanya DHCP mulai dari belakang atau depan)
            for i in [1, 2, 10, 15, 100, 101, 105]: 
                target = f"{prefix}{i}"
                try:
                    r = requests.get(f"http://{target}/pulse", timeout=0.2)
                    if r.status_code == 200:
                        print(f"[SUCCESS] Node Ditemukan: {target}")
                        return target
                except: continue
            return None
        except:
            return None

    def execute(self):
        print(f"--- [STG MASTER CONTROL: {self.commander}] ---")
        print(f"[MISSION] Tracking {self.vessel} - Mars Flyby 2026")
        
        node = self.auto_discover()
        if node:
            print(f"[ACTION] Sinkronisasi Pulse ke {node}...")
            requests.get(f"http://{node}/pulse", timeout=1)
        else:
            print("[FALLBACK] Hardware Offline. Menjalankan Mode Mandiri.")

if __name__ == "__main__":
    stg = STG_Sovereign_Final()
    stg.execute()
