#
# @lc app=leetcode.cn id=1819 lang=python3
#
# [1819] 序列中不同最大公约数的数目
#
# https://leetcode.cn/problems/number-of-different-subsequences-gcds/description/
#
# algorithms
# Hard (41.75%)
# Likes:    130
# Dislikes: 0
# Total Accepted:    10.6K
# Total Submissions: 18K
# Testcase Example:  '[6,10,3]'
#
# 给你一个由正整数组成的数组 nums 。
# 
# 数字序列的 最大公约数 定义为序列中所有整数的共有约数中的最大整数。
# 
# 
# 例如，序列 [4,6,16] 的最大公约数是 2 。
# 
# 
# 数组的一个 子序列 本质是一个序列，可以通过删除数组中的某些元素（或者不删除）得到。
# 
# 
# 例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
# 
# 
# 计算并返回 nums 的所有 非空 子序列中 不同 最大公约数的 数目 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [6,10,3]
# 输出：5
# 解释：上图显示了所有的非空子序列与各自的最大公约数。
# 不同的最大公约数为 6 、10 、3 、2 和 1 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [5,15,40,5,6]
# 输出：7
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#
import math
from typing import List


# @lc code=start
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        ans, mx = 0, max(nums)
        has = [False] * (mx + 1)
        for x in nums:
            if not has[x]:
                has[x] = True
                ans += 1  # 单独一个数也算
        for i in range(1, mx // 3 + 1):  # 优化循环上界
            if has[i]: continue
            g = 0  # 0 和任何数 x 的最大公约数都是 x
            for j in range(i * 2, mx + 1, i):  # 枚举 i 的倍数 j
                if has[j]:  # 如果 j 在 nums 中
                    g = math.gcd(g, j)  # 更新最大公约数
                    if g == i:  # 找到一个答案（g 无法继续减小）
                        ans += 1
                        break  # 提前退出循环
        return ans
        '''
        maxVal = max(nums)
        occured = [False] * (maxVal + 1)
        for num in nums:
            occured[num] = True
        ans = 0
        for i in range(1, maxVal + 1):
            subGcd = 0
            for j in range(i, maxVal + 1, i):
                if occured[j]:
                    if subGcd == 0:
                        subGcd = j
                    else:
                        subGcd = math.gcd(subGcd, j)
                    if subGcd == i:
                        ans += 1
                        break
        return ans
        '''
# @lc code=end

