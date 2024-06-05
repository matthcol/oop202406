import numpy as np

# class: numpy.ndarray
#   attributes: shape, dtype, flags, data
# objects: matrix1, matrix2, matrix3
matrix1 = np.random.normal(10, 3, (1000, 1000))
matrix2 = np.zeros((100, 100))
matrix3 = np.ones((10, 10))

for m in matrix1, matrix2, matrix3:
    print("shape:", m.shape)
    print("min:", m.min())
    print("max:", m.max())
    print("sum:", m.sum())
    print("mean:", m.mean())
    print("std:", m.std())
    m[0,0] = 3.1459
    print()

extract = matrix1[:10, :10]
res = extract.dot(matrix3)
