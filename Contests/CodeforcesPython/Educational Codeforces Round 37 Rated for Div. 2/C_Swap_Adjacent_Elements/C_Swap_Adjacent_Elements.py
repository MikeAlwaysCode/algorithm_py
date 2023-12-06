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
    s = input()
    pre = i = 0
    while i < n:
        mn = mx = nums[i]
        j = i
        while j < n - 1 and s[j] == '1':
            j += 1
            mn, mx = min(mn, nums[j]), max(mx, nums[j])
        if mn < pre:
            print("NO")
            return
        pre, i = mx, j + 1
    print("YES")

solve()