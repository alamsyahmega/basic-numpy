import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

aMat = np.zeros((2,2))
bMat = np.ones((2,2))

# stacking matrix (menumpuk matrix)

# horizontal
c = np.hstack((a,b))
print("c adalah:")
print(c)
# vertikal
d = np.vstack((a,b))
print("d adalah:")
print(d)

cMat = np.hstack((aMat, bMat))
dMat = np.vstack((aMat, bMat))

print("matrix cMat:")
print(cMat)
print("matrix dMat:")
print(dMat)


# catatan:
# apabila matrix berbeda baris atau kolom
# hstack : berbeda kolom tidak masalah, asal tidak berbeda baris
# vstack : berbeda baris tidak masalah, asal tidak berbeda kolom
# ukuran = matrix.shape = (baris, kolom)