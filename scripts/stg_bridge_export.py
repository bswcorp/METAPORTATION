import json
import time
import os

def migrate_to_global():
    print("🏛️  [STG-BRIDGE] RE-SINKRONISASI MIGRASI GLOBAL...")
    
    # Memastikan file ada
    if not os.path.exists("last_deploy_status.json"):
        print("❌ Manifes lokal hilang!")
        return

    with open("last_deploy_status.json", "r") as f:
        local_data = json.load(f)
    
    # Deteksi waktu secara dinamis jika field 'timestamp' absen
    lock_time = local_data.get('timestamp') or local_data.get('timestamp_lock') or int(time.time())
    
    migration_packet = {
        "origin_coordinates": "114 BT",
        "sovereign_vault": local_data['address'],
        "collateral_hash": local_data.get('mission_hash', '729fc52e79864f02effca2713a3b3968e50b8aa3958e2fd2f80f6f9b12f9fed2'),
        "export_valuation": "10 Quadrillion USD",
        "timestamp_lock": lock_time,
        "protocol": "WEB5-STG-MIGRATION"
    }

    with open("global_migration_packet.json", "w") as f:
        json.dump(migration_packet, f, indent=4)

    print("==================================================")
    print("✅ [BRIDGE-RESTORED] PAKET GLOBAL SIAP!")
    print(f"Target: Polygon/Ethereum Mainnet Ready")
    print("==================================================")

if __name__ == "__main__":
    migrate_to_global()
