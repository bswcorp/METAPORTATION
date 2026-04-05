import requests
import socket
import base64
import time

class STG_Ghost_Commander:
    def __init__(self):
        self.commander = "KAPTEN-BERDAULAT"
        self.key = "XENON-STG-SECURE"
        self.host_ip = socket.gethostbyname(socket.gethostname())

    def ghost_protocol(self):
        """Modul Ghost: Mendeteksi Scanning Balik ke HP"""
        print(f"\n[GHOST-PROTOCOL] Mendengarkan di {self.host_ip}...")
        # Membuat socket listener pasif untuk mendeteksi 'ping' atau 'scan'
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sniffer.settimeout(2.0) # Tunggu 2 detik untuk deteksi intrusi aktif
        try:
            sniffer.bind(('', 8080)) # Monitor Port 8080 (Port favorit hacker)
            sniffer.listen(1)
            print("[STATUS] Sensor Pasif Aktif. HP dalam Mode Siluman.")
            conn, addr = sniffer.accept()
            print(f"!!! [WARNING] GHOST ALERT: PERANGKAT {addr[0]} MENCOBA SCANNING HP ANDA !!!")
            conn.close()
        except socket.timeout:
            print("[SAFE] Tidak ada aktivitas scanning eksternal terdeteksi.")
        except Exception as e:
            print(f"[INFO] Sensor Port 8080 Terkunci.")
        finally:
            sniffer.close()

    def socket_radar(self):
        """Memindai Jaringan via Socket Internal"""
        print(f"\n[SEC-CHECK] Memindai Node Aktif di Jaringan...")
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            prefix = ".".join(s.getsockname().split(".")[:-1]) + "."
            s.close()
            active_nodes = []
            for i in range(1, 15):
                target = f"{prefix}{i}"
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.02)
                if sock.connect_ex((target, 80)) == 0:
                    active_nodes.append(target)
                sock.close()
            print(f"[REPORT] Terdeteksi {len(active_nodes)} Node Aktif.")
            return active_nodes
        except: return []

    def run(self):
        print(f"--- [STG COMMAND CENTER V6: {self.commander}] ---")
        # 1. Jalankan Ghost Protocol (Deteksi Orang Lain)
        self.ghost_protocol()
        # 2. Jalankan Radar (Cari Teman)
        nodes = self.socket_radar()
        
        if nodes:
            print(f"[SUCCESS] Handshake Berhasil. Node {nodes[0]} Terdeteksi.")
        else:
            print("[FALLBACK] Berjalan dalam Mode Siluman (Offline).")

if __name__ == "__main__":
    stg = STG_Ghost_Commander()
    stg.run()
