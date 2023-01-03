#
# @lc app=leetcode.cn id=6197 lang=python3
#
# [6197] 最长上传前缀
#
# https://leetcode.cn/problems/longest-uploaded-prefix/description/
#
# algorithms
# Medium (51.34%)
# Likes:    0
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 4.3K
# Testcase Example:  '["LUPrefix","upload","longest","upload","longest","upload","longest"]\n[[4],[3],[],[1],[],[2],[]]'
#
# 给你一个 n 个视频的上传序列，每个视频编号为 1 到 n 之间的 不同 数字，你需要依次将这些视频上传到服务器。请你实现一个数据结构，在上传的过程中计算
# 最长上传前缀 。
# 
# 如果 闭区间 1 到 i 之间的视频全部都已经被上传到服务器，那么我们称 i 是上传前缀。最长上传前缀指的是符合定义的 i 中的 最大值 。
# 
# 请你实现 LUPrefix 类：
# 
# 
# LUPrefix(int n) 初始化一个 n 个视频的流对象。
# void upload(int video) 上传 video 到服务器。
# int longest() 返回上述定义的 最长上传前缀 的长度。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：
# ["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"]
# [[4], [3], [], [1], [], [2], []]
# 输出：
# [null, null, 0, null, 1, null, 3]
# 
# 解释：
# LUPrefix server = new LUPrefix(4);   // 初始化 4个视频的上传流
# server.upload(3);                    // 上传视频 3 。
# server.longest();                    // 由于视频 1 还没有被上传，最长上传前缀是 0 。
# server.upload(1);                    // 上传视频 1 。
# server.longest();                    // 前缀 [1] 是最长上传前缀，所以我们返回 1 。
# server.upload(2);                    // 上传视频 2 。
# server.longest();                    // 前缀 [1,2,3] 是最长上传前缀，所以我们返回 3 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^5
# 1 <= video <= 10^5
# video 中所有值 互不相同 。
# upload 和 longest 总调用 次数至多不超过 2 * 10^5 次。
# 至少会调用 longest 一次。
# 
# 
#

# @lc code=start
class LUPrefix:

    def __init__(self, n: int):
        self.ans = 0
        self.cnt = [0] * (10 ** 5 + 1)

    def upload(self, video: int) -> None:
        self.cnt[video] += 1

    def longest(self) -> int:
        while self.cnt[self.ans+1]:
            self.ans += 1
        return self.ans
        
# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
# @lc code=end

