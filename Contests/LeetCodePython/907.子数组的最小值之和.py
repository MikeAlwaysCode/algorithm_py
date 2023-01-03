#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#
# https://leetcode.cn/problems/sum-of-subarray-minimums/description/
#
# algorithms
# Medium (35.21%)
# Likes:    454
# Dislikes: 0
# Total Accepted:    24.5K
# Total Submissions: 67.9K
# Testcase Example:  '[3,1,2,4]'
#
# 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
# 
# 由于答案可能很大，因此 返回答案模 10^9 + 7 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：arr = [3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
# 
# 示例 2：
# 
# 
# 输入：arr = [11,81,94,43,3]
# 输出：444
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(-1)
        ans, st = 0, [-1]  # 哨兵
        for r, x in enumerate(arr):
            # 也可以 while arr[st[-1]] > x，效率略高一点
            while len(st) > 1 and arr[st[-1]] >= x:
                i = st.pop()
                ans += arr[i] * (i - st[-1]) * (r - i)  # 累加贡献
            st.append(r)
        return ans % (10 ** 9 + 7)
# @lc code=end

