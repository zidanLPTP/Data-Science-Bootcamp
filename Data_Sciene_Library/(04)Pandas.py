import pandas as pd
import numpy as np

def tampil_info(arr):
    """
    Menampilkan informasi penting tentang array NumPy.
    """
    print("Jumlah dimensi (ndim):", arr.ndim)
    print("Shape (bentuk):", arr.shape)
    print("Size (jumlah elemen):", arr.size)
    print("Tipe data elemen (dtype):", arr.dtype)
    print(arr.index)

sl1 = pd.Series([10, 11, 12, 13, 14], name="sl1")
print("sl1")
print(sl1)
tampil_info(sl1)
print("-" * 50)

sl2 = pd.Series([1, 2, 3, 4], index=['first', 'second','third', 'fourth'], name="sl2")
print("sl2")
print(sl2)
tampil_info(sl2)
print("-" * 50)

sl3 = pd.Series({'a': 3.9, 'b':4, 'c' : 5, 'd' : 6}, name='sl3')
print("sl3")
print(sl3)
tampil_info(sl3)
print("-" * 50)

sl4 = pd.Series(42, range(10+1), name='sl4')
print("sl4")
print(sl4)
tampil_info(sl4)
print("-" * 50)

sl5 = pd.Series([sl1[0], sl2['second'], sl3['c'], sl4[3]], name='sl5')
print("sl5")
print(sl5)
tampil_info(sl5)
print("-" * 50)