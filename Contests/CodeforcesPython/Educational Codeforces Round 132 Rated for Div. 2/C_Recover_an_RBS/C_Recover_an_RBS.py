t = int(input())
'''
for _ in range(t):
    s = str(input())

    stack = list()
    count = 0

    for x in s:
        if x == '?':
            count += 1
            
        if x == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(x)
            
    if len(stack) <= 2 or count <= 2:
        print("YES")
    else:
        print("NO")
'''

O = []
for _ in range(t):
    S = input()
    N = len(S)
    A = [(0, 0)] * N
    lo = hi = 0
    for i in range(N-1, -1, -1):
        c = S[i]
 
        if c == ")":
            lo += 1; hi += 1
        elif c == "(":
            lo -= 1; hi -= 1
        else:
            lo -= 1; hi += 1
 
        lo = max(lo, 0)
        assert lo <= hi, (lo, hi)
 
        A[i] = (lo, hi)
 
    open = 0
    for i, c in enumerate(S[:N-1]):
        if c == "(":
            open += 1
        elif c == ")":
            open -= 1
        else:
            lo, hi = A[i+1]
            if lo <= open + 1 <= hi and lo <= open - 1 <= hi:
                O.append("NO")
                break
 
            if lo <= open + 1 <= hi:
                open += 1
            else:
                open -= 1
 
        assert open >= 0
    else:
        O.append("YES")
 
print("\n".join(O))