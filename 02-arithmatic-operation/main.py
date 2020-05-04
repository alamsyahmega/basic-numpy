import numpy as np

# list python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])


# INGAT BAHWA OPERASI ARITMATIKA UNTUK NUMPY BERSIFAT ELEMENTwISE ATAU OPERASINYA DILAKUKAN
# SATU PERSATU DARI TIAP-TIAP ELEMENTNYA

# Penjumlahan
addition_python_list = a + b
addition_numpy_array = anp + bnp # ELEMENTWISE operation

print("a + b =", addition_python_list)
print("anp + bnp =", addition_numpy_array)


# Pengurangan
# subtraction_python_list = b - a ; # error : TypeError: unsupported operand type(s) for -: 'list' and 'list'
subtraction_numpy_array = anp - bnp
print("anp - bnp =", subtraction_numpy_array)


# Perkalian
# multiplication_python_list = a * b ; # error TypeError: can't multiply sequence by non-int of type 'list'
multiplication_numpy_array = anp * bnp
print("anp * bnp =", multiplication_numpy_array)


# Pembagian
# division_python_list = a / b ; # error : TypeError: unsupported operand type(s) for /: 'list' and 'list'
division_numpy_array = anp / bnp
print("anp / bnp =", division_numpy_array)

# Kuadrat pada numpy
print("anp **2 =", anp**2)



# multidimensi array numpy (matrix)

c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))

# penjumlahan
np_jumlah = c + d
np_kali = c * d
print("multidimensi numpy penjumlahan c + d =", np_jumlah)
print("multidimensi numpy Perkalian c + d =", np_kali)

# NOTE : Di numpy aritmatika, operasinya adalah ELEMENTWISE, jadi saat melakukan
# Perkalian untuk matriks, itu masih dikali perelement, bukan perkalian matriks