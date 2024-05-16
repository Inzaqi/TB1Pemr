import re
from itertools import zip_longest

# Buka file dan baca matriks
with open('matrix.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    matriks = [file.readline().rstrip() for _ in range(n)]

# Transpose matriks dan gabungkan setiap baris dengan spasi
hasil_dekode = ''.join(''.join(col).strip() for col in zip_longest(*matriks, fillvalue=' '))

# Ganti pola yang cocok dengan spasi
hasil_dekode = re.sub(r'(?<=\w)\W+(?=\w)', ' ', hasil_dekode)

# Cetak hasil dekode
print(hasil_dekode)