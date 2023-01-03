from threading import local


class edge:
    to = next = 0

    def __init__(self) -> None:
        self.to = 0
        self.next = 0

n = int(input())

edges = [edge() for _ in range(n*2)]
head = [0] * (n*2)
cnt = 0

def add(u: int, v: int) -> None:
    global cnt
    cnt += 1
    edges[cnt].next = head[u]
    edges[cnt].to = v
    head[u] = cnt   # 节点u对应的边所在edges中的index
    
for _ in range(n-1):
    u, v = map(int, input().split())
    add(u, v)
    add(v, u)
    
# 所有点的深度之和等于所有点的子树大小之和，不需要求深度
# depth = [0] * (n+1)
size = [1] * (n+1)
dp = [0] * (n+1)

def dfs1(x: int, p: int):
    i = head[x]
    while i:
        v = edges[i].to
        if v != p:
            dfs1(v, x)
            size[x] += size[v]
        i = edges[i].next

def dfs2(x: int, p: int):
    i = head[x]
    while i:
        v = edges[i].to
        if v != p:
            dp[v] = dp[x] + n - 2 * size[v]
            dfs2(v, x)
        i = edges[i].next

dfs1(1, 0)

for i in range(1, n+1):
    dp[1] += size[i]

dfs2(1, 0)

depth = 0
ans = 1
for i in range(1, n+1):
    if dp[i] > depth:
        depth = dp[i]
        ans = i
# print(dp)
print(ans)
'''
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs1(x: int, p: int):
    # depth[x] = depth[p] + 1;
    for v in tree[x]:
        if v != p:
            dfs1(v, x)
            size[x] += size[v]
            # dp[x] += dp[v] + size[v]

def dfs2(x: int, p: int):
    for v in tree[x]:
        if v != p:
            dp[v] = dp[x] + n - 2 * size[v]
            dfs2(v, x)

dfs1(1, 0)

for i in range(1, n+1):
    dp[1] += size[i]

dfs2(1, 0)

depth = 0
ans = 1
for i in range(1, n+1):
    if dp[i] > depth:
        depth = dp[i]
        ans = i
# print(dp)
print(ans)
'''