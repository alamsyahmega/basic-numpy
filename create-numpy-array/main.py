import numpy as np

# lebih less RAM

# membuat vector numpy
a = np.array([1, 2, 3, 4, 5])
b = np.array([1.5, 2.5, 3, 4, 7]) # memakai koma

# membuat vector dengan range (range antara 1 - 10 dengan stepsize 2)
c = np.arange(1,10,2)

# membuat linspace (range antara 1 - 10, dibuat 4 dengan jarak yg sama)
d = np.linspace(1,10,4)

# array multidimensi/matrix
e = np.array([ (1,2,3) , (4,5,6) ])

# matrix dengan nilai nol ( (5,5) artinya 5 baris dan 5 kolom )
f = np.zeros((5,5))

# matrix dengan nilai 1 (sda)
g = np.ones((5,5))

# matrix identitas ( arg 5, berarti 5 x 5 )
h1 = np.identity(5)
h2 = np.eye(5)

