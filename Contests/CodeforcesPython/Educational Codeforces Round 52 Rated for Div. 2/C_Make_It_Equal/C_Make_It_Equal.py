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
    n, k = mint()
    nums = ints()
    nums.sort(reverse=True)
    ans = s = 0
    for i in range(1, n):
        d = nums[i - 1] - nums[i]
        if s + d * i <= k:
            s += d * i
        else:
            d -= (k - s) // i
            ans += 1 + d // (k // i)
            s = (d % (k // i)) * i
    if s:
        ans += 1
    print(ans)

solve()
