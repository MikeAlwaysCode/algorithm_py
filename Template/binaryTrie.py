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

    def remove(self, num: int) -> bool:
        if self.cnt[0] == 0: return False
        cur = 0
        rm = [0]
        for k in range(self.max_bit, -1, -1):
            bit = (num >> k) & 1
            cur = self.to[bit][cur]
            if cur == -1 or self.cnt[cur] == 0: return False
            rm.append(cur)
        for cur in rm: self.cnt[cur] -= 1
        return True

    def count(self, num: int):
        cur = 0
        for k in range(self.max_bit, -1, -1):
            bit = (num >> k) & 1
            cur = self.to[bit][cur]
            if cur == -1 or self.cnt[cur] == 0: return 0
        return self.cnt[cur]
    
    # 求与num异或严格小于limit的数量
    def count_limit_xor(self, num: int, limit: int) -> int:
        res = cur = 0
        to, cnt = self.to, self.cnt
        for k in range(self.max_bit, -1, -1):
            bit = (num >> k) & 1
            if limit >> k & 1:
                if to[bit][cur] != -1:
                    res += cnt[to[bit][cur]]
                if to[bit ^ 1][cur] == -1 or cnt[to[bit ^ 1][cur]] == 0:
                    return res
                cur = to[bit ^ 1][cur]
            else:
                if to[bit][cur] == -1 or cnt[to[bit][cur]] == 0:
                    return res
                cur = to[bit][cur]
        return res

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

    # Get min result for constant x ^ element in array
    def min_xor(self, x: int) -> int:
        if self.cnt[0] == 0: return self.inf
        res = cur = 0
        for k in range(self.max_bit, -1, -1):
            bit = (x >> k) & 1
            nxt = self.to[bit][cur]
            if nxt == -1 or self.cnt[nxt] == 0:
                res |= 1 << k
                cur = self.to[bit ^ 1][cur]
            else:
                cur = nxt
        return res
    
    # Get min max result for x ^ element in array
    def min_max(self, res: int, bit: int, cur: int) -> int:
        if bit < 0:
            return res
        if self.to[0][cur] != -1 and self.to[1][cur] != -1:
            return min(self.min_max(res | (1 << bit), bit - 1, self.to[0][cur]), self.min_max(res | (1 << bit), bit - 1, self.to[1][cur]))
        elif self.to[0][cur] != -1:
            return self.min_max(res, bit - 1, self.to[0][cur])
        elif self.to[1][cur] != -1:
            return self.min_max(res, bit - 1, self.to[1][cur])
        
'''
HIGH_BIT = 14

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.sum = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, num: int, diff: int = 1) -> None:
        cur = self.root
        for k in range(HIGH_BIT, -1, -1):
            bit = (num >> k) & 1
            if not cur.children[bit]:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
            # cur.sum += 1
            cur.sum += diff
    
    # Get max result for constant x ^ element in array
    def max_xor(self, x: int) -> int:
        res = 0
        cur = self.root
        for k in range(HIGH_BIT, -1, -1):
            bit = (x >> k) & 1
            if not cur.children[bit ^ 1] or cur.children[bit ^ 1].sum == 0:
                cur = cur.children[bit]
            else:
                res |= 1 << k
                cur = cur.children[bit ^ 1]
        return res

    # Get min result for constant x ^ element in array
    def min_xor(self, x: int) -> int:
        res = 0
        cur = self.root
        for k in range(HIGH_BIT, -1, -1):
            bit = (x >> k) & 1
            if not cur.children[bit] or cur.children[bit].sum == 0:
                res |= 1 << k
                cur = cur.children[bit ^ 1]
            else:
                cur = cur.children[bit]
        return res

    def get(self, num: int, x: int) -> int:
        res = 0
        cur = self.root
        for k in range(HIGH_BIT, -1, -1):
            bit = (num >> k) & 1
            if (x >> k) & 1:
                if cur.children[bit]:
                    res += cur.children[bit].sum
                if not cur.children[bit ^ 1]:
                    return res
                cur = cur.children[bit ^ 1]
            else:
                if not cur.children[bit]:
                    return res
                cur = cur.children[bit]
        res += cur.sum
        return res
'''