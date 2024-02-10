import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

class SegTree:
    def __init__(self, nums: list) -> None:
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 1, 1, self.n)
        
    def build(self, nums: list, o: int, l: int, r: int) -> None:
        if l == r:
            self.tree[o] = nums[l - 1]
            return

        m = (l + r) >> 1
        self.build(nums, o * 2, l, m)
        self.build(nums, o * 2 + 1, m + 1, r)
    
    def do(self, o: int, val: int) -> None:
        self.tree[o] += val
    
    def update(self, o: int, l: int, r: int, L: int, R: int, val: int) -> None:
        if L <= l and r <= R:
            self.do(o, val)
            return
        
        m = (l + r) >> 1
        if m >= L:
            self.update(o * 2, l, m, L, R, val)
        if m < R:
            self.update(o * 2 + 1, m + 1, r, L, R, val)
    
    def query(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if R < l or L > r:
            return 0
        
        if L <= l and r <= R:
            return self.tree[o]
        
        m = (l + r) >> 1
        # res = 0
        res = self.tree[o]
        if m >= L:
            res += self.query(o * 2, l, m, L, R)
        if m < R:
            res += self.query(o * 2 + 1, m + 1, r, L, R)
        
        return res

def solve() -> None:
    n, m = mint()
    nums = ints()
    box = ints()
    st = SegTree(nums)
    for b in box:
        cnt = st.query(1, 1, n, b + 1, b + 1)
        st.update(1, 1, n, b + 1, b + 1, - cnt)
        d = cnt // n
        if d:
            st.update(1, 1, n, 1, n, d)
        cnt %= n
        m = min(cnt, n - 1 - b)
        if m:
            st.update(1, 1, n, b + 2, b + m + 1, 1)
        cnt -= m
        if cnt:
            st.update(1, 1, n, 1, cnt, 1)
    for i in range(n):
        nums[i] = st.query(1, 1, n, i + 1, i + 1)
    print(*nums)


solve()
