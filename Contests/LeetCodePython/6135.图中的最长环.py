#
# @lc app=leetcode.cn id=6135 lang=python3
#
# [6135] 图中的最长环
#
# https://leetcode.cn/problems/longest-cycle-in-a-graph/description/
#
# algorithms
# Hard (31.30%)
# Likes:    4
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 10.8K
# Testcase Example:  '[3,3,4,2,3]'
#
# 给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，其中每个节点 至多 有一条出边。
# 
# 图用一个大小为 n 下标从 0 开始的数组 edges 表示，节点 i 到节点 edges[i] 之间有一条有向边。如果节点 i 没有出边，那么
# edges[i] == -1 。
# 
# 请你返回图中的 最长 环，如果没有任何环，请返回 -1 。
# 
# 一个环指的是起点和终点是 同一个 节点的路径。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：edges = [3,3,4,2,3]
# 输出去：3
# 解释：图中的最长环是：2 -> 4 -> 3 -> 2 。
# 这个环的长度为 3 ，所以返回 3 。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：edges = [2,-1,3,1]
# 输出：-1
# 解释：图中没有任何环。
# 
# 
# 
# 
# 提示：
# 
# 
# n == edges.length
# 2 <= n <= 10^5
# -1 <= edges[i] < n
# edges[i] != i
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        time = [0] * len(edges)
        clock, ans = 1, -1
        for x, t in enumerate(time):
            if t: continue
            start_time = clock
            while x >= 0:
                if time[x]:  # 重复访问
                    if time[x] >= start_time:  # 找到了一个新的环
                        ans = max(ans, clock - time[x])
                    break
                time[x] = clock
                clock += 1
                x = edges[x]
        return ans
# @lc code=end

