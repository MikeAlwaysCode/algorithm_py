class PoisonedApples:
    def buy(self, B, A, P):
        if P == 0:
            res = [0] * B
        elif A >= ( 10 ** (B - 1) ):
            res = []
            for i in range(B):
                res.append(10 ** i)
        else:
            tot = 0
            res = []
            for i in range(B):
                cur = tot + 1
                res.append(cur)
                tot += cur
            if cur > A:
                res.clear()
        
        return tuple(res)
        
