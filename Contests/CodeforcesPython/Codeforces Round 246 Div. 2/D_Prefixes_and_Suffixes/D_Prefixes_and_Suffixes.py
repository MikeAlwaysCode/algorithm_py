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

# 题做不出来，但过的人很多，请再读一遍题
# 没思路，且没读错题，不妨暴力找找规律
# 没思路，题没读错，暴力也找不到规律，别勉强，不如下班

def solve() -> None:
    s = input()

    # KMP - Prefix function
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    
    # Count for each prefix
    cnt = [0] * (n + 1)
    for i in range(n):
        # The number of occurrences of each prefix
        cnt[pi[i]] += 1
    for i in range(n - 1, 0, -1):
        # Prefix i also contain the surfix of prefix pi[i - 1]
        cnt[pi[i - 1]] += cnt[i]
    for i in range(n + 1):
        # Finally add the prefix itself
        cnt[i] += 1
    
    # Calculate the result
    ans = []
    i = n
    while i:
        ans.append((i, cnt[i]))
        i = pi[i - 1]
    ans.reverse()
    print(len(ans))
    for x, y in ans:
        print(x, y)

solve()