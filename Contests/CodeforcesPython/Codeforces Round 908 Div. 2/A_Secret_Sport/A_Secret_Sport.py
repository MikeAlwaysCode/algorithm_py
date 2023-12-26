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
    n = sint()
    s = input()
    for x in range(1, n + 1):
        cnt0 = cnt1 = 0
        win0 = win1 = 0
        last = -1
        for c in s:
            if c == 'A':
                cnt0 += 1
            else:
                cnt1 += 1
            if cnt0 >= x:
                win0 += 1
                cnt0 = cnt1 = 0
                last = 0
            elif cnt1 >= x:
                win1 += 1
                cnt0 = cnt1 = 0
                last = 1
        if cnt0 or cnt1:
            continue
        if win0 == win1:
            continue
        if win0 > win1 and last == 0:
            print('A')
            return
        if win0 < win1 and last == 1:
            print('B')
            return
    print('?')


for _ in range(int(input())):
    solve()
