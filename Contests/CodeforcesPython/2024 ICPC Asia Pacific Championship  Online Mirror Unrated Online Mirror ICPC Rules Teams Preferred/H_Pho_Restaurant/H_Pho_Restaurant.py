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

def solve() -> None:
    n = sint()
    ans0 = ans1 = ans = left0 = left1 = 0
    mn = math.inf
    for _ in range(n):
        s = input()
        m = len(s)
        cnt = s.count('1')
        ans += min(cnt, m - cnt)
        if cnt < m - cnt:
            ans1 += cnt
            mn = min(mn, m - cnt * 2)
            left0 += 1
        elif m - cnt < cnt:
            ans0 += m - cnt
            mn = min(mn, cnt * 2 - m)
            left1 += 1
    if ans and ((ans0 == ans and left0 == 0) or (ans1 == ans and left1 == 0)):
        ans += mn
    print(ans)

solve()
