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
    n, q = mint()
    s = input()
    pres = [0] * (n + 1)
    for i in range(n - 1):
        pres[i + 1] = pres[i]
        if s[i] == s[i + 1]:
            pres[i + 1] += 1
    
    for _ in range(q):
        l, r = mint()
        ans = pres[r - 1] - pres[l - 1]
        print(ans)

solve()