#
# @lc app=leetcode.cn id=1502 lang=python3
#
# [1502] 判断能否形成等差数列
#
# https://leetcode.cn/problems/can-make-arithmetic-progression-from-sequence/description/
#
# algorithms
# Easy (69.96%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    40.7K
# Total Submissions: 58.3K
# Testcase Example:  '[3,5,1]'
#
# 给你一个数字数组 arr 。
# 
# 如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。
# 
# 如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [3,5,1]
# 输出：true
# 解释：对数组重新排序得到 [1,3,5] 或者 [5,3,1] ，任意相邻两项的差分别为 2 或 -2 ，可以形成等差数列。
# 
# 
# 示例 2：
# 
# 输入：arr = [1,2,4]
# 输出：false
# 解释：无法通过重新排序得到等差数列。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= arr.length <= 1000
# -10^6 <= arr[i] <= 10^6
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return all(arr[i + 1] + arr[i - 1] == arr[i] * 2 for i in range(1, len(arr) - 1))
# @lc code=end

