#
# @lc app=leetcode.cn id=2456 lang=python3
#
# [2456] 最流行的视频创作者
#
# https://leetcode.cn/problems/most-popular-video-creator/description/
#
# algorithms
# Medium (32.21%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    6.4K
# Total Submissions: 17.2K
# Testcase Example:  '["alice","bob","alice","chris"]\n["one","two","three","four"]\n[5,10,5,4]'
#
# 给你两个字符串数组 creators 和 ids ，和一个整数数组 views ，所有数组的长度都是 n 。平台上第 i 个视频者是 creator[i]
# ，视频分配的 id 是 ids[i] ，且播放量为 views[i] 。
# 
# 视频创作者的 流行度 是该创作者的 所有 视频的播放量的 总和 。请找出流行度 最高 创作者以及该创作者播放量 最大 的视频的 id 。
# 
# 
# 如果存在多个创作者流行度都最高，则需要找出所有符合条件的创作者。
# 如果某个创作者存在多个播放量最高的视频，则只需要找出字典序最小的 id 。
# 
# 
# 返回一个二维字符串数组 answer ，其中 answer[i] = [creatori, idi] 表示 creatori 的流行度 最高
# 且其最流行的视频 id 是 idi ，可以按任何顺序返回该结果。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：creators = ["alice","bob","alice","chris"], ids =
# ["one","two","three","four"], views = [5,10,5,4]
# 输出：[["alice","one"],["bob","two"]]
# 解释：
# alice 的流行度是 5 + 5 = 10 。
# bob 的流行度是 10 。
# chris 的流行度是 4 。
# alice 和 bob 是流行度最高的创作者。
# bob 播放量最高的视频 id 为 "two" 。
# alice 播放量最高的视频 id 是 "one" 和 "three" 。由于 "one" 的字典序比 "three" 更小，所以结果中返回的 id 是
# "one" 。
# 
# 
# 示例 2：
# 
# 
# 输入：creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]
# 输出：[["alice","b"]]
# 解释：
# id 为 "b" 和 "c" 的视频都满足播放量最高的条件。
# 由于 "b" 的字典序比 "c" 更小，所以结果中返回的 id 是 "b" 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == creators.length == ids.length == views.length
# 1 <= n <= 10^5
# 1 <= creators[i].length, ids[i].length <= 5
# creators[i] 和 ids[i] 仅由小写英文字母组成
# 0 <= views[i] <= 10^5
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        m, max_view_sum = {}, 0
        for name, id, view in zip(creators, ids, views):
            if name in m:
                t = m[name]
                t[0] += view
                if view > t[1] or view == t[1] and id < t[2]:
                    t[1], t[2] = view, id
            else: m[name] = [view, view, id]
            max_view_sum = max(max_view_sum, m[name][0])
        return [[name, id] for name, (view_sum, _, id) in m.items() if view_sum == max_view_sum]
# @lc code=end

