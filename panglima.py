import requests
import hashlib
import json
import time

class STG_Sovereign_Ledger:
    def __init__(self):
        self.commander = "KAPTEN-BERDAULAT-WBP"
        self.probes = ["19564", "19546"]
        self.ledger_file = "stg_ledger.json"

    def get_hash(self, data):
        return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

    def update_ledger(self, new_block):
        """Menyimpan Blok Baru ke Ledger Lokal (Database Web5)"""
        ledger = []
        if os.path.exists(self.ledger_file):
            with open(self.ledger_file, 'r') as f:
                ledger = json.load(f)
        
        ledger.append(new_block)
        with open(self.ledger_file, 'w') as f:
            json.dump(ledger, f, indent=4)
        return ledger

    def display_visual_ledger(self):
        """Modul Visual: Menampilkan Tabel Blok yang Terkumpul"""
        print(f"\n--- [STG VISUAL LEDGER: KEDAULATAN DATA] ---")
        print(f"{'BLOK':<6} | {'TIMESTAMP':<20} | {'HASH (PREFIX)':<15} | {'STATUS'}")
        print("-" * 65)
        
        # Contoh visualisasi dari data yang baru saja ditambang
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        mock_hash = "f56b6c55..." # Dari blok genesis tadi
        print(f"{'#001':<6} | {current_time:<20} | {mock_hash:<15} | VALIDATED")
        print("-" * 65)

    def mine_now(self):
        print(f"\n[ACTION] Menambang Blok Baru...")
        mine_data = {"commander": self.commander, "ts": time.time(), "target": "16-Psyche"}
        new_hash = self.get_hash(mine_data)
        print(f"[SUCCESS] Hash Terbentuk: {new_hash}")
        self.display_visual_ledger()

if __name__ == "__main__":
    import os
    print(f"--- [STG COMMAND CENTER V12: {time.strftime('%Y-%m-%d')}] ---")
    stg = STG_Sovereign_Ledger()
    stg.mine_now()
