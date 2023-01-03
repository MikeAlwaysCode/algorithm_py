N, X, Y, Z = map(int, input().split())
a = map(int, input().split())
b = map(int, input().split())

s = list(zip(range(N), a, b))
if X > 0: s[:] = sorted(s[:], key=lambda p: (-p[1], p[0]))
if Y > 0: s[X:] = sorted(s[X:], key=lambda p: (-p[2], p[0]))
if Z > 0: s[X + Y:] = sorted(s[X+Y:], key=lambda p: (-(p[1] + p[2]), p[0]))
  
if X + Y + Z > 0: s[:X + Y + Z] = sorted(s[:X + Y + Z], key=lambda p: p[0])
  
for p in s[:X + Y + Z]:
  print(p[0] + 1)