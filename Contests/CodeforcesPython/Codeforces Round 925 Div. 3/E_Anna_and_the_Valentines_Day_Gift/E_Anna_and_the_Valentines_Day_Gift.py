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
    zero = []
    s = 0
    for a in nums:
        sa = str(a)
        k = len(sa.rstrip('0'))
        s += k
        if k < len(sa):
            zero.append(len(sa) - k)
    zero.sort(reverse=True)
    for i in range(1, len(zero), 2):
        s += zero[i]
    print("Sasha" if s > m else "Anna")


for _ in range(int(input())):
    solve()
