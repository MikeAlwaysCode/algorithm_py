#
# @lc app=leetcode.cn id=847 lang=python3
#
# [847] 访问所有节点的最短路径
#
# https://leetcode.cn/problems/shortest-path-visiting-all-nodes/description/
#
# algorithms
# Hard (67.79%)
# Likes:    337
# Dislikes: 0
# Total Accepted:    24.3K
# Total Submissions: 35.9K
# Testcase Example:  '[[1,2,3],[0],[0],[0]]'
#
# 存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。
# 
# 给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。
# 
# 返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：graph = [[1,2,3],[0],[0],[0]]
# 输出：4
# 解释：一种可能的路径为 [1,0,2,0,3]
# 
# 示例 2：
# 
# 
# 
# 
# 输入：graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# 输出：4
# 解释：一种可能的路径为 [0,1,4,2,3]
# 
# 
# 
# 
# 提示：
# 
# 
# n == graph.length
# 1 <= n <= 12
# 0 <= graph[i].length < n
# graph[i] 不包含 i
# 如果 graph[a] 包含 b ，那么 graph[b] 也包含 a
# 输入的图总是连通图
# 
# 
#
from collections import deque
from typing import List
# @lc code=start
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque((i, 1 << i, 0) for i in range(n))
        seen = {(i, 1 << i) for i in range(n)}
        ans = 0

        while q:
            u, mask, dist = q.popleft()
            if mask == (1 << n) - 1:
                ans = dist
                break
            for v in graph[u]:
                mask_v = mask | (1 << v)
                if (v, mask_v) not in seen:
                    q.append((v, mask_v, dist + 1))
                    seen.add((v, mask_v))
        
        return ans
# @lc code=end

