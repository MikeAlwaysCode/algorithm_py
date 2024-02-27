import sys

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

class Trie:
    def __init__(self):
        self.children = dict()
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
    
def solve() -> None:
    n = sint()
    s = []
    trie = Trie()
    for _ in range(n):
        s.append(input())
        trie.insert(s[-1])
    
    ans = [0] * n

    for i, w in enumerate(s):
        for j in range(1, len(w)):
            if trie.search(w[:j]) and trie.search(w[j:]):
                ans[i] = 1
                break

    print(*ans, sep='')


for _ in range(int(input())):
    solve()
