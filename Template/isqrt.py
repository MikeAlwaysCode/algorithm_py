def isqrt(n):
    """
    Return the integer part of the square root of the input.
    """
    if n < 0:
        # raise ValueError("isqrt() argument must be nonnegative")
        return -1
    if n == 0:
        return 0
    c = (n.bit_length() - 1) // 2
    a = 1
    d = 0
    for s in reversed(range(c.bit_length())):
        # Loop invariant: (a-1)**2 < (n >> 2*(c - d)) < (a+1)**2
        e = d
        d = c >> s
        a = (a << d - e - 1) + (n >> 2*c - e - d + 1) // a
    return a - (a*a > n)
