def lu(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    for i in range(n):
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]
    return L, U

A = np.array([[ЧИСЛА], [ЧИСЛА], [ЧИСЛА]], dtype='float')
L, U = 
np.allclose(A, L УМНОЖИТЬ U)
