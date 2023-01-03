import bisect
import copy
import itertools
import math
from collections import Counter, defaultdict, deque
from functools import cache, reduce
from graphlib import TopologicalSorter
from heapq import heappop, heappush, heapreplace
from itertools import accumulate
from math import gcd, inf, lcm
from re import M
from typing import List, Optional

from sortedcontainers import SortedList, SortedSet


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.map = dict()

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += 1

class Allocator:

    # def __init__(self, n: int):
    #     self.mem = SortedList([(n, 0, 0)])
    #     self.d = dict()

    # def allocate(self, size: int, mID: int) -> int:
    #     pos = bisect.bisect_left(self.mem, size, key = lambda x: x[0])
    #     if pos == len(self.mem):
    #         return -1
    #     self.d[mID] += size
    #     ans = self.mem[pos][1]
    #     leftmem = self.mem[pos][0] - size
    #     self.mem.pop(pos)
    #     if leftmem > 0:
    #         self.mem.add((leftmem, ans + size, 0))
    #     return ans

    # def free(self, mID: int) -> int:
        # if self.d[mID] == 0:
        #     return 0
        # self.d[mID] = 0
        # pre = -1
        # for size, pos in self.mem:
        #     if pos 
        
    def __init__(self, n: int):
        self.n = n
        self.mem = [0] * n
        self.d = defaultdict(int)

    def allocate(self, size: int, mID: int) -> int:
        if size > self.n:
            return -1
        l = 0
        while l < self.n - size + 1:
            if self.mem[l] == 0:
                r = l
                while r + 1 < l + size and self.mem[r + 1] == 0:
                    r += 1
                if r - l + 1 >= size:
                    for i in range(l, r + 1):
                        self.mem[i] = mID
                        self.d[mID] += size
                        return l
                l = r + 1
            else:
                i += 1
        return -1

    def free(self, mID: int) -> int:
        if self.d[mID] == 0:
            return 0
        ans = self.d[mID]
        self.d[mID] = 0
        for i in range(self.n):
            if self.mem[i] == mID:
                self.mem[i] = 0
        return ans

class BIT:
    def __init__(self, n: int):
        self.nums = [0] * (n + 1)
        self.n = n
        self.BITree = [0] * (self.n + 1)
        
    def lowbit(self, x: int) -> int:
        return x & -x
    
    def query(self, x: int) -> int:
        ans = 0
        while x:
            ans += self.BITree[x]
            x -= self.lowbit(x)
        return ans

    def add(self, x: int, val: int):
        while x <= self.n:
            self.BITree[x] += val
            x += self.lowbit(x)

    def update(self, x: int, val: int) -> None:
        self.add(x + 1, val - self.nums[x])
        self.nums[x] = val

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        suf = [0] * n
        for i in range(n-1, -1, -1):
            if not q or nums[i] <= q[-1]:
                q.append(nums[i])
            else:
                q.clear()
                q.append(nums[i])
            suf[i] = len(q)
        # print(suf)
        q.clear()
        ans = []
        for i in range(n-k-1):
            if not q or nums[i] <= q[-1]:
                q.append(nums[i])
            else:
                q.clear()
                q.append(nums[i])
            if len(q) >= k and suf[i+2] >= k:
                ans.append(i+1)
        return ans

    def closeLampInTree(self, root: TreeNode) -> int:
        # DFS
        @cache
        def dfs(node, swithc2, switch3) -> int:
            if node is None:
                return 0

            if (node.val == 1) == (swithc2 == switch3):
                res1 = dfs(node.left, swithc2, False) + dfs(node.right, swithc2, False) + 1
                res2 = dfs(node.left, not swithc2, False) + dfs(node.right, not swithc2, False) + 1
                res3 = dfs(node.left, swithc2, True) + dfs(node.right, swithc2, True) + 1
                res123 = dfs(node.left, not swithc2, True) + dfs(node.right, not swithc2, True) + 3

                return min(res1, res2, res3, res123)
            else:
                res12 = dfs(node.left, not swithc2, False) + dfs(node.right, not swithc2, False) + 2
                res23 = dfs(node.left, not swithc2, True) + dfs(node.right, not swithc2, True) + 2
                res13 = dfs(node.left, swithc2, True) + dfs(node.right, swithc2, True) + 2
                res0 = dfs(node.left, swithc2, False) + dfs(node.right, swithc2, False)

                return min(res12, res23, res13, res0)

        return dfs(root, False, False)

    def unSuitability(self, arr: List[int]) -> int:
        mx = max(arr) * 2
        dp = [inf] * (mx + 1)
        dp[0] = 0
        for x in arr:
            cur = [inf] * (mx + 1)
            for j, dis in enumerate(dp):
                if dis == inf:
                    continue
                if j + x <= mx:
                    cur[j + x] = min(cur[j + x], max(dis, j + x))
                if j >= x:
                    cur[j - x] = min(cur[j - x], dis)
                else:
                    cur[0] = min(cur[0], dis - j + x)
            dp = cur

        return min(dp)

    def longestESR(self, sales: List[int]) -> int:
        pre = {0: -1}
        ans = cursum = 0

        for i, s in enumerate(sales):
            cursum += 1 if s > 8 else -1
            if cursum > 0:
                ans  = i + 1
            if cursum - 1 in pre:
                ans = max(ans, i - pre[cursum - 1])
            pre.setdefault(cursum, i)
        return ans

        '''
        n = len(sales)
        ans = 0
        presum = list(accumulate([1 if s > 8 else -1 for s in sales],initial=0))
        mx = [0] * (n + 1)
        mx[n] = presum[n]
        for i in range(n - 1, 0, -1):
            mx[i] = max(mx[i+1], presum[i])
        i, j = 0, 1
        while i <= n and j <= n:
            if presum[i] > mx[j]:
                i += 1
                continue
            while j <= n and presum[i] < mx[j]:
                j += 1
            ans = max(ans, j - i - 1)
            i += 1
        return ans
        '''

    def lightDistribution(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        s = set()
        ansseq = set()
        ans = []

        def dfs(node) -> str:
            if node is None:
                return "null"
            left = dfs(node.left)
            right = dfs(node.right)
            cur = "C:" + str(node.val) + "L:" + left + "R:" + right
            
            if cur in s and cur not in ansseq:
                ans.append(node)
                ansseq.add(cur)
            else:
                s.add(cur)
            
            return cur
        
        dfs(root)
        return ans
    def equalFrequency(self, word: str) -> bool:
        cnt = list(Counter(word).values())
        # cnt2 = list(Counter(cnt).values())
        cnt.sort()
        # print(cnt)
        # print(cnt2)
        
        if len(cnt) == 1 or (cnt[0] == 1 and cnt[1] == cnt[-1]) or (cnt[-1] == cnt[-2] + 1 and cnt[-2] == cnt[0]):
            return True
        else:
            return False

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        ans = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff:
        #             ans += 1
        # return ans
        d = [0] * n
        for i in range(n):
            d[i] = nums1[i] - nums2[i]
        # d.sort()
        # cnt = [0] * n
        k = SortedList()
        cn = 0
        print(d)
        for i in range(n-1, -1, -1):
            if cn > 0:
                j = bisect.bisect_left(k, d[i]-diff)
                ans += cn - j
            k.add(d[i])
            cn += 1
            # print(k)
        return ans
            
    def minNumBooths(self, demand: List[str]) -> int:
        d = dict()
        for dem in demand:
            cnt = Counter(dem)
            for k, v in cnt.items():
                if k not in d:
                    d[k] = v
                else:
                    d[k] = max(d[k], v)
        return sum(d.values())

    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS
        def dfs(node):
            if node.left:
                newNode = TreeNode(-1, node.left, None)
                node.left = newNode
                dfs(newNode.left)
            if node.right:
                newNode = TreeNode(-1, None, node.right)
                node.right = newNode
                dfs(newNode.right)
        dfs(root)
        return root
        
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(flowers)
        chk = [0] * (10 ** 5 + 1)
        preIdx = 0
        ans = 0
        for i in range(n):
            chk[flowers[i]] += 1
            if chk[flowers[i]] > cnt:
                k = i - preIdx
                ans += k * (k + 1) // 2

                while chk[flowers[i]] > cnt:
                    chk[flowers[preIdx]] -= 1
                    preIdx += 1

                k = i - preIdx
                ans -= k * (k + 1) // 2

                ans %= MOD
                    
        k = n - preIdx
        ans += k * (k + 1) // 2
        ans %= MOD
        return ans
        
    def sandyLandManagement(self, size: int) -> List[List[int]]:
        ans = []
        p = 2
        k = 1
        idx = 1
        for i in range(size, 1, -1):
            if idx == 1:
                j = k
                while j <= 2 * i - 1:
                    ans.append([i, j])
                    j += 2
                k = 4 - k
                # if i == 2 and p == 2 and k == 1:
                #     ans.append([2, 1])
            else:
                ans.append([i, p])
                p ^= 3
            idx ^= 1
        ans.append([1, 1])

        return ans

    def Leetcode(self, words: List[str]) -> int:
        target = "helloleetcode"
        need = [0] * 26
        for c in target:
            need[ord(c) - 97] += 1
        
        def chk(c):
            return need[ord(c) - 97] > 0

        def get(c):
            need[ord(c) - 97] -= 1

        n = len(words)
        v = [0] * n
        h = []
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m):
                if chk(word[j]):
                    v[i] += 1
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m):
                if chk(word[j]):
                    h.append((j * (m-j-1), -v[i], j, m-j-1, i, j))
                    
        k = 13
        ans = 0
        while k:
            # print(k)
            if not h:
                return -1
            k -= 1
            h.sort()
            # print(h)
            c = h.pop(0)
            # print(h)
            ans += c[0]
            # print(words[c[3]][c[4]])
            v[c[4]] -= 1
            get(words[c[4]][c[5]])

            tmp = []
            for i in range(len(h)):
                if not chk(words[h[i][4]][h[i][5]]):
                    v[h[i][4]] -= 1
            for i in range(len(h)):
                if chk(words[h[i][4]][h[i][5]]):
                    nm, nl, nr = h[i][0], h[i][2], h[i][3]
                    if h[i][4] == c[4]:
                        if nl > c[2]:
                            nl -= 1
                        if nr > c[3]:
                            nr -= 1
                        nm = nl * nr
                    tmp.append((nm, -v[h[i][4]], nl, nr, h[i][4], h[i][5]))
            h = tmp
        return ans

    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7

        n = len(grid)
        m = len(grid[0])

        dp = [[[0] * k for _ in range(m)] for _ in range(n)]
        dp[0][0][grid[0][0]%k] = 1

        for i in range(1, m):
            for j in range(k):
                cur = (dp[0][i-1][j] + grid[0][i]) % k
                dp[0][i][cur] = dp[0][i-1][j]

        for i in range(1, n):
            for j in range(k):
                cur = (dp[i-1][0][j] + grid[i][0]) % k
                dp[i][0][cur] = dp[i-1][0][j]
        
        for i in range(1, n):
            for j in range(1, m):
                for l in range(k):
                    cur = (dp[i-1][j][l] + grid[i][j]) % k
                    dp[i][j][cur] += dp[i-1][j][l]
                    cur = (dp[i][j-1][l] + grid[i][j]) % k
                    dp[i][j][cur] += dp[i][j-1][l]
        
        return dp[n-1][m-1][0]
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # ans = tot = sum(num * c for num, c in zip(nums, cost))
        # mx = max(nums)
        # d = {num:c for num, c in zip(nums, cost)}
        # cnt = Counter(nums)
        d = dict()
        mx = tot = p = 0
        for num, c in zip(nums, cost):
            if num not in d:
                d[num] = c
            else:
                d[num] += c
            tot += num * c
            p += c
            mx = max(mx, num)
        ans = tot
        q = 0
        for i in range(1, mx + 1):
            tot += q - p
            ans = min(ans, tot)
            if i in d:
                q += d[i]
                p -= d[i]
        return ans

    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        cnt = Counter(target)
        numOdd = []
        numEven = []
        tarOdd = []
        tarEven = []
        for num in nums:
            if num in cnt and cnt[num] > 0:
                cnt[num] -= 1
            else:
                if num & 1:
                    numOdd.append(num)
                else:
                    numEven.append(num)
        for num in target:
            if cnt[num] > 0:
                cnt[num] -= 1
                if num & 1:
                    tarOdd.append(num)
                else:
                    tarEven.append(num)
        
        diff = ans = 0
        def cal(nums, target) -> int:
            nonlocal diff, ans
            for x, y in zip(nums, target):
                nd = y - x
                if (diff >= 0 and nd > 0) or (diff <= 0 and nd < 0):
                    ans += abs(nd) // 2
                elif abs(nd) > abs(diff):
                    ans += abs(nd + diff) // 2
                diff += nd
            return diff
        
        # print(numOdd)
        # print(tarOdd)
        # cal(numOdd, tarOdd)
        # print(ans, diff)
        # print(numEven)
        # print(tarEven)
        # cal(numEven, tarEven)
        # print(ans, diff)
        # diff = ans = 0

        cal(numOdd, tarOdd)
        cal(numEven, tarEven)

        return ans

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        MX = 10 ** 5 + 1
        h = [0] * MX
        q = [root]
        cur = 0
        n = 0
        parent = [-1] * MX
        child = defaultdict(list)
        leaf = []
        deep = [0] * MX
        while q:
            tmp = q
            q = []
            for x in tmp:
                n = max(n, x.val)
                h[x.val] = cur
                if x.left:
                    parent[x.left.val] = x.val
                    child[x.val].append(x.left.val)
                    q.append(x.left)
                if x.right:
                    parent[x.right.val] = x.val
                    child[x.val].append(x.right.val)
                    q.append(x.right)
                if not x.left and x.right:
                    leaf.append(x.val)
            cur += 1
        q = leaf
        cur = 0
        while q:
            tmp = q
            q = []
            cur += 1
            for x in tmp:
                if parent[x] == -1:
                    continue
                q.append(parent[x])
                deep[parent[x]] = max(deep[parent[x]], cur)

        m = len(queries)
        ans = [0] * m
        for i in range(m):
            cur = h[queries[i]]
            p = parent[queries[i]]
            d = 0
            for x in child[p]:
                d = max(d, deep[x])
            ans[i] = h[cur] + d

        return ans
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + [0]
        ans = []
        for i in range(n):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i]:
                ans.append(nums[i])
        if len(ans) < n:
            ans = ans + [0] * (n - len(ans))
        return ans

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = tot = 0
        l = r = 0
        n = len(nums)
        cnt = defaultdict(int)
        while r < n:
            cnt[nums[r]] += 1
            tot += nums[r]
            while cnt[nums[r]] > 1 or r - l + 1 > k:
                cnt[nums[l]] -= 1
                tot -= nums[l]
                l += 1
            if r - l + 1 == k:
                ans = max(ans, tot)
            r += 1
        return ans

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        preh, sufh = [10 ** 6], [10 ** 6]
        n = len(costs)
        l, r = 0, n - 1
        while l < candidates:
            heappush(preh, costs[l])
            l += 1
            if r >= candidates:
                heappush(sufh, costs[r])
                r -= 1
        ans = 0
        while k > 0:
            if sufh[0] < preh[0]:
                ans += heappop(sufh)
                if r >= l:
                    heappush(sufh, costs[r])
                    r -= 1
            else:
                ans += heappop(preh)
                if l <= r:
                    heappush(preh, costs[l])
                    l += 1
            k -= 1
        return ans

    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)
        fpos, valid = map(list, zip(*factory))

        # @cache
        def dfs(i: int, valid: list[int]) -> int:
            if i == n:
                return 0

            idx = bisect.bisect(fpos, robot[i])

            res = math.inf
            if idx > 0 and valid[idx-1] > 0:
                valid[idx-1] -= 1
                res = min(res, abs(robot[i] - fpos[idx-1]) + dfs(i+1, valid))
                valid[idx-1] += 1
                
            if idx < m and valid[idx] > 0:
                valid[idx] -= 1
                res = min(res, abs(fpos[idx] - robot[i]) + dfs(i+1, valid))
                valid[idx] += 1
            return res

        return dfs(0, valid)

    def halvesAreAlike(self, s: str) -> bool:
        s = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        cnt = [0] * 2
        n = len(s)
        for i, c in enumerate(s):
            if c in s:
                cnt[(i * 2) // n] += 1
        return cnt[0] == cnt[1]

    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        m = 1
        while m <= n:
            x = m
            cnt = 0
            p = 9
            b = 1
            while x > 0:
                cnt += b * min(p, x)
                x -= min(p, x)
                b += 1
                p *= 10
            l = len(str(m))
            cnt += (3 + l) * m + n
            print(m, cnt)
            if (cnt + limit - 1) // limit <= m:
                break
            m += 1
        if m > n:
            return []
        
        l = len(str(m))
        ans = []
        pre = 0
        for i in range(1, m + 1):
            cur = limit - l - 3 - len(str(i))
            ans.append(message[pre:pre+cur] + '<' + str(i) + '/' + str(m) + '>')
            pre += cur
        return ans
        
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def getMinSwap(arr: list[int]) -> int:
            n = len(arr)
            d = {v:i for i, v in enumerate(sorted(arr))}
            # sa = arr.copy()
            # sa.sort()
            # d = dict()
            # for i in range(n):
            #     d[sa[i]] = i
            loops = 0
            flag = [False] * n
            for i in range(n):
                if not flag[i]:
                    j = i
                    while not flag[j]:
                        flag[j] = True
                        j = d[arr[j]]
                    loops += 1
            return n - loops
        ans = 0
        q = [root]
        while q:
            tmp = q
            q = []
            vals = []
            for x in tmp:
                vals.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            ans += getMinSwap(vals)
        return ans
        
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if k == 1:
            return n

        
        s = '#' + '#'.join(list(s)) + '#'
        cnt = [0] * len(s)
        left = [-1] * len(s)
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len

            # if 2 * cur_arm_len + 1 >= k * 2:
            if cur_arm_len >= k:
                if left[i + cur_arm_len] == -1:
                    cnt[i + cur_arm_len] = 1
                    left[i + cur_arm_len] = i - cur_arm_len + 1
                else:
                    left[i + cur_arm_len] = max(left[i + cur_arm_len], i - cur_arm_len + 1)
        '''
        # if n < 2:
        #     return 1
        
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        # 递推开始
        # 先枚举子串长度
        cnt = [0] * n
        left = [-1] * n
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break
                    
                if s[i] != s[j]:
                    dp[i][j] = False 
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 >= k:
                    cnt[j] = 1
                    if left[j] == -1:
                        left[j] = i
                    else:
                        left[j] = max(left[j], i)
        '''
        print(cnt)
        print(left)
        for i in range(len(s)):
            if i > 0:
                cnt[i] = max(cnt[i-1], cnt[i])
            if left[i] != -1:
                if left[i] > 0:
                    cnt[i] = max(cnt[i], cnt[left[i]-1] + 1)
        print(cnt)
        return cnt[-1]

    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        v = list(cnt.values())
        
        ans = 0
        
        for comb in itertools.combinations(v, 3):
            ans += comb[0] * comb[1] * comb[2]
        return ans
        
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        node = root
        stack = []
        nums = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                nums.append(node.val)
                node = node.right
        
        ans = []
        for q in queries:
            j = bisect.bisect_left(nums, q)
            
            if j < len(nums):
                if nums[j] == q:
                    ans.append([q, q])
                elif j > 0:
                    ans.append([nums[j-1], nums[j]])
                else:
                    ans.append([-1, nums[j]])
            else:
                ans.append([nums[j-1], -1])
        return ans
        '''
        def find(x: int) -> List[List[int]]:
            mn = mx = -1
            node = root
            while node:
                if node.val == x:
                    mn = mx = x
                    break
                elif node.val > x:
                    mx = node.val
                    node = node.left
                else:
                    mn = node.val
                    node = node.right

            return [mn, mx]

        ans = []
        for q in queries:
            ans.append(find(q))
        return ans
        '''

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        tree = [[] for _ in range(10 ** 5 + 1)]
        n = 0
        for u, v in roads:
            tree[u].append(v)
            tree[v].append(u)
            n = max(n, u, v)

        parent = [-1] * (n + 1)
        # h = [0] * (n + 1)
        cnt = [1] * (n + 1)
        # leaf = [False] * (n + 1)
        level = [[0]]
        q = [(0, -1)]
        dep = 0
        while q:
            tmp = q
            q = []
            dep += 1
            cur = []
            for x, p in tmp:
                for u in tree[x]:
                    if u == p:
                        continue
                    q.append((u, x))
                    parent[u] = x
                    # h[u] = dep
                    cur.append(u)
                # if x != 0 and len(tree[x]) == 1:
                #     leaf[x] = True
            level.append(cur)
        
        ans = 0
        for i in range(dep, 0, -1):
            for x in level[i]:
                # if leaf[x]:
                #     ans += 1
                #     cnt[parent[x]] += 1
                #     # ans += h[x]
                #     # seat[parent[x]] += seats - 1
                # else:
                ans += (cnt[x] + seats - 1) // seats
                cnt[parent[x]] += cnt[x]

        return ans
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10 ** 9 + 7
        primes = {'2', '3', '5', '7'}

        n = len(s)
        if s[0] not in primes or s[-1] in primes or k * minLength  > n:
            return 0

        # pos = [-1]
        # m = len(s)
        # pos = []
        # pos.append(m)
        # n = len(pos)
        
        check = [False] * (n + 1)
        check[0] = check[n] = True
        for i in range(1, n):
            if s[i-1] not in primes and s[i] in primes:
                check[i] = True

        dp = [[0] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 1
        for i in range(1, k + 1):
            sum = 0
            for j in range(i * minLength, n + 1):
                if check[j-minLength]: sum = (sum + dp[i-1][j-minLength]) % MOD
                if check[j]: dp[i][j] = sum

        return dp[k][n]
    def countPalindromes(self, s: str) -> int:
        n = len(s)
        if n < 5:
            return 0
        pos = [[] for _ in range(10)]
        for i, c in enumerate(s):
            pos[int(c)].append(i)
        # print(pos)
        MOD = 10 ** 9 + 7
        ans = 0
        dp = set()
        cnt = [0] * n
        for i, c in enumerate(s):
            d = int(c)
            # print(dp)
            j = bisect.bisect(pos[d], i)
            for k in dp:
                # j = bisect.bisect(pos[d], k)
                # if j == 0:
                #     continue
                for l in range(j, len(pos[d])):
                    if pos[d][l] >= k:
                        break
                    ans += (pos[d][l] - i - 1) * cnt[k]
                    ans %= MOD
            for k in pos[d][j:]:
                dp.add(k)
                cnt[k] += 1
        return ans

    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for i in range(len(words)):
            if words[i][0] != words[i-1][-1]:
                return False
        return True
        
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 1, len(skill) - 2
        ans = skill[0] * skill[-1]
        sum = skill[0] + skill[-1]
        while l < r:
            if skill[l] + skill[r] != sum:
                return -1
            ans += skill[l] * skill[r]
            l += 1
            r -= 1
        return ans
        
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        fa = list(range(n + 1))
        s = [math.inf] * (n + 1)
        
        def find(x):
            cur = x
            while x != fa[x]:
                x = fa[x]
            if cur != x:
                fa[cur] = x
            return x

        for u, v, d in roads:
            fu = find(u)
            fv = find(v)
            s[fu] = min(s[fu], d)
            fa[fv] = fu
            
        f1 = find(1)
        ans = s[f1]
        for i in range(1, n + 1):
            if find(i) == 1 or find(i) == f1:
                ans = min(ans, s[i])

        return ans
        
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        w = [[] for _ in range(n)]
        for u, v in edges:
            if vals[v] > 0:
                w[u].append(vals[v])
            if vals[u] > 0:
                w[v].append(vals[u])

        ans = - 10 ** 10
        for i in range(n):
            w[i].sort(reverse=True)
            ans = max(ans, vals[i] + sum(w[i][:k]))
        return ans
        
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        if n <= 3:
            return stones[-1]
        
        ans = stones[1]
        for i in range(2, n):
            ans = max(ans, stones[i] - stones[i - 2])

        return ans
        
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        ans = c = 0
        cc = Counter()
        for i in range(n):
            if cnt1[nums1[i]] + cnt2[nums2[i]] > n:
                return -1
            if nums1[i] == nums2[i]:
                ans += i
                c += 1
                cc[nums1[i]] += 1

        if c == n or c == 0:
            return ans
        
        k = 0
        if cc.most_common(1)[0][1] * 2 > c:
            k = cc.most_common(1)[0][1] * 2 - c
            ns = cc.most_common(1)[0][0]

        i = 0
        while k and i < n:
            if nums1[i] != nums2[i] and nums1[i] != ns and nums2[i] != ns:
                ans += i
                k -= 1
            i += 1

        if k:
            return -1
        else:
            return ans

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
        n, m = len(grid), len(grid[0])
        mn = [[math.inf] * m for _ in range(n)]
        q = [(0, 0, 0)]
        while q:
            # p, x, y = q.popleft()
            p, x, y = heappop(q)
            p = max(p, grid[x][y])
            mn[x][y] = p
            for dr, dc in DIR:
                nx, ny = x + dr, y + dc
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if p < mn[nx][ny]:
                    # mn[nx][ny] = p
                    # q.append((nx, ny, p))
                    heappush((p, nx, ny))
        
        qs = sorted(set(queries))
        qn = len(qs)
        d = defaultdict(int)
        for i in range(n):
            for j in range(m):
                d[mn[i][j]] += 1
        cnt = 0
        i = 0
        ad = defaultdict(int)
        for k, v in sorted(d.items()):
            while i < qn and qs[i] <= k:
                ad[qs[i]] = cnt
                i += 1
            if i == qn:
                break
            cnt += v
        while i < qn:
            ad[qs[i]] = cnt
            i += 1

        for i in range(len(queries)):
            queries[i] = ad[queries[i]]
        return queries
        
    def similarPairs(self, words: List[str]) -> int:
        n = len(words)
        arr = [0] * n
        for i, word in enumerate(words):
            s = set(word)
            for c in s:
                arr[i] += (1 << (ord(c) - 97))

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    ans += 1
        
        return ans

    def smallestValue(self, n: int) -> int:
        mxn = n
        factor = [1] * (mxn + 1)
        primes = list()
        
        for i in range(2, mxn + 1):
            if factor[i] != 1:
                continue
            primes.append(i)
            for j in range(i, mxn + 1, i):
                factor[j] = i

        def prime_factor(x) -> int:
            # res = set()
            res = 0
            while x != 1:
                # res.add(factor[x])
                res += factor[x]
                x //= factor[x]
            return res

        ps = prime_factor(n)
        while ps != n:
            n = ps
            ps = prime_factor(n)

        return n
        
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        degrees = [0] * (n + 1)
        graph = [set() for _ in range(n + 1)]
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1
            graph[u].add(v)
            graph[v].add(u)

        v = []
        for i in range(1, n + 1):
            if degrees[i] & 1:
                v.append(i)

        if len(v) == 0:
            return True
        elif len(v) == 2:
            if v[0] not in graph[v[1]]:
                return True
            else:
                for i in range(1, n + 1):
                    if i != v[0] and i != v[1] and i not in graph[v[0]] and i not in graph[v[1]]:
                        return True
                return False
        elif len(v) == 4:
            if v[0] not in graph[v[1]] and v[2] not in graph[v[3]]:
                return True
            elif v[0] not in graph[v[2]] and v[1] not in graph[v[3]]:
                return True
            elif v[0] not in graph[v[3]] and v[1] not in graph[v[2]]:
                return True
            else:
                return False
        else:
            return False
            
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        m = len(queries)
        ans = [0] * m

        def cal(u, v) -> int:
            res = 0
            while u != v:
                if u > v:
                    u //= 2
                else:
                    v //= 2
                res += 1
            return res + 1

        for i in range(m):
            ans[i] = cal(queries[i][0], queries[i][1])

        return ans
        
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        ans = 0
        pre1 = pren1 = -1
        for i in range(n):
            if forts[i] == 1:
                if pren1 > pre1:
                    ans = max(ans, i - pren1 - 1)
                pre1 = i
            elif forts[i] == -1:
                if pre1 > pren1:
                    ans = max(ans, i - pre1 - 1)
                pren1 = i
        return ans


    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive = set(positive_feedback)
        negative = set(negative_feedback)
        n = len(student_id)
        ss = sorted(zip(student_id, range(n)))
        score = [0] * n
        for _, i in ss:
            rep = report[i].split()
            for word in rep:
                if word in positive:
                    score[i] += 3
                elif word in negative:
                    score[i] -= 1
        ss.sort(key = lambda x: - score[x[1]])
        ans, _ = map(list, zip(*ss))
        return ans[:k]
        
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        dlcm = math.lcm(divisor1, divisor2)
        
        def check(x) -> bool:
            ab = x // dlcm
            a = x // divisor1
            b = x // divisor2
            return (x - ab) >= (uniqueCnt1 + uniqueCnt2) and (x - a) >= uniqueCnt1 and (x - b) >= uniqueCnt2

        l, r = 1, 10 ** 15
        while l < r:
            mid = l + r >> 1
            if check(mid):
                r = mid
            else:
                l =  mid + 1
        return r
        
    def countAnagrams(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        ans = 1
        n = len(s)
        	# 阶乘
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i-1] * i % MOD
        # 逆元
        inverse = [0] * (n + 1)
        inverse[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inverse[i-1] = inverse[i] * i % MOD

        words = s.split()
        for word in words:
            cnt = Counter(word)
            res = fact[len(word)]
            for v in cnt.values():
                res = res * inverse[v] % MOD
            ans = ans * res % MOD
        return ans
        
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        l = r = startIndex
        n = len(words)
        ans = 0
        while ans < n and words[l] != target and words[r] != target:
            ans += 1
            r = (r + 1) % n
            l = (l - 1) % n
        return ans if (words[l] == target or words[r] == target) else -1
        
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = Counter(s)
        if k == 0: return 0

        if cnt['a'] < k or cnt['b'] < k or cnt['c'] < k:
            return -1

        m = len(s)
        s = s + s
        cnt.clear()
        n = len(s)
        l = r = 0
        ans = m
        while r < n:
            cnt[s[r]] += 1
            if cnt['a'] >= k and cnt['b'] >= k and cnt['c'] >= k:
                ans = min(ans, r - l + 1)
            while r >= m - 1 and l < r and cnt['a'] >= k and cnt['b'] >= k and cnt['c'] >= k and cnt[s[l]] > k:
                cnt[s[l]] -= 1
                l += 1
                ans = min(ans, r - l + 1)
            r += 1
        return ans
        
    def maximumTastiness(self, price: List[int], k: int) -> int:
        n = len(price)
        price.sort()
        if price[0] == price[-1]:
            return 0

        l, r = 0, price[-1] - price[0]
        while l < r:
            mid = l + r + 1 >> 1
            cnt = 0
            pres = - 10 ** 10
            for p in price:
                if p - pres >= mid:
                    cnt += 1
                    pres = p
            if cnt >= k:
                l = mid
            else:
                r = mid - 1
        return l
        
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        n = len(nums)
        sm = sum(nums)
        if sm < k * 2: return 0
        ans = 0
        dp = [[0] * k for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(k):
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
                if j + nums[i] < k:
                    dp[i + 1][j + nums[i]] = (dp[i + 1][j + nums[i]] + dp[i][j]) % MOD
        ans = sum(dp[n]) % MOD
        return (pow(2, n, MOD) - ans * 2) % MOD

def main():
    sol = Solution()

    

    # nums = [1,2,3,4]
    # k = 4
    # print(sol.countPartitions(nums, k))
    # # nums = [6,6]
    # # k = 2
    # nums = [73,16,86,25,98,92,15,11,87,88,88,94,83,74,1,48,91,9,45]
    # k = 61
    # print(sol.countPartitions(nums, k))

    # s = "too hot"
    # print(sol.countAnagrams(s))

    # grid = [[1,2,3],[2,5,7],[3,5,1]]
    # queries = [5,6,2]

    # print(sol.maxPoints(grid, queries))

if __name__ == '__main__':
    main()