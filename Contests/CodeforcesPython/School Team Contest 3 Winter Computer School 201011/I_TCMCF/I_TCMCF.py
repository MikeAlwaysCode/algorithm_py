import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    nums = ints()
    ans = []
    nums.sort()
    i = n - 1
    while i >= 0 and nums[i] > 0:
        ans.append(nums[i])
        i -= 1
    j = 0
    while j < i and nums[j] < 0 and nums[j + 1] < 0:
        ans.append(nums[j])
        ans.append(nums[j + 1])
        j += 2
    if not ans:
        ans.append(nums[i])

    '''
    neg = []
    zero = 0
    for x in nums:
        if x > 0:
            ans.append(x)
        elif x < 0:
            neg.append(x)
        else:
            zero += 1
    neg.sort()
    ans.extend(neg[:len(neg) // 2 * 2])
    if not ans:
        if zero:
            ans.append(0)
        else:
            ans.append(neg[0])
    '''
    print(*ans)


solve()
