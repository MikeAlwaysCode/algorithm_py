/*
 * @lc app=leetcode.cn id=32 lang=golang
 *
 * [32] 最长有效括号
 *
 * https://leetcode.cn/problems/longest-valid-parentheses/description/
 *
 * algorithms
 * Hard (37.10%)
 * Likes:    2157
 * Dislikes: 0
 * Total Accepted:    347.5K
 * Total Submissions: 936.7K
 * Testcase Example:  '"(()"'
 *
 * 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "(()"
 * 输出：2
 * 解释：最长有效括号子串是 "()"
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = ")()())"
 * 输出：4
 * 解释：最长有效括号子串是 "()()"
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = ""
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0
 * s[i] 为 '(' 或 ')'
 *
 *
 *
 *
 */

// @lc code=start
func longestValidParentheses(s string) int {
	left, right, maxLength := 0, 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			left++
		} else {
			right++
		}
		if left == right {
			maxLength = max(maxLength, 2*right)
		} else if right > left {
			left, right = 0, 0
		}
	}
	left, right = 0, 0
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == '(' {
			left++
		} else {
			right++
		}
		if left == right {
			maxLength = max(maxLength, 2*left)
		} else if left > right {
			left, right = 0, 0
		}
	}
	return maxLength
	// Stack
	// maxAns := 0
	// stack := []int{}
	// stack = append(stack, -1)
	// for i := 0; i < len(s); i++ {
	// 	if s[i] == '(' {
	// 		stack = append(stack, i)
	// 	} else {
	// 		stack = stack[:len(stack)-1]
	// 		if len(stack) == 0 {
	// 			stack = append(stack, i)
	// 		} else {
	// 			maxAns = max(maxAns, i-stack[len(stack)-1])
	// 		}
	// 	}
	// }
	// return maxAns
	// DP
	// maxAns := 0
	// dp := make([]int, len(s))
	// for i := 1; i < len(s); i++ {
	// 	if s[i] == ')' {
	// 		if s[i-1] == '(' {
	// 			if i >= 2 {
	// 				dp[i] = dp[i-2] + 2
	// 			} else {
	// 				dp[i] = 2
	// 			}
	// 		} else if i-dp[i-1] > 0 && s[i-dp[i-1]-1] == '(' {
	// 			if i-dp[i-1] >= 2 {
	// 				dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
	// 			} else {
	// 				dp[i] = dp[i-1] + 2
	// 			}
	// 		}
	// 		maxAns = max(maxAns, dp[i])
	// 	}
	// }
	// return maxAns
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// @lc code=end

