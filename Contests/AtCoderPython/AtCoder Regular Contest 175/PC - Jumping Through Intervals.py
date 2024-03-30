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
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    L, R = [0] * n, [0] * n
    for i in range(n):
        L[i], R[i] = mint()

    ans = [-1] * n
    j = 0
    l, r = -math.inf, math.inf
    pre = None
    for i in range(n):
        if R[i] < l or L[i] > r:
            cur = R[i] < l
            if pre is None:
                nl = R[i]
                for k in range(i - 1, j - 1, -1):
                    if R[i] < l:
                        nl = ans[k] = max(L[k], nl)
                    else:
                        ans[k] = r
            elif pre == cur:
                if R[i] < l:
                    nl = R[i]
                    for k in range(i - 1, j - 1, -1):
                        nl = ans[k] = max(L[k], nl)
                else:
                    nl = L[j]
                    for k in range(j, i):
                        nl = ans[k] = max(L[k], nl)
            else:
                if R[i] < l:
                    k1 = j
                    nl = L[j]
                    while k1 < i:
                        nl = ans[k1] = max(L[k1], nl)
                        k1 += 1
                        if nl == l:
                            break
                    k2 = i - 1
                    nl = R[i]
                    while k2 >= k1:
                        nl = ans[k2] = max(L[k2], nl)
                        k2 -= 1
                else:
                    for k in range(j, i):
                        ans[k] = r
                    
            j = i
            l, r = L[i], R[i]
            pre = cur
        else:
            l = max(l, L[i])
            r = min(r, R[i])
    if j < n:
        ans[j] = r if pre else l
        nl = L[j]
        for k in range(j, n):
            if pre:
                ans[k] = r
            else:
                nl = ans[k] = max(L[k], nl)
    print(*ans)


solve()
