#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#
# https://leetcode.cn/problems/flood-fill/description/
#
# algorithms
# Easy (58.32%)
# Likes:    384
# Dislikes: 0
# Total Accepted:    136.6K
# Total Submissions: 234.2K
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# 有一幅以 m x n 的二维整数数组表示的图画 image ，其中 image[i][j] 表示该图画的像素值大小。
# 
# 你也被给予三个整数 sr ,  sc 和 newColor 。你应该从像素 image[sr][sc] 开始对图像进行 上色填充 。
# 
# 为了完成 上色工作 ，从初始像素开始，记录初始坐标的 上下左右四个方向上
# 像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应 四个方向上
# 像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为 newColor 。
# 
# 最后返回 经过上色渲染后的图像 。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入: image = [[1,1,1],[1,1,0],[1,0,1]]，sr = 1, sc = 1, newColor = 2
# 输出: [[2,2,2],[2,2,0],[2,0,1]]
# 解析: 在图像的正中间，(坐标(sr,sc)=(1,1)),在路径上所有符合条件的像素点的颜色都被更改成2。
# 注意，右下角的像素没有更改为2，因为它不是在上下左右四个方向上与初始点相连的像素点。
# 
# 
# 示例 2:
# 
# 
# 输入: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
# 输出: [[2,2,2],[2,2,2]]
# 
# 
# 
# 
# 提示:
# 
# 
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], newColor < 2^16
# 0 <= sr < m
# 0 <= sc < n
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image

        DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        q = [(sr, sc)]
        n = len(image)
        m = len(image[0])
        # visit = [[True] * m for _ in range(n)]
        # visit[sr][sc] = False
        srColor = image[sr][sc]
        image[sr][sc] = color
        while q:
            x, y = q.pop()
            for dr, dc in DIR:
                nx = x + dr
                ny = y + dc
                # if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] and image[nx][ny] == image[sr][sc]:
                if 0 <= nx < n and 0 <= ny < m and image[nx][ny] == srColor:
                    image[nx][ny] = color
                    q.append((nx, ny))
                    # visit[nx][ny] = False
        return image
# @lc code=end