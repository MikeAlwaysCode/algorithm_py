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
    
    if k == 1:
        print("Yes")
        return
    
    a = nums[-1] - nums[-2]
    for i in range(k - 3, -1, -1):
        na = nums[i+1] - nums[i]
        if na > a:
            print("No")
            return
        else:
            a = na
    
    print("Yes" if a * (n - k + 1) >= nums[0] else "No")

for _ in range(int(input())):
    solve()
