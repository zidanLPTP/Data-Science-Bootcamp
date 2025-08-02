import pandas as pd
import matplotlib.pyplot as plt

# Buat DataFrame
data = {
    'Tahun': [2020, 2021, 2022, 2023],
    'Penjualan': [100, 150, 200, 180],
    'Pengeluaran': [80, 120, 160, 170]
}
df = pd.DataFrame(data)
df.set_index('Tahun', inplace=True)  # Biar Tahun jadi sumbu X

# Plot
df.plot(title="Penjualan vs Pengeluaran")
plt.xlabel("Tahun")
plt.ylabel("Rupiah (juta)")
plt.grid(True)
plt.show()

data = {
    'Produk': ['A', 'B', 'C'],
    'Penjualan': [150, 200, 180]
}
df = pd.DataFrame(data)

# Set index agar label Produk jadi sumbu X
df.set_index('Produk', inplace=True)

# Plot bar chart
df.plot(kind='bar', title='Penjualan per Produk')
plt.xlabel('Produk')
plt.ylabel('Jumlah Terjual')
plt.grid(axis='y')
plt.show()

# Tambah data tahun lain
data = {
    'Produk': ['A', 'B', 'C'],
    '2022': [150, 200, 180],
    '2023': [160, 220, 190]
}
df_multi = pd.DataFrame(data)
df_multi.set_index('Produk', inplace=True)

# Plot multiple bar
df_multi.plot(kind='bar', title='Perbandingan Penjualan per Produk (2022 vs 2023)')
plt.ylabel('Jumlah Terjual')
plt.grid(axis='y')
plt.show()
