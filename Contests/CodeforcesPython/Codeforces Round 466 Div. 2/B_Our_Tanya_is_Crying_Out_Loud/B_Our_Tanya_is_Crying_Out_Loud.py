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
    k = sint()
    a = sint()
    b = sint()
    ans = 0
    while n > 1:
        if n % k:
            if n < k:
                ans += (n - 1) * a
                n = 1
            else:
                ans += a * (n % k)
                n = n // k * k
        else:
            m = n // k
            if (n - m) * a <= b:
                ans += (n - 1) * a
                n = 1
            else:
                ans += b
                n = m
    print(ans)


solve()
