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
    nums.reverse()
    x = (1 << nums[0]) - 1
    more = False
    for i in range(1, n):
        if nums[i] < nums[i - 1] - 1:
            print(-1)
            return
        elif nums[i] == nums[i - 1] - 1:
            if not x & 1:
                print(-1)
                return
            x -= 1
            more = False
        elif more:
            print(-1)
            return
        else:
            d = nums[i] - nums[i - 1]
            low = (x & -x).bit_length() - 1
            if low > d + 1:
                print(-1)
                return
            x <<= d + 1 - low
            x -= 1
            more = True
    y = x
    for i in range(n - 1, -1, -1):
        if bin(y)[2:].count('1') != nums[i]:
            print(-1)
            return
        y += 1
    print(x)


for _ in range(int(input())):
    solve()
