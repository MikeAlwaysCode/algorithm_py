#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#
# https://leetcode.cn/problems/possible-bipartition/description/
#
# algorithms
# Medium (49.88%)
# Likes:    241
# Dislikes: 0
# Total Accepted:    24.1K
# Total Submissions: 48.1K
# Testcase Example:  '4\n[[1,2],[1,3],[2,4]]'
#
# 给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。
# 
# 给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和
# bi的人归入同一组。当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 4, dislikes = [[1,2],[1,3],[2,4]]
# 输出：true
# 解释：group1 [1,4], group2 [2,3]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 3, dislikes = [[1,2],[1,3],[2,3]]
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 2000
# 0 <= dislikes.length <= 10^4
# dislikes[i].length == 2
# 1 <= dislikes[i][j] <= n
# ai < bi
# dislikes 中每一组都 不同
# 
# 
# 
# 
#
from collections import deque
from typing import List
# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.fa = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x: int, y: int) -> None:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.fa[fy] = fx

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        for x, y in dislikes:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        uf = UnionFind(n)
        for x, nodes in enumerate(g):
            for y in nodes:
                uf.union(nodes[0], y)
                if uf.is_connected(x, y):
                    return False
        return True
    '''
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # BFS
        g = [[] for _ in range(n)]
        for x, y in dislikes:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        color = [0] * n  # color[x] = 0 表示未访问节点 x
        for i, c in enumerate(color):
            if c == 0:
                q = deque([i])
                color[i] = 1
                while q:
                    x = q.popleft()
                    for y in g[x]:
                        if color[y] == color[x]:
                            return False
                        if color[y] == 0:
                            color[y] = -color[x]
                            q.append(y)
        return True

        # DFS
        g = [[] for _ in range(n)]
        for x, y in dislikes:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        color = [0] * n  # color[x] = 0 表示未访问节点 x
        def dfs(x: int, c: int) -> bool:
            color[x] = c
            return all(color[y] != c and (color[y] or dfs(y, -c)) for y in g[x])
        return all(c or dfs(i, 1) for i, c in enumerate(color))
    '''
# @lc code=end

