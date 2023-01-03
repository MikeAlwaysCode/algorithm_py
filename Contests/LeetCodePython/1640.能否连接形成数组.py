#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#
# https://leetcode.cn/problems/check-array-formation-through-concatenation/description/
#
# algorithms
# Easy (63.41%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    20.6K
# Total Submissions: 32.4K
# Testcase Example:  '[85]\n[[85]]'
#
# 给你一个整数数组 arr ，数组中的每个整数 互不相同 。另有一个由整数数组构成的数组 pieces，其中的整数也 互不相同 。请你以 任意顺序 连接
# pieces 中的数组以形成 arr 。但是，不允许 对每个数组 pieces[i] 中的整数重新排序。
# 
# 如果可以连接 pieces 中的数组形成 arr ，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：arr = [15,88], pieces = [[88],[15]]
# 输出：true
# 解释：依次连接 [15] 和 [88]
# 
# 
# 示例 2：
# 
# 
# 输入：arr = [49,18,16], pieces = [[16,18,49]]
# 输出：false
# 解释：即便数字相符，也不能重新排列 pieces[0]
# 
# 
# 示例 3：
# 
# 
# 输入：arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
# 输出：true
# 解释：依次连接 [91]、[4,64] 和 [78]
# 
# 
# 
# 提示：
# 
# 
# 1 <= pieces.length <= arr.length <= 100
# sum(pieces[i].length) == arr.length
# 1 <= pieces[i].length <= arr.length
# 1 <= arr[i], pieces[i][j] <= 100
# arr 中的整数 互不相同
# pieces 中的整数 互不相同（也就是说，如果将 pieces 扁平化成一维数组，数组中的所有整数互不相同）
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {p[0]:i for i, p in enumerate(pieces)}
        i = 0
        while i < len(arr):
            if arr[i] not in d:
                return False
            j = d[arr[i]]
            for k in range(len(pieces[j])):
                if arr[i+k] != pieces[j][k]:
                    return False
            i += len(pieces[j])
        return True
# @lc code=end

