# 타임 카드 

time = []
times_hour = []
times_min= []
times_sec = []

for i in range(3):
    time.append(list(map(int,input().split())))
    
for i in range(3):
    
    times_hour.append(time[i][3]-time[i][0])
    times_min.append(time[i][4]-time[i][1])
    times_sec.append(time[i][5]-time[i][2])
    
    if times_sec[i] < 0:
        times_sec[i] += 60
        times_min[i] -= 1
        
    if times_min[i] < 0:
        times_min[i] += 60
        times_hour[i] -= 1

    print(times_hour[i], times_min[i], times_sec[i])