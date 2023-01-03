from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

def solve() -> None:
    n = int(input())

    tree = [[] for _ in range(n+1)]

    k = 1
    for _ in range(n-1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
        if u == 1 or v == 1:
            k += 1

    # print(tree)
    subtree = [[] for _ in range(k)]

    # def dfs(cur: int, sub: int, x: int, p: int):
    #     if x == 1:
    #         cur = sub
    #     for v in tree[x]:
    #         if v == p:
    #             continue
    #         if p != -1:
    #             subtree[cur].append((p, v))
    #         if x == 1:
    #             cur += 1
    #         dfs(sub, cur, v, x)
    # 
    # dfs(0, 0, 1, -1)

    # bfs
    q = [(1, -1, 0, 0)]
    while q:
        tmp = q
        q = []
        for x, p, cur, sub in tmp:
            if x == 1:
                cur = sub
            for v in tree[x]:
                if v == p:
                    continue
                if p != -1:
                    subtree[cur].append((p, v))
                if x == 1:
                    cur += 1
                q.append((v, x, sub, cur))

    print(k)
    for i in range(k):
        print(len(subtree[i]) + 1)
        for e in subtree[i]:
            print(*e)

# t = int(input())
# for _ in range(t):
solve()