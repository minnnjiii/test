# 사과
# 10833 


n = int(input()) # 학교의 수 

remain = 0 # 남은 사과 갯수

for i in range(n) : 
    student, apple = map(int,input().split()) 
    
    if apple < student : # 사과 갯수가 학생 수보다 적어서 나눠줄 수 없는 경우
        remain += apple # 아무도 나눠주지 못하기 때문에 사과가 그대로 남음
    else:
        remain += apple % student

print(remain)
