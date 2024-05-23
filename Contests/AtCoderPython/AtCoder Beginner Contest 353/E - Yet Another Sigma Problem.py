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

class Trie:
    def __init__(self):
        self.children = dict()
        self.cnt = 0

    def insert(self, word: str) -> int:
        node = self
        res = 0
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
            res += node.cnt
            node.cnt += 1
        return res

def solve() -> None:
    n = sint()
    s = input().split()
    trie = Trie()
    ans = 0
    for w in s:
        ans += trie.insert(w)
    print(ans)

solve()
