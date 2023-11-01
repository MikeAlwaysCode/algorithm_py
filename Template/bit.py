# 模板一：BIT
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
        # ans = math.inf
        # x += 1
        # while x <= self.n:
        #     self.BITree[x] = min(self.BITree[x], val)
        #     x += self.lowbit(x)

    def add(self, x: int, val: int):
        while x <= self.n:
            self.BITree[x] += val
            x += self.lowbit(x)

    def update(self, x: int, val: int) -> None:
        self.add(x + 1, val - self.nums[x])
        self.nums[x] = val
        # x += 1
        # while x <= self.n:
        #     self.BITree[x] = min(self.BITree[x], val)
        #     x += self.lowbit(x)

    def lower_bound(self, s):
        x = y = 0
        for i in range(self.n.bit_length() - 1, -1, -1):
            k = x + (1 << i)
            if k <= self.n and (y + self.BITree[k] < s):
                y += self.BITree[k]
                x += 1 << i
        return x + 1

    # 逆序对
    def getPairOfInversion(nums: list) -> int:
        bit = BIT(max(nums))
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            res += bit.query(nums[i])
            bit.update(nums[i], 1)
        return res

# 模板二
class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)
        for i, num in enumerate(nums, 1):
            self.add(i, num)
    def add(self, index: int, val: int):
        while index < len(self.tree):
            self.tree[index] += val
            index += index & -index
    def prefixSum(self, index) -> int:
        s = 0
        while index:
            s += self.tree[index]
            index &= index - 1
        return s
    def update(self, index: int, val: int) -> None:
        self.add(index + 1, val - self.nums[index])
        self.nums[index] = val
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right + 1) - self.prefixSum(left)


# 模板三
arr = []
n = 10
ans = 0

discretization = {v:i for i, v in enumerate(sorted(set(arr)))}
tn = len(discretization)
BITree = [0] * (tn + 1)

def lowbit(x: int) -> int:
    return x & -x

def query(x: int) -> int:
    ans = 0
    while x:
        ans += BITree[x]
        x -= lowbit(x)
    return ans

def add(x: int, val: int):
    while x <= tn:
        BITree[x] += val
        x += lowbit(x)

for i in range(n - 1, -1, -1):
    idx = discretization[arr[i]]
    ans += query(idx+1)
    add(idx+1, 1)

