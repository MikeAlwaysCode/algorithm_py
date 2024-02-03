import sys
from collections import Counter
# from string import ascii_lowercase

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

MX = (1 << 26) - 1

def solve() -> None:
    n = int(input())
    ans = 0
    
    f = Counter()
    ext = [0] * n
    mask = [0] * n
    for j in range(n):
        s = input()
        for c in s:
            b = 1 << (ord(c) - 97)
            mask[j] ^= b
            ext[j] |= b
        # cnt = Counter(s)
        # maske = masks = 0
        # for i, c in enumerate(ascii_lowercase):
        #     if cnt[c]:
        #         maske |= 1 << i
        #     if cnt[c] & 1:
        #         masks |= 1 << i
        # ext[j] = maske
        # mask[j] = masks
        
    # for i, c in enumerate(ascii_lowercase):
    for i in range(26):
        for j in range(n):
            if ext[j] >> i & 1: continue
            ans += f[MX ^ mask[j] ^ (1 << i)]
            f[mask[j]] += 1
        
        f.clear()
        # for j in range(n):
        #     if ext[j] >> i & 1: continue
        #     f[mask[j]] -= 1

    '''
    cnt = [collections.Counter() for _ in range(26)]
    for _ in range(n):
        s = input()
        cc = collections.Counter(s)
        masks = 0
        for i, c in enumerate(ascii_lowercase):
            if cc[c] & 1:
                masks |= 1 << i
        
        maskt = MX ^ masks
        for i, c in enumerate(ascii_lowercase):
            if cc[c]: continue
            ans += cnt[i][maskt ^ (1 << i)]
            cnt[i][masks] += 1
    '''

    print(ans)


solve()
