t = int(input())

for _ in range(t):
    n, h, m = map(int, input().split())
    alarms = []
    for i in range(n):
        a, b = map(int, input().split())
        alarms.append((a, b))

    alarms.sort()
    chk = False
    for alarm in alarms:
        if alarm[0] > h or ( alarm[0] == h and alarm[1] >= m ):
            chk = True
            rh = alarm[0] - h
            rm = alarm[1] - m
            break
    
    if not chk:
        rh = alarms[0][0] - h + 24
        rm = alarms[0][1] - m
    # print(rh, rm)
    if rm < 0:
        rm += 60
        rh -= 1
    
    print(rh, rm)