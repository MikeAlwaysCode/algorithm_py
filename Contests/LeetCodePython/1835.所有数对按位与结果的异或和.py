#
# @lc app=leetcode.cn id=1835 lang=python3
#
# [1835] 所有数对按位与结果的异或和
#
# https://leetcode.cn/problems/find-xor-sum-of-all-pairs-bitwise-and/description/
#
# algorithms
# Hard (54.86%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    4.8K
# Total Submissions: 8.7K
# Testcase Example:  '[1,2,3]\n[6,5]'
#
# 列表的 异或和（XOR sum）指对所有元素进行按位 XOR 运算的结果。如果列表中仅有一个元素，那么其 异或和 就等于该元素。
# 
# 
# 例如，[1,2,3,4] 的 异或和 等于 1 XOR 2 XOR 3 XOR 4 = 4 ，而 [3] 的 异或和 等于 3 。
# 
# 
# 给你两个下标 从 0 开始 计数的数组 arr1 和 arr2 ，两数组均由非负整数组成。
# 
# 根据每个 (i, j) 数对，构造一个由 arr1[i] AND arr2[j]（按位 AND 运算）结果组成的列表。其中 0 <= i <
# arr1.length 且 0 <= j < arr2.length 。
# 
# 返回上述列表的 异或和 。
# 
# 
# 
# 示例 1：
# 
# 输入：arr1 = [1,2,3], arr2 = [6,5]
# 输出：0
# 解释：列表 = [1 AND 6, 1 AND 5, 2 AND 6, 2 AND 5, 3 AND 6, 3 AND 5] =
# [0,1,2,0,2,1] ，
# 异或和 = 0 XOR 1 XOR 2 XOR 0 XOR 2 XOR 1 = 0 。
# 
# 示例 2：
# 
# 输入：arr1 = [12], arr2 = [4]
# 输出：4
# 解释：列表 = [12 AND 4] = [4] ，异或和 = 4 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr1.length, arr2.length <= 10^5
# 0 <= arr1[i], arr2[j] <= 10^9
# 
# 
#
from functools import reduce
from operator import xor
from typing import List


# @lc code=start
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        '''
        ans = 0
        for bit in range(31):
            l = r = 0
            for a in arr1:
                l ^= a >> bit & 1
            for a in arr2:
                r ^= a >> bit & 1
            ans |= (l & r) << bit
        return ans
        '''
        '''
        ans = 0
        xor2 = 0
        for a in arr1:
            xor2 ^= a
        for a in arr2:
            ans ^= (xor2 & a)
        return ans
        '''
        tot1 = reduce(xor, arr1)
        tot2 = reduce(xor, arr2)
        return tot1 & tot2
# @lc code=end

