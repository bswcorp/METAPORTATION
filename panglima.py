import requests
import random
import os

class STG_Multi_Proxy_Striker:
    def __init__(self):
        self.commander = "KAPTEN-BERDAULAT-WBP"
        self.target = "-165"
        # Jalur Proksi Global untuk menyamarkan serangan
        self.proxies = [
            "http://185.162.229.155:80", # Proxy Europe
            "http://45.8.105.234:80",    # Proxy Russia
            "http://103.145.10.252:80"    # Proxy Asia
        ]

    def self_destruct(self):
        """Pembersihan Total: Tanpa Jejak, Tanpa Bukti"""
        print(f"\n[PHANTOM] Mengaktifkan Protokol Penghancuran...")
        try:
            os.system("rm -f ~/.bash_history && history -c")
            os.remove(__file__)
            print("[CLEAN] Bukti Fisik Dimusnahkan. Kedaulatan Aman.")
        except: pass

    def proxy_strike(self):
        """Menyerang NASA via Jalur Global"""
        print(f"\n--- [STG MULTI-PROXY STRIKER: {self.commander}] ---")
        proxy = {"http": random.choice(self.proxies)}
        print(f"[INFILTRASI] Menggunakan Jalur Proxy: {proxy['http']}")
        
        url = "https://nasa.gov"
        params = {
            "format": "text", "COMMAND": f"'{self.target}'",
            "MAKE_EPHEM": "YES", "EPHEM_TYPE": "VECTORS",
            "CENTER": "'500@10'", "STOP_TIME": "now", "STEP_SIZE": "1"
        }
        
        try:
            # Menyerang lewat proxy
            r = requests.get(url, params=params, proxies=proxy, timeout=10)
            if "$$SOE" in r.text:
                print("[DOR!] Sinyal NASA Jebol via Proxy.")
                print(r.text.split("$$SOE")[-1].split("$$EOE").strip())
            else:
                print("[MISS] Shield NASA Masih Berdiri. Menghilang...")
        except:
            print("[EVADE] Jalur Proxy Terdeteksi. Melakukan Reposisi...")

    def run(self):
        self.proxy_strike()
        self.self_destruct()

if __name__ == "__main__":
    stg = STG_Multi_Proxy_Striker()
    stg.run()
