#
# @lc app=leetcode.cn id=1630 lang=python3
#
# [1630] 等差子数组
#
# https://leetcode.cn/problems/arithmetic-subarrays/description/
#
# algorithms
# Medium (75.91%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 14.9K
# Testcase Example:  '[4,6,5,9,3,7]\n[0,0,2]\n[2,3,5]'
#
# 如果一个数列由至少两个元素组成，且每两个连续元素之间的差值都相同，那么这个序列就是 等差数列 。更正式地，数列 s 是等差数列，只需要满足：对于每个有效的
# i ， s[i+1] - s[i] == s[1] - s[0] 都成立。
# 
# 例如，下面这些都是 等差数列 ：
# 
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# 
# 下面的数列 不是等差数列 ：
# 
# 1, 1, 2, 5, 7
# 
# 给你一个由 n 个整数组成的数组 nums，和两个由 m 个整数组成的数组 l 和 r，后两个数组表示 m 组范围查询，其中第 i 个查询对应范围
# [l[i], r[i]] 。所有数组的下标都是 从 0 开始 的。
# 
# 返回 boolean 元素构成的答案列表 answer 。如果子数组 nums[l[i]], nums[l[i]+1], ... , nums[r[i]]
# 可以 重新排列 形成 等差数列 ，answer[i] 的值就是 true；否则answer[i] 的值就是 false 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
# 输出：[true,false,true]
# 解释：
# 第 0 个查询，对应子数组 [4,6,5] 。可以重新排列为等差数列 [6,5,4] 。
# 第 1 个查询，对应子数组 [4,6,5,9] 。无法重新排列形成等差数列。
# 第 2 个查询，对应子数组 [5,9,3,7] 。可以重新排列为等差数列 [3,5,7,9] 。
# 
# 示例 2：
# 
# 输入：nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r =
# [4,4,9,7,9,10]
# 输出：[false,true,false,false,true,true]
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# m == l.length
# m == r.length
# 2 <= n <= 500
# 1 <= m <= 500
# 0 <= l[i] < r[i] < n
# -10^5 <= nums[i] <= 10^5
# 
# 
#
from itertools import accumulate
from typing import Counter, List


# @lc code=start
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check():
            n = len(lst)
            diff = lst[1] - lst[0]
            for j in range(2, n):
                if lst[j] - lst[j - 1] != diff:
                    return False
            return True

        ans = []
        for i, left in enumerate(l):
            lst = nums[left: r[i] + 1]
            lst.sort()
            ans.append(check())
        return ans
        '''
        ans = [False] * len(l)
        s = set()
        for i, (cl, cr) in enumerate(zip(l, r)):
            mn, mx = 10 ** 6, - 10 ** 6
            tot = 0
            s.clear()
            for j in range(cl, cr + 1):
                tot += nums[j]
                s.add(nums[j])
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])
            if mn == mx:
                ans[i] = True
            elif (mn + mx) * (cr - cl + 1) == tot * 2 and len(s) == (cr - cl + 1) and (mx - mn) % (cr - cl) == 0:
                d = (mx - mn) // (cr - cl)
                ans[i] = all(j in s for j in range(mn, mx + 1, d))
        return ans
        '''
# @lc code=end

