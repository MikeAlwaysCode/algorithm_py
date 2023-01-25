from collections import deque


def topoSort(k: int, conditions: list[list[int]]) -> list[int]:
    incnt = [0] * k
    edge = [[] for _ in range(k)]
    for a, b in conditions:
        incnt[a] += 1
        edge[b].append(a)
    
    ans = [0] * k
    cnt = 0
    q = deque(i for i, v in enumerate(incnt) if v == 0)
            
    while q:
        cur = q.popleft()
        
        ans[cnt] = cur
        cnt += 1
        
        for x in edge[cur]:
            incnt[x] -= 1
            if incnt[x] == 0:
                q.append(x)
    
    return ans if cnt == k else []
