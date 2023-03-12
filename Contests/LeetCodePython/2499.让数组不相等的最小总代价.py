#
# @lc app=leetcode.cn id=2499 lang=python3
#
# [2499] 让数组不相等的最小总代价
#
# https://leetcode.cn/problems/minimum-total-cost-to-make-arrays-unequal/description/
#
# algorithms
# Hard (42.34%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    1.4K
# Total Submissions: 3.3K
# Testcase Example:  '[1,2,3,4,5]\n[1,2,3,4,5]'
#
# 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，两者长度都为 n 。
# 
# 每次操作中，你可以选择交换 nums1 中任意两个下标处的值。操作的 开销 为两个下标的 和 。
# 
# 你的目标是对于所有的 0 <= i <= n - 1 ，都满足 nums1[i] != nums2[i] ，你可以进行 任意次
# 操作，请你返回达到这个目标的 最小 总代价。
# 
# 请你返回让 nums1 和 nums2 满足上述条件的 最小总代价 ，如果无法达成目标，返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [1,2,3,4,5], nums2 = [1,2,3,4,5]
# 输出：10
# 解释：
# 实现目标的其中一种方法为：
# - 交换下标为 0 和 3 的两个值，代价为 0 + 3 = 3 。现在 nums1 = [4,2,3,1,5] 。
# - 交换下标为 1 和 2 的两个值，代价为 1 + 2 = 3 。现在 nums1 = [4,3,2,1,5] 。
# - 交换下标为 0 和 4 的两个值，代价为 0 + 4 = 4 。现在 nums1 = [5,3,2,1,4] 。
# 最后，对于每个下标 i ，都有 nums1[i] != nums2[i] 。总代价为 10 。
# 还有别的交换值的方法，但是无法得到代价和小于 10 的方案。
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [2,2,2,1,3], nums2 = [1,2,2,3,3]
# 输出：10
# 解释：
# 实现目标的一种方法为：
# - 交换下标为 2 和 3 的两个值，代价为 2 + 3 = 5 。现在 nums1 = [2,2,1,2,3] 。
# - 交换下标为 1 和 4 的两个值，代价为 1 + 4 = 5 。现在 nums1 = [2,3,1,2,2] 。
# 总代价为 10 ，是所有方案中的最小代价。
# 
# 
# 示例 3：
# 
# 
# 输入：nums1 = [1,2,2], nums2 = [1,2,2]
# 输出：-1
# 解释：
# 不管怎么操作，都无法满足题目要求。
# 所以返回 -1 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums1.length == nums2.length
# 1 <= n <= 10^5
# 1 <= nums1[i], nums2[i] <= n
# 
# 
#
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        ans = swap_cnt = mode_cnt = mode = 0
        cnt = [0] * (len(nums1) + 1)
        for i, (x, y) in enumerate(zip(nums1, nums2)):
            if x == y:
                ans += i
                swap_cnt += 1
                cnt[x] += 1
                if cnt[x] > mode_cnt:
                    mode_cnt, mode = cnt[x], x

        for i, (x, y) in enumerate(zip(nums1, nums2)):
            if mode_cnt * 2 <= swap_cnt: break
            if x != y and x != mode and y != mode:
                ans += i
                swap_cnt += 1
        return ans if mode_cnt * 2 <= swap_cnt else -1
        '''
        n = len(nums1)
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        ans = c = 0
        cc = Counter()
        for i in range(n):
            if cnt1[nums1[i]] + cnt2[nums2[i]] > n:
                return -1
            if nums1[i] == nums2[i]:
                ans += i
                c += 1
                cc[nums1[i]] += 1

        if c == n or c == 0:
            return ans
        
        k = 0
        if cc.most_common(1)[0][1] * 2 > c:
            k = cc.most_common(1)[0][1] * 2 - c
            ns = cc.most_common(1)[0][0]

        i = 0
        while k and i < n:
            if nums1[i] != nums2[i] and nums1[i] != ns and nums2[i] != ns:
                ans += i
                k -= 1
            i += 1

        if k:
            return -1
        else:
            return ans
        '''
# @lc code=end

