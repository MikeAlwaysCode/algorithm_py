import sys
from collections import deque

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, q = mint()
    nums = [0] * n
    seen = [False] * n

    parent = list(range(n + 1))
    def find(x: int):
        cur = x
        while x != parent[x]:
            x = parent[x]
        while parent[cur] != x:
            parent[cur], cur = x, parent[cur]
        return x

    def union(x: int, y: int):
        parent[find(x)] = find(y)

    ans = []
    qry = []
    for i in range(1, q + 1):
        a, b, d = mint()
        a -= 1
        b -= 1
        if a == b:
            if d == 0:
                ans.append(i)
        elif not seen[a] and not seen[b]:
            ans.append(i)
            nums[b] = nums[a] - d
            seen[a] = seen[b] = True
            union(a, b)
        elif not seen[a]:
            ans.append(i)
            nums[a] = nums[b] + d
            seen[a] = True
            union(a, b)
        elif not seen[b]:
            ans.append(i)
            nums[b] = nums[a] - d
            seen[b] = True
            union(b, a)
        else:
            fa, fb = find(a), find(b)
            if fa == fb:
                if nums[a] - nums[b] == d:
                    ans.append(i)
            else:
                qry.append((fa, fb, a, b, d, i))

    while qry:
        tmp = qry
        qry = []
        nums2 = [0] * n
        seen = [False] * n
        parent = list(range(n + 1))
        for a, b, oa, ob, d, i in tmp:
            if not seen[a] and not seen[b]:
                ans.append(i)
                nums2[b] = nums2[a] - d
                seen[a] = seen[b] = True
                union(a, b)
            elif not seen[a]:
                ans.append(i)
                nums2[a] = nums2[b] + d
                seen[a] = True
                union(a, b)
            elif not seen[b]:
                ans.append(i)
                nums2[b] = nums2[a] - d
                seen[b] = True
                union(b, a)
            else:
                fa, fb = find(a), find(b)
                if fa == fb:
                    if nums2[fa] + nums[oa] - (nums2[fb] + nums[ob]) == d:
                        ans.append(i)
                else:
                    qry.append((fa, fb, d, i))
    ans.sort()
    print(*ans)

solve()