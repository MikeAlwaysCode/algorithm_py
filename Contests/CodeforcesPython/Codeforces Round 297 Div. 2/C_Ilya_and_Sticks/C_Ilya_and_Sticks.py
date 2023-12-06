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
    nums.sort(reverse = True)
    ans = l0 = l1 = 0
    for x in nums:
        if l0 == x or l0 == x + 1:
            if l1:
                ans += x * l1
                l1 = 0
            else:
                l1 = x
            l0 = 0
        else:
            l0 = x
    print(ans)

solve()