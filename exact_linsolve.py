from fractions import Fraction
from matrix_IO import *


def ref_(A):
    # R x C augmented matrix
    R = len(A)
    C = len(A[0])
    if not R + 1 == C:
        raise ValueError('not an augmented matrix')

    for k in range(R):
        # working on A[k][k] diagonal
        pivot_row = max(range(k, R), key=lambda i: abs(A[i][k]))
        A[k], A[pivot_row] = A[pivot_row], A[k]  # swap

        # assert A[k][k] != 0, 'singular matrix (no solutions, or infinitely many)'
        if A[k][k] == 0:
            continue

        # eliminate rows below main diagonal
        for i in range(k + 1, R):
            factor = A[i][k] / A[k][k]
            for j in range(k, C):
                A[i][j] -= factor * A[k][j]  # eliminate


def rref_(A):
    ref_(A)
    R = len(A)
    C = len(A[0])

    for k in reversed(range(R)):
        if A[k][k] == 0:
            continue
        A[k][k+1] /= A[k][k]
        A[k][k] = 1

        # eliminate rows above
        for i in range(k):
            if A[i][k] == 0:
                continue
            A[i][k+1] -= A[i][k] * A[k][k+1]
            A[i][k] = 0


matrix = read_matrix()
print_matrix(matrix)

R = len(matrix)
C = len(matrix[0])
for i in range(R):
    for j in range(C):
        matrix[i][j] = Fraction(matrix[i][j])

print()
print('RREF:')
rref_(matrix)
print_matrix(matrix)

print()
print('REF:')
ref_(matrix)
print_matrix(matrix)
