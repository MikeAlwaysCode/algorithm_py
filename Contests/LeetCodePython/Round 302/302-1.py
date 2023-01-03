#
# @lc app=leetcode.cn id=6131 lang=python3
#
# [6131] 不可能得到的最短骰子序列
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

sol = Solution()
s = "abccbaacz"
print(sol.repeatedCharacter(s))

