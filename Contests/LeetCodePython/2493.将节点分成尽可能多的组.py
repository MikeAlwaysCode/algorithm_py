#
# @lc app=leetcode.cn id=2493 lang=python3
#
# [2493] 将节点分成尽可能多的组
#
# https://leetcode.cn/problems/divide-nodes-into-the-maximum-number-of-groups/description/
#
# algorithms
# Hard (42.94%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    2.8K
# Total Submissions: 6.6K
# Testcase Example:  '6\n[[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]'
#
# 给你一个正整数 n ，表示一个 无向 图中的节点数目，节点编号从 1 到 n 。
# 
# 同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 双向
# 边。注意给定的图可能是不连通的。
# 
# 请你将图划分为 m 个组（编号从 1 开始），满足以下要求：
# 
# 
# 图中每个节点都只属于一个组。
# 图中每条边连接的两个点 [ai, bi] ，如果 ai 属于编号为 x 的组，bi 属于编号为 y 的组，那么 |y - x| = 1 。
# 
# 
# 请你返回最多可以将节点分为多少个组（也就是最大的 m ）。如果没办法在给定条件下分组，请你返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
# 输出：4
# 解释：如上图所示，
# - 节点 5 在第一个组。
# - 节点 1 在第二个组。
# - 节点 2 和节点 4 在第三个组。
# - 节点 3 和节点 6 在第四个组。
# 所有边都满足题目要求。
# 如果我们创建第五个组，将第三个组或者第四个组中任何一个节点放到第五个组，至少有一条边连接的两个节点所属的组编号不符合题目要求。
# 
# 
# 示例 2：
# 
# 输入：n = 3, edges = [[1,2],[2,3],[3,1]]
# 输出：-1
# 解释：如果我们将节点 1 放入第一个组，节点 2 放入第二个组，节点 3 放入第三个组，前两条边满足题目要求，但第三条边不满足题目要求。
# 没有任何符合题目要求的分组方式。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 500
# 1 <= edges.length <= 10^4
# edges[i].length == 2
# 1 <= ai, bi <= n
# ai != bi
# 两个点之间至多只有一条边。
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)

        time = [0] * n  # 充当 vis 数组的作用（避免在 BFS 内部重复创建 vis 数组）
        clock = 0
        def bfs(start: int) -> int:  # 返回从 start 出发的最大深度
            depth = 0
            nonlocal clock
            clock += 1
            time[start] = clock
            q = [start]
            while q:
                tmp = q
                q = []
                for x in tmp:
                    for y in g[x]:
                        if time[y] != clock:  # 没有在同一次 BFS 中访问过
                            time[y] = clock
                            q.append(y)
                depth += 1
            return depth

        color = [0] * n
        def is_bipartite(x: int, c: int) -> bool:  # 二分图判定，原理见视频讲解
            nodes.append(x)
            color[x] = c
            for y in g[x]:
                if color[y] == c or color[y] == 0 and not is_bipartite(y, -c):
                    return False
            return True

        ans = 0
        for i, c in enumerate(color):
            if c: continue
            nodes = []
            if not is_bipartite(i, 1): return -1  # 如果不是二分图（有奇环），则无法分组
            # 否则一定可以分组
            ans += max(bfs(x) for x in nodes)  # 枚举连通块的每个点，作为起点 BFS，求最大深度
        return ans
# @lc code=end

