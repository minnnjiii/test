# 전자레인지
# 14470번


'''
💡 문제 

a도의 고기를 b도까지 데우려고 함 
고기는 온도가 0도보다 낮을 때 얼어 있고 
0도보다 높을 때는 얼어 있지 않음 

온도가 정확히 0도일 때는 얼어 있을 수도 그렇지 않을수도 있음 

고기가 얼어 있고 온도가 0도 미만일 때 : 온도는 c초에 1도씩 오름 
고기가 얼어있고 온도가 정확히 0도 일때 : 해동시 d초가 걸림 
고기가 얼어 있지 않을 때 : 온도가 e초에 1도씩 오름 

⛔️ 입력 
원래 고기 온도 a도 
목표 온도 b도 
얼어있는 고기 데우는 시간 c초 
얼어있는 고기 해동시 걸리는 시간 d초 
얼어있지 않은 고기 데우는 시간 e초 


⛔️ 출력 
고기를 b도로 데우는데 걸리는 시간 


'''

originaltemp = int(input())
temp = int(input())
Csec = int(input())
Dsec = int(input())
Esec = int(input())

count = 0

if originaltemp < 0 : 
    count += Csec * abs(originaltemp)
    count += Dsec
    count += temp * Esec
    
else: 
    count+= Esec * (temp-originaltemp)

print(count)