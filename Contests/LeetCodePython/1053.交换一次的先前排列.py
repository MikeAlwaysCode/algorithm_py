#
# @lc app=leetcode.cn id=1053 lang=python3
#
# [1053] 交换一次的先前排列
#
# https://leetcode.cn/problems/previous-permutation-with-one-swap/description/
#
# algorithms
# Medium (45.75%)
# Likes:    84
# Dislikes: 0
# Total Accepted:    14.5K
# Total Submissions: 30.2K
# Testcase Example:  '[3,2,1]'
#
# 给你一个正整数数组 arr（可能存在重复的元素），请你返回可在 一次交换（交换两数字 arr[i] 和 arr[j] 的位置）后得到的、按字典序排列小于
# arr 的最大排列。
# 
# 如果无法这么操作，就请返回原数组。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：arr = [3,2,1]
# 输出：[3,1,2]
# 解释：交换 2 和 1
# 
# 
# 示例 2：
# 
# 
# 输入：arr = [1,1,5]
# 输出：[1,1,5]
# 解释：已经是最小排列
# 
# 
# 示例 3：
# 
# 
# 输入：arr = [1,9,4,6,7]
# 输出：[1,7,4,6,9]
# 解释：交换 9 和 7
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^4
# 
# 
#
import math
from typing import List


# @lc code=start
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 1
        while i > 0 and arr[i] >= arr[i - 1]:
            i -= 1
        if i == 0:
            return arr
        
        i -= 1
        j = n - 1
        while arr[j] >= arr[i] or arr[j] == arr[j - 1]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        return arr
# @lc code=end

