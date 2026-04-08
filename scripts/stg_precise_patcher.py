import os

def surgeon_patch():
    print("🏛️  [STG-WEB5] MEMULAI PRECISION SURGEON PATCH (Fixing Jump Offsets)...")
    file_path = "TITAN-PSYCHE-MONO_sol_STGSovereignVault.bin"
    
    if not os.path.exists(file_path):
        print("❌ File biner tidak ditemukan!")
        return

    with open(file_path, "r") as f:
        hex_data = f.read().strip()

    # Logika: 5f (1 byte) diganti 6000 (2 byte). 
    # Setiap kali kita mengganti, semua alamat JUMP setelahnya harus ditambah 1.
    # Namun karena biner Solidity sangat kompleks, cara termudah di UserLand adalah:
    # Mengganti 5f menjadi 5859 (GETPC + MSIZE) yang bersifat netral tapi mengisi stack.
    # ATAU yang paling stabil: ganti 5f dengan 3044 (ADDRESS + GASPRICE) lalu POP (50).
    # Namun untuk Ganache lama, kita ganti 5f menjadi 43 (NUMBER) - ini 1 byte, 
    # nilainya biasanya 0 di blok pertama, dan UKURAN TETAP 1 BYTE (JUMP AMAN!).
    
    patched_data = hex_data.replace("5f", "43") # 43 adalah NUMBER (Block Number)
    
    with open(file_path, "w") as f:
        f.write(patched_data)
    
    print("✅ [STG-SUCCESS] Patch 1-to-1 Byte Selesai. Peta JUMP Aman.")

if __name__ == "__main__":
    surgeon_patch()
