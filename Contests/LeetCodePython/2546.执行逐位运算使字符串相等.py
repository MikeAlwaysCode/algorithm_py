#
# @lc app=leetcode.cn id=2546 lang=python3
#
# [2546] 执行逐位运算使字符串相等
#
# https://leetcode.cn/problems/apply-bitwise-operations-to-make-strings-equal/description/
#
# algorithms
# Medium (41.33%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 9.1K
# Testcase Example:  '"1010"\n"0110"'
#
# 给你两个下标从 0 开始的 二元 字符串 s 和 target ，两个字符串的长度均为 n 。你可以对 s 执行下述操作 任意 次：
# 
# 
# 选择两个 不同 的下标 i 和 j ，其中 0 <= i, j < n 。
# 同时，将 s[i] 替换为 (s[i] OR s[j]) ，s[j] 替换为 (s[i] XOR s[j]) 。
# 
# 
# 例如，如果 s = "0110" ，你可以选择 i = 0 和 j = 2，然后同时将 s[0] 替换为 (s[0] OR s[2] = 0 OR 1 =
# 1)，并将 s[2] 替换为 (s[0] XOR s[2] = 0 XOR 1 = 1)，最终得到 s = "1110" 。
# 
# 如果可以使 s 等于 target ，返回 true ，否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "1010", target = "0110"
# 输出：true
# 解释：可以执行下述操作：
# - 选择 i = 2 和 j = 0 ，得到 s = "0010".
# - 选择 i = 2 和 j = 1 ，得到 s = "0110".
# 可以使 s 等于 target ，返回 true 。
# 
# 
# 示例 2：
# 
# 输入：s = "11", target = "00"
# 输出：false
# 解释：执行任意次操作都无法使 s 等于 target 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == s.length == target.length
# 2 <= n <= 10^5
# s 和 target 仅由数字 0 和 1 组成
# 
# 
#

# @lc code=start
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        # if s != target and (s.count("1") == 0 or target.count("1") == 0):
        if s != target and ("1" in s) != ("1" in target):
            return False
        return True
# @lc code=end

