import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    p = ints()
    s = input()

    def count(d: int) -> int:
        cnt = 0
        seen = [False] * n
        seen[p[0] - 1] = True
        for i in p[1:]:
            i -= 1
            if s[i] == '?' and seen[(i + d) % n]:
                cnt += 1
            elif s[i] != '?' and not seen[(i + d) % n]:
                cd = 1 if s[i] == 'L' else -1
                if cd != d:
                    return 0
            seen[i] = True
        return pow(2, cnt, MOD)
    
    ans = 0
    if s[p[0] - 1] == 'L' or s[p[0] - 1] == '?':
        ans += count(1)
    if s[p[0] - 1] == 'R' or s[p[0] - 1] == '?':
        ans += count(-1)
    print(ans % MOD)

solve()
