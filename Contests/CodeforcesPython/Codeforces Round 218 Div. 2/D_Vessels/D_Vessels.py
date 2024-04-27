import sys
from heapq import *

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

def solve() -> None:
    n = sint()
    arr = ints()
    vol = [0] * n

    fa = list(range(n+1))
    def find(x):
        cur = x
        while x != fa[x]:
            x = fa[x]
        if fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x

    m = sint()
    
    for _ in range(m):
        query = ints()
        if query[0] == 1:
            p, x = query[1] - 1, query[2]
            p = find(p)

            while x and p < n:
                v = arr[p] - vol[p]
                if x > v:
                    x -= v
                    vol[p] = arr[p]
                    fa[p] = find(p+1)
                    p = fa[p]
                else:
                    vol[p] += x
                    break
        else:
            k = query[1] - 1
            print(vol[k])


solve()
