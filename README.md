## Quantum Approximate Optimization Algorithm (QAOA)

Quantum Approximate Optimization Algorithm (QAOA) merupakan algoritma hibrida yang menggabungkan operasi kuantum dengan teknik optimisasi klasikal menyelesaikan masalah optimisasi kombinatorial. 

### Komponen Teknis Utama

1. **Pernyataan Masalah**: QAOA digunakan terutama untuk menangani masalah optimisasi kombinatorial seperti *traveling salesman problem* (TSP), *max-cut*, dan *knapsack problem*.

2. **Struktur Sirkuit Kuantum**: QAOA diimplementasikan sebagai sirkuit kuantum yang diparameterisasi. Sirkuit ini terdiri dari lapisan-lapisan dengan dua jenis gerbang kuantum:
   
   - ***Mixing Hamiltonian (Driver Hamiltonian)***: Gerbang-gerbang ini menjelajahi lanskap masalah dan mengarahkan keadaan kuantum menuju solusi-solusi yang mungkin.
   - ***Problem Hamiltonian (Cost Hamiltonian)***: Gerbang-gerbang ini mengkodekan fungsi tujuan masalah optimisasi ke dalam sirkuit kuantum.

3. ***Variational Ansatz***: Sirkuit memiliki parameter-parameter yang disesuaikan secara sistematis untuk mencari kombinasi optimal yang meminimalkan fungsi biaya.

4. **Prosedur Optimisasi**: Algoritma optimisasi klasikal digunakan untuk memperbarui parameter-parameter dalam sirkuit kuantum.

5. **Pengukuran dan Pengambilan Sampel**: Setelah mengoptimalkan parameter, sirkuit kuantum diukur untuk mendapatkan distribusi probabilitas solusi-solusi yang mungkin.

6. **Perangkat Kuantum**: QAOA memerlukan akses ke komputer kuantum atau simulator kuantum.

7. **Kompleksitas**: Kompleksitasnya bergantung pada masalah optimisasi yang spesifik dan kedalaman sirkuit kuantum.
