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


class TrieNode:
    def __init__(self, val):
        self.val = val
        self.map = dict()


class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        root = TrieNode(0)
        
        def insert(s: str) -> None:
            node = root
            for c in s:
                if c not in node.map:
                    node.map[c] = TrieNode(0)
                node = node.map[c]
                node.val += 1
        
        def find(s: str) -> int:
            ans = 0
            node = root
            for c in s:
                node = node.map[c]
                ans += node.val
            return ans
        
        for word in words:
            insert(word)
        n = len(words)
        ans = [0] * n
        for i, word in enumerate(words):
            ans[i] = find(word)
        # print(ans)
        return ans
