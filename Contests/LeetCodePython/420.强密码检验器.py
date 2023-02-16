#
# @lc app=leetcode.cn id=420 lang=python3
#
# [420] 强密码检验器
#
# https://leetcode.cn/problems/strong-password-checker/description/
#
# algorithms
# Hard (39.36%)
# Likes:    205
# Dislikes: 0
# Total Accepted:    18.1K
# Total Submissions: 46K
# Testcase Example:  '"a"'
#
# 满足以下条件的密码被认为是强密码：
# 
# 
# 由至少 6 个，至多 20 个字符组成。
# 包含至少 一个小写 字母，至少 一个大写 字母，和至少 一个数字 。
# 不包含连续三个重复字符 (比如 "Baaabb0" 是弱密码, 但是 "Baaba0" 是强密码)。
# 
# 
# 给你一个字符串 password ，返回 将 password 修改到满足强密码条件需要的最少修改步数。如果 password 已经是强密码，则返回 0
# 。
# 
# 在一步修改操作中，你可以：
# 
# 
# 插入一个字符到 password ，
# 从 password 中删除一个字符，或
# 用另一个字符来替换 password 中的某个字符。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：password = "a"
# 输出：5
# 
# 
# 示例 2：
# 
# 
# 输入：password = "aA1"
# 输出：3
# 
# 
# 示例 3：
# 
# 
# 输入：password = "1337C0d3"
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= password.length <= 50
# password 由字母、数字、点 '.' 或者感叹号 '!' 组成
# 
# 
#

# @lc code=start
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        hasLower = hasUpper = hasDigit = 1

        ans, cnt, rm2, same = 0, 0, 0, 1
        d = max(0, n - 20)

        for i, ch in enumerate(password):
            if i and password[i] == password[i - 1]:
                same += 1
            else:
                if d and same >= 3:
                    if same % 3 == 0:
                        cnt -= 1
                        d -= 1
                    elif same % 3 == 1:
                        rm2 += 1
                cnt += same // 3
                same = 1

            if ch.islower():
                hasLower = 0
            elif ch.isupper():
                hasUpper = 0
            elif ch.isdigit():
                hasDigit = 0
        
        if d and same >= 3:
            if same % 3 == 0:
                cnt -= 1
                d -= 1
            elif same % 3 == 1:
                rm2 += 1
        cnt += same // 3
        
        need = hasLower + hasUpper + hasDigit

        if n < 6:
            ans = max(6 - n, need)
        elif n <= 20:
            ans += max(cnt, need)
        else:
            # 使用 k % 3 = 1 的组的数量，由剩余的替换次数、组数和剩余的删除次数共同决定
            use2 = min(cnt, rm2, d // 2)
            cnt -= use2
            d -= use2 * 2
            # 由于每有一次替换次数就一定有 3 个连续相同的字符（k / 3 决定），因此这里可以直接计算出使用 k % 3 = 2 的组的数量
            use3 = min(cnt, d // 3)
            cnt -= use3
            d -= use3 * 3
            ans = (n - 20) + max(cnt, need)
        return ans
# @lc code=end

