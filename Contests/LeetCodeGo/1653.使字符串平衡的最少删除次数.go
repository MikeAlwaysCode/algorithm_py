/*
 * @lc app=leetcode.cn id=1653 lang=golang
 *
 * [1653] 使字符串平衡的最少删除次数
 *
 * https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced/description/
 *
 * algorithms
 * Medium (54.75%)
 * Likes:    43
 * Dislikes: 0
 * Total Accepted:    6.6K
 * Total Submissions: 12K
 * Testcase Example:  '"aababbab"'
 *
 * 给你一个字符串 s ，它仅包含字符 'a' 和 'b'​​​​ 。
 *
 * 你可以删除 s 中任意数目的字符，使得 s 平衡 。我们称 s 平衡的 当不存在下标对 (i,j) 满足 i < j 且 s[i] = 'b' 同时
 * s[j]= 'a' 。
 *
 * 请你返回使 s 平衡 的 最少 删除次数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "aababbab"
 * 输出：2
 * 解释：你可以选择以下任意一种方案：
 * 下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
 * 下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "bbaaaaabb"
 * 输出：2
 * 解释：唯一的最优解是删除最前面两个字符。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * s[i] 要么是 'a' 要么是 'b'​ 。​
 *
 *
 */

// @lc code=start
func minimumDeletions(s string) int {
	cnta, cntb := strings.Count(s, "a"), 0
	ans := cnta
	for _, c := range s {
		if c == 'a' {
			cnta--
		} else {
			cntb++
		}
		ans = min(ans, cnta+cntb)
	}
	return ans
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @lc code=end

