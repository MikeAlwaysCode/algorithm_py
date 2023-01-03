import sys

N = int(input())
V = int(input())
B = float(input())

grid = [[-1 for x in range(N)] for y in range(N)]
for r in range(N):
	for c in range(N):
		grid[r][c] = int(input())

# java -jar tester.jar -exec "python DiceRoller.py" -seed 1
# java -jar tester.jar -exec "python DiceRoller.py" -seed 1 -novis -N 30 -V 9
# log = open("log.txt", mode = "a", encoding = "utf-8")
# The grid size N is chosen between 6 and 30, inclusive.
# The maximum cell value V is chosen between 3 and 9, inclusive.
# The negation probability P is chosen between 0.05 and 0.3, inclusive.
# The bonus multiplier B is chosen between 1.0 and 1.2, inclusive.
# Each cell of the grid is filled with a value between 1 and V, inclusive.
# With probability P the number in a cell is made negative.
# All values are chosen uniformly at random.

#print random face values
# for i in range(6): print(((i%V)+1))
# top, bottom, front, back, left and right
dice = [V, V, V, V, V, V]
for i in range(6): print(dice[i])

#move in a spiral
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dir = 0

r = 0
c = 0

seen = []
print(N*N);
for i in range(N*N):
	print(str(r)+" "+str(c))
	seen.append((r,c))
	r2=r+dr[dir]
	c2=c+dc[dir]
	if r2<0 or r2>=N or c2<0 or c2>=N or (r2,c2) in seen:
		dir=(dir+1)%4
		r2=r+dr[dir]
		c2=c+dc[dir]        
	
	r=r2
	c=c2 

sys.stdout.flush()