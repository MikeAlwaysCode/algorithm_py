#
# @lc app=leetcode.cn id=1147 lang=python3
#
# [1147] 段式回文
#
# https://leetcode.cn/problems/longest-chunked-palindrome-decomposition/description/
#
# algorithms
# Hard (56.61%)
# Likes:    74
# Dislikes: 0
# Total Accepted:    9.1K
# Total Submissions: 15.7K
# Testcase Example:  '"ghiabcdefhelloadamhelloabcdefghi"'
#
# 你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足:
# 
# 
# subtexti 是 非空 字符串
# 所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text )
# 对于所有 i 的有效值( 即 1 <= i <= k ) ，subtexti == subtextk - i + 1 均成立
# 
# 
# 返回k可能最大值。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：text = "ghiabcdefhelloadamhelloabcdefghi"
# 输出：7
# 解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。
# 
# 
# 示例 2：
# 
# 
# 输入：text = "merchant"
# 输出：1
# 解释：我们可以把字符串拆分成 "(merchant)"。
# 
# 
# 示例 3：
# 
# 
# 输入：text = "antaprezatepzapreanta"
# 输出：11
# 解释：我们可以把字符串拆分成 "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)"。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= text.length <= 1000
# text 仅由小写英文字符组成
# 
# 
#

# @lc code=start
class Solution:
    def longestDecomposition(self, text: str) -> int:
        def get(l, r):
            return (h[r] - h[l - 1] * p[r - l + 1]) % mod

        n = len(text)
        base = 131
        mod = int(1e9) + 7
        h = [0] * (n + 10)
        p = [1] * (n + 10)
        for i, c in enumerate(text):
            t = ord(c) - ord('a') + 1
            h[i + 1] = (h[i] * base) % mod + t
            p[i + 1] = (p[i] * base) % mod


        ans = 0
        i, j = 0, n - 1
        while i <= j:
            k = 1
            ok = False
            while i + k - 1 < j - k + 1:
                if get(i + 1, i + k) == get(j - k + 2, j + 1):
                    ans += 2
                    i += k
                    j -= k
                    ok = True
                    break
                k += 1
            if not ok:
                ans += 1
                break
        return ans
        '''
        ans = 0
        n = len(text)
        left, right = 0, n
        while left < right:
            i, j = left + 1, right - 1
            while i <= j and text[left:i] != text[j:right]:
                i += 1
                j -= 1
            ans += 1 if i > j else 2
            left, right = i, j
        return ans
        '''
# @lc code=end

