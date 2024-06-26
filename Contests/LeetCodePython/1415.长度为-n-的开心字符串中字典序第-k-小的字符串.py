#
# @lc app=leetcode.cn id=1415 lang=python3
#
# [1415] 长度为 n 的开心字符串中字典序第 k 小的字符串
#
# https://leetcode.cn/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/
#
# algorithms
# Medium (68.61%)
# Likes:    40
# Dislikes: 0
# Total Accepted:    9K
# Total Submissions: 13.1K
# Testcase Example:  '1\n3'
#
# 一个 「开心字符串」定义为：
# 
# 
# 仅包含小写字母 ['a', 'b', 'c'].
# 对所有在 1 到 s.length - 1 之间的 i ，满足 s[i] != s[i + 1] （字符串的下标从 1 开始）。
# 
# 
# 比方说，字符串 "abc"，"ac"，"b" 和 "abcbabcbcb" 都是开心字符串，但是 "aa"，"baa" 和 "ababbc"
# 都不是开心字符串。
# 
# 给你两个整数 n 和 k ，你需要将长度为 n 的所有开心字符串按字典序排序。
# 
# 请你返回排序后的第 k 个开心字符串，如果长度为 n 的开心字符串少于 k 个，那么请你返回 空字符串 。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 1, k = 3
# 输出："c"
# 解释：列表 ["a", "b", "c"] 包含了所有长度为 1 的开心字符串。按照字典序排序后第三个字符串为 "c" 。
# 
# 
# 示例 2：
# 
# 输入：n = 1, k = 4
# 输出：""
# 解释：长度为 1 的开心字符串只有 3 个。
# 
# 
# 示例 3：
# 
# 输入：n = 3, k = 9
# 输出："cab"
# 解释：长度为 3 的开心字符串总共有 12 个 ["aba", "abc", "aca", "acb", "bab", "bac", "bca",
# "bcb", "cab", "cac", "cba", "cbc"] 。第 9 个字符串为 "cab"
# 
# 
# 示例 4：
# 
# 输入：n = 2, k = 7
# 输出：""
# 
# 
# 示例 5：
# 
# 输入：n = 10, k = 100
# 输出："abacbabacb"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10
# 1 <= k <= 100
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        m = 1 << (n - 1)
        if 3 * m < k: return ""

        s = ["a", "b", "c"]

        ans = [""] * n
        ans[0] = s[(k - 1) // m]
        k = (k - 1) % m + 1
        for i in range(1, n):
            m >>= 1
            j = 0
            while s[j] == ans[i - 1] or k > m:
                if k > m and s[j] != ans[i - 1]:
                    k -= m
                j += 1
            ans[i] = s[j]
        return "".join(ans)
# @lc code=end
def main():
    sol = Solution()
    n = 7
    k = 64
    print(sol.getHappyString(n, k))

if __name__ == '__main__':
    main()

