#
# @lc app=leetcode.cn id=6172 lang=python3
#
# [6172] 严格回文的数字
#
# https://leetcode.cn/problems/strictly-palindromic-number/description/
#
# algorithms
# Medium (87.59%)
# Likes:    0
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 3.9K
# Testcase Example:  '9'
#
# 如果一个整数 n 在 b 进制下（b 为 2 到 n - 2 之间的所有整数）对应的字符串 全部 都是 回文的 ，那么我们称这个数 n 是 严格回文
# 的。
# 
# 给你一个整数 n ，如果 n 是 严格回文 的，请返回 true ，否则返回 false 。
# 
# 如果一个字符串从前往后读和从后往前读完全相同，那么这个字符串是 回文的 。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 9
# 输出：false
# 解释：在 2 进制下：9 = 1001 ，是回文的。
# 在 3 进制下：9 = 100 ，不是回文的。
# 所以，9 不是严格回文数字，我们返回 false 。
# 注意在 4, 5, 6 和 7 进制下，n = 9 都不是回文的。
# 
# 
# 示例 2：
# 
# 输入：n = 4
# 输出：false
# 解释：我们只考虑 2 进制：4 = 100 ，不是回文的。
# 所以我们返回 false 。
# 
# 
# 
# 
# 提示：
# 
# 
# 4 <= n <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
# @lc code=end

