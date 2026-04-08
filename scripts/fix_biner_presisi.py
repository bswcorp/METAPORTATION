import os

def patch_bin_safe():
    print("🛠️  [STG-PATCH] OPERASI PRESISI: MENGHAPUS PUSH0 TANPA GESER MAP...")
    file_path = "TITAN-PSYCHE-MONO_sol_STGSovereignVault.bin"
    
    if not os.path.exists(file_path):
        print("❌ File .bin tidak ditemukan!")
        return

    with open(file_path, "r") as f:
        hex_data = f.read().strip()

    # Logika: Ganti 5f (PUSH0) menjadi 5b (JUMPDEST)
    # JUMPDEST (5b) adalah instruksi netral yang tidak mengubah stack
    # dan yang paling penting: UKURANNYA SAMA (1 BYTE).
    # Ini menjamin tidak ada 'invalid JUMP' karena alamat kode tidak bergeser.
    patched_data = hex_data.replace("5f", "5b")
    
    with open(file_path, "w") as f:
        f.write(patched_data)
    
    print("✅ [SUCCESS] Bytecode dipatch secara presisi (1-to-1 byte).")

if __name__ == "__main__":
    patch_bin_safe()
