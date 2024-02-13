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

def calc(n: int, k: int) -> int:
    x, l = divmod(n, k)
    r = k - l
    return l * (l - 1) // 2 * (x + 1) * (x + 1) + r * (r - 1) // 2 * x * x + l * r * x * (x + 1)

def solve() -> None:
    n, b, x = mint()
    nums = ints()
    ans = s = 0
    mx = max(nums)
    cnt = [0] * (mx + 1)
    for a in nums:
        last = cur = 0
        for k in range(2, a + 1):
            cur = calc(a, k)
            cnt[k] += cur - last
            last = cur

    for k in range(2, mx + 1):
        s += cnt[k]
        ans = max(ans, s * b - (k - 1) * x)
    print(ans)

for _ in range(int(input())):
    solve()
