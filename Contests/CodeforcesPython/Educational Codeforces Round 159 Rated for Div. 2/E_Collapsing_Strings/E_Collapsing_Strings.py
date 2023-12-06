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
        self.to = [[-1] for _ in range(26)]
        self.cnt = [0]

    def insert(self, word: str) -> None:
        cur = 0
        for c in word:
            c = ord(c) - 97
            if self.to[c][cur] == -1:
                self.to[c][cur] = len(self.cnt)
                for i in range(26):
                    self.to[i].append(-1)
                self.cnt.append(0)
            cur = self.to[c][cur]
            self.cnt[cur] += 1

    def search(self, word: str) -> int:
        res = 0
        cur = 0
        for c in word:
            c = ord(c) - 97
            if self.to[c][cur] == -1:
                return res
            cur = self.to[c][cur]
            res += self.cnt[cur]
        return res

def solve() -> None:
    n = sint()
    ans = tot = 0
    s = []
    trie = Trie()
    for _ in range(n):
        s.append(input())
        tot += len(s[-1])
        trie.insert(s[-1][::-1])
    for word in s:
        cnt = trie.search(word)
        ans += tot + len(word) * n - cnt * 2
    print(ans)

solve()