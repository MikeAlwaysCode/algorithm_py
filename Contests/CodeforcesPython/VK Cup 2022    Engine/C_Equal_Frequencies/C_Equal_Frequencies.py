import sys
from collections import Counter
from string import ascii_lowercase

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
    n = sint()
    s = list(input())
    cnt = Counter(s)
    v = sorted(cnt.items(), key = lambda x: -x[1])
    ans, o = n, 1
    for m in range(1, 27):
        if n % m:
            continue
        cur, k = 0, n // m
        for i in range(min(m, len(v))):
            cur += max(0, k - v[i][1])
        if len(v) < m:
            cur += (m - len(v)) * k
        if cur < ans:
            ans, o = cur, m
    
    if ans:
        k = n // o
        more = [0] * 26
        less = [0] * 26
        for i in range(len(v)):
            if i >= o or v[i][1] > k:
                more[ord(v[i][0]) - 97] += v[i][1] - k
            elif v[i][1] < k:
                less[ord(v[i][0]) - 97] += k - v[i][1]

        if len(v) < o:
            for c in ascii_lowercase:
                if cnt[c] == 0:
                    less[ord(c) - 97] += k
                    o -= 1
                    if o == len(v):
                        break
        i = 0
        for j, c in enumerate(s):
            if more[ord(c) - 97]:
                while i < 26 and less[i] == 0:
                    i += 1
                s[j] = ascii_lowercase[i]
                more[ord(c) - 97] -= 1
                less[i] -= 1

    print(ans)
    print("".join(s))


for _ in range(int(input())):
    solve()
