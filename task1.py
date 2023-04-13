def matrix(n=1, m=None, value=0):
    if m == None:
        m = n
    k = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            k[i][j] = value
    return k