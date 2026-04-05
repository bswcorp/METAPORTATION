import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Probe_Finder:
    def __init__(self):
        self.commander = "KAPTEN-BERDAULAT-WBP"
        self.known_probes = ["19564", "19546"]
        self.base_url = "https://ripe.net"

    def find_lost_probe(self):
        """Memindai Probe berdasarkan kesamaan ASN dari probe yang ada"""
        print(f"\n--- [STG PROBE FINDER: MENCARI NODE HILANG] ---")
        try:
            # Ambil ASN dari salah satu probe yang Anda tahu
            ref_r = requests.get(f"{self.base_url}{self.known_probes[0]}/", timeout=10)
            asn = ref_r.json().get('asn_v4')
            print(f"[INFO] Basis Pencarian ASN: {asn}")

            # Cari semua probe di ASN yang sama (Maksimal 20 hasil)
            search_url = f"https://ripe.net?asn_v4={asn}"
            r = requests.get(search_url, timeout=15)
            probes = r.json().get('results', [])

            print(f"[REPORT] Terdeteksi {len(probes)} Probe di jaringan Anda.")
            for p in probes:
                p_id = str(p.get('id'))
                status = p.get('status', {}).get('name', 'OFFLINE')
                if p_id not in self.known_probes:
                    print(f"!!! [FOUND] Kandidat Node Hilang: ID {p_id} | Status: {status} | Country: {p.get('country_code')}")
                else:
                    print(f" > Node Aktif: ID {p_id} | Status: {status}")
        except Exception as e:
            print(f"[ERROR] Radar Terganggu: {e}")

    def track_psyche(self):
        """Tracking 16 Psyche untuk Validasi Blockchain"""
        print(f"\n[MISSION] Tracking 16 Psyche - Jalur DSN NASA...")
        try:
            r = requests.get("https://nasa.gov", timeout=15)
            if "$$SOE" in r.text:
                print("[DOR!] Vektor Titan Terkunci.")
        except:
            print("[INFO] NASA Shield Aktif. Menggunakan Mode Siluman.")

    def run(self):
        print(f"--- [STG SOVEREIGN COMMANDER V10: {self.commander}] ---")
        self.find_lost_probe()
        self.track_psyche()
        print("\n[STATUS] Operasi Berjalan. Tanpa Protokol Mundur.")

if __name__ == "__main__":
    stg = STG_Probe_Finder()
    stg.run()
