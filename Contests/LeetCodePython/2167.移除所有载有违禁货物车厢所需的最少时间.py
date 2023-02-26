#
# @lc app=leetcode.cn id=2167 lang=python3
#
# [2167] 移除所有载有违禁货物车厢所需的最少时间
#
# https://leetcode.cn/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/description/
#
# algorithms
# Hard (48.71%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    4.4K
# Total Submissions: 9K
# Testcase Example:  '"1100101"'
#
# 给你一个下标从 0 开始的二进制字符串 s ，表示一个列车车厢序列。s[i] = '0' 表示第 i 节车厢 不 含违禁货物，而 s[i] = '1'
# 表示第 i 节车厢含违禁货物。
# 
# 作为列车长，你需要清理掉所有载有违禁货物的车厢。你可以不限次数执行下述三种操作中的任意一个：
# 
# 
# 从列车 左 端移除一节车厢（即移除 s[0]），用去 1 单位时间。
# 从列车 右 端移除一节车厢（即移除 s[s.length - 1]），用去 1 单位时间。
# 从列车车厢序列的 任意位置 移除一节车厢，用去 2 单位时间。
# 
# 
# 返回移除所有载有违禁货物车厢所需要的 最少 单位时间数。
# 
# 注意，空的列车车厢序列视为没有车厢含违禁货物。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "1100101"
# 输出：5
# 解释：
# 一种从序列中移除所有载有违禁货物的车厢的方法是：
# - 从左端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
# - 从右端移除一节车厢 1 次。所用时间是 1 。
# - 移除序列中间位置载有违禁货物的车厢。所用时间是 2 。
# 总时间是 2 + 1 + 2 = 5 。
# 
# 一种替代方法是：
# - 从左端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
# - 从右端移除一节车厢 3 次。所用时间是 3 * 1 = 3 。
# 总时间也是 2 + 3 = 5 。
# 
# 5 是移除所有载有违禁货物的车厢所需要的最少单位时间数。
# 没有其他方法能够用更少的时间移除这些车厢。
# 
# 示例 2：
# 
# 
# 输入：s = "0010"
# 输出：2
# 解释：
# 一种从序列中移除所有载有违禁货物的车厢的方法是：
# - 从左端移除一节车厢 3 次。所用时间是 3 * 1 = 3 。
# 总时间是 3.
# 
# 另一种从序列中移除所有载有违禁货物的车厢的方法是：
# - 移除序列中间位置载有违禁货物的车厢。所用时间是 2 。
# 总时间是 2.
# 
# 另一种从序列中移除所有载有违禁货物的车厢的方法是：
# - 从右端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
# 总时间是 2.
# 
# 2 是移除所有载有违禁货物的车厢所需要的最少单位时间数。
# 没有其他方法能够用更少的时间移除这些车厢。
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 2 * 10^5
# s[i] 为 '0' 或 '1'
# 
# 
#

# @lc code=start
class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        ans, preb, pres = 1, 0, 0

        for i, c in enumerate(s):
            preb = min(preb, i - 2 * pres)
            pres += int(c)
            ans = min(ans, preb + 2 * pres - i)
        return ans + n - 1

        '''
        ans, pre = n, 0
        suff = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff[i] = suff[i + 1]
            if s[i] == "1":
                suff[i] = min(suff[i] + 2, n - i)

        for i, c in enumerate(s):
            if c == "1":
                pre = min(pre + 2, i + 1, pre + n - i)
            ans = min(ans, pre + suff[i + 1])
        return ans
        '''
# @lc code=end

