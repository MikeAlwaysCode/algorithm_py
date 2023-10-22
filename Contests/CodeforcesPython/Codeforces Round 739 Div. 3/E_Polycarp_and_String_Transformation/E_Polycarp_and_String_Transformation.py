import sys
from collections import Counter

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

def solve() -> None:
    t = input()
    cnt = Counter(t)
    n = len(cnt)
    ans = []
    s = Counter()
    curr = Counter()
    nc = ''
    m = 0
    for i in range(len(t) - 1, -1, -1):
        if s[t[i]] == 0:
            if nc or cnt[t[i]] % (n - len(ans)):
                print(-1)
                return
            nc = t[i]
            s[nc] = cnt[nc] // (n - len(ans))
            m += s[nc]
            if s[nc] > 1:
                curr[nc] = s[nc] - 1
        else:
            curr[t[i]] -= 1
            if curr[t[i]] < 0:
                print(-1)
                return
            elif curr[t[i]] == 0:
                del curr[t[i]]
        if not curr and nc:
            ans.append(nc)
            nc = ''
            curr = s.copy()
    
    ans.reverse()
    fr, to = 0, m
    for c in ans:
        j = to
        for i in range(fr, to):
            if t[i] == c: continue
            if t[i] != t[j]:
                print(-1)
                return
            j += 1
        fr, to = to, j

    print(t[:m], "".join(ans))


for _ in range(int(input())):
    solve()