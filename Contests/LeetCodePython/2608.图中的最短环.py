#
# @lc app=leetcode.cn id=2608 lang=python3
#
# [2608] 图中的最短环
#
# https://leetcode.cn/problems/shortest-cycle-in-a-graph/description/
#
# algorithms
# Hard (40.31%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 6.7K
# Testcase Example:  '7\n[[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]'
#
# 现有一个含 n 个顶点的 双向 图，每个顶点按从 0 到 n - 1 标记。图中的边由二维整数数组 edges 表示，其中 edges[i] = [ui,
# vi] 表示顶点 ui 和 vi 之间存在一条边。每对顶点最多通过一条边连接，并且不存在与自身相连的顶点。
# 
# 返回图中 最短 环的长度。如果不存在环，则返回 -1 。
# 
# 环 是指以同一节点开始和结束，并且路径中的每条边仅使用一次。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
# 输出：3
# 解释：长度最小的循环是：0 -> 1 -> 2 -> 0 
# 
# 
# 示例 2：
# 
# 输入：n = 4, edges = [[0,1],[0,2]]
# 输出：-1
# 解释：图中不存在循环
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= n <= 1000
# 1 <= edges.length <= 1000
# edges[i].length == 2
# 0 <= ui, vi < n
# ui != vi
# 不存在重复的边
# 
# 
#
import math
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def bfs(start: int) -> int:
            res = math.inf
            dis = [-1] * n
            dis[start] = 0
            q = deque([(start, -1)])
            while q:
                x, f = q.popleft()
                for y in g[x]:
                    if y == f: continue
                    if dis[y] < 0:
                        dis[y] = dis[x] + 1
                        q.append((y, x))
                    else:
                        res = min(res, dis[x] + dis[y] + 1)
            return res
        ans = min(bfs(i) for i in range(n))
        return -1 if ans == math.inf else ans
# @lc code=end

