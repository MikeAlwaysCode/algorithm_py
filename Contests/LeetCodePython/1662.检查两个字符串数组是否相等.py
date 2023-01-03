#
# @lc app=leetcode.cn id=1662 lang=python3
#
# [1662] 检查两个字符串数组是否相等
#
# https://leetcode.cn/problems/check-if-two-string-arrays-are-equivalent/description/
#
# algorithms
# Easy (82.11%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    35.5K
# Total Submissions: 43.2K
# Testcase Example:  '["ab", "c"]\n["a", "bc"]'
#
# 给你两个字符串数组 word1 和 word2 。如果两个数组表示的字符串相同，返回 true ；否则，返回 false 。
# 
# 数组表示的字符串 是由数组中的所有元素 按顺序 连接形成的字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：word1 = ["ab", "c"], word2 = ["a", "bc"]
# 输出：true
# 解释：
# word1 表示的字符串为 "ab" + "c" -> "abc"
# word2 表示的字符串为 "a" + "bc" -> "abc"
# 两个字符串相同，返回 true
# 
# 示例 2：
# 
# 
# 输入：word1 = ["a", "cb"], word2 = ["ab", "c"]
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# word1[i] 和 word2[i] 由小写字母组成
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
# @lc code=end

