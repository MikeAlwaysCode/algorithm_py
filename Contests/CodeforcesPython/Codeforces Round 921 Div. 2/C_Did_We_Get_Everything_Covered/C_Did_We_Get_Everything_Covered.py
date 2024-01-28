import sys
from string import ascii_lowercase

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
    n, k, m = mint()
    s = input()
    cnt = 0
    ch = set()
    ans = []
    for c in s:
        ch.add(c)
        if len(ch) == k:
            ans.append(c)
            cnt += 1
            ch.clear()
    if cnt >= n:
        print("YES")
    else:
        print("NO")
        for c in ascii_lowercase[:k]:
            if c not in ch:
                ans.append(c * (n - cnt))
                break
        print("".join(ans))

for _ in range(int(input())):
    solve()