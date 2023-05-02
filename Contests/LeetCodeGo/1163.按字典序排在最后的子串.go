/*
 * @lc app=leetcode.cn id=1163 lang=golang
 *
 * [1163] 按字典序排在最后的子串
 *
 * https://leetcode.cn/problems/last-substring-in-lexicographical-order/description/
 *
 * algorithms
 * Hard (27.79%)
 * Likes:    142
 * Dislikes: 0
 * Total Accepted:    16.2K
 * Total Submissions: 49.1K
 * Testcase Example:  '"abab"'
 *
 * 给你一个字符串 s ，找出它的所有子串并按字典序排列，返回排在最后的那个子串。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "abab"
 * 输出："bab"
 * 解释：我们可以找出 7 个子串 ["a", "ab", "aba", "abab", "b", "ba", "bab"]。按字典序排在最后的子串是
 * "bab"。
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "leetcode"
 * 输出："tcode"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 4 * 10^5
 * s 仅含有小写英文字符。
 *
 *
 */

// @lc code=start
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func lastSubstring(s string) string {
	i, j, n := 0, 1, len(s)
	for j < n {
		k := 0
		for j+k < n && s[i+k] == s[j+k] {
			k++
		}
		if j+k < n && s[i+k] < s[j+k] {
			i, j = j, max(j+1, i+k+1)
		} else {
			j = j + k + 1
		}
	}
	return s[i:]
}

// @lc code=end

