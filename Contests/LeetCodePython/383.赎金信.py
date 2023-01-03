#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
# https://leetcode.cn/problems/ransom-note/description/
#
# algorithms
# Easy (62.06%)
# Likes:    430
# Dislikes: 0
# Total Accepted:    217.5K
# Total Submissions: 350.5K
# Testcase Example:  '"a"\n"b"'
#
# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
# 
# 如果可以，返回 true ；否则返回 false 。
# 
# magazine 中的每个字符只能在 ransomNote 中使用一次。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：ransomNote = "a", magazine = "b"
# 输出：false
# 
# 
# 示例 2：
# 
# 
# 输入：ransomNote = "aa", magazine = "ab"
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：ransomNote = "aa", magazine = "aab"
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote 和 magazine 由小写英文字母组成
# 
# 
#
from typing import collections
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
# @lc code=end

