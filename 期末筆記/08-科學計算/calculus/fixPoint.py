def fixPoint(A, x, gap = 0.0000001):
    while (True):
        ax = A(x)
        if distance(x, ax) < gap:
            break
        x = ax

    return x

