# 수도요금
# 10707

# JOI군의 집에서 지불하는 한 달간 수도요금을 첫째 줄에 출력한다.

a = int(input()) # X사의 1리터당 요금 A
b = int(input()) # Y사의 기본요금 B
c = int(input()) # Y사의 요금이 기본요금이 되는 사용량의 상한 C
d = int(input()) # Y사의 1리터 당 추가요금 D
p = int(input()) #  JOI군의 집에서 사용하는 한 달간 수도의 양 P


XP = a*p # X사 요금
if p <= c : 
    XY = b 
else: 
    XY = b 
    p = p - c 
    XY += d*p 

if XY > XP : 
    print(XP) 
else:
    print(XY)