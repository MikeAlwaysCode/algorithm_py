n = 10 ** 5
times = random.randint(100, 500)
mod = random.getrandbits(32)
powers = [1] * (n + 1)
for i in range(1, n + 1):
    powers[i] = powers[i-1] * times % mod
 
class RollingHash:
    def __init__(self, s):
        self.val = [0]
        for c in s:
            self.val.append((self.val[-1] * times + ord(c)) % mod)
    
    def substr(self, i, j):
        return (self.val[j+1] - self.val[i] * powers[j-i+1]) % mod