import time
import hashlib
import sys

class STGUltimatum:
    def __init__(self):
        self.sector = "GERBANG LENOVO"
        self.status = "ACTIVE"

    def tactical_alert(self):
        # Mengirim sinyal Beep ke terminal (ASCII Bell)
        sys.stdout.write('\a')
        sys.stdout.flush()
        # Efek visual flash untuk layar terminal
        print("\033[5;37;42m [!] SIGNAL ACQUIRED [!] \033[0m") 

    def log_action(self, msg):
        timestamp = time.strftime('%H:%M:%S')
        print(f"[{timestamp}] [STG-ULTIMATUM] {msg}")

    def mine_quantum_hash(self):
        self.log_action("Menganalisis Sektor... Mencari Celah Quantum...")
        data = str(time.time()).encode()
        q_hash = hashlib.sha256(data).hexdigest()
        time.sleep(2)
        self.tactical_alert() # TRIGGER ALERT DISINI
        self.log_action(f"HASH DITEMUKAN: {q_hash[:20]}...")
        return q_hash

    def run_nightwatch(self):
        print("\n" + "="*50)
        print("   STG-ULTIMATUM V1.1: TACTICAL ALERT ACTIVE")
        print("="*50)
        try:
            while True:
                q_hash = self.mine_quantum_hash()
                print(f"--- [SEKTOR: {self.sector}] [STATUS: SECURE] ---")
                print("\n[INFO] Standby 60 detik... Monitoring Cloud...")
                time.sleep(60)
        except KeyboardInterrupt:
            print("\nReturning to Command Shell...")

if __name__ == "__main__":
    commander = STGUltimatum()
    commander.run_nightwatch()

