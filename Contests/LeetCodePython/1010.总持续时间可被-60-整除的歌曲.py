#
# @lc app=leetcode.cn id=1010 lang=python3
#
# [1010] 总持续时间可被 60 整除的歌曲
#
# https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
#
# algorithms
# Medium (46.21%)
# Likes:    228
# Dislikes: 0
# Total Accepted:    27.2K
# Total Submissions: 56.8K
# Testcase Example:  '[30,20,150,100,40]'
#
# 在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
# 
# 返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望下标数字 i 和 j 满足  i < j 且有 (time[i] +
# time[j]) % 60 == 0。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：time = [30,20,150,100,40]
# 输出：3
# 解释：这三对的总持续时间可被 60 整除：
# (time[0] = 30, time[2] = 150): 总持续时间 180
# (time[1] = 20, time[3] = 100): 总持续时间 120
# (time[1] = 20, time[4] = 40): 总持续时间 60
# 
# 
# 示例 2：
# 
# 
# 输入：time = [60,60,60]
# 输出：3
# 解释：所有三对的总持续时间都是 120，可以被 60 整除。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= time.length <= 6 * 10^4
# 1 <= time[i] <= 500
# 
# 
#
from collections import Counter
from typing import List

# @lc code=start
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        cnt = Counter()
        for t in time:
            ans += cnt[(-t) % 60]
            cnt[t%60] += 1
        return ans
# @lc code=end

