#
# @lc app=leetcode.cn id=1681 lang=python3
#
# [1681] 最小不兼容性
#
# https://leetcode.cn/problems/minimum-incompatibility/description/
#
# algorithms
# Hard (42.76%)
# Likes:    56
# Dislikes: 0
# Total Accepted:    3.9K
# Total Submissions: 9K
# Testcase Example:  '[1,2,1,4]\n2'
#
# 给你一个整数数组 nums​​​ 和一个整数 k 。你需要将这个数组划分到 k 个相同大小的子集中，使得同一个子集里面没有两个相同的元素。
# 
# 一个子集的 不兼容性 是该子集里面最大值和最小值的差。
# 
# 请你返回将数组分成 k 个子集后，各子集 不兼容性 的 和 的 最小值 ，如果无法分成分成 k 个子集，返回 -1 。
# 
# 子集的定义是数组中一些数字的集合，对数字顺序没有要求。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,1,4], k = 2
# 输出：4
# 解释：最优的分配是 [1,2] 和 [1,4] 。
# 不兼容性和为 (2-1) + (4-1) = 4 。
# 注意到 [1,1] 和 [2,4] 可以得到更小的和，但是第一个集合有 2 个相同的元素，所以不可行。
# 
# 示例 2：
# 
# 
# 输入：nums = [6,3,8,1,3,1,2,2], k = 4
# 输出：6
# 解释：最优的子集分配为 [1,2]，[2,3]，[6,8] 和 [1,3] 。
# 不兼容性和为 (2-1) + (3-2) + (8-6) + (3-1) = 6 。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [5,3,3,6,3,3], k = 3
# 输出：-1
# 解释：没办法将这些数字分配到 3 个子集且满足每个子集里没有相同数字。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# nums.length 能被 k 整除。
# 1 
# 
# 
#
from functools import cache
from typing import List


# @lc code=start
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        self.kn = len(nums) // k
        nums = sorted(nums)

        @cache
        def solve(state = 0, lastp = -1) :
            p0s = [i for i in range(len(nums)) if not (1<<i) & state]
            if len(p0s) == 0 :
                return 0

            if lastp >= len(nums) :
                return 1e99

            if len(p0s) % self.kn == 0 :
                return solve(state|(1<<p0s[0]), p0s[0])
            
            # 一个有意思的剪枝
            if len(p0s) % self.kn > 1 :
                p0s = p0s[:- (len(p0s) % self.kn -  1)]
            
            to_ret = 1e99
            for t in p0s :
                if nums[t] <= nums[lastp] :
                    continue

                to_ret = min(to_ret, nums[t] - nums[lastp] + solve(state|(1<<t), t))
            return to_ret
            
        to_ret = solve()
        if to_ret > 1e66 :
            return -1
        return to_ret
        '''
        n = len(nums)
        
        value = dict()
        for sub in range(1 << n):
            # 判断 sub 是否有 n/k 个 1
            if bin(sub).count("1") == n // k:
                # 使用哈希表进行计数
                freq = set()
                flag = True
                for j in range(n):
                    if sub & (1 << j):
                        # 任意一个数不能出现超过 1 次
                        if nums[j] in freq:
                            flag = False
                            break
                        freq.add(nums[j])
                
                # 如果满足要求，那么计算 sub 的不兼容性
                if flag:
                    value[sub] = max(freq) - min(freq)
        
        f = dict()
        f[0] = 0
        for mask in range(1 << n):
            # 判断 mask 是否有 n/k 倍数个 1
            if bin(mask).count("1") % (n // k) == 0:
                # 如果子集个数小于 value 中满足要求的子集个数，我们才枚举子集
                if 2**bin(mask).count("1") < len(value):
                    sub = mask
                    while sub > 0:
                        if sub in value and mask ^ sub in f:
                            if mask not in f:
                                f[mask] = f[mask ^ sub] + value[sub]
                            else:
                                f[mask] = min(f[mask], f[mask ^ sub] + value[sub])
                        sub = (sub - 1) & mask
                else:
                    for sub, v in value.items():
                        if (mask & sub) == sub and mask ^ sub in f:
                            if mask not in f:
                                f[mask] = f[mask ^ sub] + v
                            else:
                                f[mask] = min(f[mask], f[mask ^ sub] + v)
            
        return -1 if (1 << n) - 1 not in f else f[(1 << n) - 1]
        '''
# @lc code=end

