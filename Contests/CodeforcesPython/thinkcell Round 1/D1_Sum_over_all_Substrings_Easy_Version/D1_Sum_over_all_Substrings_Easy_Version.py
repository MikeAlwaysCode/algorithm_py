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
    s = input()
    ans = 0
    for i in range(n):
        j = i
        cur = 0
        while j < n:
            if s[j] == '1':
                cur += 1
                ans += cur * min(3, n - j)
                j += 3
            else:
                j += 1
                ans += cur
    print(ans)


for _ in range(int(input())):
    solve()
