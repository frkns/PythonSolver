from fractions import Fraction
from matrix_IO import *
from copy import deepcopy
from enum import Enum


class Sol(Enum):
    NONE = 0
    UNIQUE = 1
    INFINITE = 2


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

        # normalize this row
        for j in reversed(range(k, C)):
            A[k][j] /= A[k][k]

        # eliminate rows above
        for i in range(k):
            factor = A[i][k]
            if factor == 0:
                continue
            for j in range(k, C):
                A[i][j] -= factor * A[k][j]

    # # renormalize all rows
    # for i in range(R):
    #     for j in range(C):
    #         if A[i][j] != 0:
    #             for k in reversed(range(j, C)):
    #                 A[i][k] /= A[i][j]
    #             break


def sol_type_(A):
    rref_(A)


def do_with_copy(f):
    def g(A, *a, **k):
        B = deepcopy(A)
        f(B, *a, **k)
        return B
    return g


ref = do_with_copy(ref_)
rref = do_with_copy(rref_)
sol_type = do_with_copy(sol_type_)


matrix = read_matrix()
print_matrix(matrix)

R = len(matrix)
C = len(matrix[0])
for i in range(R):
    for j in range(C):
        matrix[i][j] = Fraction(matrix[i][j])

print()
print('RREF:')
print_matrix(rref(matrix))
