# 잃어버린 괄호
# 백준_1541번 

# "-"를 기준으로 숫자들을 리스트에 저장함
# 55-50+40 --> ['55','50+40']
nums = list(map(str,input().split("-"))) 


# 리스트의 각 요소에서 "+" 문자가 있다면 
# "+"를 기준으로 분리하여 합하기 
# ['55','50+40'] --> ['55',90]
for i in range(len(nums)):
    if '+' in nums[i]:
        nums[i] = nums[i].split('+') 
        nums[i] = sum(map(int,nums[i]))

# 문자형은 숫자형으로 바꿔주기
# ['55',90] --> [55,90]
for j in range(len(nums)):
    nums[j] = int(nums[j])

# 리스트의 각 요소들을 빼줌 
# [55,90] --> 55 - 90
ans = nums[0]
for k in range(1,len(nums)):
    ans -= nums[k] 


print(ans)