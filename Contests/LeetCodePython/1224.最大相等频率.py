#
# @lc app=leetcode.cn id=1224 lang=python3
#
# [1224] 最大相等频率
#
# https://leetcode.cn/problems/maximum-equal-frequency/description/
#
# algorithms
# Hard (42.09%)
# Likes:    162
# Dislikes: 0
# Total Accepted:    19.9K
# Total Submissions: 47.3K
# Testcase Example:  '[2,2,1,1,5,3,3,5]'
#
# 给你一个正整数数组 nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回该前缀的长度：
# 
# 
# 从前缀中 恰好删除一个 元素后，剩下每个数字的出现次数都相同。
# 
# 
# 如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,2,1,1,5,3,3,5]
# 输出：7
# 解释：对于长度为 7 的子数组 [2,2,1,1,5,3,3]，如果我们从中删去 nums[4] = 5，就可以得到
# [2,2,1,1,3,3]，里面每个数字都出现了两次。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
# 输出：13
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq, count = Counter(), Counter()
        ans = maxFreq = 0
        for i, num in enumerate(nums):
            if count[num]:
                freq[count[num]] -= 1
            count[num] += 1
            maxFreq = max(maxFreq, count[num])
            freq[count[num]] += 1
            if maxFreq == 1 or \
               freq[maxFreq] * maxFreq + freq[maxFreq - 1] * (maxFreq - 1) == i + 1 and freq[maxFreq] == 1 or \
               freq[maxFreq] * maxFreq + 1 == i + 1 and freq[1] == 1:
                ans = max(ans, i + 1)
        return ans
# @lc code=end

