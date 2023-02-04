/*
 * @lc app=leetcode.cn id=850 lang=golang
 *
 * [850] 矩形面积 II
 *
 * https://leetcode.cn/problems/rectangle-area-ii/description/
 *
 * algorithms
 * Hard (48.50%)
 * Likes:    174
 * Dislikes: 0
 * Total Accepted:    9.1K
 * Total Submissions: 15.2K
 * Testcase Example:  '[[0,0,2,2],[1,0,2,3],[1,0,3,1]]'
 *
 * 我们给出了一个（轴对齐的）二维矩形列表 rectangles 。 对于 rectangle[i] = [x1, y1, x2,
 * y2]，其中（x1，y1）是矩形 i 左下角的坐标， (xi1, yi1) 是该矩形 左下角 的坐标， (xi2, yi2) 是该矩形 右上角
 * 的坐标。
 *
 * 计算平面中所有 rectangles 所覆盖的 总面积 。任何被两个或多个矩形覆盖的区域应只计算 一次 。
 *
 * 返回 总面积 。因为答案可能太大，返回 10^9 + 7 的 模 。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
 * 输出：6
 * 解释：如图所示，三个矩形覆盖了总面积为6的区域。
 * 从(1,1)到(2,2)，绿色矩形和红色矩形重叠。
 * 从(1,0)到(2,3)，三个矩形都重叠。
 *
 *
 * 示例 2：
 *
 *
 * 输入：rectangles = [[0,0,1000000000,1000000000]]
 * 输出：49
 * 解释：答案是 10^18 对 (10^9 + 7) 取模的结果， 即 49 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= rectangles.length <= 200
 * rectanges[i].length = 4
 * 0 <= xi1, yi1, xi2, yi2 <= 10^9
 * 矩形叠加覆盖后的总面积不会超越 2^63 - 1 ，这意味着可以用一个 64 位有符号整数来保存面积结果。
 *
 *
 */

// @lc code=start
const MOD = int64(1e9 + 7)

func rectangleArea(rectangles [][]int) int {
	list := []int{}
	for _, info := range rectangles {
		list = append(list, info[0])
		list = append(list, info[2])
	}
	sort.Ints(list)
	ans := int64(0)
	for i := 1; i < len(list); i++ {
		a, b, length := list[i-1], list[i], list[i]-list[i-1]
		if length == 0 {
			continue
		}
		lines := [][]int{}
		for _, info := range rectangles {
			if info[0] <= a && b <= info[2] {
				lines = append(lines, []int{info[1], info[3]})
			}
		}
		sort.Slice(lines, func(i, j int) bool {
			if lines[i][0] != lines[j][0] {
				return lines[i][0]-lines[j][0] < 0
			}
			return lines[i][1]-lines[j][1] < 0
		})
		total, l, r := int64(0), -1, -1
		for _, cur := range lines {
			if cur[0] > r {
				total += int64(r - l)
				l, r = cur[0], cur[1]
			} else if cur[1] > r {
				r = cur[1]
			}
		}
		total += int64(r - l)
		ans += total * int64(length)
		ans %= MOD
	}
	return int(ans)
}

// @lc code=end

