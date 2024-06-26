#
# @lc app=leetcode.cn id=1117 lang=python3
#
# [1117] H2O 生成
#
# https://leetcode.cn/problems/building-h2o/description/
#
# concurrency
# Medium (53.86%)
# Likes:    126
# Dislikes: 0
# Total Accepted:    26K
# Total Submissions: 48.3K
# Testcase Example:  '"HOH"'
#
# 现在有两种线程，氧 oxygen 和氢 hydrogen，你的目标是组织这两种线程来产生水分子。
# 
# 存在一个屏障（barrier）使得每个线程必须等候直到一个完整水分子能够被产生出来。
# 
# 氢和氧线程会被分别给予 releaseHydrogen 和 releaseOxygen 方法来允许它们突破屏障。
# 
# 这些线程应该三三成组突破屏障并能立即组合产生一个水分子。
# 
# 你必须保证产生一个水分子所需线程的结合必须发生在下一个水分子产生之前。
# 
# 换句话说:
# 
# 
# 如果一个氧线程到达屏障时没有氢线程到达，它必须等候直到两个氢线程到达。
# 如果一个氢线程到达屏障时没有其它线程到达，它必须等候直到一个氧线程和另一个氢线程到达。
# 
# 
# 书写满足这些限制条件的氢、氧线程同步代码。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: water = "HOH"
# 输出: "HHO"
# 解释: "HOH" 和 "OHH" 依然都是有效解。
# 
# 
# 示例 2:
# 
# 
# 输入: water = "OOHHHH"
# 输出: "HHOHHO"
# 解释: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" 和
# "OHHOHH" 依然都是有效解。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 * n == water.length
# 1 <= n <= 20
# water[i] == 'O' or 'H'
# 输入字符串 water 中的 'H' 总数将会是 2 * n 。
# 输入字符串 water 中的 'O' 总数将会是 n 。
# 
# 
#
from collections import deque
from typing import Callable


# @lc code=start
class H2O:
    def __init__(self):
        self.h = deque()
        self.o = deque()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        # releaseHydrogen()
        self.h.append(releaseHydrogen)
        self.res()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        # releaseOxygen()
        self.o.append(releaseOxygen)
        self.res()
        
    def res(self):
        if len(self.h) > 1 and len(self.o) > 0:
            self.h.popleft()()
            self.h.popleft()()
            self.o.popleft()()
# @lc code=end

