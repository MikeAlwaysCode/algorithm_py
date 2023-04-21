/*
 * @lc app=leetcode.cn id=2002 lang=golang
 *
 * [2002] 两个回文子序列长度的最大乘积
 *
 * https://leetcode.cn/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/description/
 *
 * algorithms
 * Medium (60.17%)
 * Likes:    47
 * Dislikes: 0
 * Total Accepted:    5.7K
 * Total Submissions: 9.4K
 * Testcase Example:  '"leetcodecom"'
 *
 * 给你一个字符串 s ，请你找到 s 中两个 不相交回文子序列 ，使得它们长度的 乘积最大 。两个子序列在原字符串中如果没有任何相同下标的字符，则它们是
 * 不相交 的。
 *
 * 请你返回两个回文子序列长度可以达到的 最大乘积 。
 *
 * 子序列
 * 指的是从原字符串中删除若干个字符（可以一个也不删除）后，剩余字符不改变顺序而得到的结果。如果一个字符串从前往后读和从后往前读一模一样，那么这个字符串是一个
 * 回文字符串 。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：s = "leetcodecom"
 * 输出：9
 * 解释：最优方案是选择 "ete" 作为第一个子序列，"cdc" 作为第二个子序列。
 * 它们的乘积为 3 * 3 = 9 。
 *
 *
 * 示例 2：
 *
 * 输入：s = "bb"
 * 输出：1
 * 解释：最优方案为选择 "b" （第一个字符）作为第一个子序列，"b" （第二个字符）作为第二个子序列。
 * 它们的乘积为 1 * 1 = 1 。
 *
 *
 * 示例 3：
 *
 * 输入：s = "accbcaxxcxx"
 * 输出：25
 * 解释：最优方案为选择 "accca" 作为第一个子序列，"xxcxx" 作为第二个子序列。
 * 它们的乘积为 5 * 5 = 25 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= s.length <= 12
 * s 只含有小写英文字母。
 *
 *
 */

// @lc code=start
func maxProduct(s string) (ans int) {
	var a, b []byte
	var f func(int)
	f = func(i int) {
		if i == len(s) {
			if len(a)*len(b) > ans && isPalindromic(a) && isPalindromic(b) {
				ans = len(a) * len(b)
			}
			return
		}

		// 不选
		f(i + 1)

		// 放入 a
		a = append(a, s[i])
		f(i + 1)
		a = a[:len(a)-1]

		// 放入 b
		b = append(b, s[i])
		f(i + 1)
		b = b[:len(b)-1]
	}
	f(0)
	return
}

func isPalindromic(a []byte) bool {
	for i, n := 0, len(a); i < n/2; i++ {
		if a[i] != a[n-1-i] {
			return false
		}
	}
	return true
}

// @lc code=end

