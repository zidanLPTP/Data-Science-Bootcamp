# operator_numpy.py
import numpy as np

# Penjelasan:
# Dalam NumPy, operasi bisa dilakukan antar array (elemen-wise), termasuk
# penjumlahan, pengurangan, perkalian, pembagian, pangkat, dan lainnya.
# Berikut ini contoh lengkap penggunaannya.

def tampil_info(arr, judul="Array"):
    print(f"=== {judul} ===")
    print(arr)
    print("Shape:", arr.shape)
    print("Dtype:", arr.dtype)
    print("====================\n")

if __name__ == "__main__":
    # Membuat dua array untuk operasi
    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])

    tampil_info(a, "Array a")
    tampil_info(b, "Array b")

    # Operasi Aritmatika
    print("Penjumlahan: a + b")
    print(a + b)  # [11 22 33 44]

    print("Pengurangan: a - b")
    print(a - b)  # [-9 -18 -27 -36]

    print("Perkalian: a * b")
    print(a * b)  # [10 40 90 160]

    print("Pembagian: a / b")
    print(a / b)  # [0.1 0.1 0.1 0.1]

    print("Pangkat: a ** 2")
    print(a ** 2)  # [1 4 9 16]

    # Operasi dengan scalar
    print("a + 5:")
    print(a + 5)

    print("a * 3:")
    print(a * 3)

    # Operasi logika (boolean)
    print("a > 2:")
    print(a > 2)  # [False False  True  True]

    print("b == 20:")
    print(b == 20)  # [False  True False False]

    # Operasi Matrix (dot product)
    print("Dot product antara a dan b:")
    print(np.dot(a, b))  # 1*10 + 2*20 + 3*30 + 4*40 = 300

    # Operasi universal function (ufunc)
    print("np.sqrt(a):")
    print(np.sqrt(a))

    print("np.exp(a):")
    print(np.exp(a))

    print("np.sin(a):")
    print(np.sin(a))

    # Operasi agregasi
    print("np.sum(b):", np.sum(b))
    print("np.mean(b):", np.mean(b))
    print("np.max(b):", np.max(b))
    print("np.min(b):", np.min(b))
    print("np.std(b):", np.std(b))
