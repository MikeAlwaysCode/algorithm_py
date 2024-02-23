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
    n, k, d = mint()
    nums = ints()
    v = ints()
    ans = sum(i == x for i, x in enumerate(nums, 1)) + (d - 1) // 2
    cnt = [0] * (n + 2)
    for i in range(min(d - 1, n * 2)):
        cnt[1] += 1
        cnt[v[i % k] + 1] -= 1
        res = cur = 0
        for j, x in enumerate(nums, 1):
            cur += cnt[j]
            if x + cur == j:
                res += 1
        res += (d - i - 2) // 2
        ans = max(ans, res)
    print(ans)


for _ in range(int(input())):
    solve()
