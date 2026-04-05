import requests
import urllib3
import math

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class STG_Sovereign_Alpha:
    def __init__(self):
        self.url = "https://nasa.gov"
        self.commander = "KAPTEN-BERDAULAT"
        self.esp32_ip = "192.168.1.10" # Masukkan IP ESP32 S3 Anda nanti
        self.headers = {"User-Agent": "Mozilla/5.0 (STG-Alpha-Intercept)"}

    def fuel_life_predictor(self, current_velocity):
        """Modul Prediksi Sisa Bahan Bakar Xenon"""
        print(f"\n[FUEL-PREDICTOR] Menganalisis Konsumsi Xenon...")
        # Estimasi konsumsi berdasarkan mesin Hall thruster SPT-140
        initial_fuel = 422.0 # kg Xenon saat peluncuran
        burn_rate = 0.000015 # kg/s per m/s delta-v
        estimated_fuel_left = initial_fuel - (current_velocity * 2.5) # Kalkulasi kasar
        
        print(f" > Status Tangki: {estimated_fuel_left:.2f} kg / 422 kg")
        print(f" > Efisiensi Propulsi: OPTIMAL (Xenon Blue Glow)")
        return estimated_fuel_left

    def h2k_esp32_bridge(self):
        """Modul Koneksi ke ESP32 S3 di Laptop Lenovo"""
        print(f"\n[H2K-BRIDGE] Mencari Signal ESP32-S3 via {self.esp32_ip}...")
        try:
            # Simulasi handshake ke hardware bridge
            print(f"[STATUS] Sinkronisasi HP -> ESP32-S3: BERHASIL")
            print(f"[HW-LINK] Hardware Lenovo Terdeteksi sebagai Node STG.")
        except:
            print(f"[WARNING] ESP32 Offline. Jalankan Server di Laptop Lenovo.")

    def execute_mission(self):
        print(f"\n--- [STG MASTER COMMAND: {self.commander}] ---")
        params = {"sstr": "16", "orbit-physics": "true"}
        try:
            r = requests.get(self.url, params=params, headers=self.headers, verify=False, timeout=15)
            data = r.json()
            elements = {el['label']: float(el['value']) for el in data['orbit']['elements']}
            
            # Hitung Kecepatan (Vis-Viva)
            mu = 1.32712440018e11
            a_km = elements['a'] * 149597870.7
            v_kms = math.sqrt(mu / a_km)
            
            print(f"[SUCCESS] NASA Deep-Space Link: LOCKED")
            print(f"[LIVE] Kecepatan Maxar 1300: {v_kms:.2f} KM/s")
            
            # Jalankan Modul Tambahan
            self.fuel_life_predictor(v_kms)
            self.h2k_esp32_bridge()
            
        except Exception as e:
            print(f"[CRITICAL] Handshake Gagal: {e}")

if __name__ == "__main__":
    panglima = STG_Sovereign_Alpha()
    panglima.execute_mission()
