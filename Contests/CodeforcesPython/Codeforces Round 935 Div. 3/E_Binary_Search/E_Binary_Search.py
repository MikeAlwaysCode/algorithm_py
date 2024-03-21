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
    n, x = mint()
    nums = ints()
    used = [False] * n
    l, r = 1, n + 1
    while l + 1 < r:
        mid = (l + r) >> 1
        used[mid - 1] = True
        if nums[mid - 1] <= x:
            l = mid
        else:
            r = mid
    if nums[l - 1] == x:
        print(0)
        return
    
    idx = nums.index(x)
    ans = [(idx + 1, l)]
    if used[idx] and (nums[idx] <= x) != (nums[l - 1] <= x):
        for i in range(n):
            if not used[i] and (nums[idx] <= x) == (nums[i] <= x):
                ans.append((idx + 1, i + 1))
                break
    print(len(ans))
    for r in ans:
        print(*r)


for _ in range(int(input())):
    solve()
