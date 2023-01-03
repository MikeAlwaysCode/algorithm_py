#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode.cn/problems/valid-anagram/description/
#
# algorithms
# Easy (65.58%)
# Likes:    637
# Dislikes: 0
# Total Accepted:    469.2K
# Total Submissions: 715.5K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 
# 
# 示例 2:
# 
# 
# 输入: s = "rat", t = "car"
# 输出: false
# 
# 
# 
# 提示:
# 
# 
# 1 
# s 和 t 仅包含小写字母
# 
# 
# 
# 
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
# 
#
from collections import defaultdict
from typing import Counter
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

        # sdict = defaultdict(int)
        # tdict = defaultdict(int)

        # for x in s:
        #     sdict[x] += 1
        # for x in t:
        #     tdict[x] += 1

        # if sdict == tdict:
        #     return True
        # else:
        #     return False
# @lc code=end

