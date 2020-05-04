import numpy as np

data = [
	('Panji', 29),
	('Dewa', 23),
	('Fariz', 26),
	('Fadel', 27),
	('Sony', 22)
]

dtipe = [('nama', 'S10'), ('umur', int)]

a = np.array(data, dtype=dtipe)

print("urutan berdasarkan nama:")
print(np.sort(a, order='nama'))
print("urutan berdasarkan umur:")
print(np.sort(a, order='umur'))