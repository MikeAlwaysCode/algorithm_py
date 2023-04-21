#
# @lc app=leetcode.cn id=1494 lang=python3
#
# [1494] 并行课程 II
#
# https://leetcode.cn/problems/parallel-courses-ii/description/
#
# algorithms
# Hard (40.61%)
# Likes:    110
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 10.7K
# Testcase Example:  '4\n[[2,1],[3,1],[1,4]]\n2'
#
# 给你一个整数 n 表示某所大学里课程的数目，编号为 1 到 n ，数组 relations 中， relations[i] = [xi, yi]
# 表示一个先修课的关系，也就是课程 xi 必须在课程 yi 之前上。同时你还有一个整数 k 。
# 
# 在一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了。
# 
# 请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
# 输出：3 
# 解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
# 输出：4 
# 解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。
# 
# 
# 示例 3：
# 
# 
# 输入：n = 11, relations = [], k = 2
# 输出：6
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 15
# 1 <= k <= n
# 0 <= relations.length <= n * (n-1) / 2
# relations[i].length == 2
# 1 <= xi, yi <= n
# xi != yi
# 所有先修关系都是不同的，也就是说 relations[i] != relations[j] 。
# 题目输入的图是个有向无环图。
# 
# 
#
from functools import cache
from itertools import combinations
from math import ceil
from typing import List


# @lc code=start
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        @cache
        def dfs(state):
            if state == (1 << n) - 1:
                return 0
            nex = [j for j in range(n) if not state & (1 << j) and state & pre[j] == pre[j]]
            m = len(nex)
            floor = m // k + int(m % k > 0)
            res = n
            for item in combinations(nex, min(m, k)):
                cur = 1 + dfs(state | sum(1 << j for j in item))
                res = res if res < cur else cur
                if res == floor: # 性能优化点，提前终止
                    break
            return res
        
        pre = [0] * n
        for x, y in relations:
            pre[y - 1] |= 1 << (x - 1)
        return dfs(0)
        '''
        if len(relations) == 1:
            res = ceil(n / k)
            return 2 if res == 1 else res
        
        #---------- 题目提示可以bitmask
        pre = [0 for _ in range(n)]
        for x, y in relations:
            x -= 1                  #归一化，从1开始->从开始
            y -= 1
            pre[y] |= (1 << x)      #n最多15位

        dp = [0 for _ in range(2 ** n)]
        for state in range(1, 2 ** n):
            dp[state] = n                   #注意不是state中1的个数。因为这只是中间的状态！！！
        for state in range(0, 2 ** n):      #枚举所有的状态
            #---- 找下一状态
            nxt = 0
            for x in range(n):
                if (state & pre[x]) == pre[x]:      #x前驱的课都已经修过了
                    nxt |= (1 << x)
            #---- 枚举nxt的子集
            nxt = nxt & (~ state)                   #state中已经为1，修过了。
            sub = nxt
            while sub > 0:
                bit1 = bin(sub)[2: ].count('1')
                # bit1 = self.cnt_bit1(sub)
                if bit1 <= k:
                    nxt_state = state | sub
                    dp[nxt_state] = min(dp[nxt_state], dp[state] + 1)    

                sub = (sub - 1) & nxt 

        return dp[2 ** n - 1]
        '''
# @lc code=end

