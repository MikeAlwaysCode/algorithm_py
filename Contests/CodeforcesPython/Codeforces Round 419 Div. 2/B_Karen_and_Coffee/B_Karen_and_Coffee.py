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

mx = 2 * 10 ** 5 + 2

def solve() -> None:
    n, k, q = mint()
    d = [0] * mx
    for _ in range(n):
        l, r = mint()
        d[l] += 1
        d[r + 1] -= 1
    
    pres = [0] * mx
    cnt = 0
    for i in range(1, mx):
        cnt += d[i]
        pres[i] = pres[i - 1]
        if cnt >= k: pres[i] += 1
    
    for _ in range(q):
        l, r = mint()
        print(pres[r] - pres[l - 1])

solve()