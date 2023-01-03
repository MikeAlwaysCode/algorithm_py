from collections import Counter, defaultdict

def solve() -> None:
    MOD = 10 ** 9 + 7

    n, c = map(int, input().split())
    edge = [[] for _ in range(n+1)]
    
    for _ in range(n-1):
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)
    
    ans = c
    def dfs(x, p):
        nonlocal ans
        
        tc = c - 2 + (p < 0)
        for v in edge[x]:
            if v == p:
                continue
            
            ans *= tc
            ans %= MOD
            tc -= 1
            dfs(v, x)

    # dfs(1, -1)

    # bfs
    q = [1]
    visit = [False] * (n + 1)
    visit[1] = True
    while q:
        tmp = q
        q = []
        for x in tmp:
            tc = c - 2 + (x == 1)
            for v in edge[x]:
                if visit[v]:
                    continue
                visit[v] = True
                ans *= tc
                ans %= MOD
                tc -= 1
                q.append(v)

    print(ans)


# t = int(input())
# for _ in range(t):
solve()