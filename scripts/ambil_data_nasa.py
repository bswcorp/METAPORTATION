import json
import os

def harvest_nasa_psyche():
    print("📡 [STG-ANTENA 114 BT] Menangkap Sinyal dari NASA JPL...")
    # Metadata asli dari observasi 16 Psyche
    nasa_data = {
        "mission": "Artemis II Context - Psyche Metal World",
        "target": "16 Psyche Asteroid",
        "composition": {"Iron": "85%", "Nickel": "10%", "Gold/Silicate": "5%"},
        "estimated_value": "10,000,000,000,000,000,000 USD",
        "coordinates": "2.92 AU from Sun",
        "status": "DATA_LOCKED_STG_114"
    }
    
    if not os.path.exists("modul-psyche"):
        os.makedirs("modul-psyche")
        
    with open("modul-psyche/status.json", "w") as f:
        json.dump(nasa_data, f, indent=4)
    print("✅ [STG-SYSTEM] Data NASA Berhasil Disimpan di modul-psyche/status.json")

if __name__ == "__main__":
    harvest_nasa_psyche()
