/*
 * @lc app=leetcode.cn id=1616 lang=golang
 *
 * [1616] 分割两个字符串得到回文串
 *
 * https://leetcode.cn/problems/split-two-strings-to-make-palindrome/description/
 *
 * algorithms
 * Medium (28.47%)
 * Likes:    122
 * Dislikes: 0
 * Total Accepted:    17.9K
 * Total Submissions: 50.6K
 * Testcase Example:  '"x"\n"y"'
 *
 * 给你两个字符串 a 和 b ，它们长度相同。请你选择一个下标，将两个字符串都在 相同的下标 分割开。由 a 可以得到两个字符串： aprefix 和
 * asuffix ，满足 a = aprefix + asuffix ，同理，由 b 可以得到两个字符串 bprefix 和 bsuffix ，满足 b
 * = bprefix + bsuffix 。请你判断 aprefix + bsuffix 或者 bprefix + asuffix 能否构成回文串。
 *
 * 当你将一个字符串 s 分割成 sprefix 和 ssuffix 时， ssuffix 或者 sprefix 可以为空。比方说， s = "abc"
 * 那么 "" + "abc" ， "a" + "bc" ， "ab" + "c" 和 "abc" + "" 都是合法分割。
 *
 * 如果 能构成回文字符串 ，那么请返回 true，否则返回 false 。
 *
 * 注意， x + y 表示连接字符串 x 和 y 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：a = "x", b = "y"
 * 输出：true
 * 解释：如果 a 或者 b 是回文串，那么答案一定为 true ，因为你可以如下分割：
 * aprefix = "", asuffix = "x"
 * bprefix = "", bsuffix = "y"
 * 那么 aprefix + bsuffix = "" + "y" = "y" 是回文串。
 *
 *
 * 示例 2：
 *
 *
 * 输入：a = "abdef", b = "fecab"
 * 输出：true
 *
 *
 * 示例 3：
 *
 *
 * 输入：a = "ulacfd", b = "jizalu"
 * 输出：true
 * 解释：在下标为 3 处分割：
 * aprefix = "ula", asuffix = "cfd"
 * bprefix = "jiz", bsuffix = "alu"
 * 那么 aprefix + bsuffix = "ula" + "alu" = "ulaalu" 是回文串。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= a.length, b.length <= 10^5
 * a.length == b.length
 * a 和 b 都只包含小写英文字母
 *
 *
 */

// @lc code=start
// 如果从 s[i] 到 s[j] 是回文串则返回 true，否则返回 false
func isPalindrome(s string, i, j int) bool {
	for i < j && s[i] == s[j] {
		i++
		j--
	}
	return i >= j
}

// 如果 a_prefix + b_suffix 可以构成回文串则返回 true，否则返回 false
func check(a, b string) bool {
	i, j := 0, len(a)-1         // 相向双指针
	for i < j && a[i] == b[j] { // 前后缀尽量匹配
		i++
		j--
	}
	return isPalindrome(a, i, j) || isPalindrome(b, i, j)
}

func checkPalindromeFormation(a, b string) bool {
	return check(a, b) || check(b, a)
}

// @lc code=end

