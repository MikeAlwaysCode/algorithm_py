import math
import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, x, p = mint()
    less = more = 0
    l, r = 0, n
    while l < r:
        mid = (l + r) >> 1
        if mid <= p:
            l = mid + 1
            less += 1
        else:
            r = mid
            more += 1

    # print(less, more)
    
    if x < less:
        print(0)
        return
    
    a = math.perm(x - 1, less - 1) % MOD
    b = math.perm(n - x, more) % MOD
    c = math.factorial(n - less - more) % MOD
    ans = (a * b * c) % MOD
    
    print(ans)

solve()
