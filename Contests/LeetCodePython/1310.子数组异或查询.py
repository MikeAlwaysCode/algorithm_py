#
# @lc app=leetcode.cn id=1310 lang=python3
#
# [1310] 子数组异或查询
#
# https://leetcode.cn/problems/xor-queries-of-a-subarray/description/
#
# algorithms
# Medium (71.85%)
# Likes:    153
# Dislikes: 0
# Total Accepted:    41.5K
# Total Submissions: 57.8K
# Testcase Example:  '[1,3,4,8]\n[[0,1],[1,2],[0,3],[3,3]]'
#
# 有一个正整数数组 arr，现给你一个对应的查询数组 queries，其中 queries[i] = [Li, Ri]。
# 
# 对于每个查询 i，请你计算从 Li 到 Ri 的 XOR 值（即 arr[Li] xor arr[Li+1] xor ... xor
# arr[Ri]）作为本次查询的结果。
# 
# 并返回一个包含给定查询 queries 所有结果的数组。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
# 输出：[2,7,14,8] 
# 解释：
# 数组中元素的二进制表示形式是：
# 1 = 0001 
# 3 = 0011 
# 4 = 0100 
# 8 = 1000 
# 查询的 XOR 值为：
# [0,1] = 1 xor 3 = 2 
# [1,2] = 3 xor 4 = 7 
# [0,3] = 1 xor 3 xor 4 xor 8 = 14 
# [3,3] = 8
# 
# 
# 示例 2：
# 
# 
# 输入：arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
# 输出：[8,0,4,4]
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
# queries[i].length == 2
# 0 
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pres = [0] * (n + 1)
        for i, a in enumerate(arr):
            pres[i + 1] = pres[i] ^ a

        ans = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            ans[i] = pres[r + 1] ^ pres[l]
        return ans
# @lc code=end

