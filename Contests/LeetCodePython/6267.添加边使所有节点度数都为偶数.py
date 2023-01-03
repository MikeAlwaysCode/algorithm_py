#
# @lc app=leetcode.cn id=6267 lang=python3
#
# [6267] 添加边使所有节点度数都为偶数
#
# https://leetcode.cn/problems/add-edges-to-make-degrees-of-all-nodes-even/description/
#
# algorithms
# Hard (27.72%)
# Likes:    8
# Dislikes: 0
# Total Accepted:    2.1K
# Total Submissions: 7.7K
# Testcase Example:  '5\n[[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]'
#
# 给你一个有 n 个节点的 无向 图，节点编号为 1 到 n 。再给你整数 n 和一个二维整数数组 edges ，其中 edges[i] = [ai,
# bi] 表示节点 ai 和 bi 之间有一条边。图不一定连通。
# 
# 你可以给图中添加 至多 两条额外的边（也可以一条边都不添加），使得图中没有重边也没有自环。
# 
# 如果添加额外的边后，可以使得图中所有点的度数都是偶数，返回 true ，否则返回 false 。
# 
# 点的度数是连接一个点的边的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
# 输出：true
# 解释：上图展示了添加一条边的合法方案。
# 最终图中每个节点都连接偶数条边。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：n = 4, edges = [[1,2],[3,4]]
# 输出：true
# 解释：上图展示了添加两条边的合法方案。
# 
# 示例 3：
# 
# 
# 
# 
# 输入：n = 4, edges = [[1,2],[1,3],[1,4]]
# 输出：false
# 解释：无法添加至多 2 条边得到一个符合要求的图。
# 
# 
# 
# 提示：
# 
# 
# 3 <= n <= 10^5
# 2 <= edges.length <= 10^5
# edges[i].length == 2
# 1 <= ai, bi <= n
# ai != bi
# 图中不会有重边
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        degrees = [0] * (n + 1)
        graph = [set() for _ in range(n + 1)]
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1
            graph[u].add(v)
            graph[v].add(u)

        # v = []
        # for i in range(1, n + 1):
        #     if degrees[i] & 1:
        #         v.append(i)
        v = [i for i in range(1, n + 1) if degrees[i] & 1]
                
        # print(len(v))
        # print(v)

        if len(v) == 0:
            return True
        elif len(v) == 2:
            if v[0] not in graph[v[1]]:
                return True
            else:
                for i in range(1, n + 1):
                    if i != v[0] and i != v[1] and i not in graph[v[0]] and i not in graph[v[1]]:
                        return True
                return False
        elif len(v) == 4:
            if v[0] not in graph[v[1]] and v[2] not in graph[v[3]]:
                return True
            elif v[0] not in graph[v[2]] and v[1] not in graph[v[3]]:
                return True
            elif v[0] not in graph[v[3]] and v[1] not in graph[v[2]]:
                return True
            else:
                return False
        else:
            return False
# @lc code=end

