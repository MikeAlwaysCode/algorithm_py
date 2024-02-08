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
    n = int(input())
    s = input()
    if n & 1:
        print(-1)
        return
    
    cnt = [0] * 26
    diff = [0] * 26
    same = 0
    i, j = 0, n - 1
    while i < j:
        if s[i] == s[j]:
            diff[ord(s[i]) - 97] += 1
            same += 1
        cnt[ord(s[i]) - 97] += 1
        cnt[ord(s[j]) - 97] += 1
        if cnt[ord(s[i]) - 97] * 2 > n or cnt[ord(s[j]) - 97] * 2 > n:
            print(-1)
            return
        i += 1
        j -= 1
    
    print(max(max(diff), (same + 1) // 2))

for _ in range(int(input())):
    solve()