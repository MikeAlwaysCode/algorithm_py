#
# @lc app=leetcode.cn id=6163 lang=python3
#
# [6163] 给定条件下构造矩阵
#
# https://leetcode.cn/problems/build-a-matrix-with-conditions/description/
#
# algorithms
# Hard (50.90%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    2.8K
# Total Submissions: 5.5K
# Testcase Example:  '3\n[[1,2],[3,2]]\n[[2,1],[3,2]]'
#
# 给你一个 正 整数 k ，同时给你：
# 
# 
# 一个大小为 n 的二维整数数组 rowConditions ，其中 rowConditions[i] = [abovei, belowi] 和
# 一个大小为 m 的二维整数数组 colConditions ，其中 colConditions[i] = [lefti, righti] 。
# 
# 
# 两个数组里的整数都是 1 到 k 之间的数字。
# 
# 你需要构造一个 k x k 的矩阵，1 到 k 每个数字需要 恰好出现一次 。剩余的数字都是 0 。
# 
# 矩阵还需要满足以下条件：
# 
# 
# 对于所有 0 到 n - 1 之间的下标 i ，数字 abovei 所在的 行 必须在数字 belowi 所在行的上面。
# 对于所有 0 到 m - 1 之间的下标 i ，数字 lefti 所在的 列 必须在数字 righti 所在列的左边。
# 
# 
# 返回满足上述要求的 任意 矩阵。如果不存在答案，返回一个空的矩阵。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
# 输出：[[3,0,0],[0,0,1],[0,2,0]]
# 解释：上图为一个符合所有条件的矩阵。
# 行要求如下：
# - 数字 1 在第 1 行，数字 2 在第 2 行，1 在 2 的上面。
# - 数字 3 在第 0 行，数字 2 在第 2 行，3 在 2 的上面。
# 列要求如下：
# - 数字 2 在第 1 列，数字 1 在第 2 列，2 在 1 的左边。
# - 数字 3 在第 0 列，数字 2 在第 1 列，3 在 2 的左边。
# 注意，可能有多种正确的答案。
# 
# 
# 示例 2：
# 
# 输入：k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
# 输出：[]
# 解释：由前两个条件可以得到 3 在 1 的下面，但第三个条件是 3 在 1 的上面。
# 没有符合条件的矩阵存在，所以我们返回空矩阵。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= k <= 400
# 1 <= rowConditions.length, colConditions.length <= 10^4
# rowConditions[i].length == colConditions[i].length == 2
# 1 <= abovei, belowi, lefti, righti <= k
# abovei != belowi
# lefti != righti
# 
# 
#
from collections import deque
from typing import List
# @lc code=start
from graphlib import TopologicalSorter
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def get_pos(cons: List[List[int]]) -> List[int]:
            ts = TopologicalSorter({i: [] for i in range(1, k+1)})
            for x, y in cons:
                ts.add(y, x)
            pos = [0] * k
            for i, x in enumerate(ts.static_order()):
                pos[x - 1] = i
            return pos

        try:
            ans = [[0] * k for _ in range(k)]
            for x, (i, j) in enumerate(zip(get_pos(rowConditions), get_pos(colConditions))):
                ans[i][j] = x + 1
            return ans
        except:
            return []
        '''
        def topoSort(conditions: List[List[int]]) -> List[int]:
            incnt = [0] * (k + 1)
            edge = [[] for _ in range(k + 1)]
            for a, b in conditions:
                incnt[b] += 1
                edge[a].append(b)
            
            ans = [0] * k
            cnt = 0
            q = deque(i for i, v in enumerate(incnt) if v == 0 and i > 0)
            
            while q:
                cur = q.popleft()
                ans[cnt] = cur
                cnt += 1

                for x in edge[cur]:
                    incnt[x] -= 1
                    if incnt[x] == 0:
                        q.append(x)
            
            return ans if cnt == k else None

        rows = topoSort(rowConditions)
        if rows is None: return []
        cols = topoSort(colConditions)
        if cols is None: return []
        
        pos = {x: i for i, x in enumerate(cols)}
        ans = [[0] * k for _ in range(k)]
        for i, x in enumerate(rows):
            ans[i][pos[x]] = x
        return ans
        '''
# @lc code=end

