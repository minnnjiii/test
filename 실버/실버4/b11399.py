# ATM
# 백준_11399번

# ATM앞에 N명의 사람들이 줄을 서있다. 
# 사람은 1번부터 N번까지 번호가 매겨져 있으며, 
# i번 사람이 돈을 인출하는데 
# 걸리는 시간은 Pi분이다.

n = int(input()) 

time = list(map(int,input().split())) 

time.sort() 

times = []
for i in range(n) : 
    times.append(time[i]*(n-i))


print(sum(times))

'''
1 
1 2 
1 2 3 
1 2 3 3 
1 2 3 3 4 
'''
