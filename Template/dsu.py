# 模板一：封装成类
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n
    
    def findset(self, x: int) -> int:
        # if self.parent[x] == x:
        #     return x
        # self.parent[x] = self.findset(self.parent[x])
        # return self.parent[x]
        cur = x
        while x != self.parent[x]:
            x = self.parent[x]
        if cur != x:
            self.parent[cur] = x
        return x
    
    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y


# 模板二：
n = 10
fa = list(range(n + 1))
s = [0] * (n + 1)

def find(x: int):
    cur = x
    while x != fa[x]:
        x = fa[x]
    while fa[cur] != x:
        fa[cur], cur = x, fa[cur]
    return x

def union(fr: int, to: int):
    fa[find(fr)] = find(to)

# ans = [0] * n
# for i in range(n - 1, 0, -1):
#     x = removeQueries[i]
#     fa[x] = find(x + 1)
#     to = fa[x] 
#     s[to] += s[x] + nums[x]
#     ans[i-1] = max(ans[i], s[to])

# 模板三：
parent = list(range(n + 1))

def find(index: int) -> int:
    if parent[index] != index:
        parent[index] = find(parent[index])
    return parent[index]

def union(index1: int, index2: int):
    parent[find(index1)] = find(index2)
