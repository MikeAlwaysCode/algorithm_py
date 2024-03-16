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
    n, m = mint()
    nums = ints()

    if n > m:
        print("YES")
        return
    
    dp = [False] * m
    dp[0] = True
    for x in nums:
        tmp = dp[:]
        for i in range(m):
            if not dp[i]: continue
            if (i + x) % m == 0:
                print("YES")
                return
            tmp[(i + x) % m] = True
        dp = tmp

    print("NO")

solve()
