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
    nums = ints()
    ans = n * (n - 1) // 2
    cnt = Counter(nums)
    p = [0] * (n + 1)
    for v in cnt.values():
        ans -= v * (v - 1) // 2
    for i in sorted(set(nums)):
        if p[i] == 1: continue
        for j in range(i + i, n + 1, i):
            if cnt[j]:
                if p[i] == 0:
                    ans -= cnt[i] * cnt[j]
                else:
                    ans += (p[i] - 1) * cnt[i] * cnt[j]
                cnt[i] += cnt[j]
                p[j] += 1
    print(ans)

for _ in range(int(input())):
    solve()