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
    if n == 2:
        while nums[0] and nums[1]:
            nums[1] = max(0, nums[1] - nums[0])
            nums[0] = max(0, nums[0] - nums[1])
    elif n == 3:
        while nums[0] and nums[1] and nums[2]:
            nums[1] = max(0, nums[1] - nums[0])
            nums[2] = max(0, nums[2] - nums[1])
            nums[0] = max(0, nums[0] - nums[2])
        for i in range(n):
            if nums[i]:
                nums[(i + 1) % n] = 0
    else:
        # def check() -> bool:
        #     for i in range(n):
        #         if nums[i] and nums[(i + 1) % n] and nums[(i + 2) % n] and nums[(i + 3) % n]:
        #             return True
        #     return False
        # while check():
        while True:
            check = False
            for i in range(n):
                nums[(i + 1) % n] = 0 if nums[(i + 1) % n] <= nums[i] else nums[(i + 1) % n] - nums[i]
                if i > 2 and nums[i] and nums[i - 1] and nums[i - 2] and nums[i - 3]:
                    check = True
            for i in range(3):
                if nums[i] and nums[i - 1] and nums[i - 2] and nums[i - 3]:
                    check = True
            if not check:
                break
        def cal(a: int, b: int) -> int:
            k = b // a
            return (b * 2 - (k + 1) * a) * k // 2
        for i in range(n):
            if not nums[i] and nums[(i + 1) % n]:
                d = cal(nums[(i + 1) % n], nums[(i + 2) % n])
                if i == n - 2:
                    d += nums[0]
                nums[(i + 3) % n] = 0 if nums[(i + 3) % n] <= d else nums[(i + 3) % n] - d
                nums[(i + 2) % n] = 0


    ans = [i + 1 for i, x in enumerate(nums) if x]
    print(len(ans))
    print(*ans)


for _ in range(int(input())):
    solve()
