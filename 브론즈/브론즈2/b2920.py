# 음계
# 백준/2920번

music = list(map(int,input().split())) 

if sorted(music) == music : 
    print("ascending") 
elif sorted(music,reverse=True) == music : 
    print("descending")
else : 
    print("mixed")