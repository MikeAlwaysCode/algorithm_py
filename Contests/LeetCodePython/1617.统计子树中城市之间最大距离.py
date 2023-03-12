#
# @lc app=leetcode.cn id=1617 lang=python3
#
# [1617] 统计子树中城市之间最大距离
#
# https://leetcode.cn/problems/count-subtrees-with-max-distance-between-cities/description/
#
# algorithms
# Hard (65.18%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    4.1K
# Total Submissions: 5.7K
# Testcase Example:  '4\n[[1,2],[2,3],[2,4]]'
#
# 给你 n 个城市，编号为从 1 到 n 。同时给你一个大小为 n-1 的数组 edges ，其中 edges[i] = [ui, vi] 表示城市 ui
# 和 vi 之间有一条双向边。题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵 树 。
# 
# 一棵 子树
# 是城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。两个子树被认为不一样的条件是至少有一个城市在其中一棵子树中存在，但在另一棵子树中不存在。
# 
# 对于 d 从 1 到 n-1 ，请你找到城市间 最大距离 恰好为 d 的所有子树数目。
# 
# 请你返回一个大小为 n-1 的数组，其中第 d 个元素（下标从 1 开始）是城市间 最大距离 恰好等于 d 的子树数目。
# 
# 请注意，两个城市间距离定义为它们之间需要经过的边的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：n = 4, edges = [[1,2],[2,3],[2,4]]
# 输出：[3,4,0]
# 解释：
# 子树 {1,2}, {2,3} 和 {2,4} 最大距离都是 1 。
# 子树 {1,2,3}, {1,2,4}, {2,3,4} 和 {1,2,3,4} 最大距离都为 2 。
# 不存在城市间最大距离为 3 的子树。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 2, edges = [[1,2]]
# 输出：[1]
# 
# 
# 示例 3：
# 
# 
# 输入：n = 3, edges = [[1,2],[2,3]]
# 输出：[2,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 2 
# edges.length == n-1
# edges[i].length == 2
# 1 i, vi 
# 题目保证 (ui, vi) 所表示的边互不相同。
# 
# 
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        # 建树
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)  # 编号改为从 0 开始

        ans = [0] * (n - 1)
        in_set = [False] * n
        def f(i: int) -> None:
            if i == n:
                vis = [False] * n
                diameter = 0
                for v, b in enumerate(in_set):
                    if not b: continue
                    # 求树的直径
                    def dfs(x: int) -> int:
                        nonlocal diameter
                        vis[x] = True
                        max_len = 0
                        for y in g[x]:
                            if not vis[y] and in_set[y]:
                                ml = dfs(y) + 1
                                diameter = max(diameter, max_len + ml)
                                max_len = max(max_len, ml)
                        return max_len
                    dfs(v)
                    break
                if diameter and vis == in_set:
                    ans[diameter - 1] += 1
                return
            
            # 不选城市 i
            f(i + 1)

            # 选城市  i
            in_set[i] = True
            f(i + 1)
            in_set[i] = False  # 恢复现场
        f(0)
        return ans
        '''
        '''
        # 建树
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)  # 编号改为从 0 开始

        ans = [0] * (n - 1)
        #  二进制枚举
        for mask in range(3, 1 << n):
            if (mask & (mask - 1)) == 0:  # 需要至少两个点
                continue
            # 求树的直径
            vis = diameter = 0
            def dfs(x: int) -> int:
                nonlocal vis, diameter
                vis |= 1 << x  # 标记 x 访问过
                max_len = 0
                for y in g[x]:
                    if (vis >> y & 1) == 0 and mask >> y & 1:  # y 没有访问过且在 mask 中
                        ml = dfs(y) + 1
                        diameter = max(diameter, max_len + ml)
                        max_len = max(max_len, ml)
                return max_len
            dfs(mask.bit_length() - 1)  # 从一个在 mask 中的点开始递归
            if vis == mask:
                ans[diameter - 1] += 1
        return ans
        '''
        # 建树
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)  # 编号改为从 0 开始

        # 计算树上任意两点的距离
        dis = [[0] * n for _ in range(n)]
        def dfs(x: int, fa: int) -> None:
            for y in g[x]:
                if y != fa:
                    dis[i][y] = dis[i][x] + 1  # 自顶向下
                    dfs(y, x)
        for i in range(n):
            dfs(i, -1)  # 计算 i 到其余点的距离

        def dfs2(x: int, fa: int) -> int:
            # 能递归到这，说明 x 可以选
            cnt = 1  # 选 x
            for y in g[x]:
                if y != fa and \
                   (di[y] < d or di[y] == d and y > j) and \
                   (dj[y] < d or dj[y] == d and y > i):  # 满足这些条件就可以选
                    cnt *= dfs2(y, x)  # 每棵子树互相独立，采用乘法原理
            if di[x] + dj[x] > d:  # x 是可选点
                cnt += 1  # 不选 x
            return cnt
        ans = [0] * (n - 1)
        for i, di in enumerate(dis):
            for j in range(i + 1, n):
                dj = dis[j]
                d = di[j]
                ans[d - 1] += dfs2(i, -1)
        return ans
# @lc code=end

