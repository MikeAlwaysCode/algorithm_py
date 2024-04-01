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
    n, x, y = mint()
    nums = ints()
    nums.sort()
    cnt = Counter()
    for i in range(1, x):
        cnt[nums[i] - nums[i - 1] - 1] += 1
    cnt[nums[0] + n - nums[-1] - 1] += 1
    ans = x - 2 + cnt[1]
    L = sorted(cnt.keys())
    for i in L:
        if i < 2 or not i & 1:
            continue
        k = (i - 1) // 2
        if y < k:
            break
        m = min(y // k, cnt[i])
        cnt[i] -= m
        ans += m * i
        y -= k * m
    for i in L:
        if i < 2 or i & 1:
            continue
        k = i // 2
        if y < k:
            break
        m = min(y // k, cnt[i])
        cnt[i] -= m
        ans += m * i
        y -= k * m
    if y:
        for i in L:
            if i < 2:
                continue
            if cnt[i]:
                ans += y * 2 - 1
                break
    print(ans)

for _ in range(int(input())):
    solve()
