#
# @lc app=leetcode.cn id=6127 lang=python3
#
# [6127] 优质数对的数目
#

from typing import *
# @lc code=start
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        # ct = Counter(x.bit_count() for x in set(nums))
        # ans = 0
        # for ak, av in ct.items():
        #     for bk, bv in ct.items():
        #         if ak + bk >= k:
        #             ans += av * bv
        # return ans
        ans = 0
        ct = [0] * 30
        for x in set(nums):
            ct[x.bit_count()] += 1
        s = sum(ct[k:]) 
        for i, c in enumerate(ct):
            ans += c * s
            if 0 <= k - i - 1 < 30:
                s += ct[k - i - 1]
        return ans
# @lc code=end

