import sys
from functools import cache

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
    # find n - 1
    mx = 0
    for i in range(1, n):
        print('?', mx, mx, i, i, flush=True)
        res = input()
        if res == '<':
            mx = i
    # find or max
    stk = []
    if mx == 0:
        stk.append(1)
    else:
        stk.append(0)
    for i in range(n):
        if i == mx or i == stk[-1]:
            continue
        print('?', mx, stk[-1], mx, i, flush=True)
        res = input()
        if res == '<':
            stk.clear()
            stk.append(i)
        elif res == '=':
            stk.append(i)
    mn = stk[0]
    for i in stk[1:]:
        print('?', mn, mn, i, i, flush=True)
        res = input()
        if res == '>':
            mn = i
    print('!', mn, mx, flush=True)


for _ in range(int(input())):
    solve()