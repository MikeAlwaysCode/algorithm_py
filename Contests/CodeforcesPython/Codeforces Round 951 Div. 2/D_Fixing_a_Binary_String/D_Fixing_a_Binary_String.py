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

def solve() -> None:
    n, k = mint()
    s = input()
    pref = [-1] * n
    suff = [False] * n
    p = ''
    cnt = k
    for i in range(n):
        if s[i] != p:
            if cnt != k:
                break
            p, cnt = s[i], 1
        else:
            cnt += 1
        if cnt > k:
            break
        pref[i] = cnt
    if pref[-1] == k:
        print(n)
        return
    j = n - 1
    suff[-1] = True
    while j > n - k and s[j - 1] == s[-1]:
        j -= 1
        suff[j] = True
    p = s[j]
    cnt = k
    for i in range(j - 1, 0, -1):
        if s[i] != p:
            if cnt != k:
                break
            p, cnt = s[i], 1
        else:
            cnt += 1
        if cnt > k:
            break
        elif cnt == k:
            if pref[i - 1] != -1 and ((pref[i - 1] == k and n - j == k and s[-1] != s[i - 1]) or (pref[i - 1] + n - j == k and s[-1] == s[i - 1])):
                print(i)
                return
    print(-1)


for _ in range(int(input())):
    solve()
