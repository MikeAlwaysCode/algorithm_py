#
# @lc app=leetcode.cn id=2685 lang=python3
#
# [2685] 统计完全连通分量的数量
#
# https://leetcode.cn/problems/count-the-number-of-complete-components/description/
#
# algorithms
# Medium (67.02%)
# Likes:    13
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 6.4K
# Testcase Example:  '6\n[[0,1],[0,2],[1,2],[3,4]]'
#
# 给你一个整数 n 。现有一个包含 n 个顶点的 无向 图，顶点按从 0 到 n - 1 编号。给你一个二维整数数组 edges 其中 edges[i] =
# [ai, bi] 表示顶点 ai 和 bi 之间存在一条 无向 边。
# 
# 返回图中 完全连通分量 的数量。
# 
# 如果在子图中任意两个顶点之间都存在路径，并且子图中没有任何一个顶点与子图外部的顶点共享边，则称其为 连通分量 。
# 
# 如果连通分量中每对节点之间都存在一条边，则称其为 完全连通分量 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
# 输出：3
# 解释：如上图所示，可以看到此图所有分量都是完全连通分量。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
# 输出：1
# 解释：包含节点 0、1 和 2 的分量是完全连通分量，因为每对节点之间都存在一条边。
# 包含节点 3 、4 和 5 的分量不是完全连通分量，因为节点 4 和 5 之间不存在边。
# 因此，在图中完全连接分量的数量是 1 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 50
# 0 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# 不存在重复的边
# 
# 
#
import math
from typing import List


# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.e = [0] * n
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
            self.e[x] += 1
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.e[x] += self.e[y] + 1
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.unite(u, v)
        ans = 0
        for i in range(n):
            if i != uf.findset(i): continue
            if uf.e[i] == math.comb(uf.size[i], 2): ans += 1
        return ans
# @lc code=end

