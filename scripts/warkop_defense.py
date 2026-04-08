import os
import time

def monitor_integrity():
    print("🛡️  [WARKOP-DEFENSE] MEMULAI PENJAGAAN MANIFES...")
    files_to_watch = ["last_deploy_status.json", "global_migration_packet.json", "hasil_jembatan_likuiditas.json"]
    
    for file in files_to_watch:
        if os.path.exists(file):
            # Set file ke mode Read-Only untuk userland agar tidak sengaja terhapus
            os.chmod(file, 0o444)
            print(f"🔒 {file} telah dikunci (Read-Only Mode)")
        else:
            print(f"⚠️ Warning: {file} tidak ditemukan dalam perimeter!")

if __name__ == "__main__":
    monitor_integrity()
