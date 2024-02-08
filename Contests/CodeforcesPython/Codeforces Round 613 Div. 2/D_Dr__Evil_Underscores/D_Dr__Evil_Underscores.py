import sys
from bisect import bisect_left

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

class BinaryTrie:
    def __init__(self, max_bit: int = 30):
        self.inf = 1 << 63
        self.to = [[-1], [-1]]
        self.cnt = [0]
        self.max_bit = max_bit

    def add(self, num: int) -> None:
        cur = 0
        self.cnt[cur] += 1
        for k in range(self.max_bit, -1, -1):
            bit = (num >> k) & 1
            if self.to[bit][cur] == -1:
                self.to[bit][cur] = len(self.cnt)
                self.to[0].append(-1)
                self.to[1].append(-1)
                self.cnt.append(0)
            cur = self.to[bit][cur]
            self.cnt[cur] += 1

    # Get max result for constant x ^ element in array
    def max_xor(self, x: int) -> int:
        if self.cnt[0] == 0: return -self.inf
        res = cur = 0
        for k in range(self.max_bit, -1, -1):
            bit = (x >> k) & 1
            nxt = self.to[bit ^ 1][cur]
            if nxt == -1 or self.cnt[nxt] == 0:
                cur = self.to[bit][cur]
            else:
                cur = nxt
                res |= 1 << k
        return res
    
    def min_max(self, res: int, bit: int, cur: int) -> int:
        if bit < 0:
            return res
        if self.to[0][cur] != -1 and self.to[1][cur] != -1:
            return min(self.min_max(res | (1 << bit), bit - 1, self.to[0][cur]), self.min_max(res | (1 << bit), bit - 1, self.to[1][cur]))
        elif self.to[0][cur] != -1:
            return self.min_max(res, bit - 1, self.to[0][cur])
        elif self.to[1][cur] != -1:
            return self.min_max(res, bit - 1, self.to[1][cur])


def f(nums: list, max_bit: int, pre: int):
    if max_bit < 0 or not nums or nums[0] == nums[-1]:
        return 0
    
    bit = 1 << max_bit
    if (nums[0] & bit) == (nums[-1] & bit):
        return f(nums, max_bit - 1, pre | (nums[0] & bit))
    else:
        i = bisect_left(nums, pre | bit)
        return min(f(nums[:i], max_bit - 1, pre), f(nums[i:], max_bit - 1, pre | bit)) | bit
    
def solve() -> None:
    n = sint()
    nums = ints()
    '''
    bit = BinaryTrie()
    for a in nums:
        bit.add(a)
    print(bit.min_max(0, 30, 0))
    '''
    '''
    nums.sort()
    print(f(nums, 30, 0))
    '''

    def z(l: int, r: int, max_bit: int, pre: int):
        if max_bit < 0 or l >= r or nums[l] == nums[r]:
            return 0
        
        bit = 1 << max_bit
        if (nums[l] & bit) == (nums[r] & bit):
            return z(l, r, max_bit - 1, pre | (nums[l] & bit))
        else:
            i = bisect_left(nums, pre | bit, l, r + 1)
            return min(z(l, i - 1, max_bit - 1, pre), z(i, r, max_bit - 1, pre | bit)) | bit

    nums.sort()
    print(z(0, n - 1, 29, 0))

solve()
