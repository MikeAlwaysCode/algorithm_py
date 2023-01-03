#
# @lc app=leetcode.cn id=6201 lang=python3
#
# [6201] 找出前缀异或的原始数组
#
# https://leetcode.cn/problems/find-the-original-array-of-prefix-xor/description/
#
# algorithms
# Medium (82.88%)
# Likes:    2
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 5K
# Testcase Example:  '[5,2,0,3,1]'
#
# 给你一个长度为 n 的 整数 数组 pref 。找出并返回满足下述条件且长度为 n 的数组 arr ：
# 
# 
# pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
# 
# 
# 注意 ^ 表示 按位异或（bitwise-xor）运算。
# 
# 可以证明答案是 唯一 的。
# 
# 
# 
# 示例 1：
# 
# 输入：pref = [5,2,0,3,1]
# 输出：[5,7,2,3,2]
# 解释：从数组 [5,7,2,3,2] 可以得到如下结果：
# - pref[0] = 5
# - pref[1] = 5 ^ 7 = 2
# - pref[2] = 5 ^ 7 ^ 2 = 0
# - pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3
# - pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1
# 
# 
# 示例 2：
# 
# 输入：pref = [13]
# 输出：[13]
# 解释：pref[0] = arr[0] = 13
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= pref.length <= 10^5
# 0 <= pref[i] <= 10^6
# 
# 
#
from itertools import pairwise
from typing import List
# @lc code=start
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [ x ^ y for x, y in pairwise(pref)]
        '''
        n = len(pref)
        ans = [0] * n
        ans[0] = pref[0]
        for i in range(1, n):
            ans[i] = pref[i-1] ^ pref[i]
        return ans
        '''
# @lc code=end

