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
    l0 = l1 = 0
    r1 = s.count('1')
    r0 = n - r1
    d = n
    ans = -1
    if r1 >= r0:
        ans, d = 0, n / 2
    for i, c in enumerate(s, 1):
        if c == '1':
            l1 += 1
            r1 -= 1
        else:
            l0 += 1
            r0 -= 1
        if l0 >= l1 and r1 >= r0:
            if abs(n // 2 - i) < d:
                ans, d = i, abs(n / 2 - i)
    print(ans)


for _ in range(int(input())):
    solve()
