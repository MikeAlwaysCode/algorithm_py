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
    n = sint()
    nums = ints()
    suff = [0] * (n + 1)
    s = mx = 0
    for i in range(n - 1, -1, -1):
        s += nums[i]
        suff[i] = max(nums[i], suff[i + 1])
    ans = []
    for i, x in enumerate(nums, 1):
        if s - x == max(suff[i], mx) * 2:
            ans.append(i)
        mx = max(mx, x)
    
    print(len(ans))
    print(*ans)


solve()
