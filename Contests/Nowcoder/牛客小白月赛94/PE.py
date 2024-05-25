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
    n, k = mint()
    v = [0] * n
    w = [0] * n
    for i in range(n):
        v[i], w[i] = mint()
    
    def check(x: int) -> bool:
        res = -1
        for i in range(n):
            if x & w[i] == x:
                res &= v[i]
        return 0 <= res <= k
    
    ans = 0
    for bit in range(30, -1, -1):
        if check(ans | 1 << bit):
            ans |= 1 << bit
    print(ans)

solve()
