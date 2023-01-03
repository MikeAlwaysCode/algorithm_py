n, m = map(int, input().split())
a = list(map(int, input().split()))

r = [[0] * n for _ in range(2)]
k1 = 0
k2 = 0
for i in range(1, n):
    k1 += max(a[i-1] - a[i], 0)
    r[0][i] = k1
    ni = n - i - 1
    k2 += max(a[ni+1] - a[ni], 0)
    r[1][ni] = k2
    
for i in range(m):
    s, t = list(map(int, input().split()))
    # print(s, t)
    # step = 1 if s < t else -1
    # d = 0
    # for j in range(s-1, t-1, step):
    #     # print(j)
    #     d += max(a[j] - a[j+step], 0)
    index = 0 if s < t else 1
    print(r[index][t-1] - r[index][s-1])
