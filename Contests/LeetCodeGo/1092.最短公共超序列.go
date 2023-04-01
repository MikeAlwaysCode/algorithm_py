/*
 * @lc app=leetcode.cn id=1092 lang=golang
 *
 * [1092] 最短公共超序列
 *
 * https://leetcode.cn/problems/shortest-common-supersequence/description/
 *
 * algorithms
 * Hard (54.26%)
 * Likes:    143
 * Dislikes: 0
 * Total Accepted:    7.2K
 * Total Submissions: 12.6K
 * Testcase Example:  '"abac"\n"cab"'
 *
 * 给出两个字符串 str1 和 str2，返回同时以 str1 和 str2
 * 作为子序列的最短字符串。如果答案不止一个，则可以返回满足条件的任意一个答案。
 *
 * （如果从字符串 T 中删除一些字符（也可能不删除，并且选出的这些字符可以位于 T 中的 任意位置），可以得到字符串 S，那么 S 就是 T
 * 的子序列）
 *
 *
 *
 * 示例：
 *
 * 输入：str1 = "abac", str2 = "cab"
 * 输出："cabac"
 * 解释：
 * str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。
 * str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。
 * 最终我们给出的答案是满足上述属性的最短字符串。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= str1.length, str2.length <= 1000
 * str1 和 str2 都由小写英文字母组成。
 *
 *
 */

// @lc code=start
func shortestCommonSupersequence(s string, t string) string {
	n, m := len(s), len(t)
	// f[i+1][j+1] 表示 s 的前 i 个字母和 t 的前 j 个字母的最短公共超序列的长度
	f := make([][]int, n+1)
	for i := range f {
		f[i] = make([]int, m+1)
	}
	for j := 1; j < m; j++ {
		f[0][j] = j // 递归边界
	}
	for i := 1; i < n; i++ {
		f[i][0] = i // 递归边界
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if s[i] == t[j] { // 最短公共超序列一定包含 s[i]
				f[i+1][j+1] = f[i][j] + 1
			} else { // 取更短的组成答案
				f[i+1][j+1] = min(f[i][j+1], f[i+1][j]) + 1
			}
		}
	}

	ans := []byte{}
	i, j := n-1, m-1
	for i >= 0 && j >= 0 {
		if s[i] == t[j] { // 公共超序列一定包含 s[i]
			ans = append(ans, s[i])
			i--
			j-- // 相当于继续递归 makeAns(i - 1, j - 1)
		} else if f[i+1][j+1] == f[i][j+1]+1 {
			ans = append(ans, s[i])
			i-- // 相当于继续递归 makeAns(i - 1, j)
		} else {
			ans = append(ans, t[j])
			j-- // 相当于继续递归 makeAns(i, j - 1)
		}
	}
	for i, n := 0, len(ans); i < n/2; i++ {
		ans[i], ans[n-1-i] = ans[n-1-i], ans[i]
	}
	// 补上前面的递归边界
	return s[:i+1] + t[:j+1] + string(ans)
}

func min(a, b int) int {
	if b < a {
		return b
	}
	return a
}

// @lc code=end

