#
# @lc app=leetcode.cn id=1697 lang=python3
#
# [1697] 检查边长度限制的路径是否存在
#
# https://leetcode.cn/problems/checking-existence-of-edge-length-limited-paths/description/
#
# algorithms
# Hard (54.89%)
# Likes:    74
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 7.8K
# Testcase Example:  '3\n[[0,1,2],[1,2,4],[2,0,8],[1,0,16]]\n[[0,1,2],[0,2,5]]'
#
# 给你一个 n 个点组成的无向图边集 edgeList ，其中 edgeList[i] = [ui, vi, disi] 表示点 ui 和点 vi
# 之间有一条长度为 disi 的边。请注意，两个点之间可能有 超过一条边 。
# 
# 给你一个查询数组queries ，其中 queries[j] = [pj, qj, limitj] ，你的任务是对于每个查询 queries[j]
# ，判断是否存在从 pj 到 qj 的路径，且这条路径上的每一条边都 严格小于 limitj 。
# 
# 请你返回一个 布尔数组 answer ，其中 answer.length == queries.length ，当 queries[j] 的查询结果为
# true 时， answer 第 j 个值为 true ，否则为 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries =
# [[0,1,2],[0,2,5]]
# 输出：[false,true]
# 解释：上图为给定的输入数据。注意到 0 和 1 之间有两条重边，分别为 2 和 16 。
# 对于第一个查询，0 和 1 之间没有小于 2 的边，所以我们返回 false 。
# 对于第二个查询，有一条路径（0 -> 1 -> 2）两条边都小于 5 ，所以这个查询我们返回 true 。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries =
# [[0,4,14],[1,4,13]]
# 输出：[true,false]
# 解释：上图为给定数据。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 
# 1 
# edgeList[i].length == 3
# queries[j].length == 3
# 0 i, vi, pj, qj 
# ui != vi
# pj != qj
# 1 i, limitj 
# 两个点之间可能有 多条 边。
# 
# 
#
from heapq import heapify, heappop
from typing import List
# @lc code=start
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        h = []
        for u, v, d in edgeList:
            h.append((d, u, v))
        heapify(h)

        m = len(queries)
        idx = list(range(m))
        idx.sort(key = lambda x: queries[x][2])

        parent = list(range(n))

        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        
        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        ans = [False] * m
        
        for i in range(m):
            while h and h[0][0] < queries[idx[i]][2]:
                d, u, v = heappop(h)
                union(u, v)
            u, v = queries[idx[i]][0], queries[idx[i]][1]
            if find(u) == find(v):
                ans[idx[i]] = True
        
        return ans
# @lc code=end

