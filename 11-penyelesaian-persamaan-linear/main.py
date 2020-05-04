import numpy as np

# soal
# y1 = 2.X1 + 3.X2
# y2 = X1 + 2.X2
# nilai y1 = 23, dan y2 = 14, berapa X1 dan X2 ?

# dalam matrix

# |y1| = | 2  3 | |X1|
# |y2| 	 | 1  2 | |X2|
# ==>
# |23| = | 2  3 | |X1|
# |14| 	 | 1  2 | |X2|


A = np.array([(2,3),(1,2)])
Y = np.array([23,14])
print(A)
print(Y)

A_inv = np.linalg.inv(A)

# menyelesaikan persamaan linear
X1 = np.dot(A_inv, Y)
print(X1) # nilai x1 dan x2

# cata lain
X2 = np.linalg.solve(A, Y)
print(X2) # nilai x1 dan x2