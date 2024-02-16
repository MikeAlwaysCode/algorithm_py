import sys
from bisect import *
# from collections import defaultdict

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

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def solve() -> None:
    n, m = mint()
    nums = ints()
    s = input()
    g = [[] for _ in range(n)]
    depth = [0] * (n)
    depth[0] = mxd = 1
    for i, p in enumerate(nums, 1):
        g[p - 1].append(i)
        depth[i] = depth[p - 1] + 1
        mxd = max(mxd, depth[i])
    
    tin = [-1] * n
    tout = [-1] * n
    # xor = defaultdict(list)
    xor = [[(0, 0)] for _ in range(mxd + 1)]
    q = [0]
    t = 0
    while q:
        u = q[-1]
        if tin[u] == -1:
            t += 1
            tin[u] = t
            xor[depth[u]].append((t, xor[depth[u]][-1][1] ^ (1 << (ord(s[u]) - 97))))
            for v in g[u]:
                q.append(v)
        else:
            q.pop()
            t += 1
            tout[u] = t
    
    '''
    @bootstrap
    def dfs(x: int, p: int, d: int):
        nonlocal t
        t += 1
        tin[x] = t
        xor[d].append((t, xor[d][-1][1] ^ (1 << (ord(s[x]) - 97))))
        for y in g[x]:
            if y == p: continue
            yield dfs(y, x, d + 1)
        t += 1
        tout[x] = t
        yield

    dfs(0, -1, 1)
    '''

    for _ in range(m):
        u, h = mint()
        u -= 1
        if h > mxd or depth[u] == h or len(xor[h]) == 1:
            print("Yes")
            continue
        l = bisect(xor[h], (tin[u], -1))
        r = bisect(xor[h], (tout[u], -1))
        ans = xor[h][l - 1][1] ^ xor[h][r - 1][1]
        print("Yes" if ans == (ans & -ans) else "No")

solve()
