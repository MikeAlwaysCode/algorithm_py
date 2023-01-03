from collections import Counter, defaultdict

arr = list(map(int, input().split()))
c = list(Counter(arr).values())
c.sort()

if len(c) != 2:
    print("No")
elif c[0] == 2 and c[1] == 3:
    print("Yes")
else:
    print("No")