#
# @lc app=leetcode.cn id=802 lang=python3
#
# [802] 找到最终的安全状态
#
# https://leetcode.cn/problems/find-eventual-safe-states/description/
#
# algorithms
# Medium (59.04%)
# Likes:    361
# Dislikes: 0
# Total Accepted:    41K
# Total Submissions: 69.5K
# Testcase Example:  '[[1,2],[2,3],[5],[0],[5],[],[]]'
#
# 有一个有 n 个节点的有向图，节点按 0 到 n - 1 编号。图由一个 索引从 0 开始 的 2D 整数数组 graph表示， graph[i]是与节点
# i 相邻的节点的整数数组，这意味着从节点 i 到 graph[i]中的每个节点都有一条边。
# 
# 如果一个节点没有连出的有向边，则它是 终端节点 。如果没有出边，则节点为终端节点。如果从该节点开始的所有可能路径都通向 终端节点 ，则该节点为 安全节点
# 。
# 
# 返回一个由图中所有 安全节点 组成的数组作为答案。答案数组中的元素应当按 升序 排列。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# 输出：[2,4,5,6]
# 解释：示意图如上。
# 节点 5 和节点 6 是终端节点，因为它们都没有出边。
# 从节点 2、4、5 和 6 开始的所有路径都指向节点 5 或 6 。
# 
# 
# 示例 2：
# 
# 
# 输入：graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# 输出：[4]
# 解释:
# 只有节点 4 是终端节点，从节点 4 开始的所有路径都通向节点 4 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == graph.length
# 1 <= n <= 10^4
# 0 <= graph[i].length <= n
# 0 <= graph[i][j] <= n - 1
# graph[i] 按严格递增顺序排列。
# 图中可能包含自环。
# 图中边的数目在范围 [1, 4 * 10^4] 内。
# 
# 
#
import collections
from typing import List
# @lc code=start
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rg = [[] for _ in range(n)]
        inDgrees = [0] * n
        for x, ys in enumerate(graph):
            for y in ys:
                rg[y].append(x)
            inDgrees[x] = len(ys)
        # print(rg)
        # print(inDgrees)
        ans = [i for i in range(n) if inDgrees[i] == 0]
        q = collections.deque(ans)
        while q:
            for x in rg[q.popleft()]:
                inDgrees[x] -= 1
                if inDgrees[x] == 0:
                    q.append(x)
                    ans.append(x)
        ans.sort()
        return ans
        '''
        n = len(graph)
        color = [0] * n

        def safe(x: int) -> bool:
            if color[x] > 0:
                return color[x] == 2
            color[x] = 1
            for y in graph[x]:
                if not safe(y):
                    return False
            color[x] = 2
            return True

        return [i for i in range(n) if safe(i)]
        '''
# @lc code=end

