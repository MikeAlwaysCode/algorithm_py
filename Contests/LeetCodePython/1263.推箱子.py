#
# @lc app=leetcode.cn id=1263 lang=python3
#
# [1263] 推箱子
#
# https://leetcode.cn/problems/minimum-moves-to-move-a-box-to-their-target-location/description/
#
# algorithms
# Hard (43.86%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    11K
# Total Submissions: 21K
# Testcase Example:  '[["#","#","#","#","#","#"],["#","T","#","#","#","#"],["#",".",".","B",".","#"],["#",".","#","#",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]'
#
# 「推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库中的目标位置。
# 
# 游戏地图用大小为 m x n 的网格 grid 表示，其中每个元素可以是墙、地板或者是箱子。
# 
# 现在你将作为玩家参与游戏，按规则将箱子 'B' 移动到目标位置 'T' ：
# 
# 
# 玩家用字符 'S' 表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。
# 地板用字符 '.' 表示，意味着可以自由行走。
# 墙用字符 '#' 表示，意味着障碍物，不能通行。 
# 箱子仅有一个，用字符 'B' 表示。相应地，网格上有一个目标位置 'T'。
# 玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。
# 玩家无法越过箱子。
# 
# 
# 返回将箱子推到目标位置的最小 推动 次数，如果无法做到，请返回 -1。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：grid = [["#","#","#","#","#","#"],
# ⁠            ["#","T","#","#","#","#"],
# ["#",".",".","B",".","#"],
# ["#",".","#","#",".","#"],
# ["#",".",".",".","S","#"],
# ["#","#","#","#","#","#"]]
# 输出：3
# 解释：我们只需要返回推箱子的次数。
# 
# 示例 2：
# 
# 
# 输入：grid = [["#","#","#","#","#","#"],
# ⁠            ["#","T","#","#","#","#"],
# ["#",".",".","B",".","#"],
# ["#","#","#","#",".","#"],
# ["#",".",".",".","S","#"],
# ["#","#","#","#","#","#"]]
# 输出：-1
# 
# 
# 示例 3：
# 
# 
# 输入：grid = [["#","#","#","#","#","#"],
# ["#","T",".",".","#","#"],
# ["#",".","#","B",".","#"],
# ["#",".",".",".",".","#"],
# ["#",".",".",".","S","#"],
# ["#","#","#","#","#","#"]]
# 输出：5
# 解释：向下、向左、向左、向上再向上。
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
# grid 仅包含字符 '.', '#',  'S' , 'T', 以及 'B'。
# grid 中 'S', 'B' 和 'T' 各只能出现一个。
# 
# 
#

# @lc code=start
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        sx, sy, bx, by = None, None, None, None # 玩家、箱子的初始位置
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 'S':
                    sx = x
                    sy = y
                elif grid[x][y] == 'B':
                    bx = x
                    by = y

        # 不越界且不在墙上
        def ok(x, y):
            return (0 <= x < m and 0 <= y < n and grid[x][y] != '#')

        d = [0, -1, 0, 1, 0]

        dp = [[float('inf')] * (m * n) for _ in range(m * n)]
        dp[sx * n + sy][bx * n + by] = 0 # 初始状态的推动次数为 0
        q = deque([(sx * n + sy, bx * n + by)])
        while q:
            q1 = deque()
            while q:
                s1, b1 = q.popleft()
                sx1, sy1 = s1 // n, s1 % n
                bx1, by1 = b1 // n, b1 % n
                if grid[bx1][by1] == 'T': # 箱子已被推到目标处
                    return dp[s1][b1]
                for i in range(4): # 玩家向四个方向移动到另一个状态
                    sx2, sy2 = sx1 + d[i], sy1 + d[i + 1]
                    s2 = sx2 * n + sy2
                    if not ok(sx2, sy2): # 玩家位置不合法
                        continue
                    if sx2 == bx1 and sy2 == by1: # 推动箱子
                        bx2, by2 = bx1 + d[i], by1 + d[i + 1]
                        b2 = bx2 * n + by2
                        if not ok(bx2, by2) or dp[s2][b2] <= dp[s1][b1] + 1: # 箱子位置不合法 或 状态已访问
                            continue
                        dp[s2][b2] = dp[s1][b1] + 1
                        q1.append((s2, b2))
                    else:
                        if dp[s2][b1] <= dp[s1][b1]: # 状态已访问
                            continue
                        dp[s2][b1] = dp[s1][b1]
                        q.append((s2, b1))
            q, q1 = q1, q
        return -1
# @lc code=end

