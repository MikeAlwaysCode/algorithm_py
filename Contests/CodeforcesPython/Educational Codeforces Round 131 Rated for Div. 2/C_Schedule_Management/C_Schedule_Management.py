import sys
# from heapq import *

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
    arr = ints()
    cnt = [0] * n
    for x in arr:
        cnt[x - 1] += 1
    
    def check(x: int) -> bool:
        ex = 0
        for v in cnt:
            if v >= x:
                ex += v - x
            else:
                ex -= (x - v) // 2
        return ex <= 0
    
    l, r = 0, m * 2
    while l < r:
        mid = (l + r) >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1
    print(r)
    
    '''
    cnt = [0] * n
    val = [0] * n
    for a in arr:
        cnt[a - 1] += 1
        val[a - 1] += 1
    h = []
    l = []
    for i, c in enumerate(cnt):
        h.append((-c, i))
        l.append((c, i))
    
    heapify(h)
    heapify(l)
    
    while cnt[h[0][1]] and l[0][0] + 2 <= - h[0][0] - 1:
        mn, i = heappop(l)
        mx, j = heappop(h)
        mn += 2
        mx += 1
        val[i] += 2
        val[j] -= 1
        cnt[j] -= 1
        heappush(l, (mn, i))
        heappush(h, (mx, j))
        while l[0][0] != val[l[0][1]]:
            mn, i = heappop(l)
            mn = val[i]
            heappush(l, (mn, i))
        while -h[0][0] != val[h[0][1]]:
            mx, j = heappop(h)
            mx = - val[j]
            heappush(h, (mx, j))

    print(-h[0][0])
    '''

for _ in range(int(input())):
    solve()
