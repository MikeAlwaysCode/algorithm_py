from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

n, m = map(int, input().split())
edges = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    edges[u-1].add(v-1)

s = set()
for i in range(n):
    if len(edges[i]) < 2:
        continue
    
    for j in edges[i]:
        for k in edges[j]:
            if k in edges[i]:
                s.add((i, j, k))

print(len(s))