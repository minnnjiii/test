# 부녀회장이 될테야_2775번

# 문제 

'''

a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 
사람들의 수의 합만큼 사람들을 데려와 살아야 함 

주어지는 양의 정수 k와 n에 대해
k층에 n호에는 몇 명이 살고 있는지 출력하라 

아파트엔 0층부터 있고 각층에는 1호부터 있으며
0층의 i호에는 i명이 산다 

'''

# 입력

# 첫 번째 줄에 Test case의 수 T가 주어짐
# 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어짐

# 출력

# 각각의 Test case에 대해서 해당 집에 거주민 수를 출력하기 


TestCase = int(input())


for _ in range(TestCase):
    floor = int(input())
    unit = int(input())
    floor0 = [x for x in range(1,unit+1)]
    
    for k in range(floor):
        for n in range(1,unit):
            floor0[n] += floor0[n-1]
            
    print(floor0[-1])