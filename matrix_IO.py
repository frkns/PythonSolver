def read_matrix():
    print('Enter matrix, whitespace separated, enter twice to finish:')
    last = -1
    mat = []
    try:
        while True:
            line = list(map(int, input().split()))
            if not line:
                break
            assert last == -1 or len(line) == last
            last = len(line)
            mat.append(line)
    except EOFError:
        pass
    return mat


def print_matrix(A):
    S = []
    for row in A:
        srow = []
        for x in row:
            if isinstance(x, float):
                srow.append(f'{x:.1f}')
            else:
                srow.append(str(x))
        S.append(srow)

    width = max(len(x) for row in S for x in row)
    width += width // 2

    first = True
    for row in S:
        print(' '.join(x.rjust(width) for x in row))
