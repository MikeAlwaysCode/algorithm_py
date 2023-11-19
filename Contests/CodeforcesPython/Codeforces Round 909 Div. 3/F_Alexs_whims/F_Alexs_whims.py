import sys

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
    n, q = mint()
    m = list(range(1, n + 1))
    l = []
    for i in range(1, n):
        print(i, i + 1)
    for _ in range(q):
        d = sint()
        if len(m) - 1 == d or len(l) + 1 == d:
            print(-1, -1, -1)
        elif d > len(m) - 1:
            k = d - len(m) + 1
            v = 2 if k >= len(l) else l[-k-1]
            print(l[-k], v, m[-1])
            m += l[-k:]
            l = l[:-k]
        else:
            k = len(m) - 1 - d
            v = 2 if not l else l[-1]
            print(m[-k], m[-k-1], v)
            l += m[-k:]
            m = m[:-k]


for _ in range(int(input())):
    solve()