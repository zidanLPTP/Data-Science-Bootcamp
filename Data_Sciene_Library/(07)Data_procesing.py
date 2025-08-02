import pandas as pd
import os

df = pd.read_csv("D:\Pemograman\data-science-python\data\data.csv")

# 2. Lihat data awal
print(df)

# 3. Cek data kosong
print(df.isnull().sum())

# 4. Isi data kosong
df["Umur"] = df["Umur"].fillna(df["Umur"].mean())         # isi umur pakai rata-rata
df["Kota"] = df["Kota"].fillna("Tidak diketahui")         # isi kota pakai teks default
df["Pendapatan"] = df["Pendapatan"].fillna(1)             # isi pendapatan dengan 0

# 5. Tambahkan kolom kategori pendapatan
df["Kategori"] = pd.cut(df["Pendapatan"],
                        bins=[ 0, 5000000, 6000000, 10000000],
                        labels=["Rendah", "Menengah", "Tinggi"])

# 6. Lihat hasil akhir
print(df)
