import numpy as np

a = np.array(([1,2],
			  [3,4]))
b = np.ones([2,2])

print('matrix a:')
print(a)
print('matrix b:')
print(b)

# perkalian matrix
c1 = np.dot(a,b)
c2 = a.dot(b)

print('matrix c1:', c1, sep='\n')
print('matrix c2:', c2, sep='\n')

# perkalian matrix beda baris atau column
e = np.array(([1, 2, 3],
			  [4, 5, 6]))
f = np.ones([3,1])

print('matrix e:')
print(e)
print('matrix e:')
print(f)

print('matrix e * matrix f:', e.dot(f), sep='\n')

