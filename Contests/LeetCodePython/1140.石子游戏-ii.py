#
# @lc app=leetcode.cn id=1140 lang=python3
#
# [1140] 石子游戏 II
#
# https://leetcode.cn/problems/stone-game-ii/description/
#
# algorithms
# Medium (66.26%)
# Likes:    167
# Dislikes: 0
# Total Accepted:    11.4K
# Total Submissions: 16.9K
# Testcase Example:  '[2,7,9,4,4]'
#
# 爱丽丝和鲍勃继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。
# 
# 爱丽丝和鲍勃轮流进行，爱丽丝先开始。最初，M = 1。
# 
# 在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。
# 
# 游戏一直持续到所有石子都被拿走。
# 
# 假设爱丽丝和鲍勃都发挥出最佳水平，返回爱丽丝可以得到的最大数量的石头。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：piles = [2,7,9,4,4]
# 输出：10
# 解释：如果一开始Alice取了一堆，Bob取了两堆，然后Alice再取两堆。爱丽丝可以得到2 + 4 + 4 =
# 10堆。如果Alice一开始拿走了两堆，那么Bob可以拿走剩下的三堆。在这种情况下，Alice得到2 + 7 = 9堆。返回10，因为它更大。
# 
# 
# 示例 2:
# 
# 
# 输入：piles = [1,2,3,4,5,100]
# 输出：104
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 10^4
# 
# 
#
from functools import cache
from itertools import accumulate
from typing import List


# @lc code=start
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        pres = list(accumulate(piles, initial=0))
        n = len(piles)

        dp = [[0] * (n + 1) for _ in range(n)]
        s = 0
        for i in range(n - 1, -1, -1):
            s += piles[i]
            for m in range(1, i // 2 + 2):
                if i + m * 2 >= n:
                    dp[i][m] = s
                else:
                    dp[i][m] = s - min(dp[i + j][max(j, m)] for j in range(1, m * 2 + 1))
        return dp[0][1]
        '''
        @cache
        def dfs(i, m) -> int:
            if i == n:
                return 0
            
            res = 0
            for j in range(1, min(m * 2 + 1, n - i + 1)):
                res = max(res, pres[-1] - pres[i] - dfs(i + j, max(j, m)))
            return res
        
        return dfs(0, 1)
        '''
# @lc code=end

