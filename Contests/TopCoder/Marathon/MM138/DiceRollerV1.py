import sys
from collections import defaultdict

N = int(input())
V = int(input())
B = float(input())

grid = [[-1 for x in range(N)] for y in range(N)]
for r in range(N):
	for c in range(N):
		grid[r][c] = int(input())

# java -jar tester.jar -exec "python DiceRoller.py" -seed 1
# java -jar tester.jar -exec "python DiceRoller.py" -seed 1 -novis -N 30 -V 9
# java -jar tester.jar -exec "python DiceRoller.py" -seed 1 -delay 10 -N 15 -V 7
# log = open("log.txt", mode = "a", encoding = "utf-8")

#print random face values
# for i in range(6): print(((i%V)+1))
# top, bottom, front, back, left and right
# dice = [V-2, V-1, V, V-2, V-1, V]
# dice = [V-2, V, V-1, V-2, V, V-1]
# dice = [V, V, V, V, V, V]

vcount = defaultdict(int)
for row in grid:
	for v in row:
		# if v < 0:
		# 	vcount[-v] -= 1
		# else:
		# 	vcount[v] += 1
		if v > 0:
			vcount[v] += v

keys = list(sorted(vcount.items(), key = lambda x:x[1]))

# dice = [keys[-1][0], keys[-2][0], keys[-3][0], keys[-1][0], keys[-2][0], keys[-3][0]]
dice = [keys[-1][0], keys[-1][0], keys[-1][0], keys[-1][0], keys[-1][0], keys[-1][0]]

for i in range(6): print(dice[i])

# 滚动的六面值变动, 新的bottom值 dice[1] = dice[roll[dir][1]]
roll = [(4, 5, 2, 3, 1, 0), (3, 2, 0, 1, 4, 5), (5, 4, 2, 3, 0, 1), (2, 3, 1, 0, 4, 5)]

#move in a spiral
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dir = 0

r = 0
c = 0
# r = N // 2
# c = N // 2

'''
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
'''
'''
steps = []
nextStep = list()

# 第一个坐标点先不做优化
steps.append((r, c))
ob, turn = 0, 0
# print("=================================================================================", file = log)

while True:
	# 下一个坐标
	# r2 = r + dr[dir]
	# c2 = c + dc[dir]

	nextStep.clear()
	for d in range(3, 6):
		ndir = (dir + d) % 4
		r2 = r + dr[ndir]
		c2 = c + dc[ndir]
		
		bottom = dice[roll[ndir][1]]

		if r2 < 0 or r2 >= N or c2 < 0 or c2 >= N or (r2, c2) in steps:
			# 不在范围内
			continue
		
		if grid[r2][c2] + bottom == 0:
			value = 0
		elif grid[r2][c2] == bottom:
			value = 3
		elif ndir == 0:
			value = 2
		else:
			value = 1

		nextStep.append((ndir, value))
	
	if not nextStep:
		break

	nextStep.sort(key = lambda x: x[1])

	dir = nextStep[-1][0]

	# # 不在范围内换方向
	# if r2 < 0 or r2 >= N or c2 < 0 or c2 >= N or (r2, c2) in steps:
	# 	dir = (dir + 1) % 4
	# 	ob += 1
	# 	turn += 1

	# 	# 4个方向都没路
	# 	if ob >= 4:
	# 		break

	# 	continue

	# # 当前六个面都是V
	# bottom = dice[roll[dir][1]]
	# # bottom = V

	# # 下一个格子是负数且绝对值和骰子下一个底一样, 4个方向都一样就原方向走
	# if grid[r2][c2] < 0 and grid[r2][c2] + bottom == 0:
	# 	if turn < 4:
	# 		# print("r2:",r2,"c2:",c2,"V:",grid[r2][c2],"dir:",dir,"bottom:",bottom, file = log)
	# 		# print("dice:",dice, file = log)
	# 		dir = (dir + 1) % 4
	# 		turn += 1
	# 		continue
	# 	# elif len(steps) * 3 > N * N * 2:
	# 	# 	break

	r = r + dr[dir]
	c = c + dc[dir]

	# 骰子值变换
	dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[roll[dir][0]], dice[roll[dir][1]], dice[roll[dir][2]], dice[roll[dir][3]], dice[roll[dir][4]], dice[roll[dir][5]]

	steps.append((r, c))
		
	# # 刚因为-V转向则再转一次,这个策略可以继续优化,估计要一次性判断4个方向
	# if turn > 0 and ob == 0:
	# 	dir = (dir + 1) % 4
	# 
	# ob, turn = 0, 0
'''
def diceRoll(tdir: int) -> None:
	# 骰子值变换
	dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[roll[tdir][0]], dice[roll[tdir][1]], dice[roll[tdir][2]], dice[roll[tdir][3]], dice[roll[tdir][4]], dice[roll[tdir][5]]


def hasRoad(i: int, j: int, tdir: int) -> int:
	count = 0
	for d in range(4, 6):
		ntdir = (tdir + d) % 4
		ni = i + dr[ntdir]
		nj = j + dc[ntdir]

		if ni < 0 or ni >= N or nj < 0 or nj >= N or (ni, nj) in steps:
			# 不在范围内
			continue
		
		count += 1
	
	return count

steps = []
steps.append((r, c))

turn = False

while True:
	# 前面绕路则左边有路
	ndir = (dir + 3) % 4
	r2 = r + dr[ndir]
	c2 = c + dc[ndir]

	bottom = dice[roll[ndir][1]]
	if r2 >= 0 and r2 < N and c2 >= 0 and c2 < N and (r2, c2) not in steps and grid[r2][c2] + bottom != 0:
		# 前面不是死路
		rc2 = hasRoad(r2, c2, ndir)
		# if (( r2 == 0 or r2 == N-1 or c2 == 0 or c2 == N-1 ) and rc2 > 0 ) or rc2 > 1:
		# if rc2 > 0 and turn:
		if rc2 > 0 and not turn:
			# turn -= 1
			dir = ndir
			r = r2
			c = c2
			diceRoll(dir)
			steps.append((r, c))
			continue

	rc = hasRoad(r, c, dir)
	if rc == 0:
		break

	turn = False

	# 下一个坐标
	r2 = r + dr[dir]
	c2 = c + dc[dir]

	rc2 = hasRoad(r2, c2, dir)
	
	# print("r:",r,"c:",c,"rc:",rc, "rc2:", rc2, "dir:", dir, file = open("log.txt", mode = "a", encoding = "utf-8"))
	# if rc2 <= 1 and rc > 1:
		# print("turn", file = open("log.txt", mode = "a", encoding = "utf-8"))
	
	if r2 < 0 or r2 >= N or c2 < 0 or c2 >= N or (r2, c2) in steps:
		# 不在范围内
		dir = (dir + 1) % 4
		continue
	
	ndir = (dir + 1) % 4
	r3 = r2 + dr[ndir]
	c3 = c2 + dc[ndir]
	# if rc2 <= 1 and rc > 1 and r2 != 0 and r2 != N-1 and c2 != 0 and c2 != N-1:
	if rc2 <= 1 and rc > 1 and (r3, c3) in steps:
		# 中间死胡同
		dir = (dir + 1) % 4
		turn = True
		continue

	# 下一个格子是负数且绝对值和骰子下一个底一样
	if grid[r2][c2] + V == 0:
		ndir = (dir + 1) % 4
		
		r3 = r + dr[ndir]
		c3 = c + dc[ndir]

		bottom = dice[roll[ndir][1]]
		if r3 >= 0 and r3 < N and c3 >= 0 and c3 < N and (r3, c3) not in steps and grid[r3][c3] + bottom != 0:
			# 绕过去
			# turn = 2
			dir = ndir
			r = r3
			c = c3
			diceRoll(dir)
			steps.append((r, c))
			continue
		
			
			# r3 = r3 + dr[dir]
			# c3 = c3 + dc[dir]

			# if r3 >= 0 and r3 < N and c3 >= 0 and c3 < N and (r3, c3) not in steps and grid[r3][c3] + V != 0:
			# 	steps.append((r3, c3))
	
	r = r2
	c = c2
	diceRoll(dir)

	steps.append((r, c))

print(len(steps))

for step in steps:
    print(str(step[0]) + " " + str(step[1]))
    # print(str(step[0]) + " " + str(step[1]), file = log)

sys.stdout.flush()