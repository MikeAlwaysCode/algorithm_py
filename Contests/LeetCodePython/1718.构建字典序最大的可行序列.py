#
# @lc app=leetcode.cn id=1718 lang=python3
#
# [1718] 构建字典序最大的可行序列
#
# https://leetcode.cn/problems/construct-the-lexicographically-largest-valid-sequence/description/
#
# algorithms
# Medium (50.63%)
# Likes:    42
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 6.6K
# Testcase Example:  '3'
#
# 给你一个整数 n ，请你找到满足下面条件的一个序列：
# 
# 
# 整数 1 在序列中只出现一次。
# 2 到 n 之间每个整数都恰好出现两次。
# 对于每个 2 到 n 之间的整数 i ，两个 i 之间出现的距离恰好为 i 。
# 
# 
# 序列里面两个数 a[i] 和 a[j] 之间的 距离 ，我们定义为它们下标绝对值之差 |j - i| 。
# 
# 请你返回满足上述条件中 字典序最大 的序列。题目保证在给定限制条件下，一定存在解。
# 
# 一个序列 a 被认为比序列 b （两者长度相同）字典序更大的条件是： a 和 b 中第一个不一样的数字处，a 序列的数字比 b
# 序列的数字大。比方说，[0,1,9,0] 比 [0,1,5,6] 字典序更大，因为第一个不同的位置是第三个数字，且 9 比 5 大。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 3
# 输出：[3,1,2,3,2]
# 解释：[2,3,2,1,3] 也是一个可行的序列，但是 [3,1,2,3,2] 是字典序最大的序列。
# 
# 
# 示例 2：
# 
# 输入：n = 5
# 输出：[5,3,1,4,3,5,2,4,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 20
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (n * 2 - 1)
        seen = [False] * (n + 1)

        def dfs(x: int) -> bool:
            if x == n * 2 - 1:
                return True
            if ans[x]: return dfs(x + 1)
            for y in range(n, 0, -1):
                if seen[y]: continue
                nxt = x if y == 1 else x + y
                if nxt >= n * 2 - 1 or ans[nxt]: continue
                seen[y] = True
                ans[x] = ans[nxt] = y
                if dfs(x + 1): return True
                seen[y] = False
                ans[x] = ans[nxt] = 0
            return False
        
        dfs(0)
        return ans
# @lc code=end

