#
# @lc app=leetcode.cn id=481 lang=python3
#
# [481] 神奇字符串
#
# https://leetcode.cn/problems/magical-string/description/
#
# algorithms
# Medium (57.62%)
# Likes:    90
# Dislikes: 0
# Total Accepted:    11.8K
# Total Submissions: 19.4K
# Testcase Example:  '6'
#
# 神奇字符串 s 仅由 '1' 和 '2' 组成，并需要遵守下面的规则：
# 
# 
# 神奇字符串 s 的神奇之处在于，串联字符串中 '1' 和 '2' 的连续出现次数可以生成该字符串。
# 
# 
# s 的前几个元素是 s = "1221121221221121122……" 。如果将 s 中连续的若干 1 和 2 进行分组，可以得到 "1 22 11
# 2 1 22 1 22 11 2 11 22 ......" 。每组中 1 或者 2 的出现次数分别是 "1 2 2 1 1 2 1 2 2 1 2 2
# ......" 。上面的出现次数正是 s 自身。
# 
# 给你一个整数 n ，返回在神奇字符串 s 的前 n 个数字中 1 的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 6
# 输出：3
# 解释：神奇字符串 s 的前 6 个元素是 “122112”，它包含三个 1，因此返回 3 。 
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def magicalString(self, n: int) -> int:
        if n < 4:
            return 1
        '''
        s = [0] * n
        s[:3] = [1, 2, 2]
        i, j = 2, 3
        ans = 1
        while j < n:
            l = min(s[i], n - j)
            if s[j-1] == 2:
                ans += l
            # s += [s[-1] ^ 3] * l
            s[j:j+l] = [s[j-1] ^ 3] * l
            j += l
            i += 1
        return ans
        '''
        '''
        s = [''] * n
        s[:3] = "122"
        res = 1
        i, j = 2, 3
        while j < n:
            size = int(s[i])
            num = 3 - int(s[j - 1])
            while size and j < n:
                s[j] = str(num)
                if num == 1:
                    res += 1
                j += 1
                size -= 1
            i += 1
        return res
        '''
        s = [1, 2, 2]
        i = 2
        while len(s) < n:
            s += [s[-1] ^ 3] * s[i]  # 1^3=2, 2^3=1，这样就能在 1 和 2 之间转换
            i += 1
        return s[:n].count(1)
# @lc code=end

