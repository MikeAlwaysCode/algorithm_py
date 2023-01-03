#
# @lc app=leetcode.cn id=6139 lang=python3
#
# [6139] 受限条件下可到达节点的数目
#
# https://leetcode.cn/problems/reachable-nodes-with-restrictions/description/
#
# algorithms
# Medium (39.25%)
# Likes:    9
# Dislikes: 0
# Total Accepted:    5.1K
# Total Submissions: 12.9K
# Testcase Example:  '7\n[[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]\n[4,5]'
#
# 现有一棵由 n 个节点组成的无向树，节点编号从 0 到 n - 1 ，共有 n - 1 条边。
# 
# 给你一个二维整数数组 edges ，长度为 n - 1 ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi
# 之间存在一条边。另给你一个整数数组 restricted 表示 受限 节点。
# 
# 在不访问受限节点的前提下，返回你可以从节点 0 到达的 最多 节点数目。
# 
# 注意，节点 0 不 会标记为受限节点。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
# 输出：4
# 解释：上图所示正是这棵树。
# 在不访问受限节点的前提下，只有节点 [0,1,2,3] 可以从节点 0 到达。
# 
# 示例 2：
# 
# 输入：n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]
# 输出：3
# 解释：上图所示正是这棵树。
# 在不访问受限节点的前提下，只有节点 [0,5,6] 可以从节点 0 到达。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= n <= 10^5
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges 表示一棵有效的树
# 1 <= restricted.length < n
# 1 <= restricted[i] < n
# restricted 中的所有值 互不相同
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        rs = set(restricted)
        ans = 0
        def dfs(x: int, p: int):
            if x in rs:
                return
            nonlocal ans
            ans += 1
            for y in g[x]:
                if y != p:
                    dfs(y, x)
        dfs(0, -1)
        return ans

        '''
        v = [[] for _ in range(n)]
        for edge in edges:
            v[edge[0]].append(edge[1])
            v[edge[1]].append(edge[0])

        s = [False] * n
        s[0] = True
        
        rs = [True] * n
        for r in restricted:
            rs[r] = False
        
        # s = set(restricted)
        ans = 1
        q = [0]
        while q:
            tmp = []
            for x in q:
                for t in v[x]:
                    if not s[t] and rs[t]:
                        tmp.append(t)
                        s[t] = True
                        ans += 1
            q = tmp
        return ans
        '''
# @lc code=end

