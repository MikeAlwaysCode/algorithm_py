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
    vis = unique = 0
    idx = 0
    for x in nums:
        vis, unique = vis | x, (~vis & x) | (unique & ~x)
    if unique == 0:
        print(*nums)
        return
    
    bit = unique.bit_length() - 1
    for i, x in enumerate(nums):
        if (x >> bit) & 1:
            idx = i
            break
    
    print(nums[i], *nums[:i], *nums[i + 1:])


solve()
