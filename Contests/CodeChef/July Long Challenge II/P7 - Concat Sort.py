# cook your dish here
a, b = [], []
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    # print(n)
    res = True
    
    a.clear()
    b.clear()
    a.append(arr[0])
    for i in range(1, n):
        if arr[i] < a[-1]:
            # print(arr[i], a[-1])
            if b and arr[i] < b[-1]:
                res = False
                break
            b.append(arr[i])
        else:
            a.append(arr[i])

    if not res:
        print("NO")
        continue
        
    if not b:
        print("YES")
        continue

    # print(a)
    # print(b)
    
    # minq = b[0]
    for i in range(len(a)):
        if a[i] >= b[-1]:
            break
        # elif a[i] > minq:
        elif a[i] > b[0]:
            res = False
            break
        # else:
        #     minq = a[i]

    # s = sorted(zip(arr, range(n)))
    # print(s)

    if res:
        print("YES")
    else:
        print("NO")
