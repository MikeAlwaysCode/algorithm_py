import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    k = 0
    x = n
    while x > 1:
        k += 1
        x = (x + 1) // 2
    qry = [[] for _ in range(k)]

    def zz(l: int, r: int, k: int):
        if l == r: return
        mid = (l + r) // 2
        qry[k].extend(list(range(l, mid + 1)))
        zz(l, mid, k + 1)
        zz(mid + 1, r, k + 1)

    zz(1, n, 0)

    print(k, flush=True)
    for i in range(k):
        print(len(qry[i]), *qry[i], flush=True)
    res = input()
    l, r = 1, n
    for c in res:
        mid = (l + r) // 2
        if c == '1':
            r = mid
        else:
            l = mid + 1
        if l == r:
            break
    print(l)

solve()
