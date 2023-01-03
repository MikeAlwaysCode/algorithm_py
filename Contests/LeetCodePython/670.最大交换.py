#
# @lc app=leetcode.cn id=670 lang=python3
#
# [670] 最大交换
#
# https://leetcode.cn/problems/maximum-swap/description/
#
# algorithms
# Medium (46.42%)
# Likes:    297
# Dislikes: 0
# Total Accepted:    38.1K
# Total Submissions: 80.7K
# Testcase Example:  '2736'
#
# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
# 
# 示例 1 :
# 
# 
# 输入: 2736
# 输出: 7236
# 解释: 交换数字2和数字7。
# 
# 
# 示例 2 :
# 
# 
# 输入: 9973
# 输出: 9973
# 解释: 不需要交换。
# 
# 
# 注意:
# 
# 
# 给定数字的范围是 [0, 10^8]
# 
# 
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        maxIdx = n - 1
        idx1 = idx2 = -1
        for i in range(n - 1, -1, -1):
            if s[i] > s[maxIdx]:
                maxIdx = i
            elif s[i] < s[maxIdx]:
                idx1, idx2 = i, maxIdx
        if idx1 < 0:
            return num
        s[idx1], s[idx2] = s[idx2], s[idx1]
        return int(''.join(s))
# @lc code=end

