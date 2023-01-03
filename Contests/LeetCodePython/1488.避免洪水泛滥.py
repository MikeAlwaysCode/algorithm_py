#
# @lc app=leetcode.cn id=1488 lang=python3
#
# [1488] 避免洪水泛滥
#
# https://leetcode.cn/problems/avoid-flood-in-the-city/description/
#
# algorithms
# Medium (25.93%)
# Likes:    111
# Dislikes: 0
# Total Accepted:    11.4K
# Total Submissions: 43.8K
# Testcase Example:  '[1,2,3,4]'
#
# 你的国家有无数个湖泊，所有湖泊一开始都是空的。当第 n 个湖泊下雨前是空的，那么它就会装满水。如果第 n 个湖泊下雨前是 满的 ，这个湖泊会发生 洪水
# 。你的目标是避免任意一个湖泊发生洪水。
# 
# 给你一个整数数组 rains ，其中：
# 
# 
# rains[i] > 0 表示第 i 天时，第 rains[i] 个湖泊会下雨。
# rains[i] == 0 表示第 i 天没有湖泊会下雨，你可以选择 一个 湖泊并 抽干 这个湖泊的水。
# 
# 
# 请返回一个数组 ans ，满足：
# 
# 
# ans.length == rains.length
# 如果 rains[i] > 0 ，那么ans[i] == -1 。
# 如果 rains[i] == 0 ，ans[i] 是你第 i 天选择抽干的湖泊。
# 
# 
# 如果有多种可行解，请返回它们中的 任意一个 。如果没办法阻止洪水，请返回一个 空的数组 。
# 
# 请注意，如果你选择抽干一个装满水的湖泊，它会变成一个空的湖泊。但如果你选择抽干一个空的湖泊，那么将无事发生。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：rains = [1,2,3,4]
# 输出：[-1,-1,-1,-1]
# 解释：第一天后，装满水的湖泊包括 [1]
# 第二天后，装满水的湖泊包括 [1,2]
# 第三天后，装满水的湖泊包括 [1,2,3]
# 第四天后，装满水的湖泊包括 [1,2,3,4]
# 没有哪一天你可以抽干任何湖泊的水，也没有湖泊会发生洪水。
# 
# 
# 示例 2：
# 
# 
# 输入：rains = [1,2,0,0,2,1]
# 输出：[-1,-1,2,1,-1,-1]
# 解释：第一天后，装满水的湖泊包括 [1]
# 第二天后，装满水的湖泊包括 [1,2]
# 第三天后，我们抽干湖泊 2 。所以剩下装满水的湖泊包括 [1]
# 第四天后，我们抽干湖泊 1 。所以暂时没有装满水的湖泊了。
# 第五天后，装满水的湖泊包括 [2]。
# 第六天后，装满水的湖泊包括 [1,2]。
# 可以看出，这个方案下不会有洪水发生。同时， [-1,-1,1,2,-1,-1] 也是另一个可行的没有洪水的方案。
# 
# 
# 示例 3：
# 
# 
# 输入：rains = [1,2,0,1,2]
# 输出：[]
# 解释：第二天后，装满水的湖泊包括 [1,2]。我们可以在第三天抽干一个湖泊的水。
# 但第三天后，湖泊 1 和 2 都会再次下雨，所以不管我们第三天抽干哪个湖泊的水，另一个湖泊都会发生洪水。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= rains.length <= 10^5
# 0 <= rains[i] <= 10^9
# 
# 
#
import collections
from heapq import heappop, heappush
from typing import List


# @lc code=start
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lakeToDays = collections.defaultdict(collections.deque)
        for i, r in enumerate(rains):
            if r != 0:
                lakeToDays[r].append(i)

        full = set()
        ans = []
        q = []
        for i, r in enumerate(rains):
            if r:
                if r in full:
                    return []
                else:
                    ans.append(-1)
                    full.add(r)
                    lakeToDays[r].popleft()
                    if lakeToDays[r]:
                        # 如果这个湖接下来某天还要下雨, 将下一个下雨日期加入优先队列
                        heappush(q, lakeToDays[r][0])
            else:
                if not q:
                    ans.append(1)
                else:
                    # 根据优先队列性质, index就是当前所有满了的湖中, 接下来要下雨的日期里距离现在最近的日期
                    index = heappop(q)
                    # 抽这个湖的水, 并将其从full集合移除
                    ans.append(rains[index])
                    full.remove(rains[index])
        return ans
# @lc code=end

