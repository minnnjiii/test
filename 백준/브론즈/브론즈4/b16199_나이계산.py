# 나이 계산하기 
# 16199번

# 만 나이 : 생일을 기준으로 나이를 셈 
# 태어났을 때 나이는 0세이고 생일이 지날 때마다 1세가 증가함


# 세는 나이 : 생년을 기준으로 계산함. 
# 태어났을 때 나이는 1세이고 연도가 바뀔 때마다 1세가 증가함

# 연 나이 : 생년을 기준으로 계산함
# 태어났을 때 나이는 0세익 연도가 바뀔 때마다 1세가 증가함 

# 문제 
# 어떤 사람의 생년월일과 기준 날짜가 주어졌을 때, 
# 기준 날짜를 기준으로 그 사람의 만 나이, 세는 나이, 연 나이를 모두 구하시오 

last_y, last_m, last_d = map(int,input().split()) # 태어난 날
current_y, current_m, current_d = map(int,input().split()) # 기준 날짜

b = current_y - last_y + 1 # 세는 나이
c = current_y - last_y  # 연 나이

# 만 나이 계산하기
a = 0 
if current_d - last_y == 0 : 
    pass
elif current_y > last_y : 
    if current_m > last_m :
        a = current_y - last_y 
    elif current_m == last_m : 
        if current_d >= last_d : 
            a = current_y - last_y 
        else : 
           a = current_y - last_y - 1 
    else: 
        a = current_y - last_y - 1 
    

print(a) # 만 나이
print(b) # 세는 나이
print(c) # 연 나이
