import pandas as pd
import numpy as np

df = pd.DataFrame([ [1, 2, 3],
                    [4, 5, 6] ],
                    columns=["kolom1", "kolom2", "kolom3"],
                    index=["baris1","baris2"] )
print(df)
print("-"*50)
ar = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
print(ar)
print("-"*50)

# Buat array
arr= np.array([[10, 20, 30],
               [40, 50, 60]])

# Konversi array ke DataFrame
dff= pd.DataFrame(arr,columns=["X", "Y", "Z"], index=["row1", "row2"])
print("DataFrame dari array NumPy:")
print(dff)
print("-"*50)

data = {
    "nama": ["Zidan", "Alya", "Rudi"],
    "nilai": [85, 90, 78],
    "lulus": [True, True, False]
}
df = pd.DataFrame(data, index=["mhs1", "mhs2", "mhs3"])
print("\nDataFrame dari dictionary:")
print(df)
print("-"*50)

ar = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

print("\nArray asli:")
print(ar)
# Operasi NumPy
print("\nArray dikali 2:")
print(ar * 2)
print("\nTranspose:")
print(ar.T)
print("-"*50)

# Data awal sebagai DataFrame
df_nilai = pd.DataFrame({
    "Matematika": [70, 80, 90],
    "Fisika": [75, 85, 95]
}, index=["Ali", "Budi", "Cici"])

print("\nDataFrame nilai siswa:")
print(df_nilai)

# Ubah ke NumPy array
arr_nilai = df_nilai.to_numpy()
print("\nArray dari DataFrame:")
print(arr_nilai)

# Hitung rerata pakai NumPy
rata_rata = np.mean(arr_nilai, axis=1)
print("\nRata-rata tiap siswa:")
print(rata_rata)
print("-"*50)

ar = pd.DataFrame([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]],
                index=["baris1","baris2","baris3"],
                columns=list("ABC"))
print(ar)

print("\nar.mean()")
ar = ar.mean()
print(ar)

print("\nar % 2:")
ar = ar % 2
print(ar)

print("\nr == 1")
ar = ar == 1
print(ar)

print("-"*50)
data = {
    "Math": [70, 80, 90, 100],
    "Physics": [65, 85, 95, 75],
    "Chemistry": [88, 92, 85, 91]
}

df = pd.DataFrame(data, index=["A", "B", "C", "D"])

print("DataFrame:")
print(df)
print("\nStatistik Ringkasan:")
print(df.describe(include="all"))

print("-"*50)
data = {'Babak Pertama':[100, 98, 100, 90],
        'Babak kedua': [90, 95, 86, 99],
        'babak Final': [97, 98, 99, 100],}

df = pd.DataFrame(data, index=['Zidan', 'Ahmad', 'Fathin', 'Alik'])
print(df)