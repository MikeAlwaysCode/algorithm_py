import sys
from collections import *
from types import GeneratorType

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + "\n")
# endregion fastio

# # region interactive
# def printQry(a, b) -> None:
#     sa = str(a)
#     sb = str(b)
#     print(f"? {sa} {sb}", flush = True)

# def printAns(ans) -> None:
#     s = str(ans)
#     print(f"! {s}", flush = True)
# # endregion interactive

# region dfsconvert
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
# endregion dfsconvert

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = sint()
    tree = [[] for _ in range(n + 1)]
    # deg = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = mint()
        tree[u].append(v)
        tree[v].append(u)
        # deg[u] += 1
        # deg[v] += 1

    cnt = [0] * (n + 1)

    # DFS 920 ms
    @bootstrap
    def dfs(u: int, p: int) -> None:
        for v in tree[u]:
            if v == p: continue
            yield dfs(v, u)
            cnt[u] += cnt[v]
        if cnt[u] == 0: cnt[u] = 1
        yield
    
    dfs(1, 0)
    # print(cnt)
    '''
    # Topo 639 ms
    q = deque()
    for i in range(2, n + 1):
        if deg[i] == 1:
            cnt[i] = 1
            q.append(i)
    while q:
        x = q.popleft()
        for y in tree[x]:
            if y > 1 and deg[y] == 1: continue
            cnt[y] += cnt[x]
            deg[y] -= 1
            if deg[y] == 1 and y > 1:
                q.append(y)
    '''

    for _ in range(sint()):
        u, v = mint()
        print(cnt[u] * cnt[v])

for _ in range(int(input())):
    solve()