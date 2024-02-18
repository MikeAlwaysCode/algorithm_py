import sys
from itertools import accumulate

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
    s = list(input())
    pres = sum(map(int, s))
    carry = 0
    for i in range(n - 1, -1, -1):
        carry += pres
        pres -= int(s[i])
        s[i] = str(carry % 10)
        carry //= 10
    if carry:
        print(str(carry) + "".join(s))
    else:
        print("".join(s).lstrip('0'))


for _ in range(int(input())):
    solve()
