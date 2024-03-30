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
    t = input()
    s0 = s.count('0')
    s1 = len(s) - s0
    t0 = t.count('0')
    t1 = len(t) - t0
    if s0 < t0 or s1 < t1:
        print(s)
        return
    
    n = len(t)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and t[i] != t[j]:
            j = pi[j - 1]
        if t[i] == t[j]:
            j += 1
        pi[i] = j

    ans = [t]
    s0 -= t0
    s1 -= t1
    left = t[pi[-1]:]
    t0 = left.count('0')
    t1 = len(left) - t0
    while s0 >= t0 and s1 >= t1:
        ans.append(left)
        s0 -= t0
        s1 -= t1
    if s0:
        ans.append('0' * s0)
    if s1:
        ans.append('1' * s1)
    print("".join(ans))


solve()
