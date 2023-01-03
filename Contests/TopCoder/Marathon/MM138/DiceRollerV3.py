import sys

N = int(input())
V = int(input())
B = float(input())

grid = [[-1 for x in range(N)] for y in range(N)]
for r in range(N):
	for c in range(N):
		grid[r][c] = int(input())

last_best_sides = []

# java -jar tester.jar -exec "python DiceRoller.py" -seed 1
# java -jar tester.jar -exec "python DiceRoller.py" -seed 1 -novis -N 30 -V 9
# log = open("log.txt", mode = "a", encoding = "utf-8")

#print random face values
# for i in range(6): print(((i%V)+1))
# top, bottom, front, back, left and right
# dice = [V-2, V-1, V, V-2, V-1, V]
# dice = [V-2, V, V-1, V-2, V, V-1]
dice = [V, V, V, V, V, V]

# 滚动的六面值变动, 新的bottom值 dice[1] = dice[roll[dir][1]]
roll = [(4, 5, 2, 3, 1, 0), (3, 2, 0, 1, 4, 5), (5, 4, 2, 3, 0, 1), (2, 3, 1, 0, 4, 5)]

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
'''
steps = []

# 第一个坐标点先不做优化
steps.append((r, c))
ob, turn = 0, 0
# print("=================================================================================", file = log)

while True:
	# 下一个坐标
	r2 = r + dr[dir]
	c2 = c + dc[dir]

	# 不在范围内换方向
	if r2 < 0 or r2 >= N or c2 < 0 or c2 >= N or (r2, c2) in steps:
		dir = (dir + 1) % 4
		ob += 1
		turn += 1

		# 4个方向都没路
		if ob >= 4:
			break

		continue

	# 当前六个面都是V
	bottom = dice[roll[dir][1]]
	# bottom = V

	# 下一个格子是负数且绝对值和骰子下一个底一样, 4个方向都一样就原方向走
	if grid[r2][c2] < 0 and grid[r2][c2] + bottom == 0:
		if turn < 4:
			# print("r2:",r2,"c2:",c2,"V:",grid[r2][c2],"dir:",dir,"bottom:",bottom, file = log)
			# print("dice:",dice, file = log)
			dir = (dir + 1) % 4
			turn += 1
			continue
		# elif len(steps) * 3 > N * N * 2:
		# 	break

	ob, turn = 0, 0

	r = r + dr[dir]
	c = c + dc[dir]

	# 骰子值变换,暂时没用上
	dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[roll[dir][0]], dice[roll[dir][1]], dice[roll[dir][2]], dice[roll[dir][3]], dice[roll[dir][4]], dice[roll[dir][5]]

	# 刚因为-V转向则再转一次,这个策略可以继续优化,估计要一次性判断4个方向
	if turn > 0 and ob == 0:
		dir = (dir + 1) % 4
		continue

	steps.append((r, c))

print(len(steps))
'''

# 输出结果
for s in last_best_sides: print(s)
for step in steps:
    print(str(step[0]) + " " + str(step[1]))
    # print(str(step[0]) + " " + str(step[1]), file = log)

sys.stdout.flush()