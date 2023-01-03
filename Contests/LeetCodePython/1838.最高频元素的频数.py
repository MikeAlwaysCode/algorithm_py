#
# @lc app=leetcode.cn id=1838 lang=python3
#
# [1838] 最高频元素的频数
#
# https://leetcode.cn/problems/frequency-of-the-most-frequent-element/description/
#
# algorithms
# Medium (42.95%)
# Likes:    251
# Dislikes: 0
# Total Accepted:    35.3K
# Total Submissions: 82.1K
# Testcase Example:  '[1,2,4]\n5'
#
# 元素的 频数 是该元素在一个数组中出现的次数。
# 
# 给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。
# 
# 执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,4], k = 5
# 输出：3
# 解释：对第一个元素执行 3 次递增操作，对第二个元素执 2 次递增操作，此时 nums = [4,4,4] 。
# 4 是数组中最高频元素，频数是 3 。
# 
# 示例 2：
# 
# 
# 输入：nums = [1,4,8,13], k = 5
# 输出：2
# 解释：存在多种最优解决方案：
# - 对第一个元素执行 3 次递增操作，此时 nums = [4,4,8,13] 。4 是数组中最高频元素，频数是 2 。
# - 对第二个元素执行 4 次递增操作，此时 nums = [1,8,8,13] 。8 是数组中最高频元素，频数是 2 。
# - 对第三个元素执行 5 次递增操作，此时 nums = [1,4,13,13] 。13 是数组中最高频元素，频数是 2 。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [3,9,6], k = 2
# 输出：1
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
# 
# 
#
from itertools import accumulate
from typing import List
# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        pres = list(accumulate(nums, initial=0))

        def check(len: int) -> bool:
            for l in range(0, n - len + 1):
                r = l + len - 1
                cur = pres[r + 1] - pres[l]
                tot = nums[r] * len
                if tot - cur <= k:
                    return True
            return False

        l, r = 0, n
        while l < r:
            mid = l + r + 1 >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return r
        '''
        nums.sort()
        n = len(nums)
        l = 0
        total = 0
        res = 1
        for r in range(1, n):
            total += (nums[r] - nums[r - 1]) * (r - l)
            while total > k:
                total -= nums[r] - nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res
        '''
# @lc code=end

