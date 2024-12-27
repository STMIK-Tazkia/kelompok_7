# Soal 1. Bagian nomor 10. Buatlah program untuk menghitung perkalian matrix 4x4
# Soal Perkalian matrix 4x4
matriksA = [
    [10, 55, 54, 10],
    [23, 5, 23, 14],
    [21, 7, 13, 11],
    [11, 88, 14, 15],
]

matriksB = [
    [3, 0, 0, 1],
    [3, 1, 0, 8],
    [8, 0, 1, 3],
    [1, 0, 0, 3]
]

# Proses perkalian matriks
hasil = [[sum(matriksA[i][k] * matriksB[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

# Menampilkan hasil perkalian
print("Hasil perkalian matriks:")
for baris in hasil:
    print(baris)