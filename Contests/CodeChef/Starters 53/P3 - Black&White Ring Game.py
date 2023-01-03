from collections import Counter, defaultdict

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = Counter(arr).most_common(1)[0][1]

    if cnt * 2 > n:
        me = cnt * 2 - n
    else:
        me = 0
    
    ce = 0
    for i in range(n):
        if arr[i] == arr[i-1]:
            ce += 1
    
    # print(ce, me)
    if ((ce - me) // 2) & 1:
        print("Alice")
    else:
        print("Bob")
    
t = int(input())
for _ in range(t):
    solve()