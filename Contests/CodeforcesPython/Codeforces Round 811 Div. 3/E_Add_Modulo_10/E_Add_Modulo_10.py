def check1(n: int, arr: list[int]) -> bool:
    for i in range(n):
        arr[i] += arr[i] % 10
        if i > 0 and arr[i] != arr[i-1]:
            return False
    return True
    
def check2(n: int, arr: list[int]) -> bool:
    for i in range(n):
        while arr[i] % 10 != 2:
            arr[i] += arr[i] % 10
        if i > 0 and abs(arr[i] - arr[i-1]) % 20 != 0:
            return False
    return True

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    type1, type2 = False, False

    for a in arr:
        if a % 5 == 0:
            type1 = True
        else:
            type2 = True
    
    chk = False
    if type1 and type2:
        chk = False
    elif type1:
        chk = check1(n, arr)
    elif type2:
        chk = check2(n, arr)
    print('Yes' if chk else 'No')

t = int(input())
for _ in range(t):
    solve()