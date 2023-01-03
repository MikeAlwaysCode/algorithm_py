class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = []
        n = len(s)

        for i in range(numRows):
            if i > n - 1:
                break
            
            curPos = i

            while curPos < n:
                if i > 0 and i < numRows - 1 and curPos > i:
                    midPos = curPos - 2 * i
                    if midPos < n:
                        res.append(s[midPos])

                res.append(s[curPos])

                curPos += 2 * numRows - 2

                if i > 0 and i < numRows - 1 and curPos >= n:
                    midPos = curPos - 2 * i
                    if midPos < n:
                        res.append(s[midPos])
            
        return ''.join(res)

    def convert2(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2
        ans = []
        for i in range(r):  # 枚举矩阵的行
            for j in range(0, n - i, t):  # 枚举每个周期的起始下标
                ans.append(s[j + i])  # 当前周期的第一个字符
                if 0 < i < r - 1 and j + t - i < n:
                    ans.append(s[j + t - i])  # 当前周期的第二个字符
        return ''.join(ans)