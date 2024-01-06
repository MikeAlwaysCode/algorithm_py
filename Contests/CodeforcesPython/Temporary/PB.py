import math
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

def getPrimes(n: int) -> list[int]:
    primes = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            primes.append(d)
            while n % d == 0:
                n //= d
        if n == 1:
            break
        d += 1
    if n > 1:
        primes.append(n)
    return primes

def solve() -> None:
    a, b = mint()
    ans = math.lcm(a, b)
    if b % a == 0:
        p = set(getPrimes(a) + getPrimes(b))
        ans *= min(p)
    print(ans)


for _ in range(int(input())):
    solve()