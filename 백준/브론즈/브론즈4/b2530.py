# 인공지능 시계

hour, min, sec = map(int,input().split())
D = int(input())

sec += D 

while sec >= 60:
    min += 1 
    sec -= 60 

while min >= 60:
    hour += 1
    min -= 60
while hour >= 24:
    hour -= 24
    
print(hour, min, sec)