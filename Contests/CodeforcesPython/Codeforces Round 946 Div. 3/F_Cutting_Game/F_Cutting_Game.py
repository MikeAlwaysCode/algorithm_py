import sys
# from heapq import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

T = "UDLR"

def solve() -> None:
    a, b, n, m = mint()
    h = [[] for _ in range(2)]
    for _ in range(n):
        x, y = mint()
        h[0].append((x, y))  # U D
        h[1].append((x, y)) # L R

    h[0].sort(key = lambda x: x[0])
    h[1].sort(key = lambda x: x[1])
    ans = [0] * 2

    bound = [1, a, 1, b]
    step = [1, -1, 1, -1]
    idx = [0, n - 1, 0, n - 1]

    for i in range(m):
        s = input().split()
        k = int(s[1])
        j = T.index(s[0])
        nb = bound[:]
        nb[j] += step[j] * k
        while idx[j & 2] <= idx[j | 1] and (h[j >> 1][idx[j]][0] < nb[0] or h[j >> 1][idx[j]][0] > nb[1] or h[j >> 1][idx[j]][1] < nb[2] or h[j >> 1][idx[j]][1] > nb[3]):
            x, y = h[j >> 1][idx[j]]
            if bound[0] <= x <= bound[1] and bound[2] <= y <= bound[3]:
                ans[i & 1] += 1
            idx[j] += step[j]
        bound = nb
    print(ans[0], ans[1])

for _ in range(int(input())):
    solve()
