#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#
# https://leetcode.cn/problems/scramble-string/description/
#
# algorithms
# Hard (47.56%)
# Likes:    506
# Dislikes: 0
# Total Accepted:    54.9K
# Total Submissions: 115.4K
# Testcase Example:  '"great"\n"rgeat"'
#
# 使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
# 
# 如果字符串的长度为 1 ，算法停止
# 如果字符串的长度 > 1 ，执行下述步骤：
# 
# 在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，且满足 s = x + y
# 。
# 随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，s 可能是 s = x + y 或者 s = y + x
# 。
# 在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。
# 
# 
# 
# 
# 给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。如果是，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s1 = "great", s2 = "rgeat"
# 输出：true
# 解释：s1 上可能发生的一种情形是：
# "great" --> "gr/eat" // 在一个随机下标处分割得到两个子字符串
# "gr/eat" --> "gr/eat" // 随机决定：「保持这两个子字符串的顺序不变」
# "gr/eat" --> "g/r / e/at" // 在子字符串上递归执行此算法。两个子字符串分别在随机下标处进行一轮分割
# "g/r / e/at" --> "r/g / e/at" // 随机决定：第一组「交换两个子字符串」，第二组「保持这两个子字符串的顺序不变」
# "r/g / e/at" --> "r/g / e/ a/t" // 继续递归执行此算法，将 "at" 分割得到 "a/t"
# "r/g / e/ a/t" --> "r/g / e/ a/t" // 随机决定：「保持这两个子字符串的顺序不变」
# 算法终止，结果字符串和 s2 相同，都是 "rgeat"
# 这是一种能够扰乱 s1 得到 s2 的情形，可以认为 s2 是 s1 的扰乱字符串，返回 true
# 
# 
# 示例 2：
# 
# 
# 输入：s1 = "abcde", s2 = "caebd"
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：s1 = "a", s2 = "a"
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# s1.length == s2.length
# 1 
# s1 和 s2 由小写英文字母组成
# 
# 
#
from collections import Counter
from functools import cache


# @lc code=start
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        n = len(s1)
        dp = [[[0] * (n + 1) for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    for k in range(1, length):
                        dp[i][j][length] = dp[i][j][length] or (dp[i][j][k] and dp[i+k][j+k][length-k]) or (dp[i][j+length-k][k] and dp[i+k][j][length-k])
        
        return dp[0][0][n]
        '''
        @cache
        def dfs(i: int, j: int, length: int) -> bool:
            if s1[i:i+length] == s2[j:j+length]:
                return True
            
            if Counter(s1[i:i+length]) != Counter(s2[j:j+length]):
                return False

            for k in range(1, length):
                if dfs(i, j, k) and dfs(i + k, j + k, length - k):
                    return True

                if dfs(i, j + length - k, k) and dfs(i + k, j, length - k):
                    return True

            return False
        
        return dfs(0, 0, len(s1))
        '''
# @lc code=end

