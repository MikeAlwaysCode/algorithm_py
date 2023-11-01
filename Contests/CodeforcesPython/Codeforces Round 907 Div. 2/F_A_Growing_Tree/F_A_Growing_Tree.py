import sys

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

class BIT:
    def __init__(self, n: int):
        self.nums = [0] * (n + 1)
        self.n = n
        self.BITree = [0] * (self.n + 1)
        
    def lowbit(self, x: int) -> int:
        return x & -x
    
    def query(self, x: int) -> int:
        ans = 0
        while x:
            ans += self.BITree[x]
            x -= self.lowbit(x)
        return ans

    def add(self, x: int, val: int):
        while x <= self.n:
            self.BITree[x] += val
            x += self.lowbit(x)

def solve() -> None:
    q = sint()
    bit = BIT(q)

    g = [[] for _ in range(q + 1)]
    update = [[] for _ in range(q + 1)]
    time = [q] * (q + 1)
    n = 1

    for t in range(q, 0, -1):
        qry = ints()
        if qry[0] == 1: # add vertex
            u = qry[1] - 1
            v = n
            n += 1
            g[u].append(v)
            g[v].append(u)
            # 记录添加节点v的时间戳
            time[v] = t
        else:
            u, k = qry[1] - 1, qry[2]
            update[u].append((t, k))
    
    ans = [0] * n
    parent = [-1] * n
    stk = [0]
    while stk:
        u = stk.pop()
        if u >= 0:
            stk.append(~u)
            for t, k in update[u]:
                bit.add(t, k)
            # 祖先节点的变更且在添加节点u之后的变化
            ans[u] = bit.query(time[u])
            for v in g[u]:
                if v == parent[u]: continue
                parent[v] = u
                stk.append(v)
        else:
            # 遍历完u的所有子树后，把u的变化回退
            for t, k in update[~u]:
                bit.add(t, -k)
    print(*ans)

for _ in range(int(input())):
    solve()