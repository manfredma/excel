import numpy as np


if __name__ == '__main__':
    array1 = np.array([10, 100, 1000.])
    array2 = np.array([[1, 2, 3.], [4, 5, 6]])
    print(array1.dtype)
    print(array2.dtype)
    print(float(array1[0]))
    print(array2 + 1)
    print(array2 * array2)
    print(array2 * array1)
    print("矩阵的积：",  (array2 @ array2.T))
    print(np.sqrt(array2))
    print(array2.sum())
    print(array1[1])
    print(array2[0, 0])
    print(array2[:, 1:])
    print(np.arange(2 * 10).reshape(2, 10))
    print(np.random.rand(2, 5))
