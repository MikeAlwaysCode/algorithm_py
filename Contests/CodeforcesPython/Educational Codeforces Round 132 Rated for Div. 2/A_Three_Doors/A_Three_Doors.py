t = int(input())

for _ in range(t):
    x = int(input())
    a = list(map(int, input().split()))

    y = a[x-1]
    if y == 0:
        print("NO")
        continue

    z = a[y-1]
    if z == 0:
        print("NO")
        continue

    print("YES")
