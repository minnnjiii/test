# 앵그리 창영
# 백준 3034

# 성냥이 박스에 들어가려면 박스의 밑면에 성냥이 모두 닿아야 함
# 박스의 크기와 성냥의 길이가 주어졌을 때, 
# 성냥이 박스에 들어갈 수 있는지 없는지



# 성냥의 개수 N, 박스의 가로 크기 W, 박스의 세로 크기 H


N, W, H = map(int,input().split()) 


for i in range(N) : 
    diagonal = (W**2 + H**2)**0.5
    match = int(input()) 

    if match <= diagonal : 
        print("DA") 
    else:
        print("NE")