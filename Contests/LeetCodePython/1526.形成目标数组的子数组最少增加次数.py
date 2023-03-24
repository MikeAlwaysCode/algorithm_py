#
# @lc app=leetcode.cn id=1526 lang=python3
#
# [1526] 形成目标数组的子数组最少增加次数
#
# https://leetcode.cn/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/
#
# algorithms
# Hard (64.56%)
# Likes:    70
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 7.6K
# Testcase Example:  '[1,2,3,2,1]'
#
# 给你一个整数数组 target 和一个数组 initial ，initial 数组与 target  数组有同样的维度，且一开始全部为 0 。
# 
# 请你返回从 initial 得到  target 的最少操作次数，每次操作需遵循以下规则：
# 
# 
# 在 initial 中选择 任意 子数组，并将子数组中每个元素增加 1 。
# 
# 
# 答案保证在 32 位有符号整数以内。
# 
# 
# 
# 示例 1：
# 
# 输入：target = [1,2,3,2,1]
# 输出：3
# 解释：我们需要至少 3 次操作从 intial 数组得到 target 数组。
# [0,0,0,0,0] 将下标为 0 到 4 的元素（包含二者）加 1 。
# [1,1,1,1,1] 将下标为 1 到 3 的元素（包含二者）加 1 。
# [1,2,2,2,1] 将下表为 2 的元素增加 1 。
# [1,2,3,2,1] 得到了目标数组。
# 
# 
# 示例 2：
# 
# 输入：target = [3,1,1,2]
# 输出：4
# 解释：(initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2]
# (target) 。
# 
# 
# 示例 3：
# 
# 输入：target = [3,1,5,4,2]
# 输出：7
# 解释：(initial)[0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] 
# ⁠                                 -> [3,1,2,2,2] -> [3,1,3,3,2] ->
# [3,1,4,4,2] -> [3,1,5,4,2] (target)。
# 
# 
# 示例 4：
# 
# 输入：target = [1,1,1,1]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= target.length <= 10^5
# 1 <= target[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        ans = target[0]
        for i in range(1, n):
            ans += max(target[i] - target[i - 1], 0)
        return ans
# @lc code=end

