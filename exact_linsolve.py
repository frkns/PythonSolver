from sol_enum import Sol
from matrix_IO import *
from copy import deepcopy


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
        # find pivot
        for p in range(k, C):
            if A[k][p] != 0:
                break
        if A[k][p] == 0:
            continue

        # normalize this row
        for j in reversed(range(p, C)):
            A[k][j] /= A[k][p]

        # eliminate rows above
        for i in range(k):
            factor = A[i][p]
            if factor == 0:
                continue
            for j in range(p, C):
                A[i][j] -= factor * A[k][j]


def do_with_copy(f):
    def g(A, *a, **k):
        B = deepcopy(A)
        f(B, *a, **k)
        return B
    return g


ref = do_with_copy(ref_)
rref = do_with_copy(rref_)


def sol_type(A):
    rref(A)
    R = len(A)
    C = len(A[0])

    zero_row = False
    for i in range(R):
        if all(x == 0 for x in A[i][:-1]):
            zero_row = True
            if A[i][-1] != 0:
                return Sol.NONE

    return Sol.INFINITE if zero_row else Sol.UNIQUE


M = read_matrix(exact=True)
print_matrix(M)


nature = sol_type(M)
print()
print('Status:')
match nature:
    case Sol.NONE:
        print('    there are no solutions')
    case Sol.UNIQUE:
        print('    there is a unique solution')
    case Sol.INFINITE:
        print('    there are infinite solutions')

print()
print('RREF:')
print_matrix(rref(M))
