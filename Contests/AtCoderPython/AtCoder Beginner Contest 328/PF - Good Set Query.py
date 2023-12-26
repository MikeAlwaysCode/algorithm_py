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
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, q = mint()

    parent = list(range(n + 1))
    weight = [0] * (n + 1)

    def find(x: int):
        cur = x
        s = weight[x]
        while x != parent[x]:
            x = parent[x]
            s += weight[x]

        while parent[cur] != x:
            s -= weight[cur]
            weight[cur] += s
            parent[cur], cur = x, parent[cur]
        return x

    def union(x: int, y: int, w: int) -> bool:
        fx, fy = find(x), find(y)
        if fx == fy: return weight[y] - weight[x] == w
        parent[fx] = fy
        weight[fx] = weight[y] - weight[x] - w
        return True

    ans = []
    for i in range(1, q + 1):
        a, b, d = mint()
        if union(a, b, d):
            ans.append(i)
        
    print(*ans)

solve()