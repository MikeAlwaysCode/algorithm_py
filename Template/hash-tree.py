
from collections import Counter


def solve() -> None:
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        
    # 栈模拟构建DFS序
    parent = [-1] * n
    order = [0]
    stack = [0]
    while stack:
        u = stack.pop()
        for v in g[u]:
            if v == parent[u]: continue
            parent[v] = u
            order.append(v)
            stack.append(v)
    
    seen = dict()
    hash_val = [0] * n
    idx = 0

    for u in order[::-1]:
        children = []
        for v in g[u]:
            if v == parent[u]: continue
            children.append(hash_val[v])
        code = tuple(sorted(children))
        if code not in seen:
            idx += 1
            seen[code] = idx
        hash_val[u] = seen[code]

    u = 0
    while True:
        cnt = Counter()
        for v in g[u]:
            if v == parent[u]: continue
            cnt[hash_val[v]] += 1
        c = 0
        for v in cnt.values():
            if v & 1: c += 1
        
        if c == 0:
            print("YES")
            return
        if c > 1:
            print("NO")
            return
        
        for v in g[u]:
            if v == parent[u]: continue
            if cnt[hash_val[v]] & 1:
                u = v
                break