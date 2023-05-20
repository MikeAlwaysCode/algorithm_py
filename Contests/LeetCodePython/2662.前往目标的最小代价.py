#
# @lc app=leetcode.cn id=2662 lang=python3
#
# [2662] 前往目标的最小代价
#
# https://leetcode.cn/problems/minimum-cost-of-a-path-with-special-roads/description/
#
# algorithms
# Medium (35.34%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 8K
# Testcase Example:  '[1,1]\n[4,5]\n[[1,2,3,3,2],[3,4,4,5,1]]'
#
# 给你一个数组 start ，其中 start = [startX, startY] 表示你的初始位置位于二维空间上的 (startX, startY)
# 。另给你一个数组 target ，其中 target = [targetX, targetY] 表示你的目标位置 (targetX, targetY)
# 。
# 
# 从位置 (x1, y1) 到空间中任一其他位置 (x2, y2) 的代价是 |x2 - x1| + |y2 - y1| 。
# 
# 给你一个二维数组 specialRoads ，表示空间中存在的一些特殊路径。其中 specialRoads[i] = [x1i, y1i, x2i,
# y2i, costi] 表示第 i 条特殊路径可以从 (x1i, y1i) 到 (x2i, y2i) ，但成本等于 costi
# 。你可以使用每条特殊路径任意次数。
# 
# 返回从 (startX, startY) 到 (targetX, targetY) 所需的最小代价。
# 
# 
# 
# 示例 1：
# 
# 输入：start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
# 输出：5
# 解释：从 (1,1) 到 (4,5) 的最优路径如下：
# - (1,1) -> (1,2) ，移动的代价是 |1 - 1| + |2 - 1| = 1 。
# - (1,2) -> (3,3) ，移动使用第一条特殊路径，代价是 2 。
# - (3,3) -> (3,4) ，移动的代价是 |3 - 3| + |4 - 3| = 1.
# - (3,4) -> (4,5) ，移动使用第二条特殊路径，代价是 1 。
# 总代价是 1 + 2 + 1 + 1 = 5 。
# 可以证明无法以小于 5 的代价完成从 (1,1) 到 (4,5) 。
# 
# 
# 示例 2：
# 
# 输入：start = [3,2], target = [5,7], specialRoads =
# [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
# 输出：7
# 解释：最优路径是不使用任何特殊路径，直接以 |5 - 3| + |7 - 2| = 7 的代价从初始位置到达目标位置。
# 
# 
# 
# 
# 提示：
# 
# 
# start.length == target.length == 2
# 1 <= startX <= targetX <= 10^5
# 1 <= startY <= targetY <= 10^5
# 1 <= specialRoads.length <= 200
# specialRoads[i].length == 5
# startX <= x1i, x2i <= targetX
# startY <= y1i, y2i <= targetY
# 1 <= costi <= 10^5
# 
# 
#
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        def f(x1, y1, x2, y2) -> int:
            return abs(x1 - x2) + abs(y1 - y2)
        dis = dict()
        dis[(start[0], start[1])] = 0
        dis[(target[0], target[1])] = target[0] - start[0] + target[1] - start[1]
        for x1, y1, x2, y2, c in specialRoads:
            dis[(x1, y1)] = f(start[0], start[1], x1, y1)
            dis[(x2, y2)] = f(start[0], start[1], x2, y2)
        q = deque([(start[0], start[1])])
        while q:
            x0, y0 = q.popleft()
            d = dis[(x0, y0)]
            for x1, y1, x2, y2, c in specialRoads:
                d1, d2 = f(x0, y0, x1, y1), f(x0, y0, x2, y2)
                if dis[(x2, y2)] > d + d1 + c:
                    dis[(x2, y2)] = d + d1 + c
                    dis[(target[0], target[1])] = min(dis[(target[0], target[1])], dis[(x2, y2)] + f(x2, y2, target[0], target[1]))
                    q.append((x2, y2))
        return dis[(target[0], target[1])]
# @lc code=end

