# Multiply two matrices stored as 2d arrays
def matmul(p, q):
    r = [[] for x in range(len(p))]
    for i in range(len(p)):
        for j in range(len(q[0])):
            t = 0
            for k in range(len(q)):
                t += p[i][k] * q[k][j]
            r[i].append(t)
            print(i, r[i])
    return r

# p = [[1, 3, -4], [1, 1, -2], [-1, -2, 5]]
# q = [[8, 3, 0], [3, 10, 2], [0, 2, 6]]
# r = matmul(p, q)