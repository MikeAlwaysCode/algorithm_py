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
    n, k = map(int, input().split())
    s = input()
    t = input()
    
    cnt = Counter()
    for i in range(n):
        if i >= n - k and i < k and s[i] != t[i]:
            print("NO")
            return
        cnt[s[i]] += 1
        cnt[t[i]] -= 1
    print("YES" if all(v == 0 for v in cnt.values()) else "NO")

for _ in range(int(input())):
    solve()
