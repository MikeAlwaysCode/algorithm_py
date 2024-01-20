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
    a = ints()
    d = ints()
    left, right = list(range(-1, n - 1)), list(range(1, n + 1))
    alive = [True] * n
    ans = [0] * n
    q = set(range(n))
    for i in range(n):
        died = []
        for j in q:
            attack = 0
            if left[j] >= 0:
                attack += a[left[j]]
            if right[j] < n:
                attack += a[right[j]]
            if attack > d[j]:
                alive[j] = False
                died.append(j)
                ans[i] += 1
                
        q.clear()
        for j in died:
            if left[j] >= 0:
                right[left[j]] = right[j]
                if alive[left[j]]:
                    q.add(left[j])
            if right[j] < n:
                left[right[j]] = left[j]
                if alive[right[j]]:
                    q.add(right[j])
        if not q or ans[i] == 0:
            break
    print(*ans)


for _ in range(int(input())):
    solve()
