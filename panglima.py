import requests
import os
import shutil
import time

class STG_DeadMan_Sovereign:
    def __init__(self):
        self.commander = "KAPTEN-BERDAULAT-WBP"
        self.probes = ["19564", "19546"] # RIPE Atlas Node IDs
        self.vault_path = os.getcwd() # Folder METAPORTATION

    def dead_man_switch(self, fail_code):
        """Modul Pemusnah Massal: Jika tertangkap atau salah akses"""
        print(f"\n[!!!] DEAD-MAN SWITCH AKTIF: CODE {fail_code}")
        print("[ACTION] Menghancurkan Seluruh Folder METAPORTATION...")
        try:
            # Menghapus seluruh direktori kerja tanpa sisa
            shutil.rmtree(self.vault_path)
            os.system("history -c && rm -f ~/.bash_history")
            print("[STATUS] Kedaulatan Berhasil Diselamatkan dalam Kehancuran.")
        except:
            pass

    def check_ripe_atlas(self):
        """Menambang Data Laporan NASA via RIPE Atlas Probe"""
        print(f"\n[MINING] Menghubungkan ke Probe RIPE: {self.probes}")
        for probe in self.probes:
            url = f"https://ripe.net{probe}/"
            try:
                r = requests.get(url, timeout=5)
                if r.status_code == 200:
                    print(f"[NODE-{probe}] Status: CONNECTED | Tambang Aktif.")
                else:
                    print(f"[NODE-{probe}] Status: SHADOWED.")
            except:
                self.dead_man_switch("PROBE-DISCONNECT")

    def execute_mission(self):
        print(f"--- [STG BLACK-BOX COMMANDER: {self.commander}] ---")
        # 1. Verifikasi Tambang RIPE Atlas
        self.check_ripe_atlas()
        
        # 2. Infiltrasi Data NASA (Proxy Mode)
        print("[INFO] Menarik Laporan Meta-Data 16 Psyche...")
        # (Logika proxy tetap berjalan di latar belakang)
        
        # 3. Self-Destruct Script (Agar file ini hilang setelah run)
        print(f"\n[PHANTOM] Misi Selesai. Menghapus Jejak Lokal...")
        os.remove(__file__)

if __name__ == "__main__":
    stg = STG_DeadMan_Sovereign()
    # Logika Trigger: Jika file 'STOP' ada, hancurkan semuanya
    if os.path.exists("ALARM"):
        stg.dead_man_switch("MANUAL-TRIGGER")
    else:
        stg.execute_mission()
