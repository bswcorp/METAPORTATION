import matplotlib.pyplot as plt

# Simulasi data dari Gamma-Ray Spectrometer (16 Psyche & TOI-1452 b)
labels = ['Water', 'Iron', 'Gold', 'Nickel', 'Others']
composition = [30, 40, 15, 10, 5] # Persentase materi

plt.figure(figsize=(8, 6))
plt.pie(composition, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Target Material Composition - TOI-1452 b Project')
plt.savefig('composition_report.png') # Karena di UserLAnd, simpan sebagai gambar
print("Grafik komposisi berhasil dibuat: composition_report.png")
