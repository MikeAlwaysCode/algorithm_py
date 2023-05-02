/*
 * @lc app=leetcode.cn id=1595 lang=golang
 *
 * [1595] 连通两组点的最小成本
 *
 * https://leetcode.cn/problems/minimum-cost-to-connect-two-groups-of-points/description/
 *
 * algorithms
 * Hard (50.02%)
 * Likes:    66
 * Dislikes: 0
 * Total Accepted:    3K
 * Total Submissions: 5.9K
 * Testcase Example:  '[[15,96],[36,2]]'
 *
 * 给你两组点，其中第一组中有 size1 个点，第二组中有 size2 个点，且 size1 >= size2 。
 * 
 * 任意两点间的连接成本 cost 由大小为 size1 x size2 矩阵给出，其中 cost[i][j] 是第一组中的点 i 和第二组中的点 j
 * 的连接成本。如果两个组中的每个点都与另一组中的一个或多个点连接，则称这两组点是连通的。换言之，第一组中的每个点必须至少与第二组中的一个点连接，且第二组中的每个点必须至少与第一组中的一个点连接。
 * 
 * 返回连通两组点所需的最小成本。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入：cost = [[15, 96], [36, 2]]
 * 输出：17
 * 解释：连通两组点的最佳方法是：
 * 1--A
 * 2--B
 * 总成本为 17 。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 输入：cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
 * 输出：4
 * 解释：连通两组点的最佳方法是：
 * 1--A
 * 2--B
 * 2--C
 * 3--A
 * 最小成本为 4 。
 * 请注意，虽然有多个点连接到第一组中的点 2 和第二组中的点 A ，但由于题目并不限制连接点的数目，所以只需要关心最低总成本。
 * 
 * 示例 3：
 * 
 * 输入：cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
 * 输出：10
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * size1 == cost.length
 * size2 == cost[i].length
 * 1 <= size1, size2 <= 12
 * size1 >= size2
 * 0 <= cost[i][j] <= 100
 * 
 * 
 */

// @lc code=start
func connectTwoGroups(cost [][]int) int {

}
// @lc code=end

