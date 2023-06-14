#
# @lc app=leetcode.cn id=1375 lang=python3
#
# [1375] 二进制字符串前缀一致的次数
#
# https://leetcode.cn/problems/number-of-times-binary-string-is-prefix-aligned/description/
#
# algorithms
# Medium (59.56%)
# Likes:    80
# Dislikes: 0
# Total Accepted:    14.3K
# Total Submissions: 22.5K
# Testcase Example:  '[3,2,4,1,5]'
#
# 给你一个长度为 n 、下标从 1 开始的二进制字符串，所有位最开始都是 0 。我们会按步翻转该二进制字符串的所有位（即，将 0 变为 1）。
# 
# 给你一个下标从 1 开始的整数数组 flips ，其中 flips[i] 表示对应下标 i 的位将会在第 i 步翻转。
# 
# 二进制字符串 前缀一致 需满足：在第 i 步之后，在 闭 区间 [1, i] 内的所有位都是 1 ，而其他位都是 0 。
# 
# 返回二进制字符串在翻转过程中 前缀一致 的次数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：flips = [3,2,4,1,5]
# 输出：2
# 解释：二进制字符串最开始是 "00000" 。
# 执行第 1 步：字符串变为 "00100" ，不属于前缀一致的情况。
# 执行第 2 步：字符串变为 "01100" ，不属于前缀一致的情况。
# 执行第 3 步：字符串变为 "01110" ，不属于前缀一致的情况。
# 执行第 4 步：字符串变为 "11110" ，属于前缀一致的情况。
# 执行第 5 步：字符串变为 "11111" ，属于前缀一致的情况。
# 在翻转过程中，前缀一致的次数为 2 ，所以返回 2 。
# 
# 
# 示例 2：
# 
# 
# 输入：flips = [4,1,2,3]
# 输出：1
# 解释：二进制字符串最开始是 "0000" 。
# 执行第 1 步：字符串变为 "0001" ，不属于前缀一致的情况。
# 执行第 2 步：字符串变为 "1001" ，不属于前缀一致的情况。
# 执行第 3 步：字符串变为 "1101" ，不属于前缀一致的情况。
# 执行第 4 步：字符串变为 "1111" ，属于前缀一致的情况。
# 在翻转过程中，前缀一致的次数为 1 ，所以返回 1 。
# 
# 
# 
# 提示：
# 
# 
# n == flips.length
# 1 <= n <= 5 * 10^4
# flips 是范围 [1, n] 中所有整数构成的一个排列
# 
# 
#
from itertools import accumulate
from typing import List


# @lc code=start
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        return sum(v == i for i, v in enumerate(list(accumulate(flips, func = max)), 1))
# @lc code=end

