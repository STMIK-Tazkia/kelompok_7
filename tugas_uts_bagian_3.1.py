# Soal bagian 3, nomor 1. Buat fungsi untuk mengurutkan himpunan A dengan menggunakan buble sort
def bubble_sort(A):
    # Mengubah himpunan menjadi list agar bisa diurutkan
    A = list(A)

    n = len(A)
    for i in range(n):
        # Flag untuk mengecek jika ada perubahan dalam iterasi ini
        swapped = False
        
        # Loop untuk perbandingan elemen yang bersebelahan
        for j in range(0, n-i-1):
            # Jika elemen lebih besar dari elemen berikutnya, tukar
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True
        
        # Jika tidak ada yang ditukar, berarti sudah terurut
        if not swapped:
            break
    
    return A

# Himpunan A
A = {109, 222, 120, 150, 200, 321, 410, 120, 230, 300, 111, 89, 70, 45, 57, 31, 39, 900, 21, 378, 400, 101, 201, 301, 1}

# Mengurutkan himpunan A menggunakan Bubble Sort
sorted_A = bubble_sort(A)
print(sorted_A)