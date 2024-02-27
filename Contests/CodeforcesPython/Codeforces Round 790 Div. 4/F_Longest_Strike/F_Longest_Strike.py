import sys
from collections import Counter
from random import shuffle

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
    n, k = mint()
    nums = ints()
    shuffle(nums)
    cnt = Counter(nums)
    ans = l = r = -1
    i = 0
    s = sorted(cnt.keys())
    for j in range(len(s)):
        if cnt[s[j]] < k:
            i = j + 1
        elif j - i < s[j] - s[i]:
            i = j
        if j - i > ans:
            ans, l, r = j - i, s[i], s[j]
    
    if ans == -1:
        print(-1)
    else:
        print(l, r)


for _ in range(int(input())):
    solve()
