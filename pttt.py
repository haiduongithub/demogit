import numpy as np

# Tạo ma trận hệ số và vectơ hằng số

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([1, 2, 3])

# Giải hệ phương trình

x = np.linalg.solve(A, b)

# Hiển thị nghiệm

print(x)
