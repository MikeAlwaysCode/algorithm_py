from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    c = Counter(arr)

    s = list(c.items())
    s.sort()
    # print(s)

    ans, preCount = 0, 0
    for num in s:
        ans = max(ans, ans + (num[1] + preCount - num[0] * ans + num[0] - 1) // num[0])
        preCount += num[1]
    print(ans)