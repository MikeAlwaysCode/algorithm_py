import sys
from bisect import bisect

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

def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        else:
            z[i] = max(0, r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z

def solve() -> None:
    s = input()
    n = len(s)
    nxt = [n] * (n + 1)
    for i in range(n - 1, -1, -1):
        if s[i] != 'a':
            nxt[i] = i
        else:
            nxt[i] = nxt[i + 1]
    if nxt[0] == n:
        print(n - 1)
        return
    z = z_function(s[nxt[0]:])
    ans = 0
    for k in range(1, n - nxt[0] + 1):
        l = i = nxt[0]
        check = True
        while i < n:
            if nxt[i + k] == n:
                break
            ni = nxt[i + k]
            l = min(l, ni - i - k)
            i = ni
            if i + k > n or z[i - nxt[0]] < k:
                check = False
                break
        if check:
            ans += l + 1
    print(ans)


for _ in range(int(input())):
    solve()
