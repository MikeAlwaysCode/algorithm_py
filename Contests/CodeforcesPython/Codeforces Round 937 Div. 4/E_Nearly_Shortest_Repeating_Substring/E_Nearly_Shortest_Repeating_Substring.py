import sys
from collections import Counter

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
    s = input()
    for k in range(1, n // 2 + 1):
        if n % k:
            continue
        for i in (0, k):
            cnt = 0
            for j in range(n):
                cnt += s[i + (j % k)] != s[j]
            if cnt <= 1:
                print(k)
                return
    print(n)


for _ in range(int(input())):
    solve()
