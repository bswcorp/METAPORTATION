import requests
import hashlib
import json
import time

class STG_Blockchain_Miner:
    def __init__(self):
        self.commander = "KAPTEN-BERDAULAT-WBP"
        self.probes = ["19564", "19546"]
        self.target = "16-Psyche"
        self.blockchain_ledger = []

    def blockchain_encryptor(self, raw_data):
        """Web5: Mengubah Data Mentah menjadi Hash Blockchain"""
        # SHA-256 Encryption (Standar Bitcoin/Ethereum)
        data_string = json.dumps(raw_data, sort_keys=True).encode()
        block_hash = hashlib.sha256(data_string).hexdigest()
        return block_hash

    def mine_sovereign_data(self):
        print(f"\n--- [STG SOVEREIGN MINER: BLOCKCHAIN MODE] ---")
        mine_results = {"commander": self.commander, "timestamp": time.time()}
        
        # 1. Menambang Status RIPE Atlas
        for p_id in self.probes:
            url = f"https://ripe.net{p_id}/"
            try:
                r = requests.get(url, timeout=10)
                if r.status_code == 200:
                    status = r.json().get('status', {}).get('name', 'N/A')
                    mine_results[f"probe_{p_id}"] = status
                    print(f"[NODE-{p_id}] Mining Status: {status}")
            except: continue

        # 2. Enkripsi Hasil Tambang ke Blockchain
        stg_hash = self.blockchain_encryptor(mine_results)
        self.blockchain_ledger.append({"hash": stg_hash, "data": mine_results})
        
        print(f"\n[BLOCKCHAIN-GENESIS] Hash Terbentuk:")
        print(f" > {stg_hash}")
        print("[STATUS] Data Terkunci secara Berdaulat di Ledger STG.")

    def probe_finder_fix(self):
        """Memperbaiki Radar untuk Mencari Node ke-3"""
        print(f"\n[RADAR] Mencari Node Tambang Tambahan...")
        # Jalur API yang sudah diperbaiki
        url = f"https://ripe.net{self.probes}/"
        try:
            r = requests.get(url, timeout=10)
            asn = r.json().get('asn_v4')
            print(f"[INFO] Basis Jaringan ASN: {asn}")
            print(f"[HINT] Cari ID lain di ASN {asn} via portal publik RIPE.")
        except:
            print("[INFO] Radar Pasif Aktif.")

if __name__ == "__main__":
    print(f"--- [STG COMMANDER V11: {time.strftime('%Y-%m-%d')}] ---")
    stg = STG_Blockchain_Miner()
    stg.mine_sovereign_data()
    stg.probe_finder_fix()
