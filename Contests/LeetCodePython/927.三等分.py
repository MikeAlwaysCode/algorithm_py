#
# @lc app=leetcode.cn id=927 lang=python3
#
# [927] 三等分
#
# https://leetcode.cn/problems/three-equal-parts/description/
#
# algorithms
# Hard (35.39%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    7.6K
# Total Submissions: 19.4K
# Testcase Example:  '[1,0,1,0,1]'
#
# 给定一个由 0 和 1 组成的数组 arr ，将数组分成  3 个非空的部分 ，使得所有这些部分表示相同的二进制值。
# 
# 如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：
# 
# 
# arr[0], arr[1], ..., arr[i] 为第一部分；
# arr[i + 1], arr[i + 2], ..., arr[j - 1] 为第二部分；
# arr[j], arr[j + 1], ..., arr[arr.length - 1] 为第三部分。
# 这三个部分所表示的二进制值相等。
# 
# 
# 如果无法做到，就返回 [-1, -1]。
# 
# 注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以
# [0,1,1] 和 [1,1] 表示相同的值。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：arr = [1,0,1,0,1]
# 输出：[0,3]
# 
# 
# 示例 2：
# 
# 
# 输入：arr = [1,1,0,1,1]
# 输出：[-1,-1]
# 
# 示例 3:
# 
# 
# 输入：arr = [1,1,0,0,1]
# 输出：[0,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 3 <= arr.length <= 3 * 10^4
# arr[i] 是 0 或 1
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        cnt = sum(arr)
        if cnt % 3 != 0:
            return [-1, -1]
        
        if cnt == 0:
            return [0, 2]

        k = cnt // 3
        n = len(arr)
        first = second = third = 0
        cur = 0
        for i, a in enumerate(arr):
            if a:
                cur += 1
                if cur == 1:
                    first = i
                elif cur == k + 1:
                    second = i
                elif cur == k * 2 + 1:
                    third = i
        l = n - third
        # print(first, second, third, l)
        if first + l > second or second + l > third:
            return [-1, -1]
        if arr[first:first+l] == arr[third:] and arr[second:second+l] == arr[third:]:
            return [first+l-1, second+l]
        else:
            return [-1, -1]

# @lc code=end

