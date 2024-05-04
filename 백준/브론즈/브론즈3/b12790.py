# Mini Fantasy War
# 백준/12790번

# 최종 전투력 계산하기
# 전투력 = 1 * (HP) + 5 * (MP) + 2 * (공격력) + 2 * (방어력)

# 단, HP와 MP는 1보다 작은 경우 1로 간주하며, 
# 공격력은 0보다 작은 경우 0으로 간주한다. 
# 방어력은 음수 여부에 상관하지 않는다.

import sys 

input = sys.stdin.readline

t = int(input()) # test case 

for i in range(t) : 
    hp, mp, attack, defence, HP_increase, MP_increase, attack_increase, defence_increase = map(int,input().split()) 

    # if hp < 1 : 
    #     hp = 1
    # if HP_increase < 1 :
    #     HP_increase = 1
    # if mp < 1 : 
    #     mp = 1 
    # if MP_increase < 1 : 
    #     MP_increase = 1 
    # if attack < 0 : 
    #     attack = 0
    # if attack_increase < 0 :
    #     attack_increase = 0 
    
    I = hp + HP_increase 
    if I < 1 : 
        I = 1 
    J = mp + MP_increase
    if J < 1 : 
        J = 1
    k = attack + attack_increase
    if k < 0 : 
        k = 0
    l = defence + defence_increase


    final = ((1*I)+(5*J)+(2*k)+(2*l))
    print(final)