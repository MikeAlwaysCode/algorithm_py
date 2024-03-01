import sys
from heapq import *

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
    s = list(input())
    m = s.count('?')
    L, R = [0] * m, [0] * m
    for i in range(m):
        L[i], R[i] = mint()
    h = []
    cnt = ans = j = 0
    for i, c in enumerate(s):
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
        elif c == '?':
            cnt -= 1
            ans += R[j]
            s[i] = ')'
            heappush(h, (L[j] - R[j], i))
            j += 1
        if cnt < 0:
            if not h:
                print(-1)
                return
            v, pi = heappop(h)
            ans += v
            cnt += 2
            s[pi] = '('
    if cnt != 0:
        print(-1)
    else:
        print(ans)
        print("".join(s))

solve()
