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
    s = input()
    cnt0, cnt1 = s.count('0'), s.count('1')
    if cnt0 + cnt1 == len(s):
        print('0' * cnt0 + '1' * cnt1)
    else:
        s = s.replace('1', '')
        j = s.index('2')
        print(s[:j] + '1' * cnt1 + s[j:])

solve()