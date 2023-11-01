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
    ans = k
    m2 = 0
    for x in nums:
        if x % k == 0:
            print(0)
            return
        ans = min(ans, k - (x % k))
        if k == 4 and x % 2 == 0:
            m2 += 1
    if m2 >= 2:
        print(0)
    elif k == 4:
        print(min(ans, 2 - m2))
    else:
        print(ans)

for _ in range(int(input())):
    solve()