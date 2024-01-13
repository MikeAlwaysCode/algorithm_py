import sys
from collections import deque

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

def solve() -> None:
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(input())
    
    visited = [False] * n

    ans = n
    res = []
    clique = []
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        con = []
        q = deque([i])
        while q:
            x = q.popleft()
            cnt = 0
            for j in range(n):
                if matrix[x][j] == '1':
                    cnt += 1
                    if not visited[j]:
                        q.append(j)
                        visited[j] = True
            con.append((cnt, x + 1))

        if len(con) == n:
            print(0)
            return

        con.sort()
        if con[0][0] == len(con) - 1:
            cur = len(con)
            _, cres = map(list, zip(*con))
            clique.append(cres[0])
        else:
            cur = 1
            cres = [con[0][1]]

        if cur < ans:
            ans = cur
            res = cres
        if ans == 1:
            break
    
    # If there are exactly 2 connected components, 
    # then apparently we will have to operate on all vertices in a connected component. 
    # So we'll choose the smaller connected component to operate, 
    # and the answer is exactly the size of it.
    # Otherwise, we can arbitrarily choose two vertices 
    # from two different connected components and operate on them. 
    # The answer is 2.
    if ans > 1 and len(clique) > 2:
        ans = 2
        res = clique[:2]

    print(ans)
    print(*res)


for _ in range(int(input())):
    solve()