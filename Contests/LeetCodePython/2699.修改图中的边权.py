#
# @lc app=leetcode.cn id=2699 lang=python3
#
# [2699] 修改图中的边权
#
# https://leetcode.cn/problems/modify-graph-edge-weights/description/
#
# algorithms
# Hard (33.62%)
# Likes:    51
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 8.7K
# Testcase Example:  '5\n[[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]\n0\n1\n5'
#
# 给你一个 n 个节点的 无向带权连通 图，节点编号为 0 到 n - 1 ，再给你一个整数数组 edges ，其中 edges[i] = [ai, bi,
# wi] 表示节点 ai 和 bi 之间有一条边权为 wi 的边。
# 
# 部分边的边权为 -1（wi = -1），其他边的边权都为 正 数（wi > 0）。
# 
# 你需要将所有边权为 -1 的边都修改为范围 [1, 2 * 10^9] 中的 正整数 ，使得从节点 source 到节点 destination 的
# 最短距离 为整数 target 。如果有 多种 修改方案可以使 source 和 destination 之间的最短距离等于 target
# ，你可以返回任意一种方案。
# 
# 如果存在使 source 到 destination 最短距离为 target
# 的方案，请你按任意顺序返回包含所有边的数组（包括未修改边权的边）。如果不存在这样的方案，请你返回一个 空数组 。
# 
# 注意：你不能修改一开始边权为正数的边。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0,
# destination = 1, target = 5
# 输出：[[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
# 解释：上图展示了一个满足题意的修改方案，从 0 到 1 的最短距离为 5 。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
# 输出：[]
# 解释：上图是一开始的图。没有办法通过修改边权为 -1 的边，使得 0 到 2 的最短距离等于 6 ，所以返回一个空数组。
# 
# 
# 示例 3：
# 
# 
# 
# 
# 输入：n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination
# = 2, target = 6
# 输出：[[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
# 解释：上图展示了一个满足题意的修改方案，从 0 到 2 的最短距离为 6 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 100
# 1 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 3
# 0 <= ai, bi < n
# wi = -1 或者 1 <= wi <= 10^7
# ai != bi
# 0 <= source, destination < n
# source != destination
# 1 <= target <= 10^9
# 输入的图是连通图，且没有自环和重边。
# 
# 
#
from heapq import heappop, heappush
import math
from typing import List


# @lc code=start
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        m = len(edges)
        vis = [False] * m
        g = [[] for _ in range(n)]
        for i, (u, v, w) in enumerate(edges):
            if w == -1:
                vis[i] = True
                edges[i][2] = 1
            g[u].append((v, i))
            g[v].append((u, i))
        
        dis1 = [math.inf] * (n)
        dis1[source] = 0
        h = [(0, source)]
        while h:
            d, u = heappop(h)
            if d > dis1[u]: continue
            for v, i in g[u]:
                new_d = d + edges[i][2]
                if new_d < dis1[v]:
                    dis1[v] = new_d
                    heappush(h, (dis1[v], v))
        
        if dis1[destination] > target:
            return []
        
        dis2 = [math.inf] * n
        dis2[source] = 0
        h = [(0, source)]
        while h:
            d, u = heappop(h)
            if d > dis2[u]: continue
            for v, i in g[u]:
                if vis[i] and edges[i][2] == 1 and edges[i][2] + d + dis1[destination] - dis1[v] < target:
                    x = target - edges[i][2] - d - dis1[destination] + dis1[v]
                    edges[i][2] += x
                new_d = d + edges[i][2]
                if new_d < dis2[v]:
                    dis2[v] = new_d
                    heappush(h, (dis2[v], v))

        if dis2[destination] == target:
            return edges
        else:
            return []
# @lc code=end

