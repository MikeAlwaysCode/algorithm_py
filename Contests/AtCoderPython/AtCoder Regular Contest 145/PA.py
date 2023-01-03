N = int(input())
S = str(input())
if N == 2:
    chk = S[0] == S[1]
else:
    chk = S[0] == 'B' or S[-1] == 'A'
if chk: print("Yes")
else: print("No")
'''
s = list(S)
if s[0] == 'A' and s[N-1] == 'B':
    print("No")
elif N&1:
    print("Yes")
else:
    j = N // 2
    i = j - 1
    chk = False
    while i >= 0 and j < N:
        if s[i] == 'A' or s[j] == 'B':
            chk = True
        i -= 1
        j += 1
    if chk: print("Yes")
    else: print("No")
'''
# i, j = 0, N-1
# chk = True
# mid = ( N - 1 ) // 2
# while i < j:
#     if s[i] != s[j]:
#         if s[i] == 'A':
#             if i <= 0 or j >= N-1:
#                 chk = False
#                 break
#         elif j > i + 1: # B ... A  BAA
#             k = j - 1
#             l = i + 1
#             exist = False
#             while l < k:
#                 if s[k] == 'B' or s[l] == 'A':
#                     exist = True
#                     j = k - 1
#                     i = l + 1
#                     break
#                 k -= 1
#                 l += 1
#             if exist:
#                 continue
#             elif N & 1:
#                 break
#             else:
#                 chk = False
#                 break
#         else:
#             chk = False
#             break
#     i += 1
#     j -= 1
    
# if chk: print("Yes")
# else: print("No")