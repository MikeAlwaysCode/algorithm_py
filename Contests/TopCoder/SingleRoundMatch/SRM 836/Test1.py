class IntersectionArea:
    def addOne(self, X1, Y1, X2, Y2, A):
        MX = 10 ** 6
        n = len(X1)

        def getAns(x, y, xt, yt):
            if A == 0:
                return (xt, yt, MX, MX)
            a = xt-x
            b = -1
            while a > 0:
                if A % a == 0:
                    b = A // a
                    break
                a -= 1
            if b == -1 or b > yt - y:
                return ()
            else:
                return (x, y, x+a, y+b)

        if n == 0:
            return getAns(0, 0, MX, MX)
        
        xn = yn = 0
        xm = ym = MX
        for i in range(n):
            xn = max(xn, X1[i])
            yn = max(yn, Y1[i])
            xm = min(xm, X2[i])
            ym = min(ym, Y2[i])
        
        area = (xm - xn) * (ym - yn)
        if area < A:
            return ()
        elif area == A:
            return (xn, yn, xm, ym)
        else:
            return getAns(xn, yn, xm, ym)
        
def main():
    x1 = [0]
    y1 = [5]
    x2 = [15]
    y2 = [10]
    A = 25
    sol = IntersectionArea()

    print(sol.addOne(x1, y1, x2, y2, A))

if __name__ == '__main__':
    main()