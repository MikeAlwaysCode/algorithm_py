from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = str(input())

    a, b = 0, 0
    for x in s:
        if x == '0':
            a += 1
        else:
            b += 1

    # ans = abs(( a + k - 1 ) // k - ( b + k - 1 ) // k)
    # if ans == 0 and a != b: ans = 1

    if a == b:
        ans = 0
    elif k == 1:
        ans = abs(a - b)
    elif a == 0 or b == 0:
        ans = (abs(a - b) + k - 1) // k
    else:
        ans = (abs(a - b) + k - 2) // (k - 1)
    
    print(ans)