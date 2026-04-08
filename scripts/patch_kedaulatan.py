import os

def patch_bin():
    print("🛠️  [STG-PATCH] MEMULAI OPERASI PATCHING BYTECODE (PUSH0 -> PUSH1 00)...")
    file_path = "TITAN-PSYCHE-MONO_sol_STGSovereignVault.bin"
    
    if not os.path.exists(file_path):
        print("❌ File .bin tidak ditemukan!")
        return

    with open(file_path, "r") as f:
        hex_data = f.read().strip()

    # Logika Patching: Ganti opcode 5f (PUSH0) menjadi 6000 (PUSH1 00)
    # Ini adalah perbaikan standar untuk EVM lama
    patched_data = hex_data.replace("5f", "6000")
    
    with open(file_path, "w") as f:
        f.write(patched_data)
    
    print("✅ [SUCCESS] Bytecode telah dipatch untuk kompatibilitas London/Paris.")

if __name__ == "__main__":
    patch_bin()
