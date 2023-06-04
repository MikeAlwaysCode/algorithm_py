#
# @lc app=leetcode.cn id=1130 lang=python3
#
# [1130] 叶值的最小代价生成树
#
# https://leetcode.cn/problems/minimum-cost-tree-from-leaf-values/description/
#
# algorithms
# Medium (64.91%)
# Likes:    295
# Dislikes: 0
# Total Accepted:    10.9K
# Total Submissions: 16.2K
# Testcase Example:  '[6,2,4]'
#
# 给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：
# 
# 
# 每个节点都有 0 个或是 2 个子节点。
# 数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。
# 每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
# 
# 
# 在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。
# 
# 如果一个节点有 0 个子节点，那么该节点为叶节点。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：arr = [6,2,4]
# 输出：32
# 解释：有两种可能的树，第一种的非叶节点的总和为 36 ，第二种非叶节点的总和为 32 。 
# 
# 
# 示例 2：
# 
# 
# 输入：arr = [4,11]
# 输出：44
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= arr.length <= 40
# 1 <= arr[i] <= 15
# 答案保证是一个 32 位带符号整数，即小于 2^31 。
# 
# 
#
import math
from typing import List


# @lc code=start
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans = 0
        stk = []
        for x in arr:
            while stk and stk[-1] <= x:
                y = stk.pop()
                if not stk or stk[-1] > x:
                    ans += y * x
                else:
                    ans += y * stk[-1]
            stk.append(x)
        while len(stk) >= 2:
            x = stk.pop()
            ans += stk[-1] * x
        return ans
        '''
        n = len(arr)
        dp = [[math.inf] * n for _ in range(n)]
        mx = [[0] * n for _ in range(n)]
        for j in range(n):
            mx[j][j] = arr[j]
            dp[j][j] = 0
            for i in range(j - 1, -1, -1):
                mx[i][j] = max(arr[i], mx[i + 1][j])
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + mx[i][k] * mx[k + 1][j])
        return dp[0][-1]
        '''
# @lc code=end

