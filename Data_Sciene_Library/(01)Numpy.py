# modul_numpy_info.py
import numpy as np
import time  # Untuk pengukuran waktu jika dibutuhkan nanti

def tampil_info(arr):
    """
    Menampilkan informasi penting tentang array NumPy.
    """
    print("Array:")
    print(arr)
    print("Jumlah dimensi (ndim):", arr.ndim)
    print("Shape (bentuk):", arr.shape)
    print("Size (jumlah elemen):", arr.size)
    print("Tipe data elemen (dtype):", arr.dtype)
    print("-" * 50)

if __name__ == "__main__":
    # Dua list Python biasa
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    print("\nMembuat array dari tuple:")
    arr = np.array((1, 2, 3, 4))
    tampil_info(arr)

    print("\nMembuat array 2D dari dua list dengan tipe data float64:")
    arr2 = np.array([list1, list2, list1], dtype=np.float64)
    tampil_info(arr2)

    print("\nArray 2x2 yang seluruh elemennya adalah 1:")
    arr3 = np.ones((2, 2))
    tampil_info(arr3)

    print("\nArray 4x3 yang seluruh elemennya adalah 0:")
    arr4 = np.zeros((4, 3))
    tampil_info(arr4)

    print("\nArray 3D dari angka 0–23 dengan shape (2, 3, 4):")
    arr3d = np.array(range(24)).reshape(2, 3, 4)
    tampil_info(arr3d)

    print("\nArray 1D dari angka 0 sampai 9:")
    arr5 = np.arange(10)
    tampil_info(arr5)

    print("\nArray dengan 31 titik yang terdistribusi merata antara 0 dan 30:")
    arr6 = np.linspace(0, 30, 31)
    tampil_info(arr6)

    print("\nArray acak dengan nilai antara 0–1 dan bentuk (2, 3):")
    arr7 = np.random.rand(2, 3)
    tampil_info(arr7)

    print("\nReshape array 1D dan buat array baru dengan bentuk sama dan isi 1:")
    arr8 = arr.reshape(4)
    arr8ini = np.ones_like(arr8)
    tampil_info(arr8ini)

    print("\nArray 3D berisi angka 8 dengan shape (2, 2, 6):")
    arr9 = np.full(shape=(2, 2, 6), fill_value=8)
    tampil_info(arr9)

    print("\nMatriks identitas 5x5:")
    arr10 = np.eye(N=5)
    tampil_info(arr10)
