#
# @lc app=leetcode.cn id=6124 lang=python3
#
# [6124] 第一个出现两次的字母
#

from typing import *
# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        c = [0] * 26
        for x in s:
            c[ord(x)-97] += 1
            if c[ord(x)-97] >= 2:
                return x
        return ""
# @lc code=end

