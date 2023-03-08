from collections import *
from typing import List


# 换根DP
class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        cnt = Counter()
        for u, v in guesses:
            cnt[(u, v)] += 1
        
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        m = ans = 0
        q = deque([(0, -1)])
        while q:
            u, p = q.popleft()
            for v in g[u]:
                if v == p: continue
                m += cnt[(u, v)]
                q.append((v, u))
        
        q = deque([(0, m)])
        visited = [False] * n
        visited[0] = True
        while q:
            u, m = q.popleft()
            if m >= k: ans += 1
            for v in g[u]:
                if visited[v]: continue
                visited[v] = True
                vm = m - cnt[(u, v)] + cnt[(v, u)]
                q.append((v, vm))

        return ans

def solve() -> None:
    n = int(input())
    tree = [[] for _ in range(n)]
    # cnt = Counter()
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        tree[u].append((v, 1))
        tree[v].append((u, -1))

        # cnt[(v, u)] += 1

    ans = defaultdict(list)
    inv = 0

    q = deque([(0, -1)])
    while q:
        u, p = q.popleft()
        for v, c in tree[u]:
            if v == p: continue
            # inv += cnt[(u, v)]
            inv += int(c < 0)
            q.append((v, u))
    ans[inv].append(1)
    q = deque([(0, -1, inv)])
    while q:
        u, p, uc = q.popleft()
        for v, c in tree[u]:
            if v == p: continue
            vc = uc + c
            if vc < inv: inv = vc
            ans[vc].append(v+1)
            q.append((v, u, vc))

    print(inv)
    print(*sorted(ans[inv]))