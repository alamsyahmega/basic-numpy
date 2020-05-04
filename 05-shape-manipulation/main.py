import numpy as np

a = np.array((
			[1,2,3],
			[4,5,6]
			))

print('matrix a dengan ukuran', a.shape)
print('matrix a:')
print(a)

# transpose matrix 3 cara
print('transpose matrix dari a:')
print(a.transpose())
print(np.transpose(a))
print(a.T)

# flatten array, -- > vector baris
print('flatten matrix a:')
print(a.ravel())
print(np.ravel(a))

# reshape matrix
print('reshape matrix a:')
print(a.reshape(3,2)) # harus sama value baris * kolomnya
print(a.reshape(6,1))

# resize matrix
# dapat merubah value a, dan mengambalikan None
print('resize matrix a:')
a.resize(3,2)
print(a) # berubah
print(a.resize(3,2)) # mengembalikan None
print('matrix a dengan ukuran', a.shape)
