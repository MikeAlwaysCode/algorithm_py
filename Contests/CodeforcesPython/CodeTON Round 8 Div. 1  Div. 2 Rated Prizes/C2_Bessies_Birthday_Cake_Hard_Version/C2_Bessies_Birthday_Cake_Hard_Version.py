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
    n, x, y = mint()
    nums = ints()
    nums.sort()
    ans = x - 2
    odd = []
    even = 0
    for i in range(1, x):
        d = nums[i] - nums[i - 1] - 1
        if d == 1:
            ans += 1
        elif d & 1:
            odd.append(d)
        else:
            even += d // 2
    d = nums[0] + n - nums[-1] - 1
    if d == 1:
        ans += 1
    elif d & 1:
        odd.append(d)
    else:
        even += d // 2
    odd.sort()
    for d in odd:
        if y < d // 2:
            ans += y * 2
            y = 0
            break
        ans += d
        y -= d // 2
    ans += min(y, even) * 2
    print(ans)

for _ in range(int(input())):
    solve()
