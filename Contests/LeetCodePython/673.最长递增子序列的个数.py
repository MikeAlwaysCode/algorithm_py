#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#
# https://leetcode.cn/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (44.42%)
# Likes:    684
# Dislikes: 0
# Total Accepted:    76.6K
# Total Submissions: 172.2K
# Testcase Example:  '[1,3,5,4,7]'
#
# 给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。
# 
# 注意 这个数列必须是 严格 递增的。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
# 
# 
# 示例 2:
# 
# 
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
# 
# 
# 
# 
# 提示: 
# 
# 
# 
# 
# 1 <= nums.length <= 2000
# -10^6 <= nums[i] <= 10^6
# 
# 
#
from typing import Callable, List

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        d, cnt = [], []
        for v in nums:
            i = bisect(len(d), lambda i: d[i][-1] >= v)
            c = 1
            if i > 0:
                k = bisect(len(d[i - 1]), lambda k: d[i - 1][k] < v)
                c = cnt[i - 1][-1] - cnt[i - 1][k]
            if i == len(d):
                d.append([v])
                cnt.append([0, c])
            else:
                d[i].append(v)
                cnt[i].append(cnt[i][-1] + c)
        return cnt[-1][-1]

def bisect(n: int, f: Callable[[int], bool]) -> int:
    l, r = 0, n
    while l < r:
        mid = (l + r) // 2
        if f(mid):
            r = mid
        else:
            l = mid + 1
    return l
# @lc code=end

