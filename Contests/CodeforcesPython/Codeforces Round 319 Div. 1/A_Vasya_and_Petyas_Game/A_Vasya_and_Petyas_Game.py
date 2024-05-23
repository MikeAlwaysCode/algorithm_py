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
    ans = []
    isprime = [True] * (n + 1)
    for i in range(2, n + 1):
        if not isprime[i]:
            continue
        v = i
        while v <= n:
            ans.append(v)
            v *= i
        for j in range(i + i, n + 1, i):
            isprime[j] = False
    print(len(ans))
    print(*ans)

solve()
