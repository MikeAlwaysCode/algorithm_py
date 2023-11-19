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
    n, q, MOD = mint()
    a = [0] + ints()
    b = [0] + ints()
    cnt0 = 0
    
    a = list((x - y) % MOD for x, y in zip(a, b))
    
    for i in range(n, 1, -1):
        a[i] = (a[i] - a[i - 1] - a[i - 2]) % MOD
        
        if a[i] == 0: cnt0 += 1

    if a[1] == 0: cnt0 += 1
        
    f = [0] * (n + 2)
    f[1] = 1
    for i in range(2, n + 2):
        f[i] = (f[i - 1] + f[i - 2]) % MOD

    def update(i: int, x: int):
        nonlocal cnt0
        if i > n:
            return
        if a[i] == 0:
            cnt0 -= 1
        a[i] = (a[i] + x) % MOD
        if a[i] == 0:
            cnt0 += 1

    for _ in range(q):
        qry = input().split()
        sgn = 1 if qry[0] == 'A' else -1
        l, r = int(qry[1]), int(qry[2])
        update(l, sgn)
        update(r + 1, -f[r - l + 2] * sgn)
        update(r + 2, -f[r - l + 1] * sgn)
        print("YES" if cnt0 == n else "NO")


solve()