from collections import Counter, defaultdict
# from sortedcontainers import SortedList

def solve() -> None:
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    mind, idx = 2 ** 31, -1
    for i, d in enumerate(arr):
        if d >= mind or y == 0:
            break
        y -= 1
        arr[i] = d ^ x
        if arr[i] < mind:
            mind = arr[i]
            idx = i
    if y&1:
        arr[idx] = arr[idx] ^ x
    arr.sort()
    print(*arr)

    # ans = SortedList(arr)

    # while y > 0:
    #     y -= 1
    #     d = ans.pop(0)
    #     ans.add(d^x)

    # print(*ans)

t = int(input())
for _ in range(t):
    solve()