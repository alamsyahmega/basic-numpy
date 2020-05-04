import numpy as np

# membuat matrix dengan tipe data tertentu
a_int = np.array(([1,2,3], [4,5,6]), dtype = int)
a_float = np.array(([1,2,3], [4,5,6]), dtype = float)
a_bool = np.array(([1,2,3], [4,5,6]), dtype = bool)

print(a_int)
print(a_float)
print(a_bool)


print("", end=("\n"*2))
# membuat array menggunakan function

def kuadrat(baris, kolom):
	return kolom**2

def jumlah(baris, kolom):
	return (kolom + baris)


b = np.fromfunction(kuadrat, (1,10), dtype=int)
c = np.fromfunction(jumlah, (4,4), dtype=float)

print(b)
print(c)


print("", end=("\n"*2))
# membuat array atau matrix dengan menggunakan iterable
iterable = (x**2 for x in range(5))

d = np.fromiter(iterable, dtype=int)
print(d, end="\n \n")


# multitype array

data = [
	('ucup', 150),
	('otong', 160),
	('mario', 180)
]

dtipe = [('nama', 'S255'), ('tinggi', int)]

e = np.array(data, dtype=dtipe)
print(e)
print(e[1])