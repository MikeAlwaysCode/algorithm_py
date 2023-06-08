#
# @lc app=leetcode.cn id=2611 lang=python3
#
# [2611] 老鼠和奶酪
#
# https://leetcode.cn/problems/mice-and-cheese/description/
#
# algorithms
# Medium (47.98%)
# Likes:    26
# Dislikes: 0
# Total Accepted:    9.9K
# Total Submissions: 18.3K
# Testcase Example:  '[1,1,3,4]\n[4,4,1,1]\n2'
#
# 有两只老鼠和 n 块不同类型的奶酪，每块奶酪都只能被其中一只老鼠吃掉。
# 
# 下标为 i 处的奶酪被吃掉的得分为：
# 
# 
# 如果第一只老鼠吃掉，则得分为 reward1[i] 。
# 如果第二只老鼠吃掉，则得分为 reward2[i] 。
# 
# 
# 给你一个正整数数组 reward1 ，一个正整数数组 reward2 ，和一个非负整数 k 。
# 
# 请你返回第一只老鼠恰好吃掉 k 块奶酪的情况下，最大 得分为多少。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2
# 输出：15
# 解释：这个例子中，第一只老鼠吃掉第 2 和 3 块奶酪（下标从 0 开始），第二只老鼠吃掉第 0 和 1 块奶酪。
# 总得分为 4 + 4 + 3 + 4 = 15 。
# 15 是最高得分。
# 
# 
# 示例 2：
# 
# 
# 输入：reward1 = [1,1], reward2 = [1,1], k = 2
# 输出：2
# 解释：这个例子中，第一只老鼠吃掉第 0 和 1 块奶酪（下标从 0 开始），第二只老鼠不吃任何奶酪。
# 总得分为 1 + 1 = 2 。
# 2 是最高得分。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n == reward1.length == reward2.length <= 10^5
# 1 <= reward1[i], reward2[i] <= 1000
# 0 <= k <= n
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        idx = list(range(n))
        idx.sort(key = lambda x: reward1[x] - reward2[x], reverse = True)
        ans = 0
        for i in range(n):
            if k:
                ans += reward1[idx[i]]
                k -= 1
            else:
                ans += reward2[idx[i]]
        return ans
# @lc code=end

