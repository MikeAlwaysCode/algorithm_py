#
# @lc app=leetcode.cn id=1466 lang=python3
#
# [1466] 重新规划路线
#
# https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
#
# algorithms
# Medium (50.48%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    9.9K
# Total Submissions: 19.5K
# Testcase Example:  '6\n[[0,1],[1,3],[2,3],[4,0],[4,5]]'
#
# n 座城市，从 0 到 n-1 编号，其间共有 n-1
# 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。
# 
# 路线用 connections 表示，其中 connections[i] = [a, b] 表示从城市 a 到 b 的一条有向路线。
# 
# 今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。
# 
# 请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。
# 
# 题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# 输出：3
# 解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
# 
# 示例 2：
# 
# 
# 
# 输入：n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
# 输出：2
# 解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
# 
# 示例 3：
# 
# 输入：n = 3, connections = [[1,0],[2,0]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= n <= 5 * 10^4
# connections.length == n-1
# connections[i].length == 2
# 0 <= connections[i][0], connections[i][1] <= n-1
# connections[i][0] != connections[i][1]
# 
# 
#
import collections
from typing import List
# @lc code=start
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        tree = [[] for _ in range(n)]
        for u, v in connections:
            tree[u].append((v, 1))
            tree[v].append((u, 0))
        # BFS
        ans = 0
        q = collections.deque([(0, -1)])
        while q:
            x, p = q.popleft()
            for u, d in tree[x]:
                if u == p:
                    continue
                ans += d
                q.append((u, x))
        return ans
        '''
        # DFS
        def dfs(x: int, p: int) -> int:
            res = 0
            for u, d in tree[x]:
                if u == p:
                    continue
                res += d + dfs(u, x)
            return res
        return dfs(0, -1)
        '''
# @lc code=end

