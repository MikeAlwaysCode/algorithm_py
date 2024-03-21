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
    n, d = mint()
    k, s = [0] * n, [0] * n
    for i in range(n):
        k[i], s[i] = mint()
    oq = list(range(n - 1, -1, -1))
    eat = [] # t, i
    nq = [] # k, t, s, i
    suff = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suff[i] = max(k[i], suff[i + 1])
    for t in range(1, d + 1):
        while eat and eat[0][0] < t:
            i = heappop(eat)[1]
            heappush(nq, (-k[i], t, s[i], i))
            
        # if nq and k[oq[-1]] < -nq[0][0]:
        if nq and suff[oq[-1]] < -nq[0][0]:
            i = heappop(nq)[3]
        else:
            i = oq.pop()
        
        if not oq:
            print(t)
            return
 
        heappush(eat, (t + s[i], i))
    print(-1)


for _ in range(int(input())):
    solve()
