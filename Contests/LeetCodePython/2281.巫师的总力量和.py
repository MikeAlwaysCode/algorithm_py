#
# @lc app=leetcode.cn id=2281 lang=python3
#
# [2281] 巫师的总力量和
#
# https://leetcode.cn/problems/sum-of-total-strength-of-wizards/description/
#
# algorithms
# Hard (26.29%)
# Likes:    84
# Dislikes: 0
# Total Accepted:    3.7K
# Total Submissions: 14.1K
# Testcase Example:  '[1,3,1,2]'
#
# 作为国王的统治者，你有一支巫师军队听你指挥。
# 
# 给你一个下标从 0 开始的整数数组 strength ，其中 strength[i] 表示第 i
# 位巫师的力量值。对于连续的一组巫师（也就是这些巫师的力量值是 strength 的 子数组），总力量 定义为以下两个值的 乘积 ：
# 
# 
# 巫师中 最弱 的能力值。
# 组中所有巫师的个人力量值 之和 。
# 
# 
# 请你返回 所有 巫师组的 总 力量之和。由于答案可能很大，请将答案对 10^9 + 7 取余 后返回。
# 
# 子数组 是一个数组里 非空 连续子序列。
# 
# 
# 
# 示例 1：
# 
# 输入：strength = [1,3,1,2]
# 输出：44
# 解释：以下是所有连续巫师组：
# - [1,3,1,2] 中 [1] ，总力量值为 min([1]) * sum([1]) = 1 * 1 = 1
# - [1,3,1,2] 中 [3] ，总力量值为 min([3]) * sum([3]) = 3 * 3 = 9
# - [1,3,1,2] 中 [1] ，总力量值为 min([1]) * sum([1]) = 1 * 1 = 1
# - [1,3,1,2] 中 [2] ，总力量值为 min([2]) * sum([2]) = 2 * 2 = 4
# - [1,3,1,2] 中 [1,3] ，总力量值为 min([1,3]) * sum([1,3]) = 1 * 4 = 4
# - [1,3,1,2] 中 [3,1] ，总力量值为 min([3,1]) * sum([3,1]) = 1 * 4 = 4
# - [1,3,1,2] 中 [1,2] ，总力量值为 min([1,2]) * sum([1,2]) = 1 * 3 = 3
# - [1,3,1,2] 中 [1,3,1] ，总力量值为 min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5
# - [1,3,1,2] 中 [3,1,2] ，总力量值为 min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6
# - [1,3,1,2] 中 [1,3,1,2] ，总力量值为 min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7
# 所有力量值之和为 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44 。
# 
# 
# 示例 2：
# 
# 输入：strength = [5,4,6]
# 输出：213
# 解释：以下是所有连续巫师组：
# - [5,4,6] 中 [5] ，总力量值为 min([5]) * sum([5]) = 5 * 5 = 25
# - [5,4,6] 中 [4] ，总力量值为 min([4]) * sum([4]) = 4 * 4 = 16
# - [5,4,6] 中 [6] ，总力量值为 min([6]) * sum([6]) = 6 * 6 = 36
# - [5,4,6] 中 [5,4] ，总力量值为 min([5,4]) * sum([5,4]) = 4 * 9 = 36
# - [5,4,6] 中 [4,6] ，总力量值为 min([4,6]) * sum([4,6]) = 4 * 10 = 40
# - [5,4,6] 中 [5,4,6] ，总力量值为 min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60
# 所有力量值之和为 25 + 16 + 36 + 36 + 40 + 60 = 213 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= strength.length <= 10^5
# 1 <= strength[i] <= 10^9
# 
# 
#
from itertools import accumulate
from typing import List


# @lc code=start
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        # left[i] 为左侧严格小于 strength[i] 的最近元素位置（不存在时为 -1）
        # right[i] 为右侧小于等于 strength[i] 的最近元素位置（不存在时为 n）
        left, right, st = [-1] * n, [n] * n, []
        for i, v in enumerate(strength):
            while st and strength[st[-1]] >= v: right[st.pop()] = i
            if st: left[i] = st[-1]
            st.append(i)

        ss = list(accumulate(accumulate(strength, initial=0), initial=0))  # 前缀和的前缀和

        ans = 0
        for i, v in enumerate(strength):
            l, r = left[i] + 1, right[i] - 1  # [l, r]  左闭右闭
            tot = (i - l + 1) * (ss[r + 2] - ss[i + 1]) - (r - i + 1) * (ss[i + 1] - ss[l])
            ans += v * tot  # 累加贡献
        return ans % (10 ** 9 + 7)
# @lc code=end

