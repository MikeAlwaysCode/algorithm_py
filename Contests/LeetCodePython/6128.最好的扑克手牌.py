#
# @lc app=leetcode.cn id=6128 lang=python3
#
# [6128] 最好的扑克手牌
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        '''
        sc = 1
        for i in range(1, len(suits)):
            if suits[i] == suits[i-1]:
              sc += 1
        
        if sc == 5:
            return "Flush"
        '''
        if len(set(suits)) == 1:
            return "Flush"
        
        c = Counter(ranks)
        # sc = c.most_common(1)[0][1]
        sc = max(c.values())
            
        if sc >= 3:
            return "Three of a Kind"
        elif sc >= 2:
            return "Pair"
        else:
            return "High Card"
# @lc code=end

