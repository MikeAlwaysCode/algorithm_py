/*
 * @lc app=leetcode.cn id=2278 lang=golang
 *
 * [2278] 字母在字符串中的百分比
 *
 * https://leetcode.cn/problems/percentage-of-letter-in-string/description/
 *
 * algorithms
 * Easy (81.18%)
 * Likes:    11
 * Dislikes: 0
 * Total Accepted:    13.3K
 * Total Submissions: 16.4K
 * Testcase Example:  '"foobar"\n"o"'
 *
 * 给你一个字符串 s 和一个字符 letter ，返回在 s 中等于 letter 字符所占的 百分比 ，向下取整到最接近的百分比。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "foobar", letter = "o"
 * 输出：33
 * 解释：
 * 等于字母 'o' 的字符在 s 中占到的百分比是 2 / 6 * 100% = 33% ，向下取整，所以返回 33 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "jjjj", letter = "k"
 * 输出：0
 * 解释：
 * 等于字母 'k' 的字符在 s 中占到的百分比是 0% ，所以返回 0 。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 100
 * s 由小写英文字母组成
 * letter 是一个小写英文字母
 *
 *
 */

// @lc code=start
func percentageLetter(s string, letter byte) int {
	n := len(s)
	cnt := 0
	for i := 0; i < n; i++ {
		if s[i] == letter {
			cnt++
		}
	}
	return int(cnt * 100 / n)
}

// @lc code=end

